import math


max_value = 50
start_list = []
copy_list = []
primes = []

#writes all numbers to start_list till max_value is reached
def wirte_start_vlaue(max_value, start_list):
    for i in range(max_value+1):
        start_list.append(int(i))
    start_list.remove(1)
    start_list.remove(0)
    print("This is the start_list: " + str(start_list))
    primeing(start_list, copy_list, max_value, primes )

#searches for primes
def primeing(start_list, copy_list, max_value, primes):
    copy_list=start_list                
    while start_list[0] <= int(math.sqrt(max_value)): #exit after reached square root of max_val     
        primes.append(start_list[0]) 
        z = start_list[0] 
        for i in range(z,max_value):    #loop for removing the values               
            try:
               # print("coppy list before : "+str(copy_list))
                copy_list.remove(i*start_list[0])
                #print("i: " + str(i))
                #print("start_list 0 " + str(start_list[0]))
                #print(i*start_list[0])
                #print("coppy list after : "+str(copy_list))
            except ValueError: #exexption for value eather is already sorted out or value is over the max_value
                #print(i)
                if i * z <= max(copy_list): #if for the differentiation above
                    pass
                else:
                    break

        start_list=copy_list
        del start_list[0]
        #print("List: ", start_list)
        #print("Primzahlen: " + str(primes))
    final = primes + start_list
    print("Finale Primzahlen: ", final)

wirte_start_vlaue(max_value, start_list)
