#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today Is:",today)

  # print out the date's individual components
 
  print("Today Is:",today.day,today.month,today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday # Is:", today.weekday())
  days = ["Mon", "Thu", "Wen","Thur", "Fri","Sat", "Sun"]
  print(days[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class

  
  # Get the current time

 

  
if __name__ == "__main__":
  main();
  
