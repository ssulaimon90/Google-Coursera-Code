def count(number):
    number = 1
    while number <= 7:
        print(number, end=" ")
        number += 1
    return number


result = count(5)
print("result is " + str(result))