import requests
from clear_text import img_to_text,read_img

def call_llm(prompt, model='mistral'):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.7,
        "stream": False  # Define False para receber a resposta toda de uma vez
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
        return resultado['response']
    else:
        return f"Erro: {response.status_code} - {response.text}"

text =  read_img("F:/Usuário/Documents/GitHub/llm_lang/shots/screenshot_rafaelagarciaok.png")
# Exemplo de uso:
def overview(text,prompt = None):
  if prompt == None:
    _prompt = f"""### Instrução:
      Extraia os seguintes campos do texto abaixo e retorne um texto com estututa parecida com o exemplo a baixo
      exemplo:
      Informações do Perfil:
      Nome de Usuário: @felipecamargo
      Nome: Felipe Camargo
      Bio: "Escalador profissional"
      Localização: Mencionada como "Mundo"
      Seguidores: 131 mil seguidores
      Seguindo: 1.216 perfis
      Publicações: 1.511 publicações
      Destaques dos Stories:
      Fixas: Provavelmente mostra momentos de escaladas bem-sucedidas.
      E tem mais!
      Ações recentes: Atualizações recentes ou conquistas.
      Parcerias: Colaborações com marcas ou outros escaladores.
      Conteúdo das Publicações:
      Escaladas: Várias imagens e vídeos de Felipe escalando em diferentes locais, incluindo paredes de rocha e ambientes indoor.
      Treinamento: Fotos de sessões de treinamento, possivelmente em academias de escalada.
      Viagens e Aventuras: Imagens de viagens e explorações em locais naturais, destacando a vida ao ar livre.
      Parcerias e Colaborações: Publicações com marcas como Patagônia e outras relacionadas ao esporte e ao estilo de vida ao ar livre.
      Momentos Pessoais: Fotos com amigos e familiares, mostrando um lado mais pessoal de sua vida.
      Publicações Destaque:
      Publicação Patrocinada: Uma publicação patrocinada pela Patagônia, destacando uma jaqueta.
      Vídeos de Escalada: Vídeos mostrando técnicas e desafios de escalada.
      Imagens de Viagens: Fotos em locais exóticos e naturais, como praias e montanhas.
      Interação:
      O perfil parece ser ativo, com muitas interações e engajamento dos seguidores.
      Há uma seção de "Conteúdo que você criou", indicando que os seguidores também compartilham conteúdo relacionado a Felipe.
      Conclusão:
      O perfil de Felipe Camargo é uma mistura de conteúdo profissional e pessoal, focado principalmente em escalada e aventuras ao ar livre. Ele parece ser um escalador experiente e influente, com uma forte presença na comunidade de escalada.

      Critérios:
      - "nome": o nome completo do indivíduo.
      - "países": nomes dos países mencionados direta ou indiretamente.
      - "estados":estado mencionados direta ou indiretamente (ex:siglas como SP).
      - "cidades": cidades mencionados direta ou indiretamente.
      - "atividades": funções profissionais e atividades (ex: ator, apresentador, maquiador, produtor de conteúdo).
      - "empresas": marcas ou empresas mencionadas no texto (inclusive em perfis relacionados, se forem claramente marcas).
      - "seguidores": número total de seguidores, convertido em número inteiro.
      - "publicações": número total de publicações (valor que antecede a palavra "publicações" no texto).
      - "seguidores": número total de seguidores (valor que antecede a palavra "seguidores" no texto).
      - "seguindo": número total de seguindo  (valor que antecede a palavra "seguindo" no texto).  
     

      Texto:
      {text}


      ### Resposta:
      """
    
    try:
      res = call_llm(_prompt)
      print(res)
    except Exception as e:
      res = f"Erro ao chamar o LLM: {e}"
  else:
    _prompt = f"""{prompt}
      Texto:
        {text}


      ### Resposta:
      """
    res = call_llm(text,prompt)
  return res


