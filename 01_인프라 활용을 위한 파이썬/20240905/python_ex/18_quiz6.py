#1
text=input("데이터를 입력하세요:")

if len(text) < 1:
    print("empty string")
elif text[0] == 'a':
    print("first char is a")
    if len(text) >= 2 and text[1] == 'x':
        print("second char is x")
elif text[0] == 'b':
    print("first char is b")
    if len(text) >= 2 and text[1] == 'o':
        print("second char is x")
