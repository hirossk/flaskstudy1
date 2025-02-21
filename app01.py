from flask import Flask 
app = Flask(__name__) 
# ルートURLにアクセスしたときに実行される関数を定義
@app.route('/')
def hello_world():
    # 'Hello, World!'という文字列を返す
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__': 
    app.run()