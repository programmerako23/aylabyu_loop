from pynput.keyboard import Key, Controller
import time

keyboard  = Controller()

time.sleep(5)

messages="You're the best"

while(True):
	for i in messages:
		keyboard.press(i)
		keyboard.release(i)
		time.sleep(0.03)
	
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(0.4)
	

