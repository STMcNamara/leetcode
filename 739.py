from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        coldest_days = []
        num_days = len(temperatures)
        deltas = [0]*num_days

        for day in range(num_days): # We can't check the last day
            print(day)
            while coldest_days and temperatures[coldest_days[-1]] < temperatures[day]:
                # Calculate the delta to day
                deltas[coldest_days[-1]] = day - coldest_days[-1]

                # Remove from stack
                coldest_days.pop()


            # Today is now the last coldest day
            coldest_days.append(day)

        return deltas

    
if __name__ == "__main__":
    s = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(temperatures))
