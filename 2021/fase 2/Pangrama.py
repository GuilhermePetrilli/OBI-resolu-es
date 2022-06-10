# f,p,r,l = input().replace(' ',''),0,'N',["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","x","z"]
# for c in l:
#     if c in f: p+=1
# if p == len(l): r = 'S'
# print(r)

f = input().replace(' ','')
l = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","x","z"]
p =0
r = 'N'
for c in l:
    if c in f: p+=1
if p == len(l): r = 'S'
print(r)

