# .csv (comma separated value)
# .txt text file

# Will create a file and write the text for a single time:
# with open('message.txt', 'w') as file:
#     file.write('I love python')

# Append the text to the file
# with open('message.txt', 'a') as file:
#     file.write('I love python, append')

# Read the text to the file
with open('message.txt', 'r') as file:
    text = file.read()
    print(text)