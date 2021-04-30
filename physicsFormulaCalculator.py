'''
@Brief: Function to calculate BMI
@Parameter : float operand1, float operand2
@return: Calculated value of BMI
'''
def bmicalci(Weight,Height):
    Height = Height/100
    BMI=Weight/(Height*Height)
    return BMI

'''
@Brief: Function to convert celcius to farenheit
@Parameter : float operand1
@return: calculated value of farenheit 
'''
def celciustofarenheit(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c


'''
@Brief: Function to convert farenheit to celcius
@Parameter : float operand1
@return: calculated value of celcius
'''
def farenheittocelius(s):
    c = float(s)
    f = (c * 9 / 5) + 32 
    return f

'''
@Brief: Function to calculate speed
@Parameter : float operand1, float operand2
@return: Calculated value of speed
'''
def cal_speed(dist,time):
    ans = dist / time
    return ans

'''
@Brief: Function to calculate BMI
@Parameter : float operand1, float operand2, float operand3
@return: Calculated value of acceleration
'''
def cal_acceleration(initialVelocity,finalVelocity,time): 
    acceleration = (finalVelocity - initialVelocity) / time
    return acceleration

'''
@Brief: Function to calculate density
@Parameter : float operand1, float operand2
@return: Calculated value of density
'''
def cal_density(mass,volume):
    ans = mass / volume
    return ans

'''
@Brief: Function to calculate force
@Parameter : float operand1, float operand2
@return: Calculated value of force
'''
def cal_force(mass,acc):
    ans = mass * acc
    return ans

'''
@Brief: Function to calculate power
@Parameter : float operand1, float operand2
@return: Calculated value of power
'''
def cal_power(work,time):
    ans = work / time
    return ans

'''
@Brief: Function to calculate weight
@Parameter : float operand1, float operand2
@return: Calculated value of weight
'''
def cal_weight(mass,acc):
    ans = mass * acc
    return ans

'''
@Brief: Function to calculate pressure
@Parameter : float operand1, float operand2
@return: Calculated value of pressure
'''
def cal_pressure(force,area):
    ans = force / area
    return ans

'''
@Brief: Function to calculate Kinetic energy
@Parameter : float operand1, float operand2
@return: Calculated value of Kinetic energy
'''
def cal_Kineticenergy(mass,velocity):
    ans = (mass * velocity * velocity) / 2
    return ans

'''
@Brief: Function to calculate ohms law
@Parameter : float operand1, float operand2
@return: Calculated value of ohms law
'''
def cal_ohmslaw(current,resistance):
    ans = current * resistance
    return ans

'''
@Brief: Function to calculate frequency
@Parameter : float operand1, float operand2
@return: Calculated value of frequency
'''
def cal_frequency(velocity,wavelength):
    ans = velocity / wavelength
    return ans

'''
@Brief: Function to calculate capacitance
@Parameter : float operand1, float operand2
@return: Calculated value of capacitance
'''
def capacitance(charge,voltage):
    ans = charge / voltage
    return ans

'''
@Brief: Function to calculate gravity
@Parameter : float operand1, float operand2, float operand3
@return: Calculated value of gravity
'''
def gravity(mass1,mass2,distance):
    grav = ( mass1 * mass2) / distance
    return grav

'''
@Brief: Function to convert kmph to mps
@Parameter : float operand1
@return: converted value is given i.e mps
'''
def con_kmph_ms(kmph):
    mps =  0.27777777777 * kmph
    return mps

'''
@Brief: Function to convert mps to kmph 
@Parameter : float operand1
@return: converted value is given i.e kmph
'''
def con_ms_kmph(mps):
    kmph = mps * 3.6
    return kmph

def operation():
    with open("input.txt") as f: 
        print(f.read())
    num = input("Enter the number according to the formula you want : ")
    if(num == "1"):
        Weight = float(input("Enter your Weight in Kg: "))
        Height = float(input("Enter your height in centimeters: "))
        print("The BMI index {} ".format(bmicalci(Height,Weight))) 
    elif(num == "2"):
        s = float(input("Enter the farehneit : "))
        print("The conversion from celcius to farenheit and the farenheit value is {} F".format(celciustofarenheit(s)))
    elif(num == "3"):
        s = float(input("Enter the celcius : "))
        print("The conversion from farenheit to celcius and the Celcius value is {} C".format(farenheittocelius(s)))
    elif(num == "4"):
        dist = float(input("Enter the distance : "))
        time = float(input("Enter the time : "))
        print("The speed is {} m/s".format(cal_speed(dist,time)))    
    elif(num == "5"):
        initialVelocity = float(input("Enter the initial velocity : "))
        finalVelocity = float(input("Enter the final velocity : "))
        time = float(int(input("Enter the time : ")))
        print("The acceleration is {} m/s2".format(cal_acceleration(initialVelocity,finalVelocity)))
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
        acc = float(input("Enter the Acceleration due to gravity : "))
        print(cal_weight(mass,acc))
    elif(num == "10"):
        force = float(input("Enter the Force applied : "))
        area = float(input("Enter the Total Area of the object : "))
        print(cal_pressure(force,area))
    elif(num == "11"):
        mass = float(input("Enter the Mass of the body : "))
        velocity = float(input("Enter The velocity with which the body is traveling : "))
        print(cal_Kineticenergy(mass,velocity)) 
    elif(num == "12"):
        current = float(input("Enter the current : "))
        resistance = float(input("Enter The resistance : "))
        print(cal_ohmslaw(current,resistance))
    elif(num == "13"):
        velocity = float(input("Enter the Velocity : "))
        wavelength = float(input("Enter the wavelength of the wave : "))
        print(cal_frequency(velocity,wavelength))
    elif(num == "14"):
        charge = float(input("Enter the Charge : "))
        voltage = float(input("Enter the Voltage : "))
        print("The capacitance : {} ".format(capacitance(charge,voltage)))    
    elif(num == "15"):
        mass1 = float(input("Enter the mass of the first Object : "))
        mass2 = float(input("Enter the mass of the second object : "))
        distance = float(input("Enter the distance between the object : "))
        print("The gravity : {} G ".format(gravity(mass1,mass2,distance)))
    elif(num == "16"):
        kmph = float(input("Enter the kmph : "))
        print(con_kmph_ms(kmph))    
    elif(num == "17"):
        mps = float(input("Enter the mps : "))
        print(con_ms_kmph(mps))
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