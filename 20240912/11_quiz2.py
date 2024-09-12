from flask import Flask, render_template
import requests

app = Flask(__name__)

def request_age():
    # name=input("이름을 입력하시오: ")
    r = requests.get(f'https://api.agify.io/?name=chaehyun')
    return r.json()

@app.route('/')
def index():
    result = request_age()
    return render_template('index.html', items=result)

if __name__ == "__main__":
    app.run(debug=True)