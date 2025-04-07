# Write your code here 
import os
import json
import random

if os.path.isfile("scores.json"):
    with open("scores.json", "r") as user_data:
        user_data =json.load(user_data)
    
else:
    user_data = {}
    



name = input("what is your name ")
score = 0
 
if name in user_data:
    list_of_scores = user_data[name]
    print(f"your privious scores are {list_of_scores}")


print(max(user_data[name]))

def main():
    
    print("\n".join([
        "1: easy multiplication (2-12)*(2-12) " ,
        "2: easy-medium multiplication (anything ending in 0 or 5) * (2-30)" ,
        "3: medium multiplication (2-30)* (2-30)" ,
        "4: hard multiplication (2-50) * (2-50)" ,
        "5: impossible (2-100) * (2-100)" 
    ]))
    choice = int(input("give a number for which option you want "))
    if choice == 1:
        return easy()
    elif choice ==2:
        return easy_medium()
    elif choice == 3:
        return hard()
    elif choice == 4:
        return impossible()
    else:
        print("please input a numeber between one and five corisponding which with which difficulty you want")
def easy():
     global score
     #easy multiplication (2-12)
     for i in range(2):
        a = random.randint(2,12)
        b = random.randint(2,12)
        answer = a*b
        user_answer =int( input(f"what is {a} * {b}  "))
        if user_answer == answer:
            print("correct")
            score += 10
        else:
            print(f"incorrect, the correct answer is {answer}")
def easy_medium():
    global score
    #things ending in 0 or 5 * anything from 2-30
    for i in range(20):
        a = random.randint(1, 10)
        b = random.choice([0, 5])
        a = a*10+b
        c = random.randint(2, 30)
        answer = a*c
        user_answer = int(input(f"what is {a} * {c} "))
        if user_answer == answer:
                print("correct")
                score += 20
        else:
            print(f"incorrect, the correct answer is {answer}")
def medium():
    global score
    #thins from 2-30*2-30
    for i in range(20):
        a = random.randint(2-30)
        b = random.randint(2-30)
        anwser = a*b
        user_answer = int(input(f"what is {a} * {b} "))
        if user_answer == anwser:
            print("correct")
            score += 30
        else:
            print(f"incorrect, the correct answer is {anwser}")    
def hard():
    global score
    #2-50*2-50
    for i in range(20):
        a = random.randint(2, 50)
        b = random.randint(2, 50)
        answer = a*b
        user_answer = int(input(f"what is {a} * {b} "))
        if user_answer == answer:
            print("correct")
            score += 50
        else:
            print(f"incorrect, the correct answer is {answer}")
def impossible():
    global score
    #2-100*2-100
    for i in range(20):
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        answer = a*b
        user_answer = int(input(f"what is {a} * {b} "))
        if user_answer == answer:
            print("correct")
            score += 100
        else:
            print(f"incorrect, the correct answer is {answer}")

main()
print(score)

# user_data[name] = score
if name in user_data:
    user_data[name].append(score)
else:
    user_data[name] = [score]





with open("scores.json", "w") as f:
        json.dump(user_data, f)
