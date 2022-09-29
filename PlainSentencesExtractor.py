'Works only for ".onf" file formats.'
'----------------------------------'

filename = 'pri_0017.onf'
file = open(filename , 'r')
newfile = open('text.txt','w')
data = file.readlines()
for index in range(len(data)):   
    if data[index] == 'Plain sentence:\n': 
        index = index + 2
        sentence = ""
        while data[index] != 'Treebanked sentence:\n':
            if data[index] != '\n':
                sentence = sentence + data[index].strip()
            index = index + 1
        newfile.write(sentence)
        newfile.write('\n')
newfile.close()
