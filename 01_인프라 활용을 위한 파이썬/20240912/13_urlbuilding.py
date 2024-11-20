from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    # index.html 템플릿을 렌더링
    return render_template('index.html')

@app.route('/login')
def login():
    # login.html 템플릿을 렌더링
    return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
    # profile.html 템플릿을 렌더링하면서 username 변수 전달
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    # 애플리케이션을 디버그 모드로 실행
    app.run(debug=True)
