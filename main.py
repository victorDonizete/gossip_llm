from shot import shot_instagram
from llm import overview
from clear_text import img_to_text

def main(urls):
  img = shot_instagram(urls)
  text = img_to_text(img)
  return overview(text)
if __name__ == "__main__":
  urls = input("Digite a url do perfil do instagram: ") 
  main(urls)