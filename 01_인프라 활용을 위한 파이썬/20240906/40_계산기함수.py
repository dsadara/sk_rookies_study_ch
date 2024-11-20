def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "multi":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "분모에 0을 사용할 수 없습니다"
        return a / b
    else:
        return "유효하지 않은 연산자입니다"
    

input_data = input("연산자와 두 수를 입력하세요. (예 add 5 3):")
input_list = input_data.split()

operation = input_list[0]
num1 = int(input_list[1])
num2 = int(input_list[2])

print(calculator(operation, num1, num2))

    
