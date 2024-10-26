
/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


*/

class Solution {


public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // start from end of vector
        // largest numbers are at the end
        int idx {m + n - 1};
        --m;
        --n;
        while (m >= 0 && n >= 0) {
            // if int in nums1 is bigger than int in nums2
            // assign it to the position at idx, it is the larger
            // number
            if (nums1[m] > nums2[n]) {
                nums1[idx] = nums1[m];
                --m;

            } else {
                nums1[idx] = nums2[n];
                --n;
            }
            --idx;
        }

        // now one of the lists is empty and the other is not
        while (m >= 0) {
            nums1[idx] = nums1[m];
            --m;
            --idx;
        }

        while (n >= 0) {
            nusm1[idx] = nums2[n];
            --n;
            --idx;
        }
        
        
    }
};