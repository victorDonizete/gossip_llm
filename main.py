from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace,HuggingFacePipeline
from transformers import pipeline
from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-base", use_fast=False)

# from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipelines
repo_id =  "facebook/bart-large-cnn"
model = pipeline(
    task = "summarization",
    model= repo_id,
    device="cpu")
reposnse = model("testando o modelo")



# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,
#     task="text-classification",
#     max_new_tokens=512,
#     do_sample = False,
#     repetition_penalty= 1.03
# )

# llm = ChatHuggingFace(llm=llm,verbose = True)

