for i in range(len(nums) - 1):
        current_value = nums[i]
        print(f"current_value = {current_value}")
        next_value = nums[i + 1]
        print(f"next_value = {next_value}")
        max_value = 0
        print(f"max_value = {max_value}")
        if current_value > next_value:
            max_value = current_value   