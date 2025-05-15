# Gossip LLM

A Django-based API for natural language processing with spaCy, featuring Portuguese language support.

## Project Overview

This project provides a REST API built with Django and Django REST Framework that leverages language models for text processing. It includes integration with:

- spaCy for natural language processing (with Portuguese language model)
- Tesseract OCR for optical character recognition
- Django REST Framework for API endpoints
- Cross-Origin Resource Sharing (CORS) support for frontend integration

## Prerequisites

Before you start, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) (version 19.03.0+)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.27.0+)

## Docker Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd gossip_llm
```

### 2. Build and Start the Docker Containers

```bash
docker-compose up --build
```

This command builds the Docker image and starts the containers as defined in the `docker-compose.yml` file. The first build might take some time as it downloads the base image and installs all dependencies.

### 3. Access the Application

Once the containers are running, you can access:

- API: http://localhost:8000/
- Django Admin: http://localhost:8000/admin/

## Environment Variables

The Docker setup uses several environment variables that can be configured in the `docker-compose.yml` file:

| Variable | Description | Default Value |
|----------|-------------|---------------|
| DJANGO_SECRET_KEY | Secret key for Django | django-insecure-4s1x5a9j*yt*rv&wq8xcd#!*!%$tbua7fwogdip90$g)+(lgz+ |
| DJANGO_DEBUG | Debug mode | True |
| DJANGO_ALLOWED_HOSTS | Allowed hosts for the application | localhost,127.0.0.1 |

**Note**: For production deployment, make sure to change these values, especially the `DJANGO_SECRET_KEY`.

## Development Workflow with Docker

### Running the Development Server

The Docker Compose setup includes hot-reload, so changes to your code will automatically be reflected in the running application:

1. Make changes to your code
2. The Django development server will automatically restart
3. Refresh your browser to see the changes

### Running Django Management Commands

To run Django management commands within the Docker container:

```bash
docker-compose exec web python manage.py <command>
```

Examples:
```bash
# Create database migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic
```

## Common Commands and Troubleshooting

### Common Docker Commands

```bash
# Start containers in detached mode
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs -f

# Rebuild containers (after changing requirements.txt)
docker-compose up --build

# Remove all stopped containers and unused images
docker system prune
```

### Troubleshooting

- **Database Issues**: If you encounter database issues, check that the SQLite database volume is properly mounted
  ```bash
  docker-compose down
  docker volume ls
  docker-compose up
  ```

- **Permission Errors**: If you encounter permission errors, verify that the `manage.py` file has execute permissions
  ```bash
  chmod +x manage.py
  docker-compose restart
  ```

- **Package Dependencies**: If you add new packages to `requirements.txt`, rebuild the containers
  ```bash
  docker-compose down
  docker-compose up --build
  ```

- **Port Conflicts**: If port 8000 is already in use, change the port mapping in `docker-compose.yml`
  ```yaml
  ports:
    - "8001:8000"  # Maps host port 8001 to container port 8000
  ```
