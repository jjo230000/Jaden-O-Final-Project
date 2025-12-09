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
endlogo = """
      ___           ___           ___                    ___           ___           ___     
     /\  \         /\__\         /\  \                  /\  \         /\__\         /\  \    
     \:\  \       /:/  /        /::\  \                /::\  \       /::|  |       /::\  \   
      \:\  \     /:/__/        /:/\:\  \              /:/\:\  \     /:|:|  |      /:/\:\  \  
      /::\  \   /::\  \ ___   /::\~\:\  \            /::\~\:\  \   /:/|:|  |__   /:/  \:\__\ 
     /:/\:\__\ /:/\:\  /\__\ /:/\:\ \:\__\          /:/\:\ \:\__\ /:/ |:| /\__\ /:/__/ \:|__|
    /:/  \/__/ \/__\:\/:/  / \:\~\:\ \/__/          \:\~\:\ \/__/ \/__|:|/:/  / \:\  \ /:/  /
   /:/  /           \::/  /   \:\ \:\__\             \:\ \:\__\       |:/:/  /   \:\  /:/  / 
   \/__/            /:/  /     \:\ \/__/              \:\ \/__/       |::/  /     \:\/:/  /  
                   /:/  /       \:\__\                 \:\__\         /:/  /       \::/__/   
                   \/__/         \/__/                  \/__/         \/__/         ~~       
"""
#The class for the Character, used for winston
class Character():
    def __init__(self):
        #These three stats are the main statistics that are being tracked.
        self.loops = 0
        self.deaths = 0
        self.realms_completed = 0
        #Tracking if each of the realms are available. 
        # At the start of the game, Milky Way, Qilia, Primordia, and Padlocke are available, but going home is not.
        self.mw_available = True
        self.q_available = True
        self.p_available = True
        self.pe_available = True
        self.home_available = False
        #Makes it so that the messgae of "you have a new quest" only appears on single time
        self.realm_completemessage_appear = True
        self.in_loop = True
    #Every path that leads to a death uses this function
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
            print(logo3)
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

    if Winston.realms_completed == 1 and Winston.realm_completemessage_appear == True: 
        Winston.realm_completemessage_appear = False
        print("\n\nYou think you're starting to understand.\nThese realms, you can actually help people there." \
        "\nMaybe if you help enough people, you can get the courage to visit your home dimension..." \
        "\nYou have a new quest.\n")
        proceed()

    if Winston.mw_available == False and Winston.q_available == False and Winston.p_available == False and Winston.pe_available == False:
        Winston.home_available = True
        print("\n\n...\n...\n...\nYou did it.\nYou helped at least one person in 4 completely different realms.\nYou think you have the courage to go back to your home dimension now.")
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

