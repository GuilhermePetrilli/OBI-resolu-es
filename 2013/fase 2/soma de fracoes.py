def GCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

a,b,c,d = [int(i) for i in input().split()]
def LCM(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
   
lcm = LCM(b,d)
a,b,c,d = a*(lcm/b),lcm,c*(lcm/d),lcm
r = [a+c,lcm]
gcd = GCD(r[0],r[1])
print(int(r[0]/gcd),int(r[1]/gcd))

