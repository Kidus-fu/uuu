user= ['kidus','dave','jc','mine']
data= [45,78,90,34,'M','CS']
# del user
print(user[0:])
user.append('cj')
print(user)
user.extend(['hope'])
print(user[0:])
user += ['holy']
print(user[0:])
# user += 'holy'
user.remove('jc')
print(user[0:])
user.extend(['kidus','jc'])
print(user[0:])
user[-1] = user[-1].upper()
user.insert(1,'bob')
user.sort(key=str.lower)
print(user)