# Problem F - Regular Expression Matching
# From Leetcode
# Given a string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
#     '.' matches any single character
#     '*' matches zero or more of the preceding character
# The matching should cover the entire input string (not partial).


# Example 1: s = "aa", p = "a" FALSE
# Explanation: "a" does not match the entire string "aa".

# Example 2: s = "aa", p = "a*" TRUE
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3: s = "ab", p = ".*" TRUE
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4: s = "aab", p = "c*a*b" TRUE
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

# Example 5: s = "mississippi", p = "mis*is*p*." FALSE
# Explanation: missing third 'i'


# For convenience, change inputs first then run program
stringInput = "aab"
patternInput = "c*a*b*"


def rem(s, p):
    sLen = len(s)
    pLen = len(p)

    data = {}

    def remLoop(sIdx, pIdx):
        if sIdx >= sLen and pIdx >= pLen: return True           # completed both strings
        elif (sIdx, pIdx) in data: return data[(sIdx, pIdx)]    # (sIdx, pIdx) previously calculated
        
        currentIdxMatch = sIdx < sLen and pIdx < pLen and (s[sIdx] == p[pIdx] or p[pIdx] == '.')
        if (pIdx + 1 < pLen and p[pIdx + 1] == '*'):
            retval = remLoop(sIdx, pIdx + 2) or (currentIdxMatch and remLoop(sIdx + 1, pIdx))
            data[(sIdx, pIdx)] = retval
            return retval
        elif currentIdxMatch:
            retval = remLoop(sIdx + 1, pIdx + 1)
            data[(sIdx, pIdx)] = retval
            return retval
        else:
            data[(sIdx, pIdx)] = False
            return False

    return remLoop(0, 0)


print(rem(stringInput, patternInput))


# I first attempted this problem using an iterative method, but got stuck when deciding to remove or repeat for '*'.
# After some research, I understood and implemented the recursive solution above.
# Lastly, it is possible for different calls to remLoop to have same sIdx and pIdx, so I used memoization to avoid calculating again.

# Source: www.youtube.com/watch?v=HAA8mgxlov8
