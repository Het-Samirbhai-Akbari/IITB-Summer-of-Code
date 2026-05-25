name="Het"
age=18
gpa=11.0
student=True #1st letter capital


print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#Explicit Type Casting

age=float(age)
print(type(age))
print(age)

gpa=int(gpa)
print(type(gpa))
print(gpa)

student=int(student)
print(type(student))
print(student)

student=bool(student)
print(type(student))
print(student)

student=str(student)
print(type(student))
print(student)


#Implicit Type Casting

x=2
y=3.14

print(x/y) #result is float
