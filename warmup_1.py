#1 sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if weekday != True or vacation == True:
    return True
  else:
    return False

#2 monkey_trouble
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
#We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  if a_smile == False and b_smile == False:
    return True
  else:
    return False
 
#3 sum_double
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b
