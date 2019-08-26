# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #BCM


#BRUSHLESS = 11
#MIN_BRUSHLESS=780
#MAX_BRUSHLESS=1500
MIN_POT=0
MAX_POT=1023

# freely chosen SPI pins
SPICLK  =   16   # BCM 16 BOARD 36
SPIMISO =   19   # BCM 19 BOARD 35
SPIMOSI =   20   # BCM 20 BOARD 38
SPICS   =   25   # BCM 25 BOARD 22

GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)


#GPIO.setup(BRUSHLESS, GPIO.OUT)


ESC=4  #Connect the ESC in this GPIO pin

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC, 0)
potentiometer_adc = 0
trim_pot=0

max_value = 1250 #change this if your ESC's max value is different or leave it be
min_value = 700 #change this if your ESC's min value is different or leave it be
print ("For first time launch, select calibrate")
print ("Type the exact word for the function you want")
print ("calibrate OR calibrate_omersway OR manual OR control OR control_omersway OR arm OR stop")

def readadc(adcnum, clockpin, mosipin, misopin, cspin):  #adcout veriyor
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

def read_potentiometer():
    trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    return round(trim_pot / 1024.0, 2)


def manual_drive(): #You will use this function to program your ESC if required
    print ("You have selected manual option so give a value between 0 and you max value")
    while True:
        inp = raw_input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break
        else:
            pi.set_servo_pulsewidth(ESC,inp)

def map(x, in_min, in_max, out_min, out_max):
        float(x)
        return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def calibrate():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control() # You can change this to any other function you want

def calibrate_omersway():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control_omersway() # You can change this to any other function you want


def control():
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 1600    # change your speed if you want to.... it should be between 700 - 2000
    print ("Controls - s to decrease speed & d to increase speed OR z to decrease a lot of speed & a to increase a lot of speed")
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = raw_input()

        if inp == "z":
            speed -= 100    # decrementing the speed like hell
            print ("speed = %d" % speed)
        elif inp == "a":
            GPIO.cleanup()
            stop()
            speed += 100    # incrementing the speed like hell
            print ("speed = %d" % speed)
        elif inp == "d":
            speed += 10     # incrementing the speed
            print ("speed = %d" % speed)
        elif inp == "s":
            speed -= 10     # decrementing the speed
            print ("speed = %d" % speed)
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break
        else:
            print ("WHAT DID I SAID!! Press a,z,d or s")

def control_omersway():
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(3)
    while True:
        trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        speed = map(trim_pot,MIN_POT,MAX_POT,min_value,max_value)

        print("trim_pot:", trim_pot)
        #print("normalized: ", round(trim_pot / 1024.0, 2))

        print("Motor Speed: ", speed)

        pi.set_servo_pulsewidth(ESC, speed)
        #print("normalized: ", round(trim_pot / 1024.0, 2))



        #if inp == "stop":
        #    GPIO.cleanup()
        #    stop()          #going for the stop function
        #    break
        #elif inp == "manual":
        #    manual_drive()
        #    break
        #elif inp == "arm":
        #    arm()
        #    break
        #else:
        #    print ("Control with potentiometer")


def arm(): #This is the arming procedure of an ESC
    print ("Connect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        control_omersway()

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.
inp = raw_input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "control_omersway":
    control_omersway()
elif inp == "calibrate_omersway":
    calibrate_omersway()
elif inp == "stop":
    stop()
else :
    print ("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")
