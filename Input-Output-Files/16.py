from sys import argv
scrip, filename = argv

print "The file %r will be erased." %filename, "\nIf you don't want it, press ctrl+c\nIf it is ok, press RETURN"

raw_input("?")
print "Opening file..."
target = open(filename,'w')

print "Truncating(erasing) file."
target.truncate()

print("Now, print some lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing them to file"

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("Closing file.")
target.close()