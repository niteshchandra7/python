# bit manipulation
# 1001(9) #2  

# Given a number find number of set bits in its
# binary representation

# 9  --> 2
# 32 --> 1
#count = 0
#1001 & 0001 = 0001 ,count=1
#right shift by 1
#0100 & 0001 = 0000 ,count=1
#right shift by 1 
#0010 & 0001 = 0000, count=1
#right shift by 1 
#0001 & 0001 = 0001, count=2

#log(N)
# for int N=2^(32)
#O(32)

# 9 1001 (N)
# 8 1000 (N-1)
# 9 & 8 1000 # 1 iteration
# 8(1000) & 7(0111) 0000 # 2 iteration

#101100
#101011
#101000

#count=0
#while num!=0:
    #count+=1
    #num=num&num-1
#return count




