students=input('Enter the name of students: ').split(',')
marks=list(map(int,input('Enter the marks of the students: ').split(',')))
updates=list(map(int,input('Enter the marks to be updated: ').split(',')))
updated_marks=[x+i for x,i in zip(marks,updates)]
record=dict(zip(students,marks))
updated_record=dict(zip(students,updated_marks))
marks.sort(reverse=True)
sorted_record={}

for i in marks:
    for j in students:
        if record[j]==i: 
            sorted_record[j]=i
print(sorted_record)

updated_marks.sort(reverse=True)
sorted_uprecord={}
for i in updated_marks:
    for j in students:
        if updated_record[j]==i:
            sorted_uprecord[j]=i
print(sorted_uprecord)
first_ranker=list(sorted_uprecord.keys())[0]
n=list(sorted_record).index(first_ranker)
a=f'jumped {n} positions'
print(first_ranker +" got maximum marks"+" and he "+a)