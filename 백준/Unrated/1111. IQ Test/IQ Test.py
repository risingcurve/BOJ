n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print('A')
elif n == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    if nums[1] == nums[0]:
        a = 0
        b = nums[1]
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        b = nums[1] - nums[0] * a
    
    for i in range(n-1):
        if nums[i+1] != nums[i]*a + b:
            print('B')
            break
    else:
        print(nums[-1]*a + b)
