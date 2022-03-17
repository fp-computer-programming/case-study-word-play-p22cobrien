# Author: CMOB 3/16/2022



words = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/words.txt","r")
out_file = open("/Users/p22cobrien/Desktop/Case Studies/case-study-word-play-p22cobrien/words_without_e.txt","a")

def no_e():
    total = 0
    e = 0
    
    while True:
        line = words.readline()
        if "e" not in line:
            words.write(line)
            total += 1
            e += 1
        elif "e" in line:
            total += 1
        if len(line) == 0:
            break
    percentage = (e / total) * 100
    print(percentage)

no_e()


words.close()
out_file.close()
