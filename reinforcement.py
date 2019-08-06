# Write code to generate a dictionary where the keys are the numbers from 1 to 50 and the values follow these rules:

# if the number is divisible by 2 the value should be one more than the key
# if the number is divisible by 7 the value should be one less than the key
# if the number is divisible by 2 and 7 the value should be the key multiplied by 2
# otherwise the value should be the same number as the key

nums = {}
dict_len = 50
for i in range(1,dict_len+1):
    if i % 2 ==0 and i % 7 ==0:
        nums[i] = i*2
    elif i%7 == 0:
        nums[i] = i-1
    elif i % 2 ==0:
        nums[i] = i+1
    else:
        nums[i] = i

for key, value in nums.items():
    print(key, value)