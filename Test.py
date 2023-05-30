from googletrans import Translator
from json import loads
from requests import get
request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=ko&q=It was so good for me that I forgot all about the bad things that happened today. But when I got back home, my mother was waiting for me.")
translated_text = request_result.text
print(translated_text)
translator = Translator()

print(translator.translate('It was so good for me that I forgot all about the bad things that happened today. But when I got back home, my mother was waiting for me.', src='en', dest='ko').text)
#print(translator.translate('나는 밥을 먹고 화장실에 갔다.', src='ko', dest='en').text)