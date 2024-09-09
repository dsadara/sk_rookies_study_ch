# read()로 출력

with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.read()
    print(content)


# readline() 한줄씩 출력
with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.readline()
    print(content)
    content = helloFile.readline()
    print(content)
    content = helloFile.readline()
    print(content)

# readlines() 리스트로 출력

with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.readlines()
    print(content)