def search(nums, target):
    l, r = 0, len(nums)-1
    # since we are rotating the array, what this means is wrt mid(m) either left or right side would be sorted
    # can be both.
    # we can only apply binary search to the sorted side.
    # for left to be sorted: nums[l] <= nums[m]
    # for right to be sorted: nums[m] <= nums[r] 
    while l<=r:
        m = (l+r)//2
        # identify sorted and unsorted sides
        if nums[m] == target:
            return m
        # check if left side is sorted
        elif nums[l] <= nums[m]: 
            # if target is on the sorted side
            if target >= nums[l] and target < nums[m]:
                r = m-1
            else:
                l = m+1
        else: # this else is when right side is sorted
        # check if target is on right sorted side or left un-sorted side
            if nums[r] >= target and target > nums[m]:
                l = m+1
            else:
                r = m-1
    return -1