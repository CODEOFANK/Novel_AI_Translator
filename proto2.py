from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
import time
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}



#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기

driver = webdriver.Chrome()

class Execute_Chrome :

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        self.buffer = ''



    def Login(self):
        Elem = driver.find_element_by_id("username")
        Elem.send_keys(self.id)
        Elem = driver.find_element_by_id("password")
        Elem.send_keys(self.pw)
        Elem.send_keys(Keys.RETURN)

    def Input_Text(self, In_text):
        Textarea = driver.find_element_by_tag_name("textarea")
        Textarea.send_keys(In_text)
        Textarea.send_keys(Keys.RETURN)

    def PromptText_Crawler(self):
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        i = soup.find_all(attrs={'class': 'promptText'})
        sum_text = ''
        for j in i:
            ToKor_url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=ko&q=" + j.get_text()
            request_result = requests.get(ToKor_url, headers=headers).json()
            # print(translator.translate(j.get_text(), dest='ko').text)
            try:
                for k in request_result['sentences']:
                    print(k['trans'])
            except KeyError:
                pass
            time.sleep(1)

    def AiText_Crawler(self, Trans_text):
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        i = soup.find_all(attrs={'class': 'undoDeletionText'})

#        self.buffer = i[-1].get_text()
#        print('buffer : ' + self.buffer)
        sum_text = ''
        for j in i:
            if j.get_text() == Trans_text:
                return -1
            else:
                # print(translator.translate(j.get_text(), dest='ko').text)
                try:
                    print(translator.translate(j.get_text(), src='en', dest='ko').text)
                except KeyError:
                    pass
                time.sleep(1)

#undoDeletionText
if __name__ == "__main__":

    driver.get('https://novelai.net/login')
    time.sleep(1)
    Executor = Execute_Chrome(input("ID를 입력하세요. : "), input("PW를 입력하세요. : "))
    translator = Translator()
    Executor.Login()
    input("시작화면으로 진입하세요. ENTER")
    Executor.PromptText_Crawler()

    while True:
        print('\n')
        In_text = input("입력 : ")
#        Trans_text = translator.translate(In_text).text

        try:
            print(translator.translate(In_text, src='ko', dest='en').text)
            Executor.Input_Text(translator.translate(In_text, src='ko', dest='en').text)
            print('\n')
            time.sleep(2)
            while Executor.AiText_Crawler(translator.translate(In_text, src='ko', dest='en').text) == -1:
                #           print('응답 대기중...')
                time.sleep(2)
        except TypeError:
            Executor.Input_Text('')
            while Executor.AiText_Crawler('') == -1:
                #           print('응답 대기중...')
                time.sleep(2)
#            Executor.AiText_Crawler('')
'''
        while Executor.AiText_Crawler(translator.translate(In_text, src='ko', dest='en').text) == -1:
            #           print('응답 대기중...')
            time.sleep(2)
'''
    #           Executor.AiText_Crawler(Trans_text)

'''
        try:
            for k in Trans_text['sentences']:
                merge_text += k['trans']
        except KeyError:
            pass
        Executor.Input_Text(merge_text)
        print('\n')
        time.sleep(2)
        while Executor.AiText_Crawler(merge_text) == -1:
 #           print('응답 대기중...')
            time.sleep(2)
 #           Executor.AiText_Crawler(Trans_text)

'''