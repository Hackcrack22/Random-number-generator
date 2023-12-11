#This tool is number randomiser that only works with intergits
print("This tool is number randomiser. Please choose a number A and a number B and only intergits (numbers without any point)")
A=int(input("A = "))
B=int(input("B = "))
import random
print("Here is your number : ",random.randint(A,B))
