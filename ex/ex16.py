from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# mode can be 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name will be erased)
# 'a' opens the file for appending; any data written to the file is automatically added to the end
# 'r+' opens the file for both reading and writing. The mode argument is optional
# 'r' will be assumed if it’s omitted.
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()