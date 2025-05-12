class Prompts:
  def __init__(self,web_sorce, text ):
    self.web_sorce = web_sorce
    self.text = text
    self.prompts ={
      "youtube" : f""" 
        Por favor, faça um resumo do perfil do YouTube a partir do seguinte texto:

        [{self.text}]

        Inclua os seguintes campos no formato JSON:
        - nome_do_canal
        - estatísticas (como número de inscritos e vídeos publicados)
        - descrição_do_canal
        - conteúdo_em_destaque (incluindo título, descrição, visualizações e data de publicação)
        - outros_vídeos_populares
        - playlists

        Exemplo de formato esperado:
        {{
          "nome_do_canal": "Nome do Canal",
          "estatisticas": {{
            "inscritos": "XX",
            "videos_publicados": XX
          }},
          "descricao_do_canal": "Descrição do canal...",
          "conteudo_em_destaque": {{
            "titulo": "Título do Vídeo",
            "descricao": "Descrição do vídeo...",
            "visualizacoes": XXXXX,
            "data_publicacao": "Data de Publicação"
          }},
          "outros_videos_populares": [
            "Vídeo 1",
            "Vídeo 2",
            "Vídeo 3"
          ],
          "playlists": [
            "Playlist 1",
            "Playlist 2",
            "Playlist 3"
          ]
        }}

      """,

      "instagram": f"""
        ### Instrução:
           Por favor, faça um resumo detalhado do perfil do Instagram a partir do seguinte texto:

            [{self.text}]

            Inclua os seguintes campos no formato JSON:
             - "nome": o nome completo do indivíduo.
             - "países": nomes dos países mencionados direta ou indiretamente.
             - "estados": estados mencionados direta ou indiretamente (ex: siglas como SP).
             - "cidades": cidades mencionadas direta ou indiretamente.
             - "atividades": funções profissionais e atividades (ex: ator, apresentador, maquiador, produtor de conteúdo).
             - "empresas": marcas ou empresas mencionadas no texto (inclusive em perfis relacionados, se forem claramente marcas).
             - "seguidores": número total de seguidores, convertido em número inteiro.
             - "publicações": número total de publicações (valor que antecede a palavra "publicações" no texto).
             - "seguindo": número total de seguindo (valor que antecede a palavra "seguindo" no texto).
             - "destaques_stories": descrição dos destaques dos stories.
             - "conteudo_publicacoes": descrição do conteúdo das publicações.
             - "interacao": descrição da interação no perfil.
             - "conclusao": conclusão sobre o perfil.

            Exemplo de formato esperado:
              {{
                "nome": "Felipe Camargo",
                "países": ["Brasil"],
                "estados": ["SP"],
                "cidades": ["São Paulo"],
                "atividades": ["Escalador profissional"],
                "empresas": ["Patagônia"],
                "seguidores": 131000,
                "publicações": 1511,
                "seguindo": 1216,
                "destaques_stories": {{
                  "fixas": "Momentos de escaladas bem-sucedidas.",
                  "acoes_recentes": "Atualizações recentes ou conquistas.",
                  "parcerias": "Colaborações com marcas ou outros escaladores."
                }},
                "conteudo_publicacoes": {{
                  "escaladas": "Imagens e vídeos de escaladas em diferentes locais.",
                  "treinamento": "Fotos de sessões de treinamento.",
                  "viagens_aventuras": "Imagens de viagens e explorações em locais naturais.",
                  "parcerias_colaboracoes": "Publicações com marcas como Patagônia.",
                  "momentos_pessoais": "Fotos com amigos e familiares."
                }},
                "interacao": "O perfil parece ser ativo, com muitas interações e engajamento dos seguidores.",
                "conclusao": "O perfil de Felipe Camargo é uma mistura de conteúdo profissional e pessoal, focado principalmente em escalada e aventuras ao ar livre."
              }}

        """,
        "facebook" : f"""
          ### Instrução:
          "Por favor, faça um resumo do perfil do Facebook  em formato JSON, a partir do seguinte texto:
          [{self.text}]
          Inclua os seguintes campos:
          - "nome": o nome  do indivíduo.
          - "países": nomes dos países mencionados direta ou indiretamente.
          - "estados":estado mencionados direta ou indiretamente (ex:siglas como SP).
          - "cidades": cidades mencionados direta ou indiretamente.
          - "atividades": funções profissionais e atividades (ex:escaldor,CO, mecanico, ator, apresentador, maquiador, produtor de conteúdo...).
          - "empresas": marcas ou empresas mencionadas no texto (inclusive em perfis relacionados, se forem claramente marcas).
          - "publicações": número total de publicações (valor que antecede a palavra "publicações" no texto).
          - "seguidores": número total de seguidores (valor que antecede a palavra "seguidores" no texto).
          - "seguindo": número total de seguindo  (valor que antecede a palavra "seguindo" no texto). 

          Extraia os seguintes campos do texto  e retorne um texto com estrutura  como o exemplo abaixo.
          exemplo:  
          {{
        "nome_do_perfil": "Demi Lovato",
        "estatisticas": {{
          "seguidores": "32 milhões",
          "seguindo": 1
        }},
        "descricao_do_perfil": "A página convida os usuários a se conectarem com amigos, parentes e pessoas que conhecem.",
        "conteudo_em_destaque": [
          {{
            "tipo": "Vídeo",
            "descricao": "Vídeo de Demi Lovato com um amigo",
            "visualizacoes": 7600,
            "reacoes": 226
          }},
          {{
            "tipo": "Post",
            "legenda": "Convincing ourselves we can communicate telepathically",
            "visualizacoes": 6300,
            "reacoes": 254
         }},
          {{
            "tipo": "Post",
            "legenda": "Me 😍 posting",
            "reacoes": 254
          }}
        ],
        "outros_links": {{
          "instagram": "@ddlovato",
          "twitter": "@ddlovato",
          "site_oficial": "demilovato.com"
        }},
        "informacoes_adicionais": "Informações adicionais sobre a página, incluindo termos de privacidade, cookies, e mais."
      }}  
     """
    }

  def get(self):
    if self.web_sorce in list(self.prompts.keys()):
      _prompt = self.prompts[self.web_sorce]
      return _prompt
    else:
      return ValueError("Web source not supported")