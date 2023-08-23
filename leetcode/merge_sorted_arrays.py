class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:
            nums1[:] = nums2
        else:
            idx1 = m - 1
            idx2 = n - 1
            idx_full = m + n - 1
            while idx1 >= 0 and idx2 >= 0:
                if nums1[idx1] >= nums2[idx2]:
                    nums1[idx_full] = nums1[idx1]
                    idx1-=1
                else:
                    nums1[idx_full] = nums2[idx2]
                    idx2-=1
                idx_full-=1
            if idx1 == -1:
                nums1[:idx_full+1] = nums2[:idx2+1]
