"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic


def main():
    while True:
        print "Calculate!"
        
        success = False         #when operation is performed success==True
        
        user_input = raw_input("> ")

        token = user_input.split(" ")   # separate different parts of operation
        
        # check  length of the [token] list to set the variables appropriately
        # make sure that token[1] and token[2] are digits
        # rename token[1] and token[2] as num1 and num2
        if len(token) == 1:
            pass
        elif len(token) == 2:
            if(token[1].isdigit() == False):
                print "Number should be in digit format"
            else:
                num1 = int(token[1])
        else:
            if(token[1].isdigit() == False or token[2].isdigit() == False):
                print "Number should be in digit format"
            else:
                num1 = int(token[1])
                num2 = int(token[2])
                
        # allow user to quit the program
        if token[0] == "q":
            break
        
        # begin arithmetic calculations
        elif token[0] == "+":
            output = arithmetic.add(num1, num2)
            success = True
            
        elif token[0] == "-":
            output = arithmetic.subtract(num1, num2)
            success = True

        elif token[0] == "*":
            output = arithmetic.multiply(num1, num2)
            success = True

        elif token[0] == "/":
            output = arithmetic.divide(num1, num2)
            success = True

        elif token[0] == "square":
            output = arithmetic.square(num1)
            success = True

        elif token[0] == "cube":
            output = arithmetic.cube(num1)
            success = True

        elif token[0] == "pow":
            output = arithmetic.power(num1, num2)
            success = True

        elif token[0] == "mod":
            output = arithmetic.mod(num1, num2)
            success = True
        
        else:
            print "I don't understand. Try again."

        if success == True:
            print output   

    # Your code goes here
    


if __name__ == '__main__':
    main()