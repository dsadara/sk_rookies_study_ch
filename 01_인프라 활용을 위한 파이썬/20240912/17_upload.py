from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 하드코딩된 사용자 정보
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

@app.route('/')
def upload():
    return render_template("upload.html")

# 단일 파일 저장
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['file']
#     file_path = os.path.join('file_upload', file.filename)
#     file.save(file_path)
#     return f"File Upload Success {file.filename}"

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('files')

    for file in files:
        file_path = os.path.join('file_upload', file.filename)
        file.save(file_path)

    return f"File Upload Success"
    
# 이 코드는 스크립트가 직접 실행될 때만 실행됨
if __name__ == '__main__':
    app.run(debug=True)