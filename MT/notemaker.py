import random

poss = ["A","B","C","D","E","F","G"]
notesAnim = []
for i in range(2400):
    NoteString = ""
    for k in range(1,random.randint(1,4)):
        NoteString = NoteString + poss[random.randint(0,len(poss)-1)]
    notesAnim.append(NoteString)
print(notesAnim)
