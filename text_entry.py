import argparse
import pyautogui
import time
import os
startDelaySec = 5

parser = argparse.ArgumentParser(description="Text field entry bot")
parser.add_argument("source", help="text file containing each entry")
parser.add_argument("--offsetX", default=0, help="x pixel offset between text field and enter button")
parser.add_argument("--offsetY", default=50, help="y pixel offset between text field and enter button")
parser.add_argument("--delay", default=1.5, help="seconds of delay between text entry and click")
args = parser.parse_args()

filename = args.source
clickOffset = (int(args.offsetX), int(args.offsetY))
clickDelay = float(args.delay)

print(f"Using {filename}")
print(f"Click offset: {clickOffset}")
print(f"Click delay: {clickDelay}")
print(f"Starting in {startDelaySec} seconds...")
time.sleep(startDelaySec)

with open(filename) as fp:
    for line in fp:
        text = line.rstrip()
        print(text)
        # click to focus on text field, enter text, and wait
        pyautogui.click()
        pyautogui.typewrite(text)
        time.sleep(clickDelay)
        # move to submit button, and back to text field
        pyautogui.moveRel(clickOffset[0], clickOffset[1], duration = .1)
        pyautogui.click()
        pyautogui.moveRel(-clickOffset[0], -clickOffset[1], duration = .1)
        #delete any field content if it persists
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.hotkey('command', 'a',interval=0.01)
        pyautogui.press('backspace')
print("Done")
