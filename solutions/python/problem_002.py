class Solution:
    @staticmethod
    def length_of_longest_substring(s):
        sub_string = {}  # hash map of most recent position of each character that has appeared
        cur_start = 0
        cur_len = 0
        longest = 0

        for i, letter in enumerate(s):
            if letter in sub_string and sub_string[letter] >= cur_start:
                cur_start = sub_string[letter] + 1
                cur_len = i - sub_string[letter]
                sub_string[letter] = i
            else:
                sub_string[letter] = i
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len
        return longest


print(Solution.length_of_longest_substring('abrkaabcdefghijjxxx'))

assert Solution.length_of_longest_substring('abrkaabcdefghijjxxx') == 10
