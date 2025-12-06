from pyfiglet import figlet_format
import pyfiglet
import pygame
import random
import cowsay
"""
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux'] 
"""
looping = False
#checking if each realm is available. True means it's able to acessed, False means it isn't.
mw = True
q = True
p = True
pe = True
#Going home won't be available until all realms are completed.
home = False
#Won't become false until the game ends.
in_loop = True
#If I want to change the message for any of the reals, I can just do it here
already_completed_message = "Realm already completed."
#A bunch of logos with ascii art.
logo = """
     ________         _      ___          __              _____              
    /_  __/ /  ___   | | /| / (_)__  ___ / /____  ___    / ___/__ ___ _  ___ 
     / / / _ \/ -_)  | |/ |/ / / _ \(_-</ __/ _ \/ _ \  / (_ / _ `/  ' \/ -_)
    /_/ /_//_/\__/   |__/|__/_/_//_/___/\__/\___/_//_/  \___/\_,_/_/_/_/\__/ 
        """
logoquestion = """
 _____ _            __    __ _           _                  ___                         ___ 
/__   \ |__   ___  / / /\ \ (_)_ __  ___| |_ ___  _ __     / _ \__ _ _ __ ___   ___    / _ \
  / /\/ '_ \ / _ \ \ \/  \/ / | '_ \/ __| __/ _ \| '_ \   / /_\/ _` | '_ ` _ \ / _ \   \// /
 / /  | | | |  __/  \  /\  /| | | | \__ \ || (_) | | | | / /_\\ (_| | | | | | |  __/_ _ _\/ 
 \/   |_| |_|\___|   \/  \/ |_|_| |_|___/\__\___/|_| |_| \____/\__,_|_| |_| |_|\___(_|_|_|) 
                                                                                            
"""
logo2 = """
 ______   __  __     ______        __     __     __     __   __     ______     ______   ______     __   __        ______     ______     __    __     ______    
/\__  _\ /\ \_\ \   /\  ___\      /\ \  _ \ \   /\ \   /\ "-.\ \   /\  ___\   /\__  _\ /\  __ \   /\ "-.\ \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\/_/\ \/ \ \  __ \  \ \  __\      \ \ \/ ".\ \  \ \ \  \ \ \-.  \  \ \___  \  \/_/\ \/ \ \ \/\ \  \ \ \-.  \     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
   \ \_\  \ \_\ \_\  \ \_____\     \ \__/".~\_\  \ \_\  \ \_\\"\_\  \/\_____\    \ \_\  \ \_____\  \ \_\\"\_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
    \/_/   \/_/\/_/   \/_____/      \/_/   \/_/   \/_/   \/_/ \/_/   \/_____/     \/_/   \/_____/   \/_/ \/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 
                                                                                                                                                               
"""
logo3 = """
 _____ _     _____   _      _  _      ____ _____ ____  _        _____ ____  _      _____
/__ __Y \ /|/  __/  / \  /|/ \/ \  /|/ ___Y__ __Y  _ \/ \  /|  /  __//  _ \/ \__/|/  __/
  / \ | |_|||  \    | |  ||| || |\ |||    \ / \ | / \|| |\ ||  | |  _| / \|| |\/|||  \  
  | | | | |||  /_   | |/\||| || | \||\___ | | | | \_/|| | \||  | |_//| |-||| |  |||  /_ 
  \_/ \_/ \|\____\  \_/  \|\_/\_/  \|\____/ \_/ \____/\_/  \|  \____\\_/ \|\_/  \|\____\\
                                                                                        
"""
logo4 = """
░        ░░  ░░░░  ░░        ░░░░░░░░  ░░░░  ░░        ░░   ░░░  ░░░      ░░░        ░░░      ░░░   ░░░  ░░░░░░░░░      ░░░░      ░░░  ░░░░  ░░        ░
▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒  ▒  ▒▒▒▒▒  ▒▒▒▒▒    ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒    ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒   ▒▒   ▒▒  ▒▒▒▒▒▒▒
▓▓▓▓  ▓▓▓▓▓        ▓▓      ▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓▓  ▓▓▓▓▓  ▓  ▓  ▓▓▓      ▓▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓  ▓  ▓  ▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓  ▓▓▓▓  ▓▓        ▓▓      ▓▓▓
████  █████  ████  ██  ██████████████   ██   █████  █████  ██    ████████  █████  █████  ████  ██  ██    ████████  ████  ██        ██  █  █  ██  ███████
████  █████  ████  ██        ████████  ████  ██        ██  ███   ███      ██████  ██████      ███  ███   █████████      ███  ████  ██  ████  ██        █
                                                                                                                                                        
"""
statslogo = """
 _______  _______  _______  _______  _______    ___  
|       ||       ||   _   ||       ||       |  |   | 
|  _____||_     _||  |_|  ||_     _||  _____|  |___| 
| |_____   |   |  |       |  |   |  | |_____    ___  
|_____  |  |   |  |       |  |   |  |_____  |  |   | 
 _____| |  |   |  |   _   |  |   |   _____| |  |___| 
|_______|  |___|  |__| |__|  |___|  |_______|       
"""
milkywaylogo = """
▄▄▄▄▄ ▄ .▄▄▄▄ .    • ▌ ▄ ·. ▪  ▄▄▌  ▄ •▄  ▄· ▄▌    ▄▄▌ ▐ ▄▌ ▄▄▄·  ▄· ▄▌     ▄▄ •  ▄▄▄· ▄▄▌   ▄▄▄· ▐▄• ▄  ▄· ▄▌
•██  ██▪▐█▀▄.▀·    ·██ ▐███▪██ ██•  █▌▄▌▪▐█▪██▌    ██· █▌▐█▐█ ▀█ ▐█▪██▌    ▐█ ▀ ▪▐█ ▀█ ██•  ▐█ ▀█  █▌█▌▪▐█▪██▌
 ▐█.▪██▀▐█▐▀▀▪▄    ▐█ ▌▐▌▐█·▐█·██▪  ▐▀▀▄·▐█▌▐█▪    ██▪▐█▐▐▌▄█▀▀█ ▐█▌▐█▪    ▄█ ▀█▄▄█▀▀█ ██▪  ▄█▀▀█  ·██· ▐█▌▐█▪
 ▐█▌·██▌▐▀▐█▄▄▌    ██ ██▌▐█▌▐█▌▐█▌▐▌▐█.█▌ ▐█▀·.    ▐█▌██▐█▌▐█ ▪▐▌ ▐█▀·.    ▐█▄▪▐█▐█ ▪▐▌▐█▌▐▌▐█ ▪▐▌▪▐█·█▌ ▐█▀·.
 ▀▀▀ ▀▀▀ · ▀▀▀     ▀▀  █▪▀▀▀▀▀▀.▀▀▀ ·▀  ▀  ▀ •      ▀▀▀▀ ▀▪ ▀  ▀   ▀ •     ·▀▀▀▀  ▀  ▀ .▀▀▀  ▀  ▀ •▀▀ ▀▀  ▀ • 
"""
thelogo = """
  _____ _        
 |_   _| |_  ___ 
   | | | ' \/ -_)
   |_| |_||_\___|
                 
"""
andromedalogo = """
    _           _                      _         ___      _               
   /_\  _ _  __| |_ _ ___ _ __  ___ __| |__ _   / __|__ _| |__ ___ ___  _ 
  / _ \| ' \/ _` | '_/ _ \ '  \/ -_) _` / _` | | (_ / _` | / _` \ \ / || |
 /_/ \_\_||_\__,_|_| \___/_|_|_\___\__,_\__,_|  \___\__,_|_\__,_/_\_\\_, |
                                                                     |__/ 
"""
qilialogo = """
 ▄▀▀▀▀▄    ▄▀▀█▀▄   ▄▀▀▀▀▄     ▄▀▀█▀▄    ▄▀▀█▄  
█      █  █   █  █ █    █     █   █  █  ▐ ▄▀ ▀▄ 
█      █  ▐   █  ▐ ▐    █     ▐   █  ▐    █▄▄▄█ 
 ▀▄▄▄▄▀▄      █        █          █      ▄▀   █ 
        █  ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▄▄▀ ▄▀▀▀▀▀▄  █   ▄▀  
        ▐ █       █  █        █       █ ▐   ▐   
          ▐       ▐  ▐        ▐       ▐         
"""
primordialogo = """
         _          _            _         _   _         _            _          _             _          _          
        /\ \       /\ \         /\ \      /\_\/\_\ _    /\ \         /\ \       /\ \          /\ \       / /\        
       /  \ \     /  \ \        \ \ \    / / / / //\_\ /  \ \       /  \ \     /  \ \____     \ \ \     / /  \       
      / /\ \ \   / /\ \ \       /\ \_\  /\ \/ \ \/ / // /\ \ \     / /\ \ \   / /\ \_____\    /\ \_\   / / /\ \      
     / / /\ \_\ / / /\ \_\     / /\/_/ /  \____\__/ // / /\ \ \   / / /\ \_\ / / /\/___  /   / /\/_/  / / /\ \ \     
    / / /_/ / // / /_/ / /    / / /   / /\/________// / /  \ \_\ / / /_/ / // / /   / / /   / / /    / / /  \ \ \    
   / / /__\/ // / /__\/ /    / / /   / / /\/_// / // / /   / / // / /__\/ // / /   / / /   / / /    / / /___/ /\ \   
  / / /_____// / /_____/    / / /   / / /    / / // / /   / / // / /_____// / /   / / /   / / /    / / /_____/ /\ \  
 / / /      / / /\ \ \  ___/ / /__ / / /    / / // / /___/ / // / /\ \ \  \ \ \__/ / /___/ / /__  / /_________/\ \ \ 
/ / /      / / /  \ \ \/\__\/_/___\\/_/    / / // / /____\/ // / /  \ \ \  \ \___\/ //\__\/_/___\/ / /_       __\ \_\
\/_/       \/_/    \_\/\/_________/        \/_/ \/_________/ \/_/    \_\/   \/_____/ \/_________/\_\___\     /____/_/

                                                                                                                   
"""
padlockelogo = """
  ____       _      ____     _       U  ___ u   ____   _  __  U _____ u  _    
U|  _"\ uU  /"\  u |  _"\   |"|       \/"_ \/U /"___| |"|/ /  \| ___"|/U|"|u  
\| |_) |/ \/ _ \/ /| | | |U | | u     | | | |\| | u   | ' /    |  _|"  \| |/  
 |  __/   / ___ \ U| |_| |\\| |/__.-,_| |_| | | |/__U/| . \\u  | |___   |_|   
 |_|     /_/   \_\ |____/ u |_____|\_)-\___/   \____| |_|\_\   |_____|  (_)   
 ||>>_    \\    >>  |||_    //  \\      \\    _// \\,-,>> \\,-.<<   >>  |||_  
(__)__)  (__)  (__)(__)_)  (_")("_)    (__)  (__)(__)\.)   (_/(__) (__)(__)_) 
"""

