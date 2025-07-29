from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        coldest_days = []
        num_days = len(temperatures)
        deltas = [0]*num_days

        for day in range(num_days): # We can't check the last day
            print(day)
            # If today is colder or equal to yesterday, today is the coldest day so far.
            if not coldest_days or temperatures[day] <= temperatures[day - 1]:
                coldest_days.append(day)
            # Today is hotter than yesterday and can't be first day
            else:
                # Some number of preceding days were colder than this one.
                while coldest_days and temperatures[coldest_days[-1]] < temperatures[day]:
                    # Calculate the delta to day
                    deltas[coldest_days[-1]] = day - coldest_days[-1]

                    # Remove from stack
                    coldest_days.pop()


                # Today is now the last coldest day
                coldest_days.append(day)

        return deltas
                       
           
           
           
           
           
           
           
        #    if not coldest_days and temperatures[day] > temperatures[day-1]:
        #         deltas[day] = 1
        #     elif temperatures[day] <= temperatures[coldest_days[-1]]:
        #         coldest_days.append(day)
        #     # Case where the day must be hotter than the coldest day
        #     else:
        #         # Today is hotter than yesterday
        #         deltas[day] = 1
                
        #         # Check how many preceeding days where colder
        #         c_index = day - 1
        #         while temperatures[day] > temperatures[c_index]:
        #             delta = day - c_index
        #             deltas[c_index] = day - c_index
        #             c_index -= 1

        #return deltas
    
if __name__ == "__main__":
    s = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(temperatures))
