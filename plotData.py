import matplotlib.pyplot as plt
grades = []
with open('science.txt','r') as f:
     f.readline()
     f.readline()
     s = f.read().splitlines()
     for i in s:
         l = i.split(',')
         if i != '':
            grades.append(l[0])

grades = list(map(float,grades))

plt.hist(grades, bins='auto')
plt.show()
