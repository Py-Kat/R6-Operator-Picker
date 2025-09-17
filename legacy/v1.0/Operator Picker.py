from time import sleep
from colorama import init, Fore, Back, Style

#Assigned Values
versionnumber = 'v1.0.0'
header = '\n|-------------|Operator Picker|-------------|'
selectprompt = '\n\nSelect options by number!'
invalidinput = '\nInvalid Input!'

#Functions

#Styletext Function - Might make work later if i end up caring
#def styletext(text):
    #return Back.RED + Fore.BLACK + str(text) + Style.RESET_ALL

print(Fore.RED + f'\n\nR6 Operator Picker! - {versionnumber}')
sleep(2)
print('\nWritten By Kat')
sleep(2)
while True:
    print(header)
    print(selectprompt)
    prompt = input('\n|1.| Random Attacker\n\n|2.| Random Defender\n\n|3.| Changelogs\n\n|4.| Exit Script\n\n> ').lower()
    if prompt == '1':
        while True:
            from random import choice
            randomoperator = choice(['Glaz', 'Fuze', 'IQ', 'Blitz', 'Twitch', 'Montagne', 'Thermite', 'Ash', 'Thatcher', 'Sledge', 'Buck', 'Blackbeard', 'Capitão', 'Hibana', 'Jackal', 'Ying', 'Zofia', 'Dokkaebi', 'Finka', 'Lion', 'Maverick', 'Nomad', 'Gridlock', 'Nøkk', 'Amaru', 'Kali', 'Iana', 'Ace', 'Zero', 'Flores', 'Osa', 'Sens', 'Grim', 'Brava', 'Ram', 'Deimos', 'Striker', 'Rauora'])
            print('\n\nYour operator is:')
            sleep(2)
            print(f'\n\n         {randomoperator}!')
            sleep(1)
            prompt = input('\n\n|1.| Pick Another\n\n|2.| Return To Menu\n\n> ')
            if prompt == '1':
                print('\n\nPicking Again...')
                sleep(0.75)
            elif prompt == '2':
                break
            else:
                print(invalidinput)
                sleep(1)
                break
    elif prompt == '2':
        while True:
            from random import choice
            randomoperator = choice(['Kapkan', 'Tachanka', 'Bandit', 'Jäger', 'Rook', 'Doc', 'Pulse', 'Castle', 'Smoke', 'Mute', 'Frost', 'Valkyrie', 'Caveira', 'Echo', 'Mira', 'Lesion', 'Ela', 'Vigil', 'Alibi', 'Maestro', 'Clash', 'Kaid', 'Mozzie', 'Warden', 'Goyo', 'Wamai', 'Oryx', 'Melusi', 'Aruni', 'Thunderbird', 'Thorn', 'Azami', 'Solis', 'Fenrir', 'Tubarão', 'Sentry', 'Skopós'])
            print('\n\nYour operator is:')
            sleep(2)
            print(f'\n\n         {randomoperator}!')
            sleep(1)
            prompt = input('\n\n|1.| Pick Another\n\n|2.| Return To Menu\n\n> ')
            if prompt == '1':
                print('\n\nPicking Again...')
                sleep(0.75)
            elif prompt == '2':
                break
            else:
                print(invalidinput)
                sleep(1)
                break
    elif prompt == '3':
        sleep(1)
        print('\n|-------------|CHANGELOGS|-------------|')
        sleep(0.5)
        print('\n v1.0.0 - First Version Done! - 7/19/25')
        sleep(1.5)
        input('\n <ENTER> To Return To Menu > ')
    elif prompt == '4':
        print('\nExiting Script...')
        sleep(1)
        import sys
        sys.exit()
    elif prompt == 'version':
        print(versionnumber)
        sleep(2)
    else:
        print(invalidinput)
        sleep(1)