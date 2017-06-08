#!/usr/bin/env python

#get delta
def check_delta(a, b, c):
    delta = b**2 - (4 * a * c)
    return delta


def format_nb(nb):
    if not nb:
        return int(nb)
    elif nb.is_integer():
        return int(nb)
    return round(nb,6)

#resolve for degree 2
def resolve(delta, a,b):
    if delta < 0:
        print "Discirminant < 0, I can't solve"
    elif delta == 0:
        solution =  (b * -1) / ( 2 * a)
        if not solution:
            solution = int(solution)
        print "Discriminant = 0. Une solution : " + str(solution)
    elif delta > 0:
        sol_1 = ((b * -1) + delta**0.5) / (2 * a)
        sol_2 = ((b * -1) - delta**0.5) / (2 * a)
        sol_1 = format_nb(sol_1)
        sol_2 = format_nb(sol_2)

        print "Discriminant > 0. Two solutions : " + str(sol_1) + " et " + str(sol_2)
    return 1

#resolve for degree 1
def resolve_degree_one(b, c):
    solution = (c * (-1)) / b
    if not solution:
        solution = int(solution)
    print "Polynome de 1er degre. The solution is : " + str(solution)
    return 1

# resolve for degree 0
def resolve_degree_zero(c):
    string = "Degree 0 equation"
    if c:
        string += "The solution is 0"
    else:
        string += "All numbers are solutions."
    print string
    return 1

#get a,b,c and check if can resolve
def resolve_equation(array, max):
    if (max > 2):
        print "The polynomial degree is strictly greater than 2, I can't solve"
        return 1
    a = 0
    b = 0
    c = 0
    for item in array:
        if item[1] == 0:
            c = item[0]
        elif item[1] == 1:
            b = item[0]
        elif item[1] == 2:
            a = item[0]
        else:
            print "There is negative powers, I can't solve"
            return 1
    if max == 0:
        resolve_degree_zero(c)
    elif max == 1:
        resolve_degree_one(b,c)
    else:
        delta = check_delta(a, b, c)
        resolve(delta, a, b)
    return 1