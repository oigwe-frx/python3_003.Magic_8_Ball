import random;

# Question Asked
question = "Will I win the MegaMillion Lottery, tonight?";

# Variable to store the Magic 8 Ball's Answer
answer = "";

# Variable to store the randomly generated value and answer
random_number = random.randint(1,9)

if random_number == 1:
  answer += "Yes - definitely"
elif random_number == 2:
  answer += "It is decidedly so"
elif random_number == 3:
  answer += "Without a doubt"
elif random_number == 4:
  answer += "Reply hazy, try again"
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 6:
  answer += "Better not tell you now"
elif random_number == 7:
  answer += "My sources say no"
elif random_number == 8:
  answer += "Outlook not so good"
elif random_numer == 9:
  answer += "Very doubtful"
else:
  answer += "Error"

# Output of the question
# Name of the individual asking the questions

#name = input('What is your name?')

try:
     name = input("What is your name?")
     if name and question:
       asks = "asks"
       print(name + " asks: " + question)
     elif name and not question:  
       print(name + "The Magic 8-Ball cannot provide a fortune unless you ask it something.")
     elif question:
        print('Question: ' + question)
     else: print("No name? No Question? Hmmm....")
except EOFError:
  print('Question: ' + question)




# Output of the generated answer
print("Magic 8-Ball's answer: " + answer)
