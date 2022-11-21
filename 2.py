string1,string2=map(str,input().split())
count=0
if((len(string1) and len(string2) >0):
   lastchar=string2[-1]
   for i in string1:
      if i==lastchar:
         count+=1
print(count)
