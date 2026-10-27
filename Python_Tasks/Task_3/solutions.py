# Task 3: Python Problem-Solving Solutions

# Qno 1: Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


# Qno 2: Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# Qno 3: Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    frequency = character_frequency(word)
    for char in word:
        if frequency[char] == 1:
            return char
    return None


# Qno 4: Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    return sorted(s1) == sorted(s2)


# Qno 5: Find the First Repeating Character in a String
def first_repeating(text):
    words = set()
    for char in text:
        if char in words:
            return char
        words.add(char)
    return None


# Qno 6: Move All Zeros to the End of a List
def move_zeros(nums):
    non_zeros = []
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zeros.append(num)
    return non_zeros + [0] * zero_count


# Qno 7: Find the Second Highest Distinct Number in a List
def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# Qno 8: Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result


# Qno 9: Find the Missing Number from 1 to N
def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Qno 10: Find Two Numbers Whose Sum Equals a Target
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []



# Qno 11: Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums, key=lambda num: (abs(num), -num))


# Qno 12: Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


# Qno 13: Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums.copy()
    return nums[-k:] + nums[:-k]


# Qno 14: Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]
    for index in range(1, len(nums) - 1):
        current_sum = nums[index] + nums[index + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


# Qno 15: Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]