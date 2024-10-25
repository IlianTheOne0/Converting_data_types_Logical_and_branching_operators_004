number = str(input('Four-digit number: '))

if len(number) == 4:
    result = number[1] + number[0] + number[3] + number[2]

    print(result)
else:
    print('Error: The number is not four-digit')