def containsDuplicate(nums):
        seen = set()
        for n in nums:
            if n in seen:   
                return True
            else:
                seen.add(n)
        return False

        # we use set for O(1) lookup.
        