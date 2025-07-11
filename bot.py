import requests
import keyboard
import time as t
import random as r
from tqdm import tqdm
import pyautogui as autogui

# Setup
base_url = 'https://raw.githubusercontent.com/Vesteria-Coding/Dad-Jokes-Bot/main/Jokes.txt'
url = f"{base_url}?t={int(t.time())}"
response = requests.get(url)
jokes = response.text.splitlines()
dad_jokes = []
bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [Time Elapsed: {elapsed}  Time Remaining: {remaining}]'
joke_choice = ''

print('Formating Dad Jokes Please Wait Please Wait')
for joke in tqdm(jokes, ncols=100, bar_format=bar_format):
    if joke not in dad_jokes:
        dad_jokes.append(joke)
    t.sleep(0.01)
print(f'Formated {len(dad_jokes)} Dad Jokes')

while True:
    try:
        keyboard.wait('f12')
        t.sleep(0.1)
        joke_choice = r.choice(dad_jokes)
        autogui.typewrite(joke_choice, interval=0.01)
        t.sleep(0.1)
        autogui.press('enter')
        t.sleep(0.5)
    except KeyboardInterrupt:
        print("User Quit")
        quit(1)
