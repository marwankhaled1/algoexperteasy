def twoSum(nums, target):
        """
       first solution using hashtable time complexity O(n),space complexity O(n)
       res=[]
       1- save array in arrayValues hashtable o(n) loop in array add elements in dict key-> number, value-> it's index
       2- loop on array to check if arrayValues [target-array[i]]!=None:
              res.append(i)
              res.append(arrayValues[target-array[i]])
              return res

        return res if not found any one []
       
       
        """
        res=[]
        arrayValues={}
        for i in range(0,len(nums)):
            if nums[i] not in arrayValues:
               arrayValues[nums[i]]=i
        for i in range (len(nums)-1,-1,-1):
            if target-nums[i] in arrayValues  and i != arrayValues[target-nums[i]] :
                 res.append(i)
                 res.append(arrayValues[target-nums[i]]) 
                 return res
        return res            
print(twoSum( [2,5,5,11] ,10) )