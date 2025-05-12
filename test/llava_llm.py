import requests
import base64
def conversar_com_llama(prompt, model='llava',image=None):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": model,
        "prompt": prompt,
        "image": pictur,
        "temperature": 0.9,
        "stream": False  # Define False para receber a resposta toda de uma vez
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        resultado = response.json()
        return resultado['response']
    else:
        return f"Erro: {response.status_code} - {response.text}"

# Exemplo de uso:
with open(f"F:/Usuário/Documents/GitHub/llm_lang/shots/screenshot_barefoot_kaleu.png","rb") as image:
    pictur = base64.b64encode(image.read()).decode('utf-8') 
pergunta = f"""### Instrução:
Extraia os seguintes campos da imagem e retorne um texto com estrututa parecida com o exemplo a baixo
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
- "publicações": número total de publicações
- "seguidores": número total de seguidores
- "seguindo": número total de seguindo
### Resposta:
"""
try:
    resposta = conversar_com_llama(pergunta,image=pictur)
    print(resposta)
except Exception as e:
    resposta = f"Erro ao chamar o LLM: {e}"

