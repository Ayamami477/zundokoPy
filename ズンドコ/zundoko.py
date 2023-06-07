import random 

zundoko = list(map(str,range(5)))
while ''.join(zundoko) != 'ズンズンズンズンドコ':
    del zundoko[0]
    zun = random.choice(['ズン','ドコ'])
    print(zun,end='')
    zundoko.append(zun)

print('キ・ヨ・シ！')    