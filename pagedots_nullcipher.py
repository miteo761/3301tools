def null_cipher(t, s):
    text = t
    words = text.split()
    letters = [i for ele in words for i in ele]
    output = []

    for i in s:
        output.append(letters[i])

    return output

# null/concealment cipher
# using the page dots in a 3 x 4 grid as such,
# where X is a dot and * is a blank space:
#
# XX**
# X***
# **XX


text = "FNM  YGDAEH  APXYH  EOEAOE  TNGEA  LITTHF  MACE DC  TROEGEANAEBUEBU  THFOE  GSOE  IP  OEXSB  WJBYMUEA"
sequence = [0, 1, 4, 10, 11, 12, 13, 16, 22, 23, 24, 25, 28, 34, 35, 36, 37, 40]

print(null_cipher(text, sequence))
