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
    else:
        print("enter valid details")

def celciustofarenheit():
    s = int(input("Enter the farehneit : "))
    f = float(s)
    c = (f - 32) * 5/9
    print("The farenheit of {} is {} celcius ".format(f,c))

def farenheittocelius():
    s = int(input("Enter the celcius : "))
    c = float(s)
    f = (c * 9 / 5) + 32 
    print("The celcius of {} is {} farenheit".format(c,f))

def cal_speed():
    dist = float(input("Enter the distance"))
    time = float(input("Enter the time"))
    ans = dist / time
    print("The speed is  : ", ans)

def cal_acceleration():
    initialVelocity = float(input("Enter the initial velocity"))
    finalVelocity = float(input("Enter the final velocity"))
    time = float(int(input("Enter the time")))
    acceleration = (finalVelocity - initialVelocity) / time
    print("Acceleration = ", acceleration)

def operation():
    print("Please enter 1 for BMI Calculator")
    print("Please enter 2 for celcius to farenheit Calculator")
    print("Please enter 3 for farenheit to celcius Calculator")
    print("Please enter 4 for Speed Calculation")
    print("Please enter 5 for acceleration  Calculation")
    print("Please enter 6 to stop")
    num = int(input("Enter the number according to the formula you want : "))
    if(num == 1):
        bmicalci() 
    elif(num == 2):
        celciustofarenheit()
    elif(num == 3):
        farenheittocelius()
    elif(num == 4):
        cal_speed()    
    elif(num == 5):
        cal_acceleration()
    else:
        exit(1)
    return True

def main():
    ans = True
    while(ans):
        ans = False
        ans = operation()

if __name__ == "__main__":
    main()