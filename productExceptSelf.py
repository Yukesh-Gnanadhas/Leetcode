class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # storing prefix in result array and then multiplying them with the postfix
        res=[1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix*=nums[i]
        
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix and suffix products
        prefix=[1]*(len(nums))
        postfix=[1]*(len(nums))
        res= [1]*(len(nums))
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]
   
        for i in range(len(nums)):
            res[i]= prefix[i]*postfix[i]
        
        return res
