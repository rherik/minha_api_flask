from time import sleep
with open('tweets.csv', 'r') as file:
    for n in file:
        sleep(2)
        print(n)