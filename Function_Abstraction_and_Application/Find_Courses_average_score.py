import math

# Calculate the average score of subjects
def score_average():
    print("Enter your scores. I will calculate your average score.")
    count = 0
    total = 0
    while True:
        score = input("score: ")
        while (score.isdigit() == False) or (score.isdigit() == True and (int(score) < 0 or int(score) > 100)):
            score = input("score again: ")
        if int(score) == 0:
            break
        else:
            score = int(score)
            total += score
            count += 1
    if count == 0:
        print("There is no score.")
    else:
        avg_score = round(total / count, 2)
        print("Your average score of {} subject(s) is {}".format(count, avg_score))

# Calculate the average score of subjects excluding errors
def score_average2():
    print("Enter your scores. I will calculate your average score.")
    count = 0
    total = 0
    fail_count = 0
    while True:
        score = input("score: ")
        while (score.isdigit() == False) or (score.isdigit() == True and (int(score) < 0 or int(score) > 100)):
            score = input("score again: ")
        if int(score) == 0:
            break
        else:
            score = int(score)
            if score < 60:
                fail_count += 1
            else:
                total += score
                count += 1
    if count == 0:
        print("There is no score.")
        print("You failed in {} subject(s).".format(fail_count))
    else:
        avg_score = round(total / count, 2)
        print("Your average score of {} subject(s) is {}".format(count, avg_score))
        print("You failed in {} subject(s).".format(fail_count))

# score_average()
# score_average2()
