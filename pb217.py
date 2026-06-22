class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """ v=[]
        for i in nums:
            if i in v :
                return True
            v.append(i)
        return False

        for i in v:
            if i>=2 or len(nums)!=sum(v):
                return True
            else:
                return False


        v=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    v.append(nums[i]-nums[j])
        for i in v:
            if  i==0:
                return True
        else:
            return False
    
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
        """
        m=set(nums)
        if len(nums)!=len(m):
            return True
        else:
            return False