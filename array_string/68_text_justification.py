'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
'''

# Solution

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        output = []
        current_line = []
        line_width = 0

        for word in words:
            if line_width + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - line_width):
                    # add a space to all words in current except the last one
                    current_line[i % (len(current_line) -1 or 1)] += ' '
                # add the words to the output list
                output.append(''.join(current_line))

                # reset the variables
                current_line = []
                line_width = 0
            
            current_line.append(word)
            line_width += len(word)
        last = ' '.join(current_line)
        while len(last) < maxWidth:
            last += ' '
        # now add the last one
        output.append(last)
        return output