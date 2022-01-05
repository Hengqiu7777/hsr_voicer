import keyboard
import playsound

sound1 = 'r2d2.wav'
playsound.playsound(sound1)


while True:
    if keyboard.read_key() == "r":
        playsound.playsound(sound1)
        break