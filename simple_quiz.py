# -*- coding: utf-8 -*-
"""Simple Quiz

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YqY_ADH_lygFDfd1UEsFKGw5lyyy3v9a
"""

#Simple Quiz
import random                                                                    #For random module
lives=3
score=0                                             
while lives >=1:                                                                 #Game ends if you lose all your lives
  num1=random.randint(0,21)                                                      #2 random numbers between 1 and 20 
  num2=random.randint(0,21)
  answer= int(input('What is %d + %d?'%(num1,num2)))                             #Prompts user to answer
  if answer == num1+num2:                                                        #Checks Answer
    score = score + 10                                                           #Updates Score
  else:
      lives= lives - 1                                                           #Updates number of lives

print('Your score is',score)                                                     #Outputs Score