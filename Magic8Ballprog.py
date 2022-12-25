#Magic 8 Ball program....................
import random

name = "Allen"
answer = ""
question = "Will I win the lottery?"


if name == "":
  print("Question: " + question)

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
  
random_number = random.randint(1, 10)
print(random_number)


if random_number == 1:
  answer = "Yes - definitely."
  print(answer)


elif random_number == 2:
  answer = "It is decidedly so."
  print(answer)

  
elif random_number == 3:
  answer = "Without a doubt."
  print(answer)


elif random_number == 4:
  answer = "Reply hazy, try again."
  print(answer)


elif random_number == 5:
  answer = "Ask again later."
  print(answer)


elif random_number == 6:
  answer = "Better not tell you now."
  print(answer)


elif random_number == 7:
  answer = "My sources say no."
  print(answer)


elif random_number == 8:
  answer = "Outlook not so good."
  print(answer)


elif random_number == 9:
  answer = "Very doubtful."
  print(answer)

elif random_number == 10:
  answer = "Maybe not."
  print(answer)

#End................