#The four realms, and the final ending realm.
#Milky Way. Interact with a motley crew. Talk to a wayward starchild, and encourage him to give himself another chance
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
            
            print("\n")
            match mwchoice2:
                case "1":
                    print("\n\n\"You're welcome, yellow sir,\" said an uptight-looking woman in a blue suit and black pants.\n\"I'm Georgia of the IGDA.\nThese are my associates, and we'd love to drop you off on your planet, but we don't have much time.\nWe have a very important expedition to get to. I can drop you off at the nearest station.\"")
                    print("\"Well handled, Georgia,\" said the Pinky-looking woman. \"You seem almost normal in this interaction.\"\n")
                    print("Well. You've been let go. Suddenly, this realm doesn't seem that interesting anymore. It's time to go, you think.")
                case "2":
                    print("\n\nSilence.\nThe tall human man steps in front of her." \
                    "\nActually, this one reminds you of your friend Mike." \
                    "\nYour *dead* friend Mike." \
                    "\n\n\"What species is this creature, even?\" says the computerized voice of the little pod thing." \
                    "\nThere's a small little dot in there, a little smaller than a closed fist." \
                    "\nIs that the actual creature, and the pod is it's vehicle?" \
                    "\nIt whips around and scans you.\n\"Unrecognized. How curious.\"" \
                    "\n\n\"Okay, we don't have time for this,\" says the stern human woman." \
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
                    "\n\nSoon, you find yourself somewhere... different.")
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
                            mwchoice4 = input("\n1. Hey, buddy. Don't worry, I'm not gonna hurt ya. I just wanna talk.\n2. Man, when was the last time you ate?\n3. [BRAAAAAAAAAAAAAAAAAP]\n4. [Say nothing, approach silently]\n")
                            match mwchoice4:
                                case "1" | "2" | "3":
                                    print("\nHe casually lifts his hand.\nA giant beam of pure darkness larger than a house shoots out.\nYou're hit with the most overwhelming power you've ever felt.\nThis kid is certainly important, and you'd love to find out more, but now you are dead.\nLike, very, very dead.")
                                    Winston.die()
                                case "4":
                                    print("\n...\n...\n...\"Who are you? Are you... with them?\"\nYou know who he's talking about.\n")
                                    print("\"No, I'm an indpendent entity.\"\nYou sit next to him. You've learned that sayind nothing and letting the kid talk works, so that's what you do.\nYou listen.")
                                    proceed()
                                    print("\n\"I'm... I dunno, I... I'm over 150 years old...\nI woke up with powers...\nI killed a lot of people..."\
                                    "\n\nBut there was these two, these two humans like me. Michael and Rebecca\nThey were nice. Genuine, not fake. It was me, and them, and Ax, and Dot.\nIt was good.\"\nThe kid starts shaking."\
                                    "\n\n\"Then I betrayed them. I... I kept killing. These Esteers. Mike and Rebecca went to prison because of me.\nAnd then they STILL tried to stop me.\nAnd then... I might've killed them.\n\nAnd then I ran away. And now I'm here.\"")
                                    proceed()
                                    print("\n\nOh my god. That IS a lot.\nYou decide to not say anything for a while.\nBut then the words come to you.\n\n")
                                    print("\"I've also made a lot of mistakes. I betrayed the trust of people I love.\nAnd I've also run away. I mean, look at where I am.\n\nBut I think... I think people are more forgiving than you thinnk they are. That's what I've learned." \
                                    "\n\nIf these humans are as as kind are you say they are, they'll take you.\nI've met those two you're talking about. They both remind me of... people I know. They were good people.\nYou'll be just fine, I think. Not... immediately, but in the end.\"")
                                    print("\n\nThe boy has been listening intently. He nods slowly. His whips around. \"I feel them. They're here. And they're in trouble.\"\nHe turns back.\n\"Thank you, weird yellow thing.\"")
                                    print("Alexander nods, and he floats up. His entire body is enveloped in darkness.\nHe blasts away at lightspeed to save his caretakers.\nYou think that you made one step to bring a family together.\nA family you never got to have in your world.")
                                    Winston.complete_realm(Winston.mw_available)
                                    Winston.mw_available = False
        case "2":
            print("You burn up into the atmosphere. While falling, you see a giant archipelogo that seems like the shape of the USA...\nWait a second, that IS the USA.\nYou're filled with so many questions as to how this could happen that you forget to try and land and die on impact.")
            Winston.die()
        case "3":
            print("You see a bunch of ruined spaceships.\nWhite tendrils that are fading.\nAnd the supermassive black hole, Saggitarius A*." \
            "\n\"Oh, hey there!\"\nA somewhat ordinary looking woman waves to you in a spaceship, from a loudspeaker.\n"\
            "\"Wanna join my organizatioin? The Intergalactic Coalition of Correction could really use someone like you.\"\nYou immediately get cult vibes." \
            "\n\"Uh... no?\"\nShe sighs.\nYou are suddenly rammed with the spaceship and are sent into the black hole, and are\nspaghettified." \
            "\nRight before you lose conciousness, you see an image of a forlorn boy sitting on an asteroid.\nYou get the stark feeling of wanting to talk to him." \
            "\nWhere IS this one?\nAnyway, it's too late now, because you're dead.")
            Winston.die()
            

    input("Press Enter to continue.")
