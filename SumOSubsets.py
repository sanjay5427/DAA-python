def sum_of_subsets(nums, target):
    def backtrack(index, current_sum, subset):
        if current_sum == target:
            print(subset)
            return True
        if current_sum > target or index == len(nums):
            return False

        include = backtrack(index + 1, current_sum + nums[index], subset + [nums[index]])
        exclude = backtrack(index + 1, current_sum, subset)

        return include or exclude

    if not backtrack(0, 0, []):
        print("No subset with the given sum exists")

# Get user input for the set of integers and the target sum
nums = list(map(int, input("Enter the set of integers (space-separated): ").split()))
target = int(input("Enter the target sum: "))

sum_of_subsets(nums, target)
