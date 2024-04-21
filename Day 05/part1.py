import os
from hashlib import md5

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

VOWELS = "aeiou"
BAD_STRINGS = ["ab", "cd", "pq", "xy"]

with open(inputFilePath) as inputFile:
	strings = [line[:-1] for line in inputFile]

niceStringCount = 0

for string in strings:
	if(any(badString in string for badString in BAD_STRINGS)):
		continue

	vowelCount = 0

	for vowel in VOWELS:
		vowelCount += string.count(vowel)

	if(vowelCount < 3):
		continue

	doubleChar = False

	for i in range(len(string)-1):
		char = string[i]

		if(char == string[i+1]):
			doubleChar = True
			break

	if(doubleChar):
		niceStringCount += 1

print(niceStringCount)
