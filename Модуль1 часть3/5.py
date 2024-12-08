num_1 = int(input("Введите число: "))

digit = num_1 % 10
num_2 = digit

num_1 = num_1 // 10

while num_1 > 0:
    digit = num_1 % 10
    num_1 = num_1 // 10
    num_2 = num_2 * 10
    num_2 = num_2 + digit

print(num_2)