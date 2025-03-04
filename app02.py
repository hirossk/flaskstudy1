from flask import Flask,render_template

app = Flask(__name__)

# URLアクセスのパス指定すると次に記述しているメソッドが呼び出される
@app.route('/')
def index():
    # Jinjaテンプレートによる展開が行われる
    return render_template('index.html')

# @app.route('/loop')
# def loop():
#     # Jinjaテンプレートによる展開が行われる, count=10は変数を渡している
#     return render_template('loop.html', count=10)

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)