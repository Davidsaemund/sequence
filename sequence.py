n = int(input("Enter the length of the sequence: ")) # Do not change this line

#sequence addar síðustu 3 tölum saman og skrifar út sem næstu sumu
num1 = 0
prev_num = 1
prev_num1 = 0
# Start with making a for loop that runs n times 
for i in range(n):
    # Make the sequence
    sum_ = num1 + prev_num + prev_num1
    prev_num1 = prev_num
    prev_num = num1
    num1 = sum_
    #print out each step
    print(sum_)


