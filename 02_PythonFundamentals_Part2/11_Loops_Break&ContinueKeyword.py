'''
Demonstrate the use of break and continue keywords in Python loops.
'''

num = 10;

while(num > 0):
    if(num == 5):
        print("Breaking the loop as num is 5")
        break  # exit the loop when num is 5
    elif(num == 8):
        print("Skipping the iteration as num is 8")
        num -= 1
        continue  # skip the rest of the code in this iteration when num is 8
        # as continue is used, the loop will go to the next iteration without executing the print statement below    
    print("Number: ", num)
    num -= 1  # decrementing the value of num by 1 in each iteration