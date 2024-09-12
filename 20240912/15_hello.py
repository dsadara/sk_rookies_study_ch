from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")는 '/' 경로에 접근할 때
# index 함수를 실행하여 'Index Page'를 반환함
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit_form():
    usern = request.form['username']
    return f"Hello, {usern}"
    
# 이 코드는 스크립트가 직접 실행될 때만 실행됨
if __name__ == '__main__':
    app.run(debug=True)