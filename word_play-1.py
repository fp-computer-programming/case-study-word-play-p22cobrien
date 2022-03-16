# Author: CMOB 3/16/2022

words = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/words.txt","r")
greater = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/greater_than_20.txt","a")
while True:
    line = words.readline()
    if len(line) > 19:
        greater.write(line)
        continue
    if len(line) == 0:
        break

words.close()
greater.close()