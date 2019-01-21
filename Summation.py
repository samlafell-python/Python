num = input(type in a number:)

addition = 0

if num < 0:
    print('make it positive, fam')
elif num == 0:
    print('cant be 0')
else:
    for i in range(1,num+1):
        addition = addition+i
    print('Adding ' + str(num) + ' by every number below it = ' + str(addition))
