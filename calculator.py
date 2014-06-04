"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic


def main():
    while True:
        print "Calculate!"
        user_input = raw_input("> ")

        token = user_input.split(" ")
        
        if len(token) == 1:
            pass
        elif len(token) == 2:
            num1 = int(token[1])
        else:
            num1 = int(token[1])
            num2 = int(token[2])

        if token[0] == "q":
            break
        elif token[0] == "+":
            output = arithmetic.add(num1, num2)
            
        elif token[0] == "-":
            output = arithmetic.subtract(num1, num2)
         
        elif token[0] == "*":
            output = arithmetic.multiply(num1, num2)
        
        elif token[0] == "/":
            output = arithmetic.divide(num1, num2)

        elif token[0] == "square":
            output = arithmetic.square(num1)

        elif token[0] == "cube":
            output = arithmetic.cube(num1)

        elif token[0] == "pow":
            output = arithmetic.power(num1, num2)

        elif token[0] == "mod":
            output = arithmetic.mod(num1, num2)

        else:
            print "I don't understand. Try again."

        print output   

    # Your code goes here
    


if __name__ == '__main__':
    main()