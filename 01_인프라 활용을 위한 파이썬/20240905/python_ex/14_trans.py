from googletrans import Translator

text=input("한글 입력:")

translator = Translator()

translated = translator.translate(text, dest="ja")

print(f"한글 입력 값: {text}")
print(f"번역 결과 값: {translated.text}")
