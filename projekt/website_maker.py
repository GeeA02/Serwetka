import sys
import os


path='index.html'
f=open('index.html',"r+")
content=f.readlines()
f.close()
f=open('index.html',"w+")

filename=sys.argv[1]
f1=open(filename,'r')
parameters=""
for p in f1:
    parameters+=p.replace('\n',', ')

filename=os.path.basename(filename)
date=sys.argv[2]

files=""
for pic in range(3,len(sys.argv)):
    if (str(sys.argv[pic]).find('.jpg')!=-1):
        files+='<a target=\'_blank\' href=\''+str(sys.argv[pic])+'\'><img height=\'100\' src=\''+str(sys.argv[pic])+'\'></a>\n'
    else:
        files+='<a target=\'_blank\' href=\''+str(sys.argv[pic])+'\'>'+os.path.basename(str(sys.argv[pic]))+'</a>'
newContent='<tr><td>'+date+'</td><td>'+filename+'</td><td>'+parameters+'</td><td>'+files+'</td></tr>\n</table>\n'

i=0
for line in content:
    if line=='</table>\n':
        content[i]=newContent
    i+=1
f.writelines(content)
f.close()
f1.close()

