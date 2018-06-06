
readop=open('data1.csv')
writeop=open('newfil.csv','w')
f=0
writeop.write('SN,F1,F2,F3,F4,F5,F6,Class\n')
for line in readop :
    if(f==0):
        f=1
    else:    
        l2=line.split(',')
        sn=l2[0]
        seq=l2[1]
        f1=str(seq.count('N'))  #counts no. of 'N's in sequence
        f2=str(seq.count('H'))
        f3=str(seq.count('Q'))
        f4=str(seq.count('G'))
        f5=str(seq.count('D'))
        f6=str(seq.count('T'))
        if(l2[2]=='+\n'):
            cl='1'
        else:
            cl='0'
        writeop.write(sn+','+f1+','+f2+','+f3+','+f4+','+f5+','+f6+','+cl+'\n')
        
    
    
writeop.close()
readop.close()
print('done')    
    
    