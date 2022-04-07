import os, re
file_path = "G:\\Try\\1.txt"
text = open(file_path).readlines()
key = 'foia'
for i in text:
    if key in i:
        s = re.findall('(.*?)', i)
        s1 = ''.join(s)
        print(s1)

