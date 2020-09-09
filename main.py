#!Python3

import datetime, time, os

class MyClass:
    def __init__(self, class_name : str):

        self.name = class_name

#setting up my personal class schedule
schedule = []
schedule.append(MyClass("Internet_Systems_Programming"))
schedule.append(MyClass("Food_Ethics"))
schedule.append(MyClass("Computer_Systems"))

#Menu Selction
for x in range(len(schedule)):
    print('{}. {}'.format(x+1, schedule[x].name))
print("\nSelect a Class: ", end = "")

#Need to add error handling
current_class = schedule[int(input())-1]

current_time = time.localtime()


print("\nStart taking notes!!\n(Press Enter w/o any input to EXIT)")

#File name is the current date .txt
#files are stored in a folder for the name of the class
f = open(os.getcwd() + "/notes/" + "/" + current_class.name + "/" + "{}-{}-{}".format(current_time.tm_year, current_time.tm_mon, current_time.tm_mday) + ".txt", "a+")

while True:
    current_time = time.localtime()
    current_time = "\n{}:{} -- ".format(str(current_time.tm_hour), str(current_time.tm_min)) 
    line = current_time + input()
    if line == current_time:
        break
    f.write(line)

f.close()