class Character():
    def __init__(self):
        self.loops = 0
        self.deaths = 0
        self.realms_completed = 0
        self.mw_available = True
        self.q_available = True
        self.p_available = True
        self.pe_available = True
        self.home_available = False

    def die(self):
        self.deaths += 1

    def complete_realm(self, stat):
        self.realms_completed += 1
        stat = False
    

def intro_text(Winston):
    if Winston.loops == 0:
        print("\n\n\nYou're a man.\nA circle.\nYou're something." \
        " You've been through quite a lot.\nExistential crises, a death of a friend, a divorce, " \
        "a takeover of the town you hold dear.\nBut now that's all over.\nYou are now in a blank liminal space."
        "\nWhere will you go?" \
        "\nWhat will you do?")
        print(logo)
        proceed()
    elif Winston.loops == 1:
        if Winston.realms_completed == 0:
            print("\n\n\nYou're a man.\nYou're a... what a second. You've been here before.")
            print(logo2)
            proceed()
    elif Winston.loops == 2:
        if Winston.realms_completed == 0:
            print("\n\n\nThis will keep happening, won't it?")
            print(logo3)
            proceed()
    elif Winston.loops == 3:
        if Winston.realms_completed == 0:
            print("\n\n\nThere has to be a way to progess, to feel satisfied...?")
            print(logo3)
            proceed()
    elif Winston.loops > 4:
        if Winston.realms_completed == 0:
            print("\n\n\nYou realize you aren't satisfied...\nYou want to go home one day...\nBut how can you get the courage to do so...?")
            print(logo)
            proceed()

    if Winston.realms_completed == 1: 
        print("\n\nYou think you're starting to understand.\nThese realms, you can actually help people there." \
        "\nMaybe if you help enough people, you can get the courage to visit your home dimension..." \
        "\nYou have a new quest.\n")
        proceed()

