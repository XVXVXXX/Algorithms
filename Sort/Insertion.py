# 插入排序
class Insertion:
    def sort(self, a):
        length = len(a)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j],a[j-1] = a[j-1],a[j]
                    pass
                else:
                    break
                pass
        return None

s = Insertion()
array = [9,8,7,6,5,4,3,2,1,0]
o = s.sort(array)
print(o)