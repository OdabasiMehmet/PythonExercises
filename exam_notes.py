#Open students.txt file and write a program that finds average mark for each student.If the
#mark is lower than 50, students fail.If the mark is equal or graeter to 50, then the student passes.
#Crteate two text files. One will show who passed and the other who failed.

with open ("students.txt","r",encoding="utf-8") as slist:
    mark_list= slist.readlines()
fail_list=[]
pass_list=[]
for i in mark_list:
    name = (i.strip("\n")).split(",")
    avg_note= str(int(int(name[1])*0.3 + int(name[2])*0.3 +int(name[3])*0.4))
    name.append(avg_note)
    if name[4] >= "50":
        passing= ",".join(name)
        passing+= "\n"
        pass_list.append(passing)
    else:
        failing= ",".join(name)
        failing+= "\n"
        fail_list.append(failing)


# with open("failed_students.txt","w",encoding="utf-8") as file1:
#     file1.writelines(fail_list)

with open ("passing_students.txt","w",encoding="utf-8") as file2:
    file2.writelines(pass_list)
    

