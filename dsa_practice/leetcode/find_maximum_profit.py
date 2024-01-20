def get_maximum_profit_to_buy_and_sell_stock(nums, n):
    buy_p = nums[0]
    max_profit = 0

    for i in range(1, n):
        if buy_p > nums[i]:
            buy_p = nums[i]
        else:
            max_profit = max(max_profit, nums[i] - buy_p)

    return max_profit


a=[
    # 7, 1, 5, 3, 6, 4
    7, 6, 4, 3, 1
   ]
print(get_maximum_profit_to_buy_and_sell_stock(a, len(a)))