# 1768 Merge Strings Alternately
 
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.


class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged_string = ""
        if len(word1) == len(word2):
            for x in range(len(word1)):
                merged_string = merged_string + word1[x] + word2[x]
        elif len(word1) < len(word2):
            for x in range(len(word2)):
                if x < len(word1):
                    merged_string = merged_string + word1[x] + word2[x]
                else:
                    merged_string = merged_string + word2[x]
        else:
            for x in range(len(word1)):
                if x < len(word2):
                    merged_string = merged_string + word1[x] + word2[x]
                else:
                    merged_string = merged_string + word1[x]
        return merged_string

# tests
tests = []
tests.append({
    'input': {
        'word1': "abc",
        'word2': "pqr"
    },
    'output': "apbqcr"
})

tests.append({
    'input': {
        'word1': "ab",
        'word2': "pqrs"
    },
    'output': "apbqrs"
})

tests.append({
    'input': {
        'word1': "abcd",
        'word2': "pq"
    },
    'output': "apbqcd"
})


sol = Solution()
for test in tests:
    input_data = test['input']
    word1 = input_data['word1']
    word2 = input_data['word2']
    expected_output = test['output']
    output = sol.mergeAlternately(word1, word2)

    if output == expected_output:
        print("Test passed")
    else:
        print("Test failed. Expected:", expected_output, "but got:", output)
            