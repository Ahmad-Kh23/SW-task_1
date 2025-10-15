


z = str

while z != 'q':
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        print(f"x + y = {x + y}")
        z = input("Press 'q' to quit or any other key to continue: ")
        if z.lower() == 'q':
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue