#The code has been modified a bit
#To get this running on your own you will need: Selenium, pyautogui and pillow
#There are a few bugs that I need to fix
import time
import pyautogui
from selenium import webdriver
chrome_path = chrome directory
current_date = time.strftime("%w")
current_hour = time.strftime("%H")
current_minute = time.strftime("%M")
meeting1= #link for meetings
meeting2=
meeting3=
meeting4=
meeting5=
def join_meeting(course):
	driver = webdriver.Chrome(chrome_path)
	driver.get(course)
	time.sleep(10)
	discard=pyautogui.locateCenterOnScreen(picture  of discard)
	pyautogui.click(discard)
	autostart=pyautogui.locateCenterOnScreen(picture of open zoom meetings)
	pyautogui.click(autostart) 
	driver.quit()

while current_hour < "18": #put your time window then use the function this is an example
	if current_date == "1":
		if current_hour == "8" and current_minute >="50": 
			join_meeting(meeting1)
	else:
		print('🎉🥳There is no class today!!🥳🎉')
