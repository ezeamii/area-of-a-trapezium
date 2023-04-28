# PROGRAM TO FIND THE AREA OF A TRAPEZIUM
firstlength = int(input("Input the value of the first parallel line: "))
secondlength = int(input("Input the value of the second parallel line: "))
height = int(input("Input the value of the height: "))

area = 0.5 * (firstlength + secondlength) * height
print("The area of this trapezium is", area, "cm^2")