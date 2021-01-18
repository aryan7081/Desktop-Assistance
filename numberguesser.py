import random
import time




x = 0
while x<5:

    numb = random.randint(1,5)

    user = input("Guess a number between 1 to 5:\t")
    user = int(user)




    if user==numb:

        print("Congrats... You won")
        time.sleep(3)
        exit()
            


    else:
        if x==4:
            print("Opps! Correct number is:",numb)

        else:



   

            print("Opps! Correct number is:\t",numb, "\n Try again")

    x = x+1
    y = 5-x
    if y==0:
        
        print('You loose')
        time.sleep(3)
    else:

        print(y,"Attempt left.")
   

       



    



