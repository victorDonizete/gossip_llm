# from docling.document_converter import DocumentConverter
from PIL import Image
import pytesseract
import spacy

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
