def list_ifname_ip(fin):
  d = {}
  keys = []
  val = []
  for line in fin:
    line = line.strip()
    
    words = line.split()
    for i in range(len(words)-1):
      if("nameif" == words[i]):
        keys.append(words[i+1])
      elif("." in words[i]):
        val.append((words[i],words[i+1]))
  #print(len(keys))
  #print(len(val))
  for i in range(len(keys)):
    d.update({keys[i] : val[i]})
  return d

fin = open("running-config.cfg")
dic = list_ifname_ip(fin)
print(dic)
