from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import QRect, QTimer
from PyQt5.QtGui import QPixmap
from standing import StandingLogic
from translation import TranslationLogic

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.standing_logic = StandingLogic(self)
        self.translation_logic = TranslationLogic(self)
        self.setupUi()

    def setupUi(self):
        # ... (existing setupUi code) ...
        self.setObjectName("기사님 잠시만요")
        self.resize(960, 480)
        # 버튼 위치 인자
        x = 5
        y = 120
        a = 95
        b = 60
        # 위치 좌표
        positions = [(x, y), (x + a, y), (x + 2 * a, y), (x + 3 * a, y), (x + 4 * a, y),
                     (x, y + b), (x + a, y + b), (x + 2 * a, y + b), (x + 3 * a, y + b), (x + 4 * a, y + b)]
        sizes = [(90, 40) for _ in positions]

        labels = ["English", "日本語", "中文", "Deutsch", "Français",
                  "Español", "Русский", "Português", "العربية", "Tiếng Việt"]

        self.buttons = [QPushButton(label, self) for label in labels]
        for btn, pos, size in zip(self.buttons, positions, sizes):
            btn.clicked.connect(self.translate_labels)  # Adding click event
            btn.setGeometry(QRect(*pos, *size))

        # Special Button with different size
        self.speak_btn = QPushButton("speak(click this button and speak!)", self)
        self.speak_btn.setGeometry(QRect(40, 260, 400, 61))  # Adjusted size here
        self.speak_btn.clicked.connect(self.translation_logic.translate)

        # Labels
        self.label = QLabel("this stop : Kookmin University", self)
        self.label.setGeometry(QRect(20, 10, 441, 41))

        self.label_2 = QLabel("Next stop : Seunggasa Temple entrance", self)
        self.label_2.setGeometry(QRect(20, 60, 441, 41))

        self.label_3 = QLabel("you say : ", self)
        self.label_3.setGeometry(QRect(10, 360, 200, 41))

        self.label_4 = QLabel("translate korean : ", self)
        self.label_4.setGeometry(QRect(10, 410, 200, 41))

        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(600, 410, 200, 41))

        self.setWindowTitle("승객 편의 시스템")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.standing_logic.standing)
        self.timer_interval = 5000  # 1 second (1000 milliseconds)
        self.timer.start(self.timer_interval)

        # Create a QLabel for displaying the image
        image_label = QLabel(self)
        image_label.setGeometry(QRect(480, 0, 480, 410))

        # Load and set the image using QPixmap
        image_path = "C:/Users/oyg03/PycharmProjects/pythonProject/etri api/image/image.png"  # Update with your image path
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap)
        self.standing_logic.setup()
        self.translation_logic.setup()
    def translate_labels(self):
        sender = self.sender()
        language = sender.text()
        translations = {
            "English": {
                "stop": "this stop: Kookmin University",
                "next_stop": "Next stop: Seunggasa Temple entrance",
                "you_say": "you say : ",
                "translate": "translate korean : ",
                "speak": "speak(click this button and speak!)"
            },
            "日本語": {
                "stop": "この停留所：国民大学",
                "next_stop": "次の停留所：スングガサ寺入口",
                "you_say": "あなたは言う : ",
                "translate": "韓国語翻訳 : ",
                "speak": "話す（このボタンをクリックして話す！）"
            },
            "中文": {
                "stop": "这一站：国民大学",
                "next_stop": "下一站：承嘉寺入口",
                "you_say": "你说：",
                "translate": "韩语翻译：",
                "speak": "说话（点击此按钮并说话！）"
            },
            "Deutsch": {
                "stop": "diese Haltestelle: Kookmin Universität",
                "next_stop": "Nächster Halt: Eingang zum Seunggasa Tempel",
                "you_say": "du sagst : ",
                "translate": "Koreanisch übersetzen : ",
                "speak": "sprechen(Sie auf diesen Knopf klicken und sprechen!)"
            },
            "Français": {
                "stop": "ce arrêt : Université Kookmin",
                "next_stop": "Prochain arrêt : Entrée du temple Seunggasa",
                "you_say": "vous dites : ",
                "translate": "traduire en coréen : ",
                "speak": "parler(cliquez sur ce bouton et parlez!)"
            },
            "Español": {
                "stop": "esta parada: Universidad Kookmin",
                "next_stop": "Próxima parada: Entrada del templo Seunggasa",
                "you_say": "tú dices : ",
                "translate": "traducir al coreano : ",
                "speak": "hablar(¡haz clic en este botón y habla!)"
            },
            "Русский": {  # Russian
                "stop": "эта остановка: Университет Kookmin",
                "next_stop": "Следующая остановка: Вход в храм Seunggasa",
                "you_say": "вы говорите : ",
                "translate": "перевод на корейский : ",
                "speak": "говорить(нажмите эту кнопку и говорите!)"
            },
            "Português": {  # Portuguese
                "stop": "esta paragem: Universidade Kookmin",
                "next_stop": "Próxima paragem: Entrada do templo Seunggasa",
                "you_say": "você diz : ",
                "translate": "traduzir para coreano : ",
                "speak": "falar(clique neste botão e fale!)"
            },
            "العربية": {  # Arabic
                "stop": "هذه المحطة: جامعة كوكمين",
                "next_stop": "المحطة التالية: مدخل معبد سونغاسا",
                "you_say": "تقول : ",
                "translate": "ترجمة إلى الكورية : ",
                "speak": "تحدث (اضغط على هذا الزر وتكلم!)"
            },
            "Tiếng Việt": {  # Vietnamese
                "stop": "trạm này: Đại học Kookmin",
                "next_stop": "Trạm tiếp theo: Lối vào chùa Seunggasa",
                "you_say": "bạn nói : ",
                "translate": "dịch sang tiếng Hàn : ",
                "speak": "nói(nhấn vào nút này và nói lên!)"
            }
        }
        translation = translations.get(language, {})
        self.label.setText(translation.get("stop", ""))
        self.label_2.setText(translation.get("next_stop", ""))
        self.label_3.setText(translation.get("you_say", ""))
        self.label_4.setText(translation.get("translate", ""))
        self.speak_btn.setText(translation.get("speak", ""))
        current_text = self.label_4.text()
        additional_text = self.translation_logic.trans  # 수정된 코드
        new_text = current_text + additional_text
        self.label_4.setText(new_text)


    # ... (existing methods for translating labels) ...
