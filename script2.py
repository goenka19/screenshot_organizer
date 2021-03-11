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
    if not file.endswith(".png"):
        #print(file)
        #print("File not compatible") #mainly for .ds store file
        continue
    if not file.startswith("Screenshot"):
        #for any png that is not a screenshot
        continue
    date_time = datetime.strptime(file, "Screenshot %Y-%m-%d at %I.%M.%S %p.png")
    only_time = date_time.time()
    day = date_time.strftime("%A")
    if not datetime.date(date_time) > start_date:
        #print("Time Not Bound")
        continue
    if class_one_start < only_time < class_one_end:
        _subject_map = {'Monday': dir_one, 'Tuesday': dir_three, 'Wednesday': dir_four, 'Thursday': dir_three, 'Friday': dir_four, 'Saturday':dir_five}    
    elif class_two_start < only_time < class_two_end:
        _subject_map = {'Monday': dir_two, 'Tuesday': dir_one, 'Wednesday': dir_five, 'Saturday': dir_six, 'Friday': dir_two}
    elif class_three_start < only_time < class_three_end:
        _subject_map = {'Thursday' : dir_six}  
    else:
       #print("Error")
       continue

    src_path = f'{home_dir}/{file}'
    #print(src_path)
    dst_dir = _subject_map.get(day, None)
    if dst_dir is None:
        #print(f'Could not figure out which class {file} belongs to')
        continue
    dst_path = f'{dst_dir}/{file}'
    #print(f'Moving {src_path} to {dst_path}')
    shutil.move(src_path, dst_path)