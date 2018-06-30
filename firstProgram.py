# The point of this exercise is to examine conditional statement/logic flow
# A large portion of programming and development is working in a team
# Essentially you will be given a small portion of a larger project
# This program is a conditional role-playing game through CLI (Command Line Interface)
# Each segment of the story is printed to the console (CLI) and progresses via user input ( "Y" / "N" )
# Your task, should you choose to accept it, is outlined below
# Be sure to study the code, as it has all of the answers already within it

### HINT: Feel free to copy paste certain bits of code and change it within your section as you need.
###       A core principal of programming and development is laziness. However, don't feel obligated 
###       to copy/paste if you don't yet grasp the code, as it is beneficial to understand it also.

##This class handles the ANSI color options for printing to console :::DO NOT MODIFY:::

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

##Beggining of story
print(bcolors.WARNING + "This is a story, and you will decide the ending" + bcolors.ENDC)

##Capture user input as name 
name = raw_input(bcolors.OKGREEN + "--Please, tell us your name? \n" + bcolors.ENDC)

##Confirm user input with greeting
print(bcolors.OKBLUE + "--Hello, " + name + "!!! \n" + bcolors.ENDC)

##Ask and store user input into answer variable
answer = raw_input(bcolors.OKGREEN + "--The tower pyre has gone dark, and we have no signal for aide. \n Please, "
                   + name +
                   ", could you find it in your heart to help us poor souls and relight the signal fire? \n Y/N \n" + bcolors.ENDC)

##Convert user input into uppercase for typecatching evaluation
answer_upper = answer.upper()

##Test if user answer is positive
if answer_upper == 'Y' :
    ##Continue engaging user
    print(bcolors.OKBLUE + "--You have the heart of a lion, praise heavens to our good fortune!" + bcolors.ENDC)

    ##Continue plot action
    print(bcolors.WARNING + "--You make your way to the stairs." + bcolors.ENDC)
    print(bcolors.WARNING + "--You look back at the steward of the tower, he grins softly in the dim candlelight" + bcolors.ENDC)

    ##Grab user input for action scenario
    first_terrace = raw_input(bcolors.OKGREEN + "--First terrace: \n You look around a pale moonlit room. \n Cobwebs obscure your view; however, you see the shape of a chest. \n Clear a path and open the chest? \n Y/N \n" + bcolors.ENDC)

    ##Convert user input into uppercase for typecatching evaluation
    first_terrace_upper = first_terrace.upper()

    ##Test if user answer is positive
    if first_terrace_upper == 'Y' :

        ##Warn user of consequence
        print(bcolors.WARNING + "--You've awakened the arachnid Ophelia." + bcolors.ENDC)

        ##Capture user input 
        fight = raw_input(bcolors.OKGREEN + "--She darts towards you, do you : \n 1. Dodge her advance \n 2. Attempt to draw your blade \n 3. Freeze in horror \n " + bcolors.ENDC)

        ##Test user input among a set of conditionals
        if fight == str(1) :
            print(bcolors.OKBLUE + "--You successfully avoided attack! \n You draw your blade and plunge it deep into Ophelia's thorax, rendering her dead." + bcolors.ENDC)
            print(bcolors.BOLD + "--You obtain a vial of Arachnid Venom!".upper() + bcolors.ENDC)
            print(bcolors.OKGREEN + "--You smash the hilt of your sword against the padlock of the chest revealing the contents. \n" + bcolors.ENDC)
            print(bcolors.BOLD + "--You obtain a Helm of Lights Mercy!".upper() + bcolors.ENDC)


            #######################################
            ###### YOUR CODE BELOW THIS LINE ######
            #######################################



            # First create a prompt for user input and store that input within a semantic variable 
            ### HINT: User input should be in the form of number options or a string literal of "Y" or "N"
            
            # Next create a conditional statement
            ### HINT: If testing for a number(int) input ensure that you are using the str(input) function to coerce data types
            ### HINT: For a prompt that accepts only 2 responses, you only need to test logic for one
            ### HINT: For a prompt that accepts multiple responses, you might save the one that ends the program for the else condition



            #######################################
            ###### YOUR CODE ABOVE THIS LINE ######
            #######################################

        elif fight == str(2) :
            print(bcolors.FAIL + "--You couldn't draw your blade quick enough, Ophelia has rendered you lifeless. \n Farewell brave traveler." + bcolors.ENDC)

        ##End Program
        else :
            print(bcolors.FAIL + "--You didn't even try?" + bcolors.ENDC)
    ##End Program
    else :
        print(bcolors.WARNING + "Fortune favors the bold... too bad you're just a bitch..." + bcolors.ENDC)

##End Program
else :
    print(bcolors.FAIL + "--You coward, be gone!" + bcolors.ENDC)
    print(bcolors.FAIL + "--You were forcefully thrown out of the tower window to your death." + bcolors.ENDC)


##############################################################################
#
# For the future : 
#       We will be taking the items gathered from each scene and storing 
#       them into an array or form of collection. This will allow us to
#       use the items in our RPG at a later time.
#
# Use case :
#       When user reaches top of tower, user will have the tools needed 
#       to light the pyre. A test will be needed to check users collection
#       for the right equipment, if true => light the fire and trigger 
#       win case, else => trigger lose case and end program.
#
# For the future : 
#       We will eventually refactor the program to utilize functions when
#       engaged in combat. These functions will implement a stats system
#       that will track user hit points/atk/def. As well as build objects
#       that represent enemy encounters.
#
# Use case :
#       When user encounters enemy, user will be able to utilize attacks
#       and users equipment will determine the users atk/def skills.
#       User will also be able to utilize equipment earned through each 
#       tier to heal/replenish life.
#
##############################################################################