def stats_page(Winston):
    if Winston.loops > 0:
        print(statslogo)
        print(f"Total Loops: {Winston.loops}")
        print(f"Deaths: {Winston.deaths}")

        if Winston.realms_completed > 0:
            print(f"*Realms Completed: {Winston.realms_completed}*")
        print("\n")
    
#An easy shorthand instead of copy and pasting this same prompt throughout the game. The proceed() function is so that you don't get huge chunks of text at once.
def proceed():
    input("Press Enter to continue.")

def main():
    #setting the character, Winston. All the default values suffice
    winston = Character()
    
    #The Core Loop
    while in_loop == True:
        #At the start of every loop will be a line to signify the beginning
        print("------------------------------------------------------------------------")
        #Intro text, will change on certain conditions like loops passed through, or if at least one realm was completed
        intro_text(winston)

        #The Stats Page that comes before the dimension select screen, only appears if you've been through a loop at least a single time
        stats_page(winston)

        print(winston.mw_available)
        #The core option
        if winston.mw_available == True: 
            print("1. Visit the bussling galactic metropolis, the Milky Way Galaxy")
        if winston.q_available == True:
            print("2. Journey to the cursed demon planet, Qilia")
        if winston.p_available == True:
            print("3. Go to the primitive gas giant Primordia")
        if winston.pe_available == True:
            print("4. Volunteer at the completely ordinary Padlocke Elementary School")
        if winston.home_available == True:
            print("5. Go... home?")
        #Giving the player the core choice of the game
        travel_choice = input("Which realm will you visit?\n\n")
        
        match travel_choice:
            case "1":
                if winston.mw_available == True:
                    milkyway(winston)
                else:
                    print(already_completed_message)
                    continue
            case "2":
                if winston.q_available == True:
                    qilia(winston)
                else:
                    print(already_completed_message)
            case "3":
                if winston.p_available == True:
                    primordia(winston)
                else:
                    print(already_completed_message)
            case "4":
                if winston.pe_available == True:
                    padlocke(winston)
                else:
                    print(already_completed_message)
            case "5":
                if winston.home_avaiable == True:
                    home(winston)
            case _:
                print("Option not valid. You find yourself stretching to some unknown place in the universe...\nMaybe just pick one of the numbers given next time...\n")
                input("Press Enter to continue.")
        #add another to the loop counter
        winston.loops += 1


