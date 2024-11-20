#1 

text = "   Extra spaces   "
print(text.strip().upper())


#2

text = "one,two,three,four"
print('&'.join(text.split(',')))

#3

filename = input("Enter the file name: ")
extensions = ('.png', '.jpg', '.jpeg', '.gif') # 화이트리스트

if filename.endswith(extensions):
    print("Image file detected")
else:
    print("Not an image file")