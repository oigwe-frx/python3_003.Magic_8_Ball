import random;

# Name of the individual asking the questions
name = "Osita";

# Question Asked
question = "Will I win the MegaMillion Lottery, tonight?";

# Variable to store the Magic 8 Ball's Answer
answer = "";

# Variable to store the randomly generated value and answer
random_number = random.randint(1,9);

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
elif randome_numer == 9:
  answer += "Very doubtful"
else:
  answer += "Error"

# Output of the question
print(name + ' '  + "asks: " + question)

# Output of the generated answer
print("Magic 8-Ball's answer: " + answer)
