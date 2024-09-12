import os
import zipfile
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

# 업로드 폴더 설정
UPLOAD_FOLDER = 'file_upload'
ZIP_FOLDER = 'zips'

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)  # 업로드 폴더에서 파일 목록 가져오기
    return render_template('select_files.html', files=files)  # 파일 선택 페이지 렌더링

@app.route('/download', methods=['POST'])
def download_selected_files():
    selected_files = request.form.getlist('files')  # 선택된 파일들 가져오기
    if not selected_files:
        return 'No files selected'  # 선택된 파일이 없을 경우 처리
    
    # 선택된 파일들을 압축
    zip_filename = os.path.join(ZIP_FOLDER, 'selected_files.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for filename in selected_files:
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            zipf.write(file_path, filename)
    
    # 압축 파일 전송
    return send_file(zip_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)