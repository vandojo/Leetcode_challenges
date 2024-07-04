'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
'''

# Solution
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # store word length and length of concatenated string
        # all words have the same length
        wordLength = len(words[0])

        # any valid permutation of words would be of this length
        concatStrLength = wordLength * len(words)

        # create a frequency map for word occurences
        wordFreq = {}
        for word in words:
            if word in wordFreq:
                wordFreq[word] += 1
            else:
                wordFreq[word] = 1
        

        output = []

        # move sliding window of concatStrLength across s
        # check if sub strings of wordLength are a permutation of words
        for i in range(wordLength):
            leftPointer = i

            count = 0
            tempWordFreq = {}

            for j in range(i, len(s) - wordLength + 1, wordLength):
                # current possible word
                word = s[j:j + wordLength]
                if word in wordFreq:
                    tempWordFreq[word] = tempWordFreq.get(word, 0) + 1
                    count += 1

                    while tempWordFreq[word] > wordFreq[word]:
                        leftWord = s[leftPointer : leftPointer + wordLength]
                        tempWordFreq[leftWord] -= 1
                        leftPointer += wordLength
                        count -= 1
                    if count == len(words):
                        output.append(leftPointer)
                
                else:
                    # if current word is not in the dictionary
                    # clear current count and move to the next word
                    tempWordFreq.clear()
                    count = 0
                    leftPointer = j + wordLength
        return output