def bmicalci(Height,Weight):
    Height = Height/100
    BMI=Weight/(Height*Height)
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
    return BMI

def celciustofarenheit(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

def farenheittocelius(s):
    c = float(s)
    f = (c * 9 / 5) + 32 
    return f

def cal_speed(dist,time):
    ans = dist / time
    return ans

def cal_acceleration(initialVelocity,finalVelocity):
    time = float(int(input("Enter the time")))
    acceleration = (finalVelocity - initialVelocity) / time
    return acceleration

def cal_density(mass,volume):
    ans = mass / volume
    return ans

def cal_force(mass,acc):
    ans = mass * acc
    return ans

def cal_power(work,time):
    ans = work / time
    return ans

def cal_weight(mass,acc):
    ans = mass * acc
    return ans

def cal_pressure(force,area):
    ans = force / area
    return ans

def cal_Kineticenergy(mass,velocity):
    ans = (mass * velocity * velocity) / 2
    return ans

def cal_ohmslaw(current,resistance):
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
    with open("input.txt") as f: 
        print(f.read())
    num = input("Enter the number according to the formula you want : ")
    if(num == "1"):
        Height = float(input("Enter your height in centimeters: "))
        Weight = float(input("Enter your Weight in Kg: "))
        print(bmicalci(Height,Weight)) 
    elif(num == "2"):
        s = int(input("Enter the farehneit : "))
        print(celciustofarenheit(s))
    elif(num == "3"):
        s = int(input("Enter the celcius : "))
        print(farenheittocelius(s))
    elif(num == "4"):
        dist = float(input("Enter the distance : "))
        time = float(input("Enter the time : "))
        print(cal_speed(dist,time))    
    elif(num == "5"):
        initialVelocity = float(input("Enter the initial velocity : "))
        finalVelocity = float(input("Enter the final velocity : "))
        print(cal_acceleration(initialVelocity,finalVelocity))
    elif(num == "6"):
        mass = float(input("Enter the distance : "))
        volume = float(input("Enter the time : "))
        print(cal_density(mass,volume)) 
    elif(num == "7"):
        mass = float(input("Enter the Mass of the body : "))
        acc = float(input("Enter the Acceleration in velocity available : "))
        print(cal_force(mass,acc))
    elif(num == "8"):
        work = float(input("Enter the work : "))
        time = float(input("Enter the time : "))
        print(cal_power(work,time))
    elif(num == "9"):
        mass = float(input("Enter the Mass of the body : "))
    a   acc = float(input("Enter the Acceleration due to gravity : "))
        cal_weight(mass,acc)    
    elif(num == "10"):
        force = float(input("Enter the Force applied : "))
        area = float(input("Enter the Total Area of the object : "))
        print(cal_pressure(force,area))
    elif(num == "11"):
        mass = float(input("Enter the Mass of the body : "))
        velocity = float(input("Enter The velocity with which the body is traveling : "))
        print(cal_Kineticenergy(mass,velocity)) 
    elif(num == "12"):
        current = float(input("Enter the Mass of the body : "))
        resistance = float(input("Enter The velocity with which the body is traveling : "))
        print(cal_ohmslaw(current,resistance))
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