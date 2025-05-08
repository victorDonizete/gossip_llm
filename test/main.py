from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace,HuggingFacePipeline
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from transformers import pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration #AutoFeatureExtractor, AutoTokenizer, AutoModelForImageClassification
import torch
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
token = os.getenv("HUGGINGFACE_API_TOKEN")
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))


image = Image.open("F:/Usuário/Documents/GitHub/llm_lang/shots/screenshot_rafaelagarciaok.png")

repo_id = "Salesforce/blip2-flan-t5-xl" 
# Salesforce/blip-image-captioning-base res: {'generated_text': 'a screenshot of a woman climbing on a mountain'}
#HuggingFaceM4/idefics-9b modelo que precisa de uma maquina boa min 24g Ram + 24g vram
#ByteDance-Seed/UI-TARS-1.5-7B travou minh maquina

processor = BlipProcessor.from_pretrained(repo_id)
model = pipeline(
    task = "image-text-to-text",
    model= repo_id,
    device="cuda:0")



def get_imagem_info(input:dict)->str:
    image = input["image"]
    quention = input["question"]
    inputs = processor(image, quention, return_tensors="pt").to(model)
    out = model.generate(**inputs,max_new_tokens=100)
    res = processor.decode(out[0], skip_special_tokens=True)
    return res

chain = (
    RunnablePassthrough.assign() |
    RunnableLambda(get_imagem_info) |
    StrOutputParser()
)

question = " A imagem e um conjunto de fotos, e a um cabeçalho com informaçoes de um perfil de usuaruio, quero façao um overview desse perfil."

# Chamar a chain
result = chain.invoke({"image": image, "question": question})
print(result)
# inputs = extractor(images=image, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits
#     predicted_class_idx = logits.argmax(-1).item()

# # Nome da classe
# print("Classe prevista:", model.config.id2label[predicted_class_idx])

# prompt = """
# A inteligência artificial (IA) está revolucionando o mundo dos negócios, da saúde e da educação.
# Sistemas de IA são capazes de analisar grandes volumes de dados, reconhecer padrões e tomar decisões com base em algoritmos.
# O uso ético da IA é uma preocupação crescente entre especialistas, que alertam para a necessidade de regulação.
# """
# response = model(prompt, max_length=50, min_length=25, do_sample=False)

# print(response)

# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,
#     task="text-classification",
#     max_new_tokens=512,
#     do_sample = False,
#     repetition_penalty= 1.03
# )

# llm = ChatHuggingFace(llm=llm,verbose = True)

