import pygame
import time
import pyttsx3

pygame.mixer.init()
sound1 = pygame.mixer.Sound("tone-alarm.mp3")
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("Starting Pomodoro timer...")
work_time = int(input("Enter work time in minutes: "))
break_time = int(input("Enter break time in minutes: "))
repeat = int(input("Enter number of Pomodoro cycles: "))

while repeat > 0:
    sound1.play()
    while pygame.mixer.get_busy():
        time.sleep(1)
    speak("Time to work! Focus!")
    print("Working Time...")
    time.sleep(work_time * 60)

    sound1.play()
    while pygame.mixer.get_busy():
        time.sleep(1)
    speak("Time for a break! Relax!")
    print("Break Time...")
    time.sleep(break_time * 60)
    repeat -= 1
