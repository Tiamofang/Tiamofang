#practice while-else
#Simple guessing game:start with a random number and
#guess with hint until
#guess is correct
#the guess is out of range indicating the user is quitting
import random #get the random number module
number =random.randint(0,100)#get a random number
                             #between 0 and 100 inclusive
print 'Hi-lo Number_Guessing Game:between 0 and 100 inclusive.'
print # show a  blank line
guessString =raw_input('Guess a number:')
guess=int(guessString)#convert a str to an int

#while guess is range ,keep asking
while 0<=guess<=100:
    if guess<number:
        print 'Guessed Too Low!'
    elif guess>number:
        print 'Guessed Too High!'
    else:#guess the right one
        print 'Congraduationg!You get the num:',number
        break #break when you guess the right one~ so the lower level than
              #else expression
              #just break the while!!!attention!
    #keep going,get the next guess
    guessString =raw_input('Guess a number:')
    guess=int(guessString)
else:
    print "You quit early,the number was:",number
print "test the break!"