#Qilia. Help two sisters grow closer.
def qilia(Winston):
    print(qilialogo)
    print("\nYou feel an overwhelming sense of dread and despair.\nIs this what the presense of demons feel like?" \
    "\nAfter you stop yourself from throwing up, you find yourslf in a basement." \
    "\nThere are multiple bookshelves filled with potions, spellbooks, and wands.\nSuddenly, " \
    "\n\"Oooooh! Girls, there's another demon here to torture you! " \
    "Wait a second, this is no demon.\"\nTwo very surly looking teenage girls turn the corner and stare you down.")
    
    print("What will you do?\n\n")
    proceed()
    q_option1 = input("1. Run as fast as you can out of this basement.\n2. Attempt to fight\n3. Activate a ritual that summons Satan, Demon Overlord, to this world.\nHe will be at full infinite cosmic power, and fuse the Demon Realm with this mostly human populated planet."\
    "\nThis will be the end of all joy in this world.\nWait, how did you even think of that?\n")
    print("\n")
    match q_option1:
        case "1":
            print("\n\nYou run out of the basement, the demon waving goodbye.\n\nThe first thing you notice when you run out the front door is that the sky is PURPLE.\nThe entire horizon is blocked by a giant crater wall.\nWhere exactly IS this place?" \
            "\n\nYou keep running, out into the harsh barren desert, where the ground is red sand.\nThere are monsters everywhere...\nYou see a white squirrel. It suddenly goes from blurry to clear.\n\nYou feel that your fate has been sealed.\n\nSuddenly, a--\n[THE FOLLOWING DEATH HAS BEEN CENSORED FOR BEING TOO HORRIFFIC]\n")
            Winston.die()
        case "2":
            print("You hold up your arms in fisticuffs. The older of the sisters sets effortlessly herself on fire. You are very quickly incapacitated.")
            proceed()
            print("\nYou wake up, and you are glued to the wall.\nThere are ropes tied around your arms and leading to a big circle on the floor.\nIt seems these sadistic sisters are using you and your quite literally otherworldly body for some kind of spell.\n")
            proceed()
            print("\n\nYou learn a few things about them.\nThe older one's name is Qatherine, and the younger Qaitlyn.\nThey seem like they're enjoying this ritual, almost in a cute way.\nThey start off working in silence, but slowly start talking with each other more." \
            "\n\nThey're relationship seems a bit tenuos. You sense a slight bit of tension between them.\n What makes it worse is Raymond, the demon. Every time the demon opens his mouth, the sisters' mood gets worse.\nYou get the impression that Raymond is doing it intentionally.\n\n\"\"")
            q_finaloption = input("1. Go between the girls and try and fizzle out the conflict.\n2. Laugh obnoxiously and go on a villain monologue\n")
            print("\n")
            match q_finaloption:
                case "1":
                    print("\"STOP FIGHTING!\"\nThe two sisters look blankly at you.\n\"C'mon, can't you guys just get along?\"\n\nThe two of them stare at you.\"Soooo, what are you trying to say?\" Qaitlyn said.\n\n\"I, uh... I dunno. I guess what I just \"")
                case "2":
                    print("\n\"MWAHAHAHAHAHAHA!\nLITTLE DO YOU LITTLE GIRLS KNOW, ME AND MY BEST BUDDY RAYMOND HERE ARE SLOWLY CORRODING YOUR ALREADY SHAKY RELATIONSHIP!\n\"\nAs you bleed out, you hear one sister go, \"You're not bad.\"" \
                    "\nYou think, despite being killed, you did the right thing in this realm.")
                    Winston.die()
                    Winston.complete_realm(Winston.q_available)
                    Winston.q_available = False
        case "3":
            print("Well... what you wanted to happen happens.\nI don't think that was the right choice, because you experienced a terrifying painful death.")
            Winston.die()
    
    proceed()
#Primordia. Help an engineer with her insecurity
def primordia(Winston):
    print(primordialogo)
    print("You're in a lush jungle.\nYou look over the edge of this island and you see bright skies. " \
    "Endless sky, actually." \
    "\nIt goes down endlessly, with other islands dotting the landscape.\nSuddenly, a large shadow looms over you.\nYou turn around and a giant Tyrannosaurus Rex is staring you down.")
    proceed()
    cowsay.trex("What are you doing here?")
    print("\nWhat do you do...?\n")
    primordiachoice1 = input("1. I mean you no harm, sir!\n2. PLEASE HAVE MERCY!\n3. I'm a multiversal traveller from an entirely different plane of existence, and I'm here to explore you world.\n4. [Run away screaming]\n5. 6767676767676767")
    
    print("\nThe T-rex opens his giant mouth and swallows you whole. You get the stark feeling this would have been the conclusion no matter what you picked.\nYou d...\nWait, you're still alive.\nSomething about this dino's stomach acid isn't melting you immediately.\n")
    proceed()

    print("\nThe T-Rex enters a flying ship. You can hear all the wrrs of the place.\nYou hear various voices.\n\"Hiiiiii, Rock! Can we do super cool muscle training soon?\"\n\"Rock, we're going to Salasaquam Island in 0800 hours, just thought you'd want to know.\"" \
          "\n\"Hey, uh... Rock. Could you enter my lab with me for a sec?\"\n \"Rock follows this voice.\"")
    proceed()
    print("\"What's up?\" Rock rumbles.\n\"Well, I've had a lot on my mind.\"")
    primordia_final_choice = input("1. \"I'm very sorry about that, Gilda.\"\n2. Slap her ungrateful self in the face.")
    match primordia_final_choice:
        case "1":
            print("")
        case "2":
            print("*SMACK*\n\"So you're telling me, you have a fulfilling job as an engineer,\na family that takes you in and loves you, including children that look up to you," \
            "\nand you're here like a weepy willow sack of sand?")
            print("...")
            print("...")
            Winston.complete_realm(Winston.p_available)
            Winston.p_available = False
    proceed()
