import random

main_courses = ['chicken fillet', 'filet mignon', 'steak']
side_dish = ['potatoes', 'french potatoes', 'rice']
salads = ['caesar salad', 'tomato salad', 'pickles']
drinks = ['natural juice', 'soda', 'tea', 'coffee']
desserts = ['chocolate cake', 'honey cake', 'bun']

def questionairre(name, category) :
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

def randomize(category) :
    number = len(category) - 1
    randomized_number = random.randint(0, number)
    return category[randomized_number]

try :
    while True :
        is_program_running = input('Do you want to make yourself dinner, but cant decide what? (y/n)')
        if is_program_running == 'y' or is_program_running == 'yes' :
            print('Alright, lets start!')
            questionairre('main course', main_courses)
            questionairre('side dish', side_dish)
            questionairre('salad', salads)
            questionairre('drink', drinks)
            questionairre('dessert', desserts)
            reroll = input('Do you wish to try another dinner idea? (y/n)')
            if reroll == 'n' or reroll == 'no' :
                print('Alrighty then! See ya!')
                break

        elif is_program_running == 'n' or is_program_running == 'no' :
            print('Well, alright then! If you change your mind, come back!')
            break
        else :
            print('Make sure you input an correct answer!')
except :
    print('Something went pickles :( please contact my creator!')
