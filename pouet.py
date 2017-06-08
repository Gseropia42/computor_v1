#!/usr/bin/env python

import sys
import re
from error import get_error
from resolve import resolve_equation

#verifie la syntaxe de chaque bloc
def get_syntax(item):
    if not re.match('^[\+\-]{0,1}\d+\.{0,1}\d*\*X\^[\+\-]{0,1}\d+$', item):
        print "error on this part : " + item + "\nCorrect syntax nb*X^p"
        get_error(0)
        return 0
    return 1

## convert array to raw numbers when all is valid
def get_reduced_form(array):
    list = []
    for item in array:
        done = 0
        new_item = []
        multi = re.sub('\*X\^.*', '', item)
        power = re.sub('.*\^', '', item)
        for done_item in list:
            if done_item[1] == int(power):
                done_item[0] = done_item[0] + float(multi)
                done = 1
                break
        if not done:
            new_item.append(float(multi))
            new_item.append(int(power))
            list.append(new_item)
    return list

## display reduced form
def display_reduced_form(array):
    string = ""
    max = 0
    for item in array:
        number = item[0]
        if number < 0:
            string += ' - '
            number = number * -1
        elif string:
            string += ' + '
        if number.is_integer():
            string += str(int(number)) + " * X^" + str(item[1]) + " "
        else:
            string += str(number) + " * X^" + str(item[1]) + " "
        if item[0] and item[1] > max:
            max = item[1]
    print "Reduced form : " + string + "= 0"
    return max

## Check si string in good format
def check_valid(str):
    str = str.replace(' ', '')

    #decoupe le string
    results = []
    block = ""
    i = 0
    check = 0
    while i < len(str):
        if (str[i] == '+' or str[i] == '-') and i > 0 and str[i-1] != '^':
            results.append(block)
            block = ""
        elif str[i] == '=':
            results.append(block)
            block = ""
            check += 1
            i += 1
        if check:
            if check != 1 or i + 1 > len(str):
                return get_error(1)
            if str[i] == '+' and i > 0 and str[i-1] != '^':
                block+='-'
            elif str[i] == '-' and i > 0 and str[i-1] != '^':
                block += '+'
            elif not block:
                block += '-'
                block += str[i]
            else:
                block += str[i]
        else:
            block+=str[i]
        i += 1
    results.append(block)
    if check != 1:
        return get_error(1)
    return results

#Appel depuis le main
def computor(string):
    array = check_valid(string)
    if not array:
        return
    for item in array:
        if not get_syntax(item):
            return
    array = get_reduced_form(array)
    max = display_reduced_form(array)
    if max < 0:
        print 'Decimal power, unsolvable equation'
        return
    print 'Polynomial degree: ' + str(max)
    resolve_equation(array,max)
    return

## main
sys.argv = sys.argv[1:]
if not sys.argv:
    get_error(2)
else:
    for item in sys.argv:
        #if sys.argv == "What is the answer ?":
        #    print "The answer is 42."
        #   continue
        computor(item)