def Keymaker(k):
  kst = []
  step = 0
  result = ''
  num = []
  o = []
  for j in range(k): 
    if step == 0: # первый этап
      for i in range(k):
        kst.append('1')
      step += 1  
    else: # второй и последующие этапы
      for i in range(k):
        if i%(j+1) == j:
          if kst[i] == '0':
            kst.insert(i,'1')
            kst.pop(i+1)
          else:  
            kst.insert(i,'0')
            kst.pop(i+1)
        if kst[i] == '1' and j == k-1:
          num.append(i)
        elif kst[i] == '0' and j == k-1:
          o.append(i)
    print(kst)
  for i in range(len(kst)):
    result += str(kst[i])
  print('test - ',len(kst),num,o)
  return result

#
print(Keymaker(20))
#for i in range(n):
#  print(i,Keymaker(i))


# 1 - открытая дверь, 0 - закрытая дверь, 