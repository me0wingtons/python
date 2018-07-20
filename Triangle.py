def triangle(n):
    if n == 1:
        return '*\n'
    else:
        star = ''
        stacker = ''
        for i in range(1,n+1):
            if i == 1:
                star += '*'
                stacker += star +'\n'
            elif i % 2 != 0: #odd
                star = '*' + star
                stacker += star +'\n'
            else:
                star = ' ' + star
                stacker += star +'\n'
    
    print(stacker)

print('triangle(n) where n is any number you want')
