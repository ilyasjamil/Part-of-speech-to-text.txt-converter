'Works only for ".onf" file formats.'
'----------------------------------'

filename = 'abc_0044.onf'
file = open(filename , 'r')
newfile = open('PlainSentences.txt','w')
data = file.readlines()
for index in range(len(data)):   
    if data[index] == 'Plain sentence:\n':               
        while data[index+2] != 'Treebanked sentence:\n':
            if data[index+2] != '\n':
                sentence = data[index+2]
                newfile.write(sentence)
            index = index + 1
newfile.close()