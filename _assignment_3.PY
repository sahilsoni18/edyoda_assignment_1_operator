
numbers = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 15, 16, 18, 19, 20)
count_odd = 0
count_even = 0
for x in numbers:
    if x % 2 == 0:
        count_even+= 1
    else:
        count_odd += 1

print("Numbers of even numbers : ", count_even)
print("Numbers of odd numbers : ", count_odd)