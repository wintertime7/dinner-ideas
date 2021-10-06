import random

#Lists of dinner choices
main_courses = ['chicken fillet', 'filet mignon', 'steak', 'porkchop with cheese']
side_dish = ['potatoes', 'french potatoes', 'rice', 'buckwheat']
salads = ['caesar salad', 'tomato salad', 'pickles']
drinks = ['natural juice', 'soda', 'tea', 'coffee', 'iced tea']
desserts = ['chocolate cake', 'honey cake', 'bun']

#This function takes name and category of dinner course and uses randomize function to ask questions to user and display randomized foods/drinks
def questionairre(name, category) :
    #While True loop to allow user chance to retry input in case they misclick
    while True :
        random = randomize(category)
        answer = input('Do you want an ' + name + '? (y/n)')
        if answer == 'y' or answer == 'yes' :
            print('Okay! Your ' + name + ' is ' + random + '!')
            return
        elif answer == 'n' or answer == 'no' :
            print('As you wish!')
            return
        else :
            print('Make sure you input an correct answer!')

#This function takes dinner course category and randomizes an number from list lenght and returns string from that list according to randomized number
def randomize(category) :
    number = len(category) - 1
    randomized_number = random.randint(0, number)
    return category[randomized_number]

#Main function, which contains both functions which are ran from this fragment of code
#Try except code to prevent problems ruining further code, for example, user is using Python version below 3
try :
    #While True loop to allow user chance to retry input in case they misclick
    while True :
        #Kind of useless line of code, but its there for aesthetic
        is_program_running = input('Do you want to make yourself dinner, but cant decide what? (y/n)')
        if is_program_running == 'y' or is_program_running == 'yes' :
            print('Alright, lets start!')
            questionairre('main course', main_courses)
            questionairre('side dish', side_dish)
            questionairre('salad', salads)
            questionairre('drink', drinks)
            questionairre('dessert', desserts)
            #Reroll code to allow user to try randomizing again without exiting programm
            reroll = input('Do you wish to roll another dinner idea? (y/n)')
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
