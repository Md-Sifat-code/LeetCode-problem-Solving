class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        print(f"goal {goal}")

        for i in range(len(nums) - 2, -1, -1):

            print(i)
            if i + nums[i] >= goal:
                goal = i
                print(f"goal {goal}")
        
        return True if goal == 0 else False