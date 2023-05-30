# Normal way to handle files
# file = open('test_file.txt')
# content = file.read()
# print(content)
# file.close()

# Better way to use the above, "with" will close the file for us, the rest of the code should be indented as shown below

# with open('test_file.txt') as file:
#     content = file.read()
#     print(content)

# Write to a file, mode "w" deletes what's in the file and write what you pass to it, mode "a" will add the input to a new line

# with open('test_file.txt', mode="w") as file:
#     file.write("Holiiiii")
