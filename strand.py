import math
def solve_strand(lower_bound, upper_bound): #input the bounds of the closed interval (contains bounds) for which solutions want to be found within
    answer_list = []
    for i in range(lower_bound,upper_bound+1): #length of street
        length = i
        
        house_list = [] #creation of list of houses
        for j in range(1,i+1):
            house_list.append(j)
            
        for j in range(1,i-2): #calculates left and right side sums for each possible house location for a given street length
            house_index = j
            left_side = house_list[0:j]
            right_side = house_list[j+1:i]
            left_sum = sum(left_side)
            right_sum = sum(right_side)
            
            if left_sum == right_sum: #adds answers to list
                answer_list.append([i,house_list[j]])
                
    for i in range(0,len(answer_list)): #output in word form
        answer_list[i] = "Street Length: "+str(answer_list[i][0])+", House Number: "+str(answer_list[i][1])
        print(answer_list[i])
    return 'Done'

print(solve_strand(5,500)) #example
            
        
        
