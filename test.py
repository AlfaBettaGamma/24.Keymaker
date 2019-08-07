def Keymaker(k):
  kst = []
  step = 0
  result = ''
  for j in range(k): 
    if step == 0: # первый этап
      for i in range(k):
        kst.append(1)
      step += 1  
    else: # второй и последующие этапы
      for i in range(k):
        if i%(j+1) == j:
          if kst[i] == 0:
            kst.insert(i,1)
            kst.pop(i+1)
          else:  
            kst.insert(i,0)
            kst.pop(i+1)
  for i in range(len(kst)):
    result += str(kst[i])
  return result

print(Keymaker(1))
print(Keymaker(2)) 
print(Keymaker(3))
print(Keymaker(4))
print(Keymaker(5))
print(Keymaker(6)) 
print(Keymaker(7))
print(Keymaker(8))
print(Keymaker(9))
print(Keymaker(10)) 
print(Keymaker(11))
print(Keymaker(12))
print(Keymaker(13))
print(Keymaker(14)) 
print(Keymaker(15))
print(Keymaker(16))

# 1 - открфтая дверь, 0 - закрытая дверь, 