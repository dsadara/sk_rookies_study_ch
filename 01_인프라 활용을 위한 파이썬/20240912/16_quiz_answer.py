from flask import Flask, render_template, request

app = Flask(__name__)

# 하드코딩된 사용자 정보
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        id = request.form['username']
        password = request.form['password']
        if id == VALID_USERNAME and password == VALID_PASSWORD:
            return render_template("login_success.html")
        else:
            error = "Login Fail"

    return render_template("login_form.html", error=error)
    
# 이 코드는 스크립트가 직접 실행될 때만 실행됨
if __name__ == '__main__':
    app.run(debug=True)