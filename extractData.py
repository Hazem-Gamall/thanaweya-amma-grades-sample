
#convenient for now
total = 3
clan = 19
arabic = 21
english = 23
secondLang = 25
puremath = 27
history = 29
geography = 31
philosophy = 33
psycho = 35
chem = 37
bio = 39
geology = 41
appliedmath = 43
physics = 45

mathSubj = {total,arabic,english,secondLang,puremath,chem,appliedmath,physics}
scienceSubj = {total, arabic, english, secondLang, chem, bio, geology, physics}
literatureSubj = {total,arabic,english,secondLang,history,geography,philosophy,psycho}

# religion = 49 //just in case
# nation = 51
# eco = 53

s = []
student = []

mathFile = 'math.txt'
scienceFile = 'science.txt'
literatureFile = 'literature.txt'

def writeGrades(filename):
    if filename == mathFile:
        with open(filename,'a') as f:
            for counter, i in enumerate(mathSubj):
                if counter:
                    f.write(',')

                f.write(student[i])
            f.write('\n')

    elif filename == scienceFile:
        with open(filename,'a') as f:
            for counter, i in enumerate(scienceSubj):
                if counter:
                    f.write(',')

                f.write(student[i])
            f.write('\n')

    elif filename == literatureFile:
        with open(filename,'a') as f:
            for counter, i in enumerate(literatureSubj):
                if counter:
                    f.write(',')

                f.write(student[i])
            f.write('\n')

with open('test.txt','r')as f, open(scienceFile,'w') as sci, open(mathFile,'w') as m, open(literatureFile,'w') as l:

    #kick start the files
    sci.write('المجموع, عربي, انجليزي, لغة ثانية, كيمياء, احياء, جيولوجيا فيزياء\n')
    m.write('المجموع,عربي,انجليزي,لغة ثانية,رياضات بحتة,كيمياء,رياضيات تطبيقية,فيزياء\n')
    l.write('المجموع,عربي,انجليزي,لغة ثانية,تاريخ,جغرافيا,فلسفة,علم نفس\n')

    s = f.read().splitlines()


i = 0
while i < len(s)-54:

    student = s[i:i+54] #each student takes 54 lines of data

    if student[clan] == ' أدبي':
        writeGrades(literatureFile)
    elif student[clan] == ' علمي علوم':
        writeGrades(scienceFile)
    elif student[clan] == ' علمي رياضة':
        writeGrades(mathFile)

    i+=54