def milkyway(Winston):
    print(milkywaylogo)
    print("\nYou find yourself spawned in the middle of outer space.\nYou've done this whole space thing before, many times." \
    "\nYou are reminded of following your then-wife to her fancy new job," \
    "\nand then reminded of being towed by your then-ex-wife in space a year later." \
    "\n\nYou land on an asteroid, and see a few locations you can float too.")
    mwchoice1 = input("1. An very large ant-shaped spaceship\n2. Earth\n3. A supermassive black hole\n")
    print("\n")
    match mwchoice1:
        case "1":
            print("You drift right in the vessel's path, and surprisingly, it stops.\nIt's airlock opens, and figures carry you in.\nOnce on the vessel, you see multiple people of different species -- a purple one with scales,\nholding hands with a very short tan woman, next to them is a tiny little pod thing, close to a tall black man,\nan axolotol standing on 2 feet, some uptight looking lightskinned woman, and...\nand...\nis that your wife?\nObviously not, this woman has tan skin and has katanas sheithed.\nBut you can't help but be remined of your ex-wife, Pinky.\nWhat do you say?")

            mwchoice2 = input("\n1. \"Thank you, kind strangers.\" \n2. \"OH MY GOD YOU LOOK JUST LIKE MY EX-WIFE!\"\n")

            match mwchoice2:
                case "1":
                    print("\n\n\"You're welcome, yellow sir,\" said an uptight-looking woman in a blue suit and black pants.\n\"I'm Georgia of the IGDA.\nThese are my associates, and we'd love to drop you off on your planet, but we don't have much time.\nWe have a very important expedition to get to. I can drop you off at the nearest station.\"")
                    print("\"Well handled, Georgia,\" said the Pinky-looking woman. \"You seem almost normal in this interaction.\"\n")
                    print("Well. You've been let go. Suddenly, this realm doesn't seem that interesting anymore. It's time to go, you think.")
                case "2":
                    print("\n\nSilence.\nThe tall human man steps in front of her." \
                    "\nActually, this one reminds you of your friend Mike." \
                    "\nYour *dead* friend Mike." \
                    "\n\"What species is this creature, even?\" says the computerized voice of the little pod thing." \
                    "\nThere's a small little dot in there, a little smaller than a closed fist." \
                    "\nIs that the actual creature, and the pod is it's vehicle?" \
                    "\nIt whips around and scans you.\n\"Unrecognized. How curious.\"" \
                    "\n\"Okay, we don't have time for this,\" says the stern human woman." \
                    "\n\"Rebecca, Michael, throw the unidentified yellow thing out. I'd like to be on the path to the Andromeda soon." \
                    "\"\n\nRebecca, huh?\nMICHAEL? They share the same name?" \
                    "\nAnd a journey to the Andromeda? Now this was getting interesting.")
                    proceed()
                    print("\nYou let the two escort you out onto some random travel station, but you decide to stow away\nin a crevasse of the ship on the outside." \
                    "\nIt isn't the first time you've stowed away on a spaceship." \
                    "\nBesides, this realm was getting too interesting to pass up." \
                    "\n\nThis ant-shaped ship travels through the galaxy, and you see different planets that you\nidentify with a random drifting map, like Verfuctum, Exeplum, Gree." \
                    "\nYou even see the now-ruined Galactic Core." \
                    "\nIt seems that this crew is getting to the bottom of whatever's  to this galaxy." \
                    "\nSoon it enters some kind of much-much-faster-than-light-speed travel." \
                    "\nThis also isn't the first time you've experienced something like this, and hold on for dear life." \
                    "\nSoon, you find yourself somewhere... different.")
                    proceed()
                    print(thelogo)
                    print(andromedalogo)
                    print("This place feels a lot less populated, and a lot more dangerous.\nSounds like it could be fun.")
                    mwchoice3 = input("\n1. Keep going with this ship\n2. Drift away and explore by yourself\n")
                    match mwchoice3:
                        case "1":
                            print("\nThe ship keeps going into the galaxy.\nIt's been many weeks at this point, and it's starting to get boring.\nOne day, the very short tan one comes out in a vibrant teal blue spacesuit,\nseeming to do some kind of maintanece on the ship.\nShe sees you, and screams bloody murder. You can''t actually hear her, but you can see her face.\nShe stomps on you over, and over, and over, and over, and over like a little rat.\nYou die.")
                            Winston.die()
                        case "2":
                            print("\nYou kick off the ship and see the surroundings for yourself.\nOuter space feels red, for some reason.\nYou drift along, not seeing much except for...\nis that a human teenager, sitting on an asteroid? No spacesuit?\nUnless he's also trancending reality like you, this shouldn't be happenning.\nYou have to approach this kid, maybe he has something to do with\nwhat's been happening to the Milky Way")
                            mwchoice4 = input("\n1. Hey, buddy. Don't worry, I'm not gonna hurt ya. I just wanna talk.\n2. Man, when was the last time you ate?\n3. [BRAAAAAAAAAAAAAAAAAP]\n4. [Say nothing, approach silently]")
                            match mwchoice4:
                                case "1" | "2" | "3":
                                    print("\nHe casually lifts his hand.\nA giant beam of pure darkness larger than a house shoots out.\nYou're hit with the most overwhelming power you've ever felt.\nThis kid is certainly important, and you'd love to find out more, but now you are dead.\nLike, very, very dead.")
                                    Winston.die()
                                case "4":
                                    print("\n...\n...\n...\"Who are you? Are you... with them?\"\nYou know who he's talking about.\n")
                                    print("\"No, I'm an indpendent entity.\"\nYou sit next to him. You've learned that sayind nothing and letting the kid talk works, so that's what you do.\n")
                                    print("Alexander nods, and he floats up. His entire body is enveloped in darkness.\nHe blasts away at lightspeed to save his caretakers.\nYou think that you made one step to bring a family together.\nA family you never got to have in your world.")
                                    Winston.complete_realm(Winston.mw_available)
                                    Winston.mw_available = False
        case "2":
            print("You burn up into the atmosphere. While falling, you see a giant archipelogo that seems like the shape of the USA...\nWait a second, that IS the USA.\nYou're filled with so many questions as to how this could happen that you forget to try and land and die on impact.")
            Winston.die()
        case "3":
            print("You see a bunch of ruined spaceships.")
            

    input("Press Enter to continue.")

