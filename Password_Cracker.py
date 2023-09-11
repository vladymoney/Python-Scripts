import random
import pyautogui

charater = '0123456789abcdefghijklmnopqrstuvwxyz'
character_list = list(charater)


password = pyautogui.password('Enter password here:')


guess_password = ''
while (guess_password!=password):
    guess_password = random.choices(character_list, k=len(password))
    
    print('>>>>>'+ str(guess_password)+ '<<<<<<')
    
    
    if guess_password == list(password):
        print('Your Password is:' + ''.join(guess_password))
        break
    
    
    