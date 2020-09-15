user_input = input()

order = ['8', '5', '2', '4', '3', '7', '6', '1', '0', '9']

temp = []
for chr in user_input.split(' '):
    temp.append((order.index(chr), chr))

for num in sorted(temp):
    print(num[1], end=' ')
