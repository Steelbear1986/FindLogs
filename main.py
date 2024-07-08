import glob
result=[lne for i in [fl for fl in glob.glob('inset your mask for file')]  for lne in open(f'{i}')  if 'key word for search in the file list' in lne]
f= open ("result.txt","w")
for i in result: f.write(i)





