# halloween_baby_crane

Small raspberry pi project for Halloween: a moving crane with a stepper motor, sound with baby cries, cracks, background music and random on/off light operated with a relay for an automated crane in a horror setup.
Was finally used without the stepper motor, just swithing on/off a lamp and having crane sounds and baby cries.  The crane had a baby skull.  It was all part of an amateur tunnel of terror set up in 2023.  

The setup switches on and off randomly a relay controlled lamp which should iluminate the crane.  

Every now and then, the baby cries. Every now and then, the stepper motor starts circling and the crane sounds go on. 

DISCLAIMER: The stepper motor was thought to slightly move the crane (as if there was something alive in it, or an invisible hand rocking it, but finally it had not enough torque to actually move it. :(

## requirements

This was running in a RaspBerry pi 4 with a relay, a stepper motor and an external audio speaker. 
It also needs a Python 3 interpreter. 

## HW setup

Relay was connected at GPIO pin 12.
Stepper motor at 7,11,13,15

## missing sound files

As I have licence to use them, but not for distribute them, please do create a "sounds" folder with: 

 - sounds/lloro_1.wav
 - sounds/lloro_2.wav
 - sounds/lloro_3.wav

...with different baby cries (no more than 30 secs each), and

 - sounds/chirrido_1.wav
 - sounds/chirrido_2.wav

for crane cracks and sounds (I ended up using rocking chair sounds), and
 
 - sounds/musica.mp3

...for background music. 
