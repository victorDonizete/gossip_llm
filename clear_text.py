# from bs4 import BeautifulSoup
# import httpx
# with open("page_html.txt","r",encoding ="utf-8") as file:
#     html = file.read()
# soup = BeautifulSoup(html, 'html.parser')
# imagens = ["{}//".format(img['src']) for img in soup.find_all('img') if img.get('src')]
# # try:
# #     for i in range(6):
# #         img = httpx.get(imagens[i])
# #         with open("{}.png".format(i),"wb") as png:
# #             img_png = png.write(img.content)
# # except Exception as e:
# #     print(e)
# print(soup)

from docling.document_converter import DocumentConverter
from PIL import Image
import pytesseract
import spacy

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

nlp = spacy.load("pt_core_news_sm")

def clear_text(texto):
    doc = nlp(texto)

    # Mantém apenas tokens que não são stopwords, pontuação ou espaços
    tokens_limpos = [
        token.lemma_.lower() 
        for token in doc 
        if not token.is_stop and not token.is_punct and not token.is_space
    ]

    return " ".join(tokens_limpos)

def read_img(image_path):
  img = Image.open(image_path)
  text = pytesseract.image_to_string(img)
  
 # PDF path or URL
  # converter = DocumentConverter()
  # result = converter.convert(source)
  return text  # output: "### Docling Technical Report[...]"

def img_to_text(image_path):
  # Carregar a imagem
  text = read_img(image_path)
  # cleared_text = clear_text(text)

  return text

