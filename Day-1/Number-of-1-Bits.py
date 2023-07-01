def decimalToBinary(N):
    return bin(N).replace("0b", "")
N = input("Enter a number: ")
binary = decimalToBinary(N)
count = 0
for i in binary:
    if i == "1":
        count += 1
print(count)
