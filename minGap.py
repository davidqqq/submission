"""
Q1. Given an unsorted array arr of n integers, write codes to find the smallest difference between any two elements (let us call it the minimum gap).
int find_minimum_gap(int arr[], int n) {
// your code here
}
gap = find_minimum_gap(arr,3); // gap is the answer for the array arr with length 3
For example: if n=3, arr[0]=20, arr[1]=0, arr[2]=35, the smallest difference between any two elements in the array (or minimum gap) will be 15, which is abs(arr[0]-arr[2]).
As another example: if n=4, arr[0]=10, arr[1]=9, arr[2]=19, arr[3]=20, the minimum gap is 1, which is the difference between arr[0] and arr[1], or arr[2] and arr[3].
"""


class Solution:
    '''
        Sort items
        Set minimum_gap to max gap in items
        Pair-wise comparison
    '''
    @staticmethod
    def find_minimum_gap(items):
        items = sorted(items)
        minimum_gap = items[len(items)-1]-items[0]
        for i in range(len(items)):
            gap = abs(items[i]-items[i-1])
            if (minimum_gap > gap):
                minimum_gap = gap
        return minimum_gap


print('Min gap is:', Solution.find_minimum_gap([20, 0, 35]))
print('Min gap is:', Solution.find_minimum_gap([10, 9, 19, 20]))

print('Min gap is:', Solution.find_minimum_gap([1, 35]))
print('Min gap is:', Solution.find_minimum_gap([1]))
# 1 - (-2) = 3
print('Min gap is:', Solution.find_minimum_gap(
    [-2, 5, -12, 14, 34, 99, 1, 40, 21, -29]))
