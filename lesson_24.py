def Keymaker(k):
  kst = []
  step = 0
  result = ''
  for j in range(k): 
    if step == 0: # первый этап
      for i in range(k):
        kst.append(1)
      step += 1  
    else: # второй этап
      for i in range(k):
        if i%(j+1) != 0:
          if kst[i] == 0:
            kst.insert(i,1)
            kst.pop(i+1)
          else:  
            kst.insert(i,0)
            kst.pop(i+1)
  for i in range(len(kst)):
    result += str(kst[i])
  return result