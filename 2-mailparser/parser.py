import re

filename = "./mails.txt"
file = open(filename,"r")

emails = []
for line in file:
    emailsMatched = re.findall(r"(\w+@\w+\.\w+\.*\w*)",line)
    for emailMatch in emailsMatched:
        emails.append(emailMatch)
print(emails)
