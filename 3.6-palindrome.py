#word = "madam"
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
print(word[::-1])
###
integer = word == word[::-1]
string = str(integer)
print (string)
is_palindrome = string.find("True")

# TESTING
print (is_palindrome)
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"