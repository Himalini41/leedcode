class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        v=[]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        #pass 20 test case time limit exists 
        """
        l=0
        r=len(numbers)-1
        for i in range(len(numbers)):
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1