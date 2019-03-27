import pylab
import json

pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir = 'path/filename.json'
file_name = []
f = open(dataDir, 'r', encoding='utf-8')

for line in f.readlines():
    dic = json.loads(line)
    t = dic['images']
    print(len(t))
    for i in range(len(t)):
        i = str(t[i]['file_name'])
        f = open('path.txt', 'a', encoding='utf-8')
        f.writelines(str(i))
        f.write('\n')
