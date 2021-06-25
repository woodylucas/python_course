def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == "[":
            check += 1

        elif bracket == "]":
            check -= 1

        if check < 0:
            break

    return check == 0


def palindrome_removal(string):
    if len(string) == 0:
        return False

    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return is_valid_palindrome(string, left + 1, right) or is_valid_palindrome(string, left, right - 1)

    return False


def is_valid_palindrome(string, left_idx, right_idx):
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def longest_prefix(words):
    prefix = ""
    if len(words) == 0:
        return prefix

    for i in range(0, len(words[0])):
        char = words[0][i]
        for j in range(1, len(words)):
            if i == len(words[j]) or words[j][i] != char:
                return prefix
        prefix += char
    return prefix


# end


def add_binary(s1, s2):
    idx1, idx2 = len(s1) - 1, len(s2) - 1
    carry = 0
    result = ""

    while idx1 >= 0 or idx2 >= 0 or carry != 0:
        digit_one = ord(s1[idx1]) - ord("0") if idx1 >= 0 else 0
        digit_two = ord(s2[idx2]) - ord("0") if idx2 >= 0 else 0
        sum = digit_one + digit_two + carry
        solution = sum % 2
        carry = sum // 2
        result = chr(ord("0") + solution) + result
        idx1 -= 1
        idx2 -= 1

    return result


def two_sum(nums, k):
    if k == 0:
        return False

    seen = {}
    for num in nums:
        possible = abs(num - k)
        if possible in seen:
            return True
        seen[num] = True

    return False


# print(two_sum([4, 2, 6, 5, 2], 4))


def vaccum_cleaner(string):
    if len(string) == 0:
        return False
    x, y = 0, 0

    for dir in string:
        if dir == "U":
            x += 1
        elif dir == "D":
            x -= 1
        elif dir == "L":
            y -= 1
        else:
            y += 1

    return x == 0 and y == 0


def reverse_string(word):
    char = list(word)
    left, right = 0, len(char) - 1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left += 1
        right -= 1

    return "".join(char)


# print(reverse_string("civic"))


def add_strings(num1, num2):
    idx_one, idx_two = len(num1) - 1, len(num2) - 1
    carry = 0
    solution = ""

    while idx_one >= 0 or idx_two >= 0 or carry != 0:
        digit_one = ord(num1[idx_one]) - ord("0") if idx_one >= 0 else 0
        digit_two = ord(num2[idx_two]) - ord("0") if idx_two >= 0 else 0
        sum = digit_one + digit_two + carry
        current_digit = sum % 10
        solution = chr(ord("0") + current_digit) + solution
        carry = sum // 10

        idx_one -= 1
        idx_one -= 1

    return solution


# end


def sum_of_two_inegers(a, b):
    pass


# end


def reverse_int(n):
    pass


# end


def my_atoi(string):
    pass


# end


def add_to_array_form_integer(nums, k):
    pass


# end


def multiply_strings(num1, num2):
    solution = [0 for i in range(len(num1) + len(num2))]

    for j in reversed(range(len(num2))):
        carry = 0
        idx = len(num1) + j
        for i in reversed(range(len(num1))):
            product = (ord(num2[j]) - ord("0")) * (ord(num1[i]) - ord("0")) + carry + solution[idx]
            solution[idx] = product % 10
            carry = product // 10
            idx -= 1

        solution[j] += carry

    idx = 0
    while idx < len(solution) and solution[idx] == 0:
        idx += 1

    product_string = ""

    for i in range(idx, len(solution)):
        product_string += chr(ord("0") + solution[i])

    return "0" if product_string == "" else product_string


def correct_cap(word):
    valid_cap = False
    if word[0] == word[0].lower() and word[len(word) - 1] != word[len(word) - 1].lower():
        return False

    for i in range(1, len(word)):
        if word[0] == word[0].upper() and word[i] == word[i].upper():
            valid_cap = True
        elif word[0] == word[0].upper() and word[i] == word[i].lower():
            if word[len(word) - 1] == word[len(word) - 1].upper():
                valid_cap = False
                return valid_cap
            valid_cap = True
        elif word[0] == word[0].lower() and word[i] == word[i].lower():
            valid_cap = True
        elif word[0] == word[0].lower() and word[i] != word[i].lower():
            valid_cap = False
            break

    return valid_cap


# print(correct_cap("coding"))


def num_jewels_stones(jewels, stones):
    jewels_count = characterCount(jewels)
    stones_count = characterCount(stones)
    total = 0
    for stone in stones_count:
        if stone in jewels_count:
            total += stones_count[stone]

    return total


def characterCount(string):
    map = {}
    for char in string:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    return map


def num_jewels_alternate(jewels, stones):
    jewels_set = set(jewels)
    return sum(stone in jewels_set for stone in stones)


def valid_anagrams(s, t):
    if len(s) != len(t):
        return False
    charCount = [0 for i in range(0, 20)]
    for i in range(0, len(s)):
        charCount[ord(s[i]) - 97] += 1
        charCount[ord(t[i]) - 97] -= 1

    for i in range(0, len(charCount)):
        if charCount[i] != 0:
            return False

    return True


# end

# print(valid_anagrams("program", "function"))


def first_unique_character(string):
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    for idx in range(len(string)):
        if char_frequency[string[idx]] == 1:
            return idx

    return -1


def find_the_difference(s, t):
    if len(s) == 0:
        return t
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return char
        else:
            char_count[char] -= 1


def intersection(num1, num2):
    if len(num1) == 0 or len(num2) == 0:
        return False

    number1_set = set(num1)
    number2_set = set(num2)

    intersect = [num for num in number1_set if num in number2_set]

    return intersect


def uncommon_words(s1, s2):
    word1 = s1.split(" ")
    word2 = s2.split(" ")

    character_map = {}
    for i in range(0, len(word1)):
        character_map[word1[i]] = character_map.get(word1[i], 0) + 1
    for i in range(0, len(word2)):
        character_map[word2[i]] = character_map.get(word2[i], 0) + 1

    container = [word for word, counter in character_map.items() if counter == 1]

    return container


def majority_elem(nums):
    candidate, counter = 0, 0

    for num in nums:
        if candidate == num:
            counter += 1
        elif counter == 0:
            candidate = num
            counter += 1
        else:
            counter -= 1

    return candidate