def qilia(Winston):
    print(qilialogo)
    print("You feel an overwhelming sense of dread and despair.\nIs this what the presense of demons feel like?\nAfter you stop yourself from throwing up, you find yourslf in a basement.\nThere are multiple bookshelves filled with potions, spellbooks, and wands.\n\"Ooh! Girls, there's another demon here to torture you! Wait a second, this is no demon.\"\nTwo very surly looking teenage girls turn the corner and stare you down.")
    
    input("Press Enter to continue.")

def primordia(Winston):
    print(primordialogo)
    print("You're in a lush jungle.\nYou look over the edge of this island and you see bright skies. " \
    "Endless sky, actually." \
    "\nIt goes down endlessly, with other islands dotting the landscap")

    input("Press Enter to continue.")

    cowsay.trex("What are you doing here?")

    input("Press Enter to continue.")

def padlocke(Winston):
    michaelapicked = False 
    print(padlockelogo)
    print("\nYou spawn right outside an elementary school with a statue of a giant smiling cartoon penguin.\nWait a minute, they're not gonna let you in the building as some random dude.\nYou look around, and realize that everyone seems like a normal human in this world.\nThis gives you two options.")
    padlockechoice1 = input("1. Pass yourself off as a colorful mascot entertainer\n2. Register as a substitute teacher and just tell everyone you have jaundice\n")

    print("\n")
    match padlockechoice1:
        case "1":
            print("The administration seems to love your wacky yellow guy act.\nYou pass through with ease, and are allowed into Ms. Ottoman's Kindergarten class, where a kid is having a birthday party.\n10 minutes into your \"rolling around the room like a tire\" act, a kindergartner jumps up to you and tears your face off.\nMs. Ottoman sighs. \"Not AGAIN, Stacy.\"\nYou die.")
            Winston.die()
        case "2":
            print("\n\nAdministration is... very interested in your appearence, but lets you through.\nIt turns out that Mrs. Baker's class has ZERO teachers right now.\nMrs. Baker is out, and her student teacher is swamped with finals.\nYou are very glad you are not swamped with finals.\n\nYou're warned that this is the \"gifted and talented\" class.\nYou're a bit confused. Shouldn't that mean that they should be easier to deal with?")
            #proceed()
            print("\nYou find a very long and organized binder for all... eight kids? How hard could eight kids be--\nYou were very wrong.\nRunning around, screaming, far too impassioned debates about children's cartoons...\nand one of the students is in the corner. You see their description, and it seems like it's Michaela.\n\nWhich student will you go to first?")
            
            while michaelapicked == False:
                padlockechoice2 = input("\n1. The boisterous and overconfident Cooper" \
                "\n2. Levelheaded and \"alt\" Chloe" \
                "\n3. Overdramatic Augustine" \
                "\n4. Silent but mischevious Micah" \
                "\n5. Introvert and general nerd Erin" \
                "\n6. (Usually) extrememly energetic Michaela" \
                "\n7. Studious and just a tad stuck-up Aashvi\n8. Self-described class clown Jesse")
                print("\n\n")
                match padlockechoice2:
                    case "1":
                        print("\"Sooooooo, how many lambos you got?\"")
                    case "2":
                        print("Chloe was flipping throw a tween fashion magazine, \"Riot\"")
                    case "3":
                        print("The kid swishes his hair." \
                        "\n\"You look like you'd enjoy the series Neon Genesis Evangelion, sir.\nYou're obviously going through an existential crisis.\"" \
                        "His silent friend, Micah, nods.\nYou decide to watch it for yourself.\nBy time you finish The End of Evangelion you're genuinely too depressed to wanna do anything.\n")
                    case "4":
                        print("Micah looks at you with his large innocnet eyes." \
                        "\nYou read on the binder that he's semiverbal and communicatess with drawings. How cute!\nMicah shows you a drawing of...\na yellow man...\nwith his eyes pecked out and his intestines exposed while seagulls flying above him" \
                        "\n\nYou recoil.\n\n\"Oh, Micah's just trying to get a reaction out of you,\" " \
                        "Augustine, his friend, said.\n\nReaction gotten.\nMaybe it's best to check on a different kid...")
                    case "5":
                        print("")
                    case "6":
                        print("You enter the \"Chill-Out Corral\".\nThe girl seems very uncomfortable with a random adult")
                        michaelapicked = True
                        proceed()
                        Winston.complete_realm(Winston.pe_available)
                        Winston.pe_availavle = False
                    case "7":
                        print("")
                    case "8":
                        print("When you approach the kid, he tilts his head.\n\"You know... you kinda look constipated.\"\nThe other kids stare at him.\n\"No he doesn't...?\" said Chloe.\nYou get such strong second-hand embarrasement that you actually just die.")
                proceed()
    #nThis feels like the same place you were created in. The 'current' you, actually.

    proceed()

def home(Winston):
    print("...gulp.")
    proceed()
    print("You've learned so much through your journey through this strange, vast multiverse.\nYou learned that it's never too late to redeem yourself.\nBonds that have been sour for long don't have to stay that way.\n\nAnd growing up is... okay.")

if __name__ == "__main__":
    main()