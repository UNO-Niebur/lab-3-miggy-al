#TempConvert.py
#Name: Miguel Alvarado
#Date: 2/2/2026
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  temp = int(input("Give me any number and I'll tell you in Celsuis:"))
  #Convert that temperature to celsius, rounding to 1 decimal percision

  #Output converted temperature.
  tempC = (temp - 32)*5/9 
  tempC = round(tempC,1)
  

  print(temp, "is", tempC , "degrees celsius.")
if __name__ == '__main__':
  main()
