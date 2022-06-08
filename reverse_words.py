# Function to reverse words of string


def rev_sentence(sentence):

    # first split the string into words
    words = sentence.split(" ")[::-1]

    #  join using space
    reverse_sentence = " ".join(words)

    # finally return the joined string
    return reverse_sentence


input = "Yash Ravindra Dabhade"
print(rev_sentence(input))
