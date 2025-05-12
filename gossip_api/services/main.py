from gossip_api.services.shot import screen_shot
from gossip_api.services.llm import call_llm
from gossip_api.services.prompts import Prompts
from gossip_api.services.clearText import img_to_text


def overview(text, web_source, prompt=None):
    try:
        if prompt == None:
            _prompt = Prompts(web_source, text).get()
            # print(_prompt)
            res = call_llm(_prompt)
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


def res_overview(urls, web_source=None):
    img, _web_source = screen_shot(urls)
    if web_source == None:
        web_source = _web_source
    text = img_to_text(img)
    return overview(text, web_source)

