def menu():
    
    while True:
        
        value = input('Enter 1/add - addition || 2/sub - subtraction || 3/mul - multiplication || 4/div - division || 5/square - square || 6/cube - cube || other\'s to exit : ')
        
        if value == '1' or value.lower() == 'add' :
            num1 = float(input('Enter num1 : '))
            num2 = float(input('Enter num2 : '))
            print(f'{num1} + {num2} = {num1 + num2}')

        elif value == '2' or value.lower() == 'sub' :
            num1 = float(input('Enter num1 : '))
            num2 = float(input('Enter num2 : '))
            print(f'{num1} - {num2} = {num1 - num2}')
        
        elif value == '3' or value.lower() == 'mul' :
            num1 = float(input('Enter num1 : '))
            num2 = float(input('Enter num2 : '))
            print(f'{num1} X {num2} = {num1 * num2}')
        
        elif value == '4' or value.lower() == 'div' :
            num1 = float(input('Enter num1 : '))
            num2 = float(input('Enter num2 : '))
            if num2 == 0:
                print('Division by Zero Error !!')
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
                
        elif value == '5' or value.lower() == 'square' :
            number = float(input('Enter a number to square it : '))
            print(number ** 2)
        
        elif value == '6' or value.lower() == 'cube':
            number = float(input('Enter a number to cube it : '))
            print(number ** 3)
        
        else:
            print('Invalid option !!')
            return

menu()
