import random
import getpass

from configparser import ConfigParser

#Lists of dinner choices
main_courses = ['chicken fillet', 'filet mignon', 'steak', 'porkchop with cheese']
side_dish = ['potatoes', 'french potatoes', 'rice', 'buckwheat']
salads = ['caesar salad', 'tomato salad', 'pickles']
drinks = ['natural juice', 'soda', 'tea', 'coffee', 'iced tea', 'wine']
desserts = ['chocolate cake', 'honey cake', 'bun']

array = []

#This function takes name and category of dinner course and uses randomize function to ask questions to user and display randomized foods/drinks
def questionairre(name, category_list) :
    #While True loop to allow user chance to retry input in case they misclick
    while True :
        random = randomize(category_list)
        answer = input('Do you want an ' + name + '? (y/n)' )
        if answer == 'y' or answer == 'yes' :
            print('Okay! Your ' + name + ' is ' + random + '!')
            return random
        elif answer == 'n' or answer == 'no' :
            print('As you wish!')
            return
        else :
            print('Make sure you input an correct answer!')

#This function takes dinner course category and randomizes an number from list lenght and returns string from that list according to randomized number
def randomize(category_list) :
    lenght = len(category_list) - 1
    if lenght <= -1 :
        return 'solanka'
    else :
        randomized_number = random.randint(0, lenght)
        return category_list[randomized_number]

#Reads config.ini file to get uname and password for developer access, then uses it to allow access to developer
def authorized_access() :
    try :
        config = ConfigParser()
        config.read('config.ini')

        dev_uname = config.get('developers', 'dev1_uname')
        dev_pass = config.get('developers', 'dev1_pass')
    except :
        print('Ah, pickles! Something wrong with config.ini file!')

    #Gives user chance to input username and password provided in the config.ini file
    try :
        uname = input('Username: ')
        pswd = getpass.getpass('Password: ')

        if uname == dev_uname and pswd == dev_pass :
            return True
        else :
            return False
    except :
        print('Ah, pickles! Something wrong with authorization')

#Uses previous authorized_access function to give user chance to log in as guest or developer
def authorization() :
    try:
        print('1. Guest')
        print('2. Authorized access')
        what_kinda_access = input('Which access you wish to have? ')
        if what_kinda_access == '2' :
            return authorized_access()
        elif what_kinda_access == '1' :
            return
    except:
        print('Ah pickles! Something went wrong with authorization')

if __name__ == "__main__" :
    #Main function, which contains both functions which are ran from this fragment of code
    #Try except code to prevent problems ruining further code, for example, user is using Python version below 3
    try :
        #Runs the authorization code, which determines if user is either guest or developer
        access = authorization()
        if access == True :
            print('Hello developer!')
        else :
            print('Hello guest!')
        #While True loop to allow user chance to retry input in case they misclick
        while True :
            #Kind of useless line of code, but its there for aesthetic
            is_program_running = input('Do you want to make yourself dinner, but cant decide what? (y/n) ')
            if is_program_running == 'y' or is_program_running == 'yes' :
                print('Alright, lets start!')
                l1 = questionairre('main course', main_courses)
                l2 = questionairre('side dish', side_dish)
                l3 = questionairre('salad', salads)
                l4 = questionairre('drink', drinks)
                l5 = questionairre('dessert', desserts)
                #Reroll code to allow user to try randomizing again without exiting programm
                reroll = input('Do you wish to roll another dinner idea? (y/n) ')
                if reroll == 'n' or reroll == 'no' :
                    print('Alrighty then! See ya!')
                    break

            elif is_program_running == 'n' or is_program_running == 'no' :
                print('Well, alright then! If you change your mind, come back! :)')
                break
            else :
                print('Make sure you input an correct answer!')
    except :
        #Except text to let user know that something went wrong or they are using Python version below 3
        print('Something went pickles :( please contact my creator! And make sure you are using Python version 3! :)')
