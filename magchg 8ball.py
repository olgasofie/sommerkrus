import random 
name = "lisa"
answer = ""

random_number = random.randint(1,8)
quesion = input ("what do you want ot ask ? ")

if random_number == 1:
     answer = "yes"
     
elif random_number == 2:
   answer = "mabye"

elif random_number == 3:
   answer = "no"
elif random_number == 4:
    answer = "thru"
elif random_number == 5:
    answer = "dare"
elif random_number == 6:
    answer = "ded "
elif random_number == 7:
    answer= "survive"
else:
    answer = "sorry somting went wrong"
print(f"\n hi {name} the answer to you question is {answer}\n")