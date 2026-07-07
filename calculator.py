print("This only accepts number form(intergers and decimals) and * for times, + for plus, / for divide and - for minus (there is no square root or other).")
first_number = (input ("first number?:"))
operation = (input ("operation?:"))
second_number = (input ("second number?:"))

try :


    if operation == ("*") :
        answer = float(first_number) * float(second_number)
    elif operation == ("+") :
        answer = float(first_number) + float(second_number)
    elif operation == ("-") :
        answer = float(first_number) - float(second_number)
    elif operation == ("/") :
        answer = float(first_number) / float(second_number)
    else :
        print ("Invalid operation!")
        quit() 

    print(answer)
except ValueError:
    print("This only accepts number form(intergers and decimals) and * for times, + for plus, / for divide and - for minus (there is no square root or other).")
except ZeroDivisionError:
    print("No dividing by zero / 0")