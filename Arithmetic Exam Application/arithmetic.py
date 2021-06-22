import random
import time
exam_task = None
tasks = 0
success = 0
easy = 'simple operations with numbers 2-9'
hard = 'integral squares of 11-29'
level = None
def squares_tasks():
    global exam_task
    task = random.randrange(11, 30)
    exam_task = task
    print(task)

def task_generator():
    global exam_task
    num_1 = random.randrange(2, 10)
    num_2 = random.randrange(2, 10)
    oper = random.choice('+-*')
    task = f'{num_1} {oper} {num_2}'
    exam_task = task
    print(task)


def user_exam():
    global tasks, success
    start = time.perf_counter()
    print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
    choice = input()
    if choice == '1':
        level = easy
        task_generator()
        while tasks != 5:
            answer = input()
            if answer.lstrip('-+').isdigit() is False:
                print("Wrong format! Try again.")
            elif int(answer) == int(eval(exam_task)):
                print('Right!')
                task_generator()
                tasks += 1
                success += 1
            elif int(answer) != int(eval(exam_task)):
                tasks += 1
                print('Wrong!')
                task_generator()
    elif choice == '2':
        level = hard
        squares_tasks()
        while tasks != 5:
            answer = input()
            if answer.lstrip('-+').isdigit() is False:
                print("Incorrect format.")
            elif int(answer) == int(exam_task) ** 2:
                print('Right!')
                squares_tasks()
                tasks += 1
                success += 1
            elif int(answer) != int(exam_task) ** 2:
                tasks += 1
                print('Wrong!')
                squares_tasks()
    if tasks == 5:
        end = time.perf_counter()
        spent_time = round((end - start), 2)
        result = f"Your mark is {success}/5"
        print(f"{result}. Would you like to save the result? Enter yes or no. ")
        saving = input()
        if saving == "yes" or saving == 'Yes' or saving == 'YES' or saving == 'y':
            print('What is your name?')
            name = input()
            with open("results.txt", 'a', encoding="utf-8") as res:
                if level == easy:
                    res.write(f'{name}: {result} level 1 ({easy}).\n Time spent: {spent_time} sec')
                    res.close()
                    print('The results are saved in "results.txt".')
                elif level == hard:
                    res.write(f'{name}: {result} level 2 ({hard}).\n Time spent: {spent_time} sec')
                    res.close()
                    print('The results are saved in "results.txt".')
        else:
            exit()


user_exam()
