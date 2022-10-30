def add_nums(num1, num2):
    return num1+num2

def subtract_nums(num1, num2):
    return num1-num2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    done = False
    menu = 'Options menu\n' \
           '-----------------------\n' \
           '1. Add two numbers\n' \
           '2. Subtract two numbers\n' \
           '3. Exit\n'

    valid_choices = [1,2,3]

    while not done:
        print(menu)
        valid = False
        while not valid:
            choice = int(input('Please select an option: '))
            if choice not in valid_choices:
                print('Invalid choice.\n')
                continue
            else:
                valid = True
        if choice == 1:
            num1 = int(input('Input a number: '))
            num2 = int(input('Input another number: '))
            print(f'The sum of your numbers is: {add_nums(num1, num2)}')
            print()
        elif choice == 2:
            num1 = int(input('Input a number: '))
            num2 = int(input('Input another number: '))
            print(f'The difference of your numbers is: {subtract_nums(num1, num2)}')
            print()
        elif choice == 3:
            done = True

