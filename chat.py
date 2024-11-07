#chat.py 
# A python chatbot designed to teach the principles of AI to DSA students 
#   <------- created by ------->
#       @author: Jacob Eason
#       @date: 11.1.24
#       @version: 0.1.1
#   <-------------------------->
# This is a modular chatbot written in python. This means that there are functions that contain response data and/or solutions
# to questions presented. for example: the AskForTheData function contains what code needs to execute when the chatbot is asked 
# what today's date is in the main body function. 


#imports <------ these are external modules that gives your core python installation extra functionality.
import sys
import random
from datetime import date    
from time import sleep


#typewriter effect
def typeOut(words):
    for char in words:
        sleep(0.125)
        sys.stdout.write(char)
        sys.stdout.flush()

#response to user asking for today's date
def AskForTheDate():
    def TodaysDate():
        today = date.today().isoformat()
        #print(today) #YYYY-MM-DD
        return(today)
    typeOut("today's date is: ")
    typeOut(str(TodaysDate()))

#tell jokes
def jokes():
    jokeList = ["What's a ghost\'s favorite street?", "What do you call a broken clock?", "What do you call an italian vampire?"]
    janswers = ["A dead end!", "A clo\tck", "Sad, because he can't eat garlic bread! :("]
    jnum = jokeList[random.randint(0,2)]
    typeOut(jokeList[jnum])
    sleep(2)
    typeOut(janswers[jnum])

#bot's favorite color
def colorFav():
    colorlist = ["Blue", "Green", "Yellow", "Grey"]
    cnum = [random.randint(0,3)]
    typeOut(colorlist[cnum])
    sleep(1)

#bot's favorite song
def songFav():
    songlist = ["Mr. Roboto by Styx!", "Better Harder Faster Stronger, by Daft punk!"]
    snum = [random.randint(0,1)]
    typeOut(songlist[snum])
    sleep(1)

#DSA info for the bot
def aboutBot():
    typeOut("I'm DolphinBOT! I'm a chatbot that can tell you all about Dolphin STEM Academy and answer basic questions like what\'s the current date or even tell jokes!")

def aboutDSA():
    typeOut("Dolphin STEM academy is an online learning community, dedicated to helping students develop a passion for STEM.\nOffering online homeschooling, online private school, and collage prep - our goal is to provide you with a unique learning experience that will prepare you for your future career.")

#main program starts here
def body():
    #name = "DolphinBOT"
    typeOut("\nHiya, My name's DolphinBOT! It's a pleasure to meet you!")
    sleep(1)
    #user enters a question and DolphinBOT responds 
    def helpMe():
        typeOut("\nLet me know exactly how I can be of assistance!")
        sleep(1.5)
        #program loop, runs while true - you can type quit to end it bc of the 'break' line in the elif statement 
        while(1):
            userInput = input("\n\nEnter your question here:\t")
            #userInputDate = userInput.find("date")
            if 'date' in userInput:
                AskForTheDate()
            if 'who are you' in userInput or 'tell me about yourself' in userInput:
                aboutBot()
            if 'STEM' in userInput or 'stem' in userInput:
                typeOut("STEM stands for Science, Technology, Engineering, and Math and is an approach to learning and development that integrates these core areas. Through STEM, students develop key skills including: problem solving, creativity, and critical analysis.")
           
            if 'what is dolphin stem academy' in userInput or 'what\'s dolphin stem academy' in userInput or 'what is Dolphin Stem Academy' in userInput or 'what\'s Dolphin Stem Academy' in userInput or 'what is DSA' or 'what\'s DSA' or 'what is Dolphin STEM Academy' in userInput or 'what\'s Dolphin STEM Academy' in userInput:
                aboutDSA()
            if 'joke' in userInput:
                jokes()
            if 'favorite color' in userInput:
                colorFav()
            if 'song' in userInput:
                songFav()
            #end program loop
            elif 'quit' in userInput or 'Quit' in userInput or 'QUIT' in userInput:
                typeOut("Goodbye!")
                sleep(3)
                break
            #catchall else statement
            else:
                typeOut("Sorry! I'm not quite sure how to respond to that kind of question yet!")
    helpMe()


#run DolphinBOT
body()