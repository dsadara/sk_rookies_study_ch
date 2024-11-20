import zipfile
import os

def zip_file(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                zipf.write(file_path)

zip_file('static', 'static_output.zip')