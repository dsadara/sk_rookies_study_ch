from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/list')
def file_list():
    files = os.listdir(r'C:\python_ex\file_upload')
    return render_template("file_list.html", files=files)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('file_upload', filename)
    return send_file(file_path, as_attachment=True)

# 이 코드는 스크립트가 직접 실행될 때만 실행됨
if __name__ == '__main__':
    app.run(debug=True)