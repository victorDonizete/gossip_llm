from bs4 import BeautifulSoup
import httpx
with open("page_html.txt","r",encoding ="utf-8") as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')
imagens = ["{}//".format(img['src']) for img in soup.find_all('img') if img.get('src')]
try:
    for i in range(6):
        img = httpx.get(imagens[i])
        with open("{}.png".format(i),"wb") as png:
            img_png = png.write(img.content)
except Exception as e:
    print(e)
    