first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

operation = int(input(
  "What you want to perform? \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponential \n Enter the number - "
))


if (operation == 1):
  print(int(first_num) + int(second_num))
elif operation == 2:
  print(int(first_num) - int(second_num))
elif operation == 3:
  print(int(first_num) * int(second_num))
elif operation == 4:
  print(first_num / second_num)
elif operation == 5:
  print(first_num**second_num)
