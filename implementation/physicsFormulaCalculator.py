def bmicalci():
    Height=float(input("Enter your height in centimeters: "))
    Weight=float(input("Enter your Weight in Kg: "))
    Height = Height/100
    BMI=Weight/(Height*Height)
    print("your Body Mass Index is: ",BMI)
    if(BMI>0):
        if(BMI<=16):
            print("you are severely underweight")
        elif(BMI<=18.5):
            print("you are underweight")
        elif(BMI<=25):
            print("you are Healthy")
        elif(BMI<=30):
            print("you are overweight")
        else: print("you are severely overweight")
    else:("enter valid details")

def celciustofarenheit():
    s = int(input("Enter the farehneit : "))
    f = float(s)
    c = (f - 32) * 5/9
    print(c)

def farenheittocelius():
    s = int(input("Enter the farehneit : "))
    f = float(s)
    c = (f - 32) * 5/9
    print(c)

def operation():
    print("Please enter 1 for BMI Calculator")
    print("Please enter 2 for celcius to farenheit Calculator")
    print("Please enter 3 for farenheit to celcius Calculator")
    num = int(input("Enter the number according to the formula you want : "))
    if(num == 1):
        bmicalci() 
    elif(num == 2):
        celciustofarenheit()
    elif(num == 3):
        farenheittocelius()
    # elif num == 4:
       # performIntegerDivision()
    #elif num == 5:
     #   performMultiplication()
    return

def main():
    while(True):
        operation()

if __name__ == "__main__":
    main()
