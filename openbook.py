#Task 1

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

#Task 2

import re
fin1 = open("running-config.cfg")
fout1 = open("running-config-copy.cfg","w")
ip_pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

for line in fin1: 
  line = line.replace('192','10')
  line = line.replace('172','10')
  line = line.replace('255.255.0.0','255.0.0.0')
  line = line.replace('255.255.255.0','255.0.0.0')
  fout1.write(line)
'''
  words = line.split()
  for word in words:
    if(ip_pattern.match(word)):
      if(('192' in word) or ('172' in word)):
        c = word.split('.')
        c[0] = '10'
        word = '.'.join(c)
        line.replace("192*",word)
        line.replace("172*",word)
      elif('255' in word):
        word = '255.0.0.0'
        line.replace("255*",word)
'''


#Task 3
fin3 = open("running-config.cfg")

transit_access_in = []
fw_management_access_in = []
global_access = []

for line in fin3:
  line = line.strip()
  if("transit_access_in" in line):
    transit_access_in.append(line)
  elif("fw-management_access_in" in line):
    fw_management_access_in.append(line)
  elif("global_access" in line):
    global_access.append(line)


print(transit_access_in)
print()
print(fw_management_access_in)
print()
print(global_access)
