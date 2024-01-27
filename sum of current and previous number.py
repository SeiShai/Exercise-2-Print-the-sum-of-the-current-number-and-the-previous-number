# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

# starting number
previous_number = 0

# iterations
for i in range(1,11):
    sum = previous_number + i
    print('current number ',i , 'previous number ',previous_number ,'sum:', sum)
    previous_number = i


