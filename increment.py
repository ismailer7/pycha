import re

'''
      9 9 9
  +  
      0 0 1
    -------
    1 0 0 0
'''  

def increment(string):
    match = re.search('\d+$', string)
    if match:
        s1 = list(match.group(0))
        s2 = ['0' for i in range(len(s1) - 1)] + ['1']
        res = []
        for i in range(len(s1) - 1, -1, -1):
            a = str(int(s1[i]) + int(s2[i]))
            if len(a) != 2:
                res.append(a)
            else:
                res.append(a[1])
                if i-1 < 0:
                    res.append('1')
                else:
                    s2[i-1] = a[0]
    else:
        return string + '1'
    return re.sub('\d+$', ''.join(res[::-1]), string)
    


if __name__ == "__main__":
    print(increment('foobar102'))

    