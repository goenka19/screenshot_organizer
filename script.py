#first script  - uses clunky if else statements

import os 
import shutil
from datetime import date, datetime, time

#The Home directory where screenshots will be stored initially and where action will take place
home_dir= "/Users/ujjwalgoenka/Desktop/Screenshots"

#directory path to the folders where screenshots need to be transferred
dir_one = "/Users/ujjwalgoenka/Desktop/Semester 2/Managment Accounting/screenshots" #MA
dir_two = "/Users/ujjwalgoenka/Desktop/Semester 2/Corporate Finance/new"            #CF
dir_three = "/Users/ujjwalgoenka/Desktop/Semester 2/QT/screenshots"                 #QT
dir_four = "/Users/ujjwalgoenka/Desktop/Semester 2/Macro/screenshots"               #Macro
dir_five = "/Users/ujjwalgoenka/Desktop/Semester 2/POM/screenshots"                 #POM
dir_six = "/Users/ujjwalgoenka/Desktop/Semester 2/IT/screenshots"                   #IT

dir_error_check = "/Users/ujjwalgoenka/Desktop/untitled"


#time to compare
class_one_start = time(12,30,00)
class_one_end = time(14,30,00)
class_two_start = time(15,00,00)
class_two_end = time(17,00,00)
class_three_start = time(10,00,00)
class_three_end = time(12,00,00)

#date after it starts comparing 
start_date = date(2021,1,10)

#listing the content of home directory
files = os.listdir(home_dir)

for file in files:
    if file.endswith(".png"):
        date_time = datetime.strptime(file, "Screenshot %Y-%m-%d at %I.%M.%S %p.png")
        only_time = date_time.time()
        day = date_time.strftime("%A")
        if datetime.date(date_time) > start_date:
            if (only_time > class_one_start and only_time < class_one_end and day == "Monday") or (only_time > class_two_start and only_time < class_two_end and day =="Tuesday" ): # Management Accounting 
                print("MA")
                shutil.move(home_dir+"/"+file,dir_one+"/"+file)
            elif (only_time > class_two_start and only_time < class_two_end and day == "Monday") or (only_time > class_two_start and only_time < class_two_end and day =="Friday" ): # Corporate Finance
                print("CF")
                shutil.move(home_dir+"/"+file,dir_two+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Tuesday") or (only_time > class_one_start and only_time < class_one_end and day =="Thursday" ): # Quantative 
                print("QT")
                shutil.move(home_dir+"/"+file,dir_three+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Wednesday") or (only_time > class_one_start and only_time < class_one_end and day =="Friday" ): # Macroeconomics
                print("Macro")
                shutil.move(home_dir+"/"+file,dir_four+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Saturday") or (only_time > class_two_start and only_time < class_two_end and day =="Wednesday" ): # POM
                print("BST")
                shutil.move(home_dir+"/"+file,dir_five+"/"+file)
            elif (only_time > class_three_start and only_time < class_three_end and day == "Thursday") or (only_time > class_two_start and only_time < class_two_end and day =="Saturday" ): # IT
                print("IT")
                shutil.move(home_dir+"/"+file,dir_six+"/"+file)
            else:
                pass
                #print("Time not bound")
        else:
            #print("Error")
            pass
    
    else:
        #print(file)
        #print("File not compatible") #mainly for .ds store file 
        pass

