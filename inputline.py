def grade(course):
    avg=sum(course)/len(course)
    if avg>=90:
        grade="A"
    elif avg>=80:
        grade="B"
    elif avg>=70:
        grade="C"
    elif avg>=60:
        grade="D"
    else:
        grade="F"
    return grade

def evaluation(course):
    maximum=max(course)
    minmum=min(course)
    average=sum(course)/len(course)
    return maximum,average,minmum
file1 = open('output.txt', 'w') 
with open("myfile.txt") as fp: 
    for line in fp: 
        student=line.split(':')
        course=student[1].split(",")
        course[-1]=course[-1].rstrip("\n")
        for i in range(0, len(course)): 
            course[i] = int(course[i]) 
        grad=grade(course)
        eval=evaluation(course)
        outline="\nName:{} \nAverage Marks:{} \nMax MArks:{}\
        \nMin Marks:{} \nGrade Earned:{}\n".format(student[0],eval[1],eval[0],eval[2],grad)
        file1.writelines(outline) 
file1.close() 

