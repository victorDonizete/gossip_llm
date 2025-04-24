#criar vetorizacao dos dados coletados
# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import WebBaseLoader
import httpx
# loader = WebBaseLoader("https://www.instagram.com/rafaelagarciaok/")
# docs =loader.load()
# print(docs)

http = httpx.get("https://www.instagram.com/rafaelagarciaok/")
page_html = str(http.content)
print(http.content)
try:
    with open("page_html.txt","w") as txt:
        txt.write(page_html)
        txt.close
except FileExistsError:
    print("File already exists")