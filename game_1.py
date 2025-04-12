import random

import time
def riddle_1():
    input("Press Enter to continue...")
    print(f"DEMON : Hey asshole, I have a riddle for you\n")
    time.sleep(2)
    print("Guess the number between 1 and 10\nIf your guess is wrong.I will fuck you and tear your ass.\nIf your guesss is right ,you get the key bastard!!")
    a=random.randint(1,10)
    print(a)
    b=int(input("Tell your guess : "))
    while(b!=a):
       
       print("Bam! You are fucked, try again.",end="\n")
       time.sleep(2)
       b=int(input("Tell your guess : "))
       
       
    #    print(a)
    else:
        print("You get the key, you lucky fucker!!")

    input("Press Enter to continue...")
       
    pass
def riddle_2():
    input("Press Enter to continue...")
    print("DEMON : Welcome Motherfucker\nThe second riddle goes as :\nFuck this dungeon, fuck that bitch, and fuck me if I care.")
    print("SOUL : In this riddle you have to count the no of time the word fuck has been repeated")
    time.sleep(3)
    s="Fuck this world, suck my soul, you damn fools, fuck everything, I will fuck you up, suckers,I am the mighty, fuck the rabid dog, burn in hell, you worthless, miserable fucks."
    print(s,"Count the number of time the word \"fuck\" is there in the sentence : ",sep="\n")

    while(True):

        b=input("Your Guess : ")
        if(int(b)==s.lower().count("fuck")):
            break
        else:
            print("DEMON : Try Again ,bastard")

    print("Fuck yeah, you got it!")
    input("Press Enter to continue...")
    pass
def riddle_3():
    hint = [
        "It is something sometimes even the wealthy struggle to achieve",
        "It is the light in the darkest of dungeons, the wind that whispers beyond these walls",
        "Birds soaring in the sky represent this concept",
        "Prison inmates dream of this every night",
        "Breaking chains leads to this ultimate goal",
        "Seven letters hold the key to your escape",
        "It's what rebels fight for in every revolution",
        "The opposite of captivity and confinement",
        "When restrictions and rules no longer bind you",
        "The American statue in New York symbolizes this"
    ]
    print("DEMON : Welcome Motherfucker\nThe Third riddle goes as :\n")
    print("Guess the password, or I will assume you are a Dumb bastard.\nYou have got 10 chances to guess")
    time.sleep(2)
    print("SOUL : This riddle is definately difficult where all of them have failed\nI hope you will shine to glory and escape this dungeon\n")
    print("SOUL : Here goes your hint : it is what you want most.")
    for i in range(10):
        
        print("DEMON : Enter your guess: ",end="")
        guess = input().strip()
        if guess.lower() == "freedom":
            print("DEMON : You got it, you bastard!")
            print("SOUL : Congragulation!!!\nYou are free to go, you made us proud!")
            break
        else:
            print("DEMON : Wrong guess you bastard")
            time.sleep(2)
            print("SOUL : Here is another hint: ", random.choice(hint))
            time.sleep(2)
    else:
        print("SOUL : Well it seems you are just another trespasser!!")
        print("DEMON : HAHA!!!,As i guessed it right you are just another dumb bastard who will be stuck forever in my dungeon rotting to death,HAHA!!!")
        game_over()
    pass
def game_over():
    print("GAME OVER!!! TRY AGAIN !!!")
print("Hey!,You bastard \nWelcome to my dungeon of doom\nTry to escape if you can\nMany tried all failed but some failed souls are still here who might guide you through this")
time.sleep(3)
print("SOUL : Hey whats your name?")
name = input("Enter your name: ")
print(f"SOUL : Hey {name}, You wake up in a shitty dungeon hell, you need to go through 3 levels to escape this hell\n")
time.sleep(1)
print("DEMON : Hey bastard seems you been talking some fucking soul over here!!")
time.sleep(2)


print("DEMON:Well if u have to escape this hell, you need to answer my riddle\n")
riddle_1()
print("DEMON : Well Well ,seems some bastard got lucky this time\nI am sure you wont get past my second riddle\nHere you go Son of bitch")
time.sleep(1)
riddle_2()
print("DEMON : I underestimated you, but this time I am sure you wont get past my third riddle\n")
riddle_3()

print("DEMON : Well, well, well, seems like you are the only lucky bastard\n")
print("SOUL : ENJOY YOUR FREEDOM, YOU DESERVE IT\n")
time.sleep(2)
print("GAME OVER !!!!")
input("press enter to continue...")

# print("\nI will give you a chance to escape\nBut first, you need to answer my riddle\nIf you answer correctly, I will let you go\nIf not, you will be trapped here forever\nSo, are you ready?\n")