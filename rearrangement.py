def special_rearrangement(nums):
    oddlist=[]
    evenlist=[]
    for i in range(len(nums)):
        if nums[i]%2==0:
            evenlist.append(nums[i])
        else:
            oddlist.append(nums[i])
    nums=[]
    for i in range(len(nums)):
        nums.append(evenlist[i])
    for i in range(len(oddlist)):
        nums.append(oddlist[i])

    return nums