class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        done = []

        for i in range(1, len(height)):
            print(i)
            if height[i-1] > threshold:
                print(f'this is h {height[i-1]}')
                done.append(i)
        return done