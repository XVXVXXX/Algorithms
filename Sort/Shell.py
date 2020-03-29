# 希尔排序
class Shell:
    def sort(self, a):
        length = len(a)
        h = 1
        while (h<h//3):
            h = h*3+1;
            pass

        while (h>=1):
            for i in range(h, length):
                for j in range(i, h-1, -1*h):
                    if a[j] < a[j-h]:
                        a[j],a[j-h] = a[j-h],a[j]
                        pass
                    else:
                        break
                    pass
                pass
            h = h//3
        return a


s = Shell()
array = [9,8,7,6,5,4,3,2,1,0]
o = s.sort(array)
print(o)                