import base64
import json
import urllib.request
import urllib3
from gtts import gTTS
from playsound import playsound

class TranslationLogic:
    def __init__(self, parent):
        self.parent = parent
        self.trans = ""  # trans 변수 초기화

    def setup(self):
        self.parent.speak_btn.clicked.connect(self.translate)

    def translate(self):
        # ... (existing translate method code) ...
        sender = self.sender()
        openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
        accessKey = "e3b444fb-71c0-4a32-9959-8e65cad07696"
        audioFilePath = "C:/Users/oyg03/PycharmProjects/pythonProject/etri api/audio/rec.m4a"
        languageCode = "english"
        file = open(audioFilePath, "rb")
        audioContents = base64.b64encode(file.read()).decode("utf8")
        file.close()
        requestJson = {
            "argument": {
                "language_code": languageCode,
                "audio": audioContents
            }
        }
        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey},
            body=json.dumps(requestJson)
        )
        result = json.loads(response.data)
        file_path = "./result.json"
        write = True
        if write == True:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(result, file, indent="\t")
        state = dict()
        read = True
        if read == True:
            with open(file_path, 'r') as data:
                result = json.load(data)
        current_text = self.parent.label_3.text()  # self.parent.label_3를 사용
        additional_text = result['return_object']['recognized']  # 추가할 텍스트
        new_text = current_text + additional_text
        self.parent.label_3.setText(new_text)
        print(result['return_object']['recognized'])
        client_id = "wSVVTofzQ_J41pgEypnz"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "mA_mLLSPqN"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(result['return_object']['recognized'])
        data = "source=" + languageCode[0:2] + "&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        trans = ""
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            result = result.split('"')
            self.trans = result[27]
        else:
            print("Error Code:" + rescode)
        from gtts import gTTS
        from playsound import playsound
        def play_text(text, lang='ko', audio_filename='voice.mp3'):
            tts = gTTS(text=text, lang=lang)
            tts.save(audio_filename)
            playsound(audio_filename)

        current_text = self.parent.label_4.text()  # self.parent.label_4를 사용
        additional_text = self.trans  # self.trans를 사용
        new_text = current_text + additional_text
        self.parent.label_4.setText(new_text)
def play_text(self, text, lang='ko', audio_filename='voice.mp3'):
        # ... (existing play_text method code) ...
        tts = gTTS(text=text, lang=lang)
        tts.save(audio_filename)
        playsound(audio_filename)

