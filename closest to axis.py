# Here I am trying to find the closest point to each axis without using loops or arrays solely with the help of if, eif and else  statements


x1 = float(input("Enter the x-coordinate of A: "))
y1 = float(input("Enter the y-coordinate of A: "))

point_A = (x1, y1)

x2 = float(input("Enter the x-coordinate of B: "))
y2 = float(input("Enter the y-coordinate of B: "))

point_B = (x2, y2)

x3 = float(input("Enter the x-coordinate of C: "))
y3 = float(input("Enter the y-coordinate of C: "))

point_C = (x3, y3)


# For proximity to the y-axis, we compare the absolute values of the x-coordinates of the points.\

if abs(point_A[0]) < abs(point_B[0]) and abs(point_A[0]) < abs(point_C[0]):
    print(f"The point closest to the y-axis is A {point_A}")
elif abs(point_B[0]) < abs(point_A[0]) and abs(point_B[0]) < abs(point_C[0]):
    print(f"The point closest to the y-axis is B {point_B}")
elif abs(point_C[0]) < abs(point_A[0]) and abs(point_C[0]) < abs(point_B[0]):
    print(f"The point closest to the y-axis is C {point_C}")
elif abs(point_A[0]) == abs(point_B[0]) and abs(point_A[0]) < abs(point_C[0]):
    print(f"The points A {point_A} and B {point_B} are equidistant from the y-axis and closer than C {point_C}.")
elif abs(point_A[0]) == abs(point_C[0]) and abs(point_A[0]) < abs(point_B[0]):
    print(f"The points A {point_A} and C {point_C} are equidistant from the y-axis and closer than B {point_B}.")
elif abs(point_B[0]) == abs(point_C[0]) and abs(point_B[0]) < abs(point_A[0]):
    print(f"The points B {point_B} and C {point_C} are equidistant from the y-axis and closer than A {point_A}.")
elif abs(point_A[0]) == abs(point_B[0]) and abs(point_A[0]) == abs(point_C[0]):
    print("All points are equidistant from the y-axis.")
else:
    print("All points are equidistant from the y-axis.")



# For proximity to the x-axis, we compare the absolute values of the y-coordinates of the points.

if abs(point_A[1]) < abs(point_B[1]) and abs(point_A[1]) < abs(point_C[1]):
    print(f"The point closest to the x-axis is A {point_A}")
elif abs(point_B[1]) < abs(point_A[1]) and abs(point_B[1]) < abs(point_C[1]):
    print(f"The point closest to the x-axis is B {point_B}")
elif abs(point_C[1]) < abs(point_A[1]) and abs(point_C[1]) < abs(point_B[1]):
    print(f"The point closest to the x-axis is C {point_C}")
elif abs(point_A[1]) == abs(point_B[1]) and abs(point_A[1]) == abs(point_C[1]):
    print("All points are equidistant from the x-axis.")
elif abs(point_A[1]) == abs(point_B[1]) and abs(point_A[1]) < abs(point_C[1]):
    print(f"The points A {point_A} and B {point_B} are equidistant from the x-axis and closer than C {point_C}.")
elif abs(point_A[1]) == abs(point_C[1]) and abs(point_A[1]) < abs(point_B[1]):
    print(f"The points A {point_A} and C {point_C} are equidistant from the x-axis and closer than B {point_B}.")
elif abs(point_B[1]) == abs(point_C[1]) and abs(point_B[1]) < abs(point_A[1]):
    print(f"The points B {point_B} and C {point_C} are equidistant from the x-axis and closer than A {point_A}.")
else: 
    print("All points are equidistant from the x-axis.")