#Padlocke. Talk to a bunch of eccentric children, and help a very sad one.
def padlocke(Winston):
    michaelapicked = False 
    print(padlockelogo)
    print("\nYou spawn right outside an elementary school with a statue of a giant smiling cartoon penguin. It has a sign that reads:")
    cowsay.tux("Paddy the Padlocke Penguin welcomes you to\nPadlocke Elementary School!")
    proceed()
    print("Wait a minute, they're not gonna let you in the building as some random dude.\nYou look around, and realize that everyone seems like a normal human in this world.\nThis gives you two options.")
    padlockechoice1 = input("1. Pass yourself off as a colorful mascot entertainer\n2. Register as a substitute teacher and just tell everyone you have jaundice\n")

    print("\n")
    match padlockechoice1:
        case "1":
            print("The administration seems to love your wacky yellow guy act.\nYou pass through with ease, and are allowed into Ms. Ottoman's Kindergarten class, where a kid is having a birthday party.\n10 minutes into your \"rolling around the room like a tire\" act, a kindergartner jumps up to you and tears your face off.\nMs. Ottoman sighs. \"Not AGAIN, Stacy.\"\nYou die.")
            Winston.die()
        case "2":
            print("\n\nAdministration is... very interested in your appearence, but lets you through.\nIt turns out that Mrs. Baker's class has ZERO teachers right now.\nMrs. Baker is out, and her student teacher is swamped with finals.\nYou are very glad you are not swamped with finals.\n\nYou're warned that this is the \"gifted and talented\" class.\nYou're a bit confused. Shouldn't that mean that they should be easier to deal with?")
            proceed()
            print("\nIn the classroom, you find a very long and organized binder for all... eight kids? How hard could eight kids be--\nYou were very wrong.\nRunning around, screaming, far too impassioned debates about children's cartoons...\nand one of the students is in the corner, in some partitioned \"Chill-Out Corral\". You see their description, and it seems like it's Michaela.\nIt's possible the other kids could use your attention.\nWhich student will you go to first?")
            while michaelapicked == False:
                padlockechoice2 = input("\n1. The boisterous and overconfident Cooper" \
                "\n2. Levelheaded and \"alt\" Chloe" \
                "\n3. Overdramatic Augustine" \
                "\n4. Silent but mischevious Micah" \
                "\n5. Introvert and general nerd Erin" \
                "\n6. (Usually) extrememly energetic Michaela" \
                "\n7. Studious and just a tad stuck-up Aashvi\n8. Self-described class clown Jesse\n\n")
                print("\n\n")
                match padlockechoice2:
                    case "1":
                        print("\"Sooooooo, how many lambos you got?\"\nThe binder warned you about Cooper.\nA very showy boy.\n\"My online mentor said that if I meet an older man and he doesn't make at least 6 bands, he's not worth my time.\nConsidering that you're working as a substitue teacher... you're probably a cuck.\"\n\nOkay, that's enough. Next kid.")
                    case "2":
                        print("Chloe was flipping throw a tween fashion magazine, \"Riot\".\n\"So, do you have jaundice?\"\n\"Yes, I do, little lady.\"\n\"Cool,\" is all she says before flipping through her magazine again.\nApparently, jaundice is cool. Duly noted.")
                    case "3":
                        print("The kid swishes his hair." \
                        "\n\"You look like you'd enjoy the series Neon Genesis Evangelion, sir.\nYou're obviously going through an existential crisis.\"" \
                        "\nHis silent friend, Micah, nods.\nYou decide to watch it for yourself.\nBy time you finish The End of Evangelion you're genuinely too depressed to wanna do anything.\n")
                    case "4":
                        print("Micah looks at you with his large innocnet eyes." \
                        "\nYou read on the binder that he's semiverbal and communicatess with drawings. How cute!\nMicah shows you a drawing of...\na yellow man...\nwith his eyes pecked out and his intestines exposed, with while seagulls flying above him." \
                        "\n\nYou recoil.\n\n\"Oh, Micah's just trying to get a reaction out of you,\" " \
                        "Augustine, his friend, said.\n\nReaction gotten.\nMaybe it's best to check on a different kid...")
                    case "5":
                        print("You approach a girl who has the thickest book you've ever seen, along with a neat stack of a bunch of math homework.\n\"Would you like to double-check my calculus problems? Just something I did for fun.\"\n\"I, uh, never did calculus in high school.\"\n\"Well, can I at least give you a lore dump of Braden Sandman's fantasy-sci fi universe?\" She hoolds up the ginormous book.\nAfter 2 hours, you know a lot more about subatomic physics than you thought you'd ever know.\nOkay, next kid.")
                    case "6":
                        michaelapicked = True
                        print("You enter the \"Chill-Out Corral\".\nThe girl seems very uncomfortable with a random adult entering this space.\nYou decide just say \"are you okay?\"")
                        print("The girl looks of to the side. \"Not really.\"")
                        proceed()
                        print("\n\"Sometimes I feel... weird. I'm happy, then suddenly I'm not.\nI like how things are now, mostly, but it's not gonna be like that forver.\nSoon I'm gonna havta learn how to pay taxes, and be depressed because I'm an adult,\nand I'll never have fun until I'm 75 but by then I'll have arthritis and not be able to move, or something.\nAnd then I'll just watch old cartoons all day. And then die.\"")
                        proceed()
                        print("\n\nYou're not sure of what to say at first.\n\"Getting older's not that bad. You'll have new things you can be grateful for, like greater freedom.\nI guess it's not all sunshine and rainbows,\nbut you get to drive Wiggle Wagglez and have Guys Nights and gamble and mess up lotteries and go out into space and blow stuff up...\nAt least, that's what I did.\"")
                        print("The girl looks very curious, and a bit delighted, so you deciede to tell her some tales of your life.\nAfter a while, she seems to feel just a bit better.\nThe clock strikes 3:00 pm and all the kids go home.\nIt's time to for you to go... well, not home, but back to the liminal space.\n")
                        Winston.complete_realm(Winston.pe_available)
                        Winston.pe_available = False
                    case "7":
                        print("The braided girl has dozens of papers surrounding her.\n\"Can you help me with this 9th grade Algebra? I need to compete with Erin.\"\nYou took a look at the papers. Math was never your strong suit. You shrug at her.\n\"Then you're USELESS to me.\"\nOkay, then.")
                    case "8":
                        print("When you approach the kid, he tilts his head.\n\"You know... you kinda look constipated.\"\nThe other kids stare at him.\n\"No he doesn't...?\" said Chloe.\nYou get such strong second-hand embarrasement that you wanna die.")
                input("Press Enter onne more time to get back out there.")
    #nThis feels like the same place you were created in. The 'current' you, actually.

