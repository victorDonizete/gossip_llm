#!/bin/bash
set -e

# Create app user and group for running the Django application
# Use the same UID/GID as the owner of the mounted volume to avoid permission issues
APP_UID=${APP_UID:-1000}
APP_GID=${APP_GID:-1000}

echo "Setting up app user (uid: $APP_UID, gid: $APP_GID)..."
groupadd -g $APP_GID app_group || true
useradd -u $APP_UID -g $APP_GID -d /app -s /bin/bash app_user || true

# Create data directory if it doesn't exist
mkdir -p /app/data
echo "Data directory created or already exists"

# Update settings to use the data directory for the database
if [ ! -f /app/data/db.sqlite3 ]; then
    echo "Initializing database..."
    touch /app/data/db.sqlite3
fi

# Set proper ownership and permissions
chown -R app_user:app_group /app/data
chmod -R 775 /app/data
chmod 664 /app/data/db.sqlite3
echo "Set ownership and permissions for data directory"

# Point Django to use the database in the data directory
export SQLITE_DB_PATH=/app/data/db.sqlite3

# Update the database ENGINE setting if needed
if [ -f /app/api_root/settings.py ]; then
    echo "Configuring Django settings for database path..."
    # This is a precaution - these lines might need to be adapted based on your actual settings file
    sed -i 's/"NAME": BASE_DIR \/ "db.sqlite3",/"NAME": os.environ.get("SQLITE_DB_PATH", BASE_DIR \/ "db.sqlite3"),/g' /app/api_root/settings.py
    # Also add os import if it's missing
    grep -q "import os" /app/api_root/settings.py || sed -i '1s/^/import os\n/' /app/api_root/settings.py
fi

echo "Running database migrations as app_user..."
cd /app && su app_user -c "python manage.py migrate --noinput"

# Create static directory if it doesn't exist
mkdir -p /app/staticfiles
chown -R app_user:app_group /app/staticfiles
chmod -R 775 /app/staticfiles
echo "Static files directory created or already exists"

# Collect static files
echo "Collecting static files as app_user..."
cd /app && su app_user -c "python manage.py collectstatic --noinput"

echo "Initialization completed."

# Make sure manage.py is executable
chmod +x /app/manage.py

echo "Running Django as app_user..."
# Run the command passed as parameters as the app_user
exec su app_user -c "$*"

