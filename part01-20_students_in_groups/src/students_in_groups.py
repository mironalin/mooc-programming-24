# Write your solution here
student = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

if student % size == 0:
    print(f"Number of groups formed: {student // size}")
else:
    print(f"Number of groups formed: {student // size + 1}")
