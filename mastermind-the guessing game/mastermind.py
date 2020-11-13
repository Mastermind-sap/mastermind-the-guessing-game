import random
import itertools


class mastermind:
    def __init__(self):
        self.answer=str(random.randrange(1000,9999))

    def check_numbers(self,guess):
        num_correct=0
        a=list(self.answer)
        b=list(guess)
        for i in (b):
            if i in (a):
                a.remove(i)
                b.remove(i)
                num_correct+=1
        return num_correct

    def check_position(self,guess):
        pos_correct=0
        for (i,j) in zip(list(guess),list(self.answer)):
            if i==j:
                pos_correct+=1
        return pos_correct

    def main(self):
        for i in range(8):
            guess=input("Guess: ")
            if (guess.isnumeric()) and (int(guess) in range(1000,10000)) and (guess!=self.answer):
                print("You got "+str(self.check_numbers(guess))+" digits correct")
                print("You got "+str(self.check_position(guess))+" digits in correct position")
            elif (guess==self.answer):
                print("YOU WON! \nThe correct number is indeed "+self.answer)
                break
            else:
                print("Bad guess! \nThe number needs to be 4-digit")
        else:
            print("YOU LOOSE! \nYou exhausted all your eight guesses \nThe correct number is indeed "+self.answer)

print("MASTERMIND -THE GUESSING GAME")
print("\n\nYou will have 8 guesses to guess the four digit number")

while True:
    run=mastermind()
    run.main()
    a=input("Do you want to play again?(y,n) ")
    if a in ["YES","yes","y","Y","Yes"]:
        continue
    elif a in ["NO","No","n", "N","no"]:
        break
    
            
    
                
                
                
                
