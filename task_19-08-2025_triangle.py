def triangle(side1,side2,side3):

    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2 :
        print('By using these sides we can form a valid Traingle.')
        if  side1 == side2 == side3 :
            print('It is a equilateral triangle.')
            return
        elif side1 != side2 != side3 :
            print('It is a scalene triangle.')
        else:
            print('It is a isosceles triangle.')

        li = [side1,side2,side3]
        li.sort()
        if li[0] ** 2 + li[1] ** 2 == li[2] ** 2:
            print('It is also a Right angled triangle.')
    else:
        print("We can't form a valid triangle by using these sides!!")

side1 = float(input('Enter length of a side : '))
side2 = float(input('Enter length of a side : '))
side3 = float(input('Enter length of a side : '))

triangle(side1,side2,side3)
