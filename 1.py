class Inttobase3:
   def convert(self, num):
      signofnumber = '-' if num<0 else ''
      num = abs(num)
      if num < 3:
         return str(num)
      mystring =''
      while num != 0:
         mystring = str(num%3) + mystring
         num = num//3
      return signofnumber +mystring
myobj = Inttobase3()
n=int(input())
print(myobj.convert(n))
