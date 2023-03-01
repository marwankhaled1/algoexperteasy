"""
time complexity o(n) and space complexity o(n) for the result array 
1-set pointer to the start of array and end of array 
create new array for result 
2- loop on array while (start != end)
if(nums[end]*nums[end]>=nums[start]*nums[start]):
    res.append(nums[end]*nums[end])
    end=end-1
else:
    res.append(nums[start]*nums[start])
    start=start+1

    return res
"""
def sortedSquares(nums):
        start=0
        end=len(nums)-1
        res=[]
        while start <= end:
            if(nums[end]*nums[end]>=nums[start]*nums[start]):
                res.append(nums[end]*nums[end])
                end=end-1
            else:
              res.append(nums[start]*nums[start])
              start=start+1

        return res[::-1]
                 

print(sortedSquares([-7,-3,2,3,11]))                