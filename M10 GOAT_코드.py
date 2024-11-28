import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
print("max1mizer")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("cho gi hwa")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            stop = time.time()
        
        check_time = stop - start
        d = check_time * 34300 / 2
        print("distance from the door : %.1f mm" % d)
        time.sleep(0.04)

        if d < 10000:
            ledpin = 17
            buzzer = 18
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(buzzer, GPIO.OUT)
            GPIO.setup(ledpin, GPIO.OUT)
            GPIO.setwarnings(False)

            pwm = GPIO.PWM(buzzer, 500)
            pwm.start(50.0)
            time.sleep(0.5)
            GPIO.output(ledpin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(ledpin, GPIO.LOW)

            pwm.stop()

            # RuntimeError : A PWM  object already exists for this GPIO channel: 이거 뜨면 중복된 GPIO.cleanup() 찾아서 하나로 만들기

except KeyboardInterrupt:
    print("KeyboardInterrupt")
    GPIO.cleanup()