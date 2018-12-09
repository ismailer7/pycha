import re
import unittest

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
    


class TestIncrementString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(increment('foo'), 'foo1')
        self.assertEqual(increment('foobar124'), 'foobar125')
        self.assertEqual(increment('foo002'), 'foo003')
        self.assertEqual(increment('foo099'), 'foo100')
        self.assertEqual(increment('foo009'), 'foo010')
        

if __name__ == "__main__":
    unittest.main()
