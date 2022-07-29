str1 = 'Our test string 1'
str2 = 'Some another text as example'

for i in str1:
  for i in str2:
   s = set(str1).intersection(set(str2))

if len(s) == 0:
  print ("This strings haven't the same symbols")
else:
  s = list(s)
  s.sort()
  print (*s, sep=' ')