def home(Winston):
    Winston.in_loop = False
    print("...gulp.")
    proceed()
    print("You've learned so much through your journey through this strange, vast multiverse." \
    "\nYou learned that it's never too late to redeem yourself." \
    "\nBonds that have been sour for long don't have to stay that way." \
    "\n\nAnd growing up is... okay.")
    proceed()
    print("You go back to your old town.\nSince the Kate-Marcimus Empire was defeated by you, things have gotten better." \
    "\nYou pay a visit to your old friend Michael Theque Whytman's grave.\n\"I hope that other Michael's as weird as you were.\"")
    proceed()
    print("You go to Hopper's old house. You missed him--her?!")
    proceed()
    print("Pinky.\n\"Hey.\"\n\"Hey.\"\n...\"You look happier,\" Pinky says.\n\"You, too,\" you say.")
    proceed()
    print("Well, that's enough. You're thinking that you could go back out there.")
    proceed()
    print(endlogo)

def main():
    #setting the character, Winston. All the default values suffice
    winston = Character()
    
    
    #The Core Loop
    while winston.in_loop == True:
        #At the start of every loop will be a line to signify the beginning
        print("------------------------------------------------------------------------")
        #Intro text, will change on certain conditions like loops passed through, or if at least one realm was completed
        intro_text(winston)

        #The Stats Page that comes before the dimension select screen, only appears if you've been through a loop at least a single time
        stats_page(winston)

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
                if winston.home_available == True:
                    home(winston)
                    #in_loop = False
            case _:
                print("Option not valid. You find yourself stretching to some unknown place in the universe...\nMaybe just pick one of the numbers given next time...\n")
                input("Press Enter to continue.")
        #add another to the loop counter
        winston.loops += 1

if __name__ == "__main__":
    main()