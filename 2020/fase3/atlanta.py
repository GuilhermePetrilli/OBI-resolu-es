A,B = int(input()),int(input())
par = 1
ok = 1
if A % 2 == 0:
  par = 0
for b in range(3,round(A/2)+par):
  H = A/2 - b+2
  if H - int(H) == 0:
    if H >= 3:
      if (H - 2) * (b-2) == B:
        ok = 0
        print(b,int(H))
if ok == 1:
  print(-1,-1)
        