# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20221644 / w2052800
# Date: 2023.12.13

from graphics import *

#Function

def GetMarks (pass_credit,defer_credit,fail_credit):
    "  "
    if pass_credit==120:
        print("\nProgress")
        return "Progress - 120, 0, 0" 
  
    elif pass_credit==100 and (defer_credit==20 or fail_credit==20):
        print("\nProgress (Module Trailer)")
        return "Progress (Module Trailer) - {} , {} , {}".format(pass_credit,defer_credit,fail_credit)
            
    elif 100<pass_credit<=0 and 0<=defer_credit<=100 or 0<=fail_credit<=60:
        print("\nDo not Progress - Module retriver ")
        return "Module retriever - {} , {} , {}".format(pass_credit, defer_credit, fail_credit)
           
    else:
        print("\nExclude")
        return "Exclude .- {} , {} , {}".format(pass_credit, defer_credit, fail_credit)
    
def File_Save(value):
    file_name = f"{2052800}.txt"   #f string used to make it easier to format the string
    with open(file_name, 'w') as f: #with open = it closes the file without gettin errors
        for i in value:
            f.write(f"{i}\n")
        
def Histogram(progress,trailer,retriever,exclude):
   
    win= GraphWin("Histogram Results" , 550,400)
    outcomes=["Progress" , "Trailer" , "Retriever" , "Exclude"]
    counts=[progress,trailer,retriever,exclude]
    colors=["red","green","pink","yellow"]
    x=50

    topic=Text(Point(100,50), "Histogram Results")
    topic.setStyle("bold")
    topic.draw(win)
    line=Line(Point(30,261),Point(500,261))
    line.draw(win)
    
    for i in range(4):
        coloumn= Rectangle(Point(x,260),Point(x+70,260- counts[i] * 20))
        rectangle_size=260- counts[i] * 20
        coloumn.draw(win)
        coloumn.setFill(colors[i])
        win.setBackground("white")
        
        label=Text(Point(x+25,300), outcomes[i])
        label.draw(win)
                                               
        count_label =Text(Point(x+25,rectangle_size-20), str(counts[i]))
        count_label.draw(win)
        
        x+=120
        
    total_label=Text(Point(260,380), f"Outcomes in total : {sum(counts)}")
    total_label.draw(win)
    total_label.setStyle("bold")
    
    win.getMouse()
    win.close()
    return
    
#main program
progression_data = []

#declaring variables
Pass=0
Defer=0
Fail=0
user_input=""
count = True
value_range=[0,20,40,60,80,100,120] #if i use a tuple,it cant be moved.
Progress_count=0
Trailer_count=0
Retreiver_count=0
Exclude_count=0


while count:
    try:
        
        Pass = int(input("\nPlease enter your credits at pass : "))
        if Pass>120 or Pass not in value_range:
            print("Out of range \n")
            continue
        Defer= int(input("Please enter your credits at defer : "))
        if Defer not in value_range :
            print("Out of range \n ")
            continue
        Fail= int(input("Please enter your credits at Fail : "))
        if Fail not in value_range :
            print("Out of range \n ")
            continue
            
        if Pass+Defer+Fail!= 120:
            print("Total Incorrect \n")
        else:
            #calling the function and making a new variable
            outcome = GetMarks(Pass,Defer,Fail)
            progression_data.append(outcome)
        repeat  =0      
        while repeat<1 :
            user_input= input("\nWould you like to enter another set of data ? Enter 'y' for yes or 'q' to quit and view results :")

            if user_input == "y":
                repeat+=1
                continue
            elif user_input=="q":
                print("\n")
                repeat+=1
                count=False           
            else:
                print("Enter 'y' or 'q' Only")
                                
    except ValueError:
        print("Integer Requried")

# Making the progression data ( List : 'Part 2 ' )
for data in progression_data:
    if data[0:11]=='Progress - ':
        Progress_count+=1     
    elif data[0:11]=='Progress (M':
        Trailer_count+=1
    elif data[0:11]=='Module retr':
        Retreiver_count+=1
    elif data[0:11]=='Exclude .- ':
        Exclude_count+=1
    else:
        print(" ")

#calling Histogram function
Histogram(Progress_count,Trailer_count,Retreiver_count,Exclude_count)

#Printing the List
for i in progression_data:
    print(i)
    
#calling the function to save data to a file
File_Save(progression_data)







    
        
    





