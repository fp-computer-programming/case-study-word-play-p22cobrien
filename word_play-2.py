# Author: CMOB 3/16/2022

from unittest.util import _count_diff_all_purpose


words = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/words.txt","r")
out_file = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/words_without_e.txt","a")

def no_e():
    total = 0
    no_e = 0
    while True:
        line = words.readline()
        total += 1
        if "e" not in line:
            out_file.write(line)
            no_e += 1
            continue
        if len(line) == 0:
            perc = no_e / total
            break

no_e()


words.close()
out_file.close()
