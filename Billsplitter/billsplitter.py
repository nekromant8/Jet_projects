# write your code here
import random
friends = {}
names = []
print("Enter the number of friends joining (including you):")

try:
    number_of_friend = int(input())
    if number_of_friend <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _i in range(number_of_friend):
            name_of_friends = input()
            names.append(name_of_friends)
        print("Enter the total bill value:")
        bill_value = int(input())
        friends = dict.fromkeys(names, round(bill_value / number_of_friend, 2))
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky = input()
        if lucky == "Yes":
            lucky_name = random.choice(names)
            print(f"{lucky_name} is the lucky one!")
            friends = dict.fromkeys(names, round(bill_value / (number_of_friend - 1), 2))
            friends.update({f"{lucky_name}": 0})
            print(friends)
        else:
            print("No one is going to be lucky")
            print(friends)
except ValueError:
    print("No one is joining for the party")

