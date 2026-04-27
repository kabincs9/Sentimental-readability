# Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text,
# and S is the average number of sentences per 100 words in the text.
# input and more complex more grade like in problem no 2

from cs50 import get_string
# ask the user value
text = get_string("Text: ")
# to instalize the counters from 0
letters = 0
words = 1  # start from 1 not zero Since the number of spaces is one less than the number of words. or last word is not followed by space so last in first
sentences = 0
for char in text:
    # start a loop that iterate over character char in text
    if char.isalpha():  # like in c isalpha check if current character is a-z or A-Z other otherwise false
        letters += 1  # count by +1
    elif char == ' ':  # like space as one word
        words += 1
    elif char in '.!?':  # how the sentence end count it as one
        sentences += 1  # one space can cause error
        # most important manage the sentence like space ..

# to calculate L( aver letters per 100 words) and S ( aver sentence per 100 words )
L = (letters / words) * 100
S = (sentences / words) * 100  # like setence is 2 and word is 5 then 0.4 * 100 = 40
# now using index formula as question
index = 0.0588 * L - 0.296 * S - 15.8

# to count grade with index and round to fix value like floating value
grade = round(index)  # so like index is 5.23 then 5 and using conditional
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")  # here Grade not Before other wise error like only from question if addition error
# and for others from 1 to 10
else:
    print(f"Grade {grade}")  # print the grade obtained from index
