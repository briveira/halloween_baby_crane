import pygame
import time
import random
import threading
import RPi.GPIO as GPIO


# GPIO mode

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# load wav files in pygame

pygame.mixer.init(buffer=2048)
cries = [pygame.mixer.Sound("sounds/lloro_1.wav"), pygame.mixer.Sound("sounds/lloro_2.wav"), pygame.mixer.Sound("sounds/lloro_3.wav")]

# set Sound volumes to 1.0

for cry in cries:
    cry.set_volume(1.0)


creaks = [pygame.mixer.Sound("sounds/chirrido_1.wav"), pygame.mixer.Sound("sounds/chirrido_2.wav")]

# set Sound volumes to 1.0

for creak in creaks:
    creak.set_volume(0.4)


# launch sound of baby cry in background

def launch_sound_of_baby_cry_in_background():
    cries[random.randint(0, len(cries)-1)].play()
    print("launched crying effect...")


# launch sound of creak in background

def launch_sound_of_wheelchair_creak_in_background():
    creaks[random.randint(0, len(creaks)-1)].play()
    print("launched wheelchair creak effect...")


# background sound and effects

def launch_background_music():

    print("Launching background thread with infinite music... and crying effects")

    # start music
    pygame.mixer.music.load("sounds/musica.mp3")

    # start music at 1.0 volume
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    print("background music started (looped)...")


# background loop of crying effects

def infinite_loop_music():

    launch_background_music()

    # music loop with sound effects
    while True:
        try:
            # random wait time
            time.sleep(random.uniform(20, 30))

            # play random cry from cries array
            launch_sound_of_baby_cry_in_background()
            
        except KeyboardInterrupt: # break if control + c is pressed
            break


# start infinite loop music in background thread

def launch_background_thread_with_infinite_music():
    background_thread = threading.Thread(target=infinite_loop_music)
    background_thread.daemon = True
    background_thread.start()    


# full circle stepper motor movement function

def move_stepper_motor_forward_full_circle(control_pins):

    # define step sequences
    halfstep_seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
    ]

    # loop through step sequences
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)


# function to move stepper motor in background using GPIO

def stepper_motor_movement():
    
    print("Launching background thread with stepper motor movement...")
    
    # set GPIO mode to BOARD
    GPIO.setmode(GPIO.BOARD)

    # set GPIO pins
    control_pins = [7,11,13,15]

    # set GPIO pins as output
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
        
    while True:    
        # background sound
        launch_sound_of_wheelchair_creak_in_background()
        move_stepper_motor_forward_full_circle(control_pins)
        move_stepper_motor_forward_full_circle(control_pins)
        move_stepper_motor_forward_full_circle(control_pins)
        move_stepper_motor_forward_full_circle(control_pins)
        time.sleep(15)



# launch another background thread for checking distance sensor with GPIO

def launch_background_thread_with_stepper_motor_movement():
    background_thread = threading.Thread(target=stepper_motor_movement)
    background_thread.daemon = True
    background_thread.start()


# relay status

relay_state = False

# activate / deactivate relay 

def activate_relay(state):
    global relay_state
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, state)
    relay_state = state
    print("Relay state: " + str(relay_state))
    

# toggle relay 

def toogle_relay_state():
    activate_relay(not relay_state)


# toggle relay state randomly every second

def toggle_relay_state_randomly():
    while True:
        time.sleep(2)
        if random.choice([True, False, False, False]):
            toogle_relay_state()


# launch another background thread for changing relay state in random

def launch_background_thread_with_relay_state_changing():
    background_thread = threading.Thread(target=toggle_relay_state_randomly)
    background_thread.daemon = True
    background_thread.start()


# main process start

if __name__ == "__main__":
    launch_background_thread_with_infinite_music()
    launch_background_thread_with_stepper_motor_movement()
    launch_background_thread_with_relay_state_changing()
    try:
        while True:
            time.sleep(1)
    finally:
        GPIO.cleanup()