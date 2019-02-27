import re



filename = "./mails.txt"
file = open(filename,"r")
for line in file:
    print(line)
    #print(re.match("@",line))
