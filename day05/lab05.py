import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()



## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

for line in obama:
  if not re.search(r"the [a-z]*",line):
    print(line)



# TODO: print lines that contain a word of any length starting with s and ending with e
sAnde=re.compile(r"(s[a-z]*e$)")
for line in obama:
  if sAnde.search(line):
    print(line)


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = input("Please enter a date in the format MM.DD.YY: ")
results=re.findall(r"\d{2}",date)
print("""
Month: %s
Day: %s
Year: %s
"""%(results[0],results[1],results[2]))
