# first command-line argument should be the mail user
# to decode the attachment, the subject should end with 
# 'b64' followed by a '-' and the filetype, such as:
# "b64-csv"

# currently, in order for this to work,
# the words "Content-Transfer-Encoding: base64"\
# cannot be a line in the email
import sys
import base64

mailfile = open(f"/var/mail/{sys.argv[1]}")
filetypes = []
attachments = []
skip_lines = 0
b64_line = False
for line in mailfile.readlines():
    if skip_lines > 0: 
        skip_lines -= 1
        continue
    if b64_line:
        line = line.removesuffix('\n')
        attachments.append(line)
        b64_line = False
        continue
    if "Content-Transfer-Encoding: base64" in line:
        skip_lines = 2
        b64_line = True
    words = line.split()
    if len(words) > 1:
        if words[0] == "Subject:":
            for word in words:
                if "b64" in word:
                    filetypes.append(word.split("-")[1])
            
filenames = []
for i in range(0, len(attachments)):
    filenames.append(f"attachment{i}.{filetypes[i]}")
for i in range(0, len(filenames)):
    with open(filenames[i], "wb") as file:
        file.write(base64.b64decode(attachments[i]))
with open(f"/var/mail/{sys.argv[1]}", "w") as file:
    file.write("")