# for문을 사용한 경우
total_for = 0
output_for = ""

for i in range(1, 101):
    total_for += i
    if i < 100:
        output_for += str(i) + "+"
    else:
        output_for += str(i)

output_for += " = " + str(total_for)
print(output_for)
print()

# while문을 사용한 경우
total_while = 0
output_while = ""
i = 1

while i <= 100:
    total_while += i
    if i < 100:
        output_while += str(i) + "+"
    else:
        output_while += str(i)
    i += 1

output_while += " = " + str(total_while)
print(output_while)
print()
