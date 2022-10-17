# GRADE CALCULATOR
def gradeCalculator():
    print('***********Grade Calculator************\n')
    try:
        project_score = float(input('Please enter your Project Score: '))
        exam_score = float(input('Please enter your Exam Score: '))
        final_score = (project_score + exam_score) * .5
        if final_score > 100 or project_score > 100 or exam_score > 100:
            print("Score Error: Please enter right score, it can't be over 100")
        elif final_score >= 80:
            print(f"Your final Assessment Score is {final_score}%\n"
                  f"Your Final Assessment Grade: A ")
        elif final_score >= 70:
            print(f"Your final Assessment Score is {final_score}%\n"
                  f"Your Final Assessment Grade: B ")
        elif final_score >= 60:
            print(f"Your final Assessment Score is {final_score}%\n"
                  f"Your Final Assessment Grade: C ")
        elif final_score >= 50:
            print(f"Your final Assessment Score is {final_score}%\n"
                  f"Your Final Assessment Grade: D ")
        else:
            print("You're Fail")
            print('Work hard next time')
    except:
        print('Please enter right score')

gradeCalculator()

# Test Case 1 (
# Please enter your Project Score: 59
# Please enter your Exam Score: 59
# Your final Assessment Score is 59.0%
# Your Final Assessment Grade: D

# Test Case 2
# Please enter your Project Score: 80
# Please enter your Exam Score: 85
# Your final Assessment Score is 82.5%
# Your Final Assessment Grade: A
