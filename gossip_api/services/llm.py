import requests
from gossip_api.services.prompts import Prompts


def call_llm(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.9,
        "stream": False,  # Define False para receber a resposta toda de uma vez
    }
    #     payload = {
    #     "model": "llama3",
    #     "prompt": "Explique a teoria da relatividade em termos simples.",
    #     "temperature": 0.8,
    #     "top_k": 50,
    #     "top_p": 0.95,
    #     "repeat_penalty": 1.1,
    #     "presence_penalty": 0.2,
    #     "frequency_penalty": 0.2,
    #     "stream": False
    # }

    # response = requests.post("http://localhost:11434/api/generate", json=payload)
    # print(response.json()["response"])

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        resultado = response.json()
        return resultado["response"]
    else:
        return f"Erro: {response.status_code} - {response.text}"


# Exemplo de uso:
def overview(text, web_source, prompt=None):
    try:
        if prompt == None:
            _prompt = Prompts(web_source, text).get()
            res = call_llm(_prompt)
            print(res)

        else:
            _prompt = f"""{prompt}
        Texto:
          {text}

        ### Resposta:
        """
            res = call_llm(text, prompt)
        return res
    except Exception as e:
        res = f"Erro ao chamar o LLM: {e}"
