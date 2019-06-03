#!/usr/bin/env python
# -*- coding: utf-8 -*-

# max_sum_dac solves the max-sum-subarray-problem with Divide and Conquer
# in O(m*log(m))

# example 1: max_sum_dac( [3,-5,0,2,100,-2,-5,9] )
# max-sum-subarray: [2,100,-2,-5,9]
# max-sum: 2+100-2-5+9 = 104

# example 2: max_sum_dac( [-3,5,-1,2,-5,3] )
# max-sum-subarray: [5,-1,2]
# max-sum: 5-1+2 = 6

def max_prefix_sum(a):
  i = 0
  accumulator, maxval = a[i], a[i]
  
  for j in range(1,len(a)):
    accumulator += a[j]
    maxval = max(maxval, accumulator)
  return maxval

def max_sum_dac(a):
  m = len(a)

  # trivial case
  if m == 1:
    return a[0]

  # divide
  a1 = a[:len(a)//2]
  a2 = a[len(a1):]

  # recursion
  l = max_sum_dac(a1)
  r = max_sum_dac(a2)

  # conquer
  left_max = max_prefix_sum([a1[i] for i in range(len(a1)-1, -1, -1)]) #reversed a1
  right_max = max_prefix_sum(a2)
  max_sum_over_middle = left_max + right_max
  return max(max_sum_over_middle, l, r)