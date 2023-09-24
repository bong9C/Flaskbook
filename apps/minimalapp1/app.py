from flask import Flask     # falsk 클래스를 import 한다.

app = Flask(__name__)       # flask 클래스를 인스턴스화한다.


@app.route("/")             # URL과 실행할 함수를 매핑한다.
def index():
    return "Hello Falskbook!!!"
