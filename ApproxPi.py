#ApproxPi.py
#Name: Miguel Alvarado
#Date: 2/2/2026
#Assignment: Lab 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  numbers = int(input("Tell me how much decimal places:"))
  start = time.time()
  #calculate pi using the approximation technique
  piEstimate = 0
  n = 1
  sign = 1
  
  precision = 10**(-numbers)

  

  #Loop until the level of percision is reached
  while True:
   piEstimate = piEstimate + sign * (4 / n)
   if abs(piEstimate - realPi) < precision:
       break
   n = n + 2
   sign = sign * -1

  

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)
  print("ApproxPi:", piEstimate)
  print("Actual Pi:", realPi)
  print("Elapsed time:", round(elapsedTime, 5), "seconds")


if __name__ == '__main__':
  main()
