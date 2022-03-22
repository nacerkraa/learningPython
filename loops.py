#
# Exemple of code in here..for loop
#

def main():
    x, y = 0, 10
    # Define while loop
    while(x < y):
        print(x)
        x = x + 1
    # Define for loop

    for x in range(4,10):
        print(x)

    # use for loop over a collection
    days = ["Sat", "Sun", "Mon", "thu","Wen","Tur","Fri"]
    for t in days:
        print(t)
    # use the break and the Continue in the loop
    for x in range(0,10):
        if(x==8): break
        if(x % 2 == 0): continue
        
        print(x)
    
    # using the enumerate() funcion
    days = ["Sat", "Sun", "Mon", "thu","Wen","Tur","Fri"]
    for i,t in enumerate(days) :
        print(i, t)
   

if __name__ == "__main__":
    main()
