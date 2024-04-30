'Mouse and keyboard automation in python'
import pyautogui
import time
#print(pyautogui.size())
# moveTo() function - moving the mouse from point a on the x-axis to point by y-axis
pyautogui.moveTo(100, 100, duration=1)
#moveRel function - moves the mouse relative to its previous position
pyautogui.moveRel(300, 300, duration=3)

#pyautogui.click(70, 20, duration= 2)

# We have the funstions DragTo and DragRel we can draw a square using these
#pyautogui.dragTo()
#pyautogui.dragRel()

time.sleep(10)
pyautogui.moveTo(500, 500,duration=1)
pyautogui.dragRel(0, 100,duration=1)
pyautogui.dragRel(-100, 0,duration=1)
pyautogui.dragRel(0, -100,duration=1)