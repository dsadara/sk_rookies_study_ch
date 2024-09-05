x = 20
if x > 10:
    print("x는 10보다 큽니다.")
else:
    print("x는 10이하입니다.")

# elif 적용 전

x = 3
if x > 10:
    print("x는 10보다 큽니다.")
else:
    if x > 5:
        print("x는 5보다 크고 10 이하입니다.")
    else:
        print("x는 5이하입니다.")


# elif 적용 후

x = 3
if x > 10:
    print("x는 10보다 큽니다.")
elif x > 5:
    print("x는 5보다 크고 10 이하입니다.")
else:
    print("x는 5이하입니다.")

