from max_sum_subarray import max_sum_dac

print("Tests:")
a = [3,-5,0,2,100,-2,-5,9]
print(max_sum_dac(a) == 104)
a = [-3,5,-1,2,-5,3]
print(max_sum_dac(a) == 6)
a = [13,-5,-1,7,-5,4]
print(max_sum_dac(a) == 14)
a = [3,-5,0,1,10,-2,-5,6]
print(max_sum_dac(a) == 11)
a = [3,-5,0,1,0,-2,-5,6]
print(max_sum_dac(a) == 6)
a = [-3,-9,-4,-5,-2,-1]
print(max_sum_dac(a) == -1)
a = [3,5,10,9,2,3]
print(max_sum_dac(a) == 32)
a = [3,-5,-10,-9,-2,-3]
print(max_sum_dac(a) == 3)
a = [3,-5,10,9,-2,-3]
print(max_sum_dac(a) == 19)