import os
import shutil

#the program manages the text input and passes the lines to Hershey's text extension

os.chdir('/home/swayam/Desktop/hershey\'sMultilineInput/Manual Writer')           #add the location of the txt file where you pasted the text
with open('stage-text input.txt', mode='r', encoding="ISO-8859-1") as file:       #input the name of the txt file

    with open('newfile.txt',mode='w', encoding="ISO-8859-1") as output:           #another text file which gets passed to the hershey's text extension
        for i in file:
            j=list(i)
            n = 70
            #print(len(j))
            if len(j)<=n:
                for k in j:
                    print(k,end='', file=output)
            elif j[n]==' ':
                count=0
                for k in j:
                    print(k,end='', file=output)
                    count=count+1
                    if count==n+1:
                        print("\n", end='', file=output)
            else:
                count2=0
                flag=0
                p1=0
                p2=n
                while(1):

                    if p2>len(j):
                        for l in j[p1:len(j)]:
                            print(l, end='', file=output)
                        break
                    while j[p2] != ' ':
                        p2=p2-1
                    for k in j[p1:p2]:
                        print(k, end='', file=output)
                        # count2=count2+1
                    print("\n", end='', file=output)
                    p1=p2
                    p2=p2+n
with open('tocopystring.txt', mode='w+', encoding="ISO-8859-1") as stringFile:
    with open('newfile.txt', mode='r', encoding="ISO-8859-1") as finalFile:
        for i in finalFile:
            print("\"", end='', file=stringFile)
            for j in i:
                if j != '\n':
                    print(j, end='', file=stringFile)
            print("\",", end='', file=stringFile)
           # print("\""+i+"\",", end='')
with open('tocopystring.txt', mode='r', encoding="ISO-8859-1") as stringFile:
    for i1 in stringFile:

        print(i1)
        #changing directory to write on the python file

        os.chdir('/home/swayam/Desktop/hershey\'sMultilineInput/Hershey\'sTextExtension') #local directory containing the extension files

        with open('hershey.py', mode='r', encoding="ISO-8859-1") as file:
            j=[]
            for i in file:
                j.append(i)
                # if i[0:9]=='docuWrite':
                #     i[9:]='it is alive'

        j[63] = "docuWrite = [" + i1 +"]\n"
        print(j)
        with open('hershey.py', mode='w', encoding="ISO-8859-1") as file2:
            for k1 in j:
                print(k1,end='', file=file2)


#pasting the files in Inkscape extensions folder (run as administrator or root)
shutil.copyfile('/home/swayam/Desktop/hershey\'sMultilineInput/Hershey\'sTextExtension/hershey.py','/usr/share/inkscape/extensions/hershey.py')


