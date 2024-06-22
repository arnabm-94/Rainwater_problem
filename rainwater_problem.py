'''
Rainwater problem :

Given n non negetive integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining 
'''

'''
To solve this problem, we can use a two-pointer approach which is efficient in terms of both time 
and space complexity. The basic idea is to traverse the elevation map using two pointers 
from both ends towards the center, while keeping track of the maximum heights encountered on both sides. 
'''

def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])

    return water_trapped

# Example usage:
elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(elevation_map))  # Output: 6

'''
#Initialization:

left and right pointers are initialized to point to the first and the last bar respectively.
left_max and right_max are initialized to keep track of the maximum height encountered so far 
from the left and the right.
water_trapped is initialized to 0 to store the total amount of trapped water.


#Traversal:

We use a while loop to traverse the elevation map until the left pointer is less than the right pointer.
If the height at the left pointer is less than the height at the right pointer, we move the left pointer
one step to the right.
Update the left_max with the maximum value between the current left_max and the height at the new left pointer.
Calculate the trapped water at the current left position and add it to water_trapped.
Otherwise, we move the right pointer one step to the left.
Update the right_max with the maximum value between the current right_max and the height at the new right pointer.
Calculate the trapped water at the current right position and add it to water_trapped.

#Return Result:

Finally, return the total amount of trapped water stored in water_trapped.
This approach efficiently calculates the total trapped water in O(n) time complexity with O(1) additional space.
'''
