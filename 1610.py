from typing import List
from math import atan2, degrees


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # Creat a dictionary ordered by angles, with count along each angle
        angle_counts = dict()
        for point in points:
            p_angle = self.getAngle(location, point)
            if p_angle in angle_counts:
                angle_counts[p_angle] += 1
            else:
                angle_counts[p_angle] = 1
        
        # Sort
        angle_counts = dict(sorted(angle_counts.items()))
        print(angle_counts)
        angles = []
        counts = []


        for key in angle_counts.keys():
            angles.append(key)
        for value in angle_counts.values():
            counts.append(value)
        
        print(angles)
        print(counts)

        # Get the first sector
        datum_angle = 0

        count, last_index = self.countSectorByIndex(datum_angle, angle, angles, counts)
        datum_angle += 1
        print(count)
        print(last_index)

        # Evaluate only small additional views
        while last_index < len(angles):
            view_angle = angles[datum_angle] - angles[datum_angle-1]
            

    def countSectorByIndex(self, datum_index, view_angle, angles, counts):
        """
        datum_index: the clockwise edge of the sector to be counted
        
        """
        count = 0
        angle_index = datum_index
        view_clock_angle = angles[angle_index]
        view_anti_angle = view_clock_angle + view_angle

        eval_angle = view_clock_angle
        
        while eval_angle <= view_anti_angle:
            # Count along the evaluation line
            count += counts[angle_index]
            # Advance to the next index
            angle_index += 1
            eval_angle = angles[angle_index]# Start at the datum position

        return count, angle_index - 1 # The count and the last counted index

    
    def getAngle(self, location:List[int], point:List[int]):
        dx, dy = point[0] - location[0], point[1] - location[1]
        degs = degrees(atan2(dy, dx))
        if degs < 0:
            degs = (180 + degs) + 180

        return degs


if __name__ == "__main__":
    s = Solution()
    points1 = [[1, 0],[2,1],[2,2],[3,3],[-1, 2], ]
    angle1 = 90
    pos1 = [1,1]
    s.visiblePoints(points1, angle1, pos1)
