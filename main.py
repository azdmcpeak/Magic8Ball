import random


# ackward introduction explaining what the program is
print("Hello, I am a magic 8 ball, but not like a physical magic 8 ball (since i'm a computer program) but a digital construct of a magic 8 ball, I will also answer any question you have.")

# asking for the users name while splitting the inputs into two different variables
first, last = input('\n What is your First and Last name? ').split()

#putting the first and last name into a list so it can be called as two seperate entities
name = [first,last]


#creating a loop, if entering an integer is entetered, it will prompt them to enter their name again
while  first.isdigit() or last.isdigit():
    if name != str:
        print('Please enter a name. ')
    first, last = input('\n What is your First and Last name? ').split()
else:
    pass

# asking the user a question
question = input('\n Ask me any question, you are seeking an answer to. ')

#creating a loop, if entering a integer, it will prompt them to enter their question again
while question.isdigit():
    if question != str:
        print('Please enter a valid question ')
    question = input('\n Ask me any question you are seeking an answer to. ')
else:
    pass


# takes the first and second input (first and last name) and converts them into all lower case expect the first letter and makes them into one varible
name_new = first.capitalize() + " " + last.capitalize()

# in progress statement
print(f'\n Well, {name_new} , "{question}",  is a good question, let me think about it. ')

# list of responses to be given to question
responses = [
    'What will happpen is going to the happen the way it was meant to happen and will not happen any other way.',
    'It will not not happen.', 'Sounds like a you problem.', 'yeah sure, why not.', 'error 404, answer not found.',
    'That sounds like a question for Siri.', ' I pridict this happening in the future.', 'yolo!!', 'yyyaasssss!!!',
    'Do it, but get really drunk first.', 'Only on Tuesdays.', 'If the sky is blue, then yes.',
    "We'll agree to disagree.", 'No. Just No. Not maybe, not kinda. Just, No.', 'No hablo ingles.',
    "In your dreams... so if you're dreaming than yes.", 'Chances seem high, I have spoken.', " 'probs. ",
    'Totes ma gotes.', 'I am Groot.']

# making a function that chooses a random choise from the list of responses so it can be called in a print statment
given_reponse = random.choice(responses)

# giving the user an answer to their question with a reandomly chosen response from the previous list.
print(f'\n The answer to your question, " {question} " is, {given_reponse}')


#function including the "question" variable, answer and answers to be given.
def tellem():
    question_2 = input('\n Ask me any question you are seeking an answer to. ')
    while question.isdigit():
        if question_2 != str:
            print('Please do not enter a valid question.')
        # in progress statement
    print(f'\n Well, {name_new} , "{question_2}",  is a good question, let me think about it. ')
    responses_2 = [
            'What will happpen is going to the happen the way it was meant to happen and will not happen any other way.',
            'It will not not happen.', 'Sounds like a you problem.', 'yeah sure, why not.', 'error 404, answer not found.',
            'That sounds like a question for Siri.', ' I pridict this happening in the future.', 'yolo!!', 'yyyaasssss!!!',
            'Do it, but get really drunk first.', 'Only on Tuesdays.', 'If the sky is blue, then yes.',
            "We'll agree to disagree.", 'No. Just No. Not maybe, not kinda. Just. NO.', 'No hablo ingles.',
            "In your dreams... so if you're dreaming than yes.", 'Chances seem high, I have spoken.', " 'probs. ",
            'Totes ma gotes.', 'I am Groot.']
    # making a function that chooses a random choise from the list of responses so it can be called in a print statment
    given_reponse_2 = random.choice(responses_2)
    # giving the user an answer to their question with a reandomly chosen response from the previous list.
    print(f'\n The answer to your question, " {question_2} " is, {given_reponse_2}')


#loop asking if they want to play again, as long as the user answers "yes" to the "a" question, it will run infintly.
    #if they answer "no" there is a unique response and the program terminates,
    #and if they answer anything other than "yes" or "no" they get a unqiue response and program terminates.
answer = 'yes'
while answer:
    a = input('\n Would you like to ask me another question? Yes or No. ')
    answer_2 = a.capitalize()
    if answer_2 == 'Yes':
       tellem()
    elif answer_2 == 'No':
        print('Peace out girl Scout')
        break
    else:
        print ('No more soup for you!, come back ONE YEAR!')
        break