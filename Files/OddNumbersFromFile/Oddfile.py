file1=open('lang.txt','r')
file2=open('copy.txt','w')

content=file1.readlines()
print(content)

for i in range (0,len(content)):
    print(i)
    
    if(i%2!=0):
        file2.write(content[i])
    
    else:
        pass
    
file2.close()


file2=open('copy.txt','r')

content1=file2.read()
print(content1)

file1.close()
file2.close()
