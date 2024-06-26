'''There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

# Solution

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candies = [1] * len(ratings)

        # give current child 1 more candy than previous child 
        # if it has a higher rating, start from second child
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                # current candy is one more than previous
                candies[i] = candies[i-1] + 1
        
        # Go through ratings from right to left
        # start from penultimate child
        # give a child more if the rating is higher than that of the previous child
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1


        
        return sum(candies)


            



        