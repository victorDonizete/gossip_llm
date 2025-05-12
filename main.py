from shot import screen_shot
from llm import overview
from clear_text import img_to_text

def main(urls,web_source=None):
  img,_web_source = screen_shot(urls)
  if web_source == None:
    web_source = _web_source
  text = img_to_text(img)
  return overview(text,web_source)
 
if __name__ == "__main__":
  urls = input("Digite a url do perfil : ") 
  web_source = input("Digite a fonte da web (instagram, facebook, youtube): ")
  main(urls)