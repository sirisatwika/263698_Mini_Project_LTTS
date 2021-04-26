def resultfun(ans):
    with open("output.txt","w") as file:
        file.write(str(ans))
    exit(0)
    
def bmicalci():
    Height = float(input("Enter your height in centimeters: "))
    Weight = float(input("Enter your Weight in Kg: "))
    Height = Height/100
    BMI=Weight/(Height*Height)
    resultfun(BMI)
    if(BMI>0):
        if(BMI<=16):
            print("you are severely underweight\n")
        elif(BMI<=18.5):
            print("you are underweight\n")
        elif(BMI<=25):
            print("you are Healthy\n")
        elif(BMI<=30):
            print("you are overweight\n")
        else: print("you are severely overweight\n")
    else:
        print("enter valid details\n")

def celciustofarenheit():
    s = int(input("Enter the farehneit : "))
    f = float(s)
    c = (f - 32) * 5/9
    resultfun(c)

def farenheittocelius():
    s = int(input("Enter the celcius : "))
    c = float(s)
    f = (c * 9 / 5) + 32 
    resultfun(f)

def cal_speed():
    dist = float(input("Enter the distance : "))
    time = float(input("Enter the time : "))
    ans = dist / time
    resultfun(ans)

def cal_acceleration():
    initialVelocity = float(input("Enter the initial velocity : "))
    finalVelocity = float(input("Enter the final velocity : "))
    time = float(int(input("Enter the time")))
    acceleration = (finalVelocity - initialVelocity) / time
    resultfun(acceleration)

def cal_density():
    mass = float(input("Enter the distance : "))
    volume = float(input("Enter the time : "))
    ans = mass / volume
    resultfun(ans)

def cal_force():
    mass = float(input("Enter the Mass of the body : "))
    acc = float(input("Enter the Acceleration in velocity available : "))
    ans = mass * acc
    resultfun(ans)

def cal_power():
    work = float(input("Enter the work : "))
    time = float(input("Enter the time : "))
    ans = work / time
    resultfun(ans)

def cal_weight():
    mass = float(input("Enter the Mass of the body : "))
    acc = float(input("Enter the Acceleration due to gravity : "))
    ans = mass * acc
    resultfun(ans)

def cal_pressure():
    force = float(input("Enter the Force applied : "))
    area = float(input("Enter the Total Area of the object : "))
    ans = force / area
    resultfun(ans)

def cal_Kineticenergy():
    mass = float(input("Enter the Mass of the body : "))
    velocity = float(input("Enter The velocity with which the body is traveling : "))
    ans = (mass * velocity * velocity) / 2
    resultfun(ans)

def cal_ohmslaw():
    current = float(input("Enter the Mass of the body : "))
    resistance = float(input("Enter The velocity with which the body is traveling : "))
    ans = current * resistance
    resultfun(ans)

def cal_frequency():
    velocity = float(input("Enter the Velocity : "))
    wavelength = float(input("Enter the wavelength of the wave : "))
    ans = velocity / wavelength
    resultfun(ans)

def con_kmph_ms():
    kmph = float(input("Enter the kmph : "))
    mps =  0.27777777777 * kmph
    resultfun(mps)

def con_ms_kmph():
    mps = float(input("Enter the mps : "))
    kmph = mps * 3.6
    resultfun(kmph)

def operation():
    print("Please enter 1 for BMI Calculator")
    print("Please enter 2 for celcius to farenheit Calculator")
    print("Please enter 3 for farenheit to celcius Calculator")
    print("Please enter 4 for Speed Calculation")
    print("Please enter 5 for acceleration  Calculation")
    print("Please enter 6 for density Calculator")
    print("Please enter 7 for force Calculator")
    print("Please enter 8 for power to celcius Calculator")
    print("Please enter 9 for weight Calculation")
    print("Please enter 10 for pressure  Calculation")
    print("Please enter 11 for kinetic Energy  Calculation")
    print("Please enter 12 for ohms  Calculation")
    print("Please enter 13 for frequency  Calculation")
    print("Please enter 14 for kmph to m/s  Conversion")
    print("Please enter 15 for m/s to kmph Conversion")
    print("Please enter any key to stop")
    num = input("Enter the number according to the formula you want : ")
    if(num == "1"):
        bmicalci() 
    elif(num == "2"):
        celciustofarenheit()
    elif(num == "3"):
        farenheittocelius()
    elif(num == "4"):
        cal_speed()    
    elif(num == "5"):
        cal_acceleration()
    elif(num == "6"):
        cal_density() 
    elif(num == "7"):
        cal_force()
    elif(num == "8"):
        cal_power()
    elif(num == "9"):
        cal_weight()    
    elif(num == "10"):
        cal_pressure()
    elif(num == "11"):
        cal_Kineticenergy() 
    elif(num == "12"):
        cal_ohmslaw()
    elif(num == "13"):
        cal_frequency()
    elif(num == "14"):
        con_kmph_ms()    
    elif(num == "15"):
        con_ms_kmph()
    else:
        exit(1)
    return True

def main():
    a = True
    while(a):
        a = False
        a = operation()

if __name__ == "__main__":
    main()