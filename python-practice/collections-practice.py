nums = [4, 2, 8, 2, 4, 9, 1, 8]

nums_set = set(nums)
print(nums_set, type(nums_set))
desc_nums_tup = tuple(sorted(nums_set, reverse=True))
print(desc_nums_tup, type(desc_nums_tup))

print(100*'x')

prices = {"apple": 50, "banana": 20, "mango": 80}
max_no = -1
mx_key = ''
for key,val in prices.items():
    if val > max_no:
        max_no = val
        mx_key = key

print(mx_key)

# Optimized approach
print(100*'-')
mx_key = max(prices, key=prices.get)
print(mx_key)


print(100*'1')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sq = [i**2 for i in nums if i % 2 == 0]
print(even_sq)


print(100*'=*')

nums = [1, 2, 3, 4, 5]

dict_comp={k :('even' if k % 2== 0 else 'odd') for k in nums}
print(dict_comp)

