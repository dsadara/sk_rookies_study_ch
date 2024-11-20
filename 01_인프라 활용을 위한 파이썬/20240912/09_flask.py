from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    numbers = [1,2,3,4,5,6,7,8,9,10] 
    return render_template('index.html', item_list=numbers, title='SK 쉴더스 루키즈 플라스크', heading='환영합니다!', content='동적 페이지 연습')

@app.route("/hello12345")
def hello_world():
    return "<h1>Hello, World! TEST EDIT 1234</h1>"

@app.route('/hello')
def hello():
    return "Hello, World!"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {username}'

@app.route('/post/<int:post_idx>')
def show_post(post_idx):
    return f"게시글 번호 {int:post_idx}"

@app.route('/user/<username>/<int:post_id>')
def show_user_profile(username, post_id):
    return f'사용자 {escape(username)} 게시글 번호 {post_id}'

if __name__ == "__main__":
    app.run(debug=True)