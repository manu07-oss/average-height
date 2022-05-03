# this is code by for loop 
#find the avg height of , number of student ?

student_height = input("enter a list of student heights").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])

total_height = 0
for height in student_height:
    total_height += height
  #print (total_height) 
number_of_student = 0 
for student in student_height:
    number_of_student += student

average_height = round(total_height / number_of_student)
print(average_height)       
  
    

