from flask import Flask, render_template
from markupsafe import escape
import random

app = Flask(__name__)


@app.route('/')
def index():
    random_int = random.randint(1, 100)
    return render_template('index.html', title='난수 생성 페이지',
    heading='난수 생성 페이지', content=f"동적 페이지 연습",
    random_number=random_int)

if __name__ == "__main__":
    app.run(debug=True)