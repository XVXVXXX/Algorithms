# 快排
class Quick:
    def sort(self, a):
        length = len(a)
        self.innerSort(a,0,length-1)
        return a
        pass

    def innerSort(self, a, lo, hi):
        if lo>=hi:
            return

        j = self.partition(a,lo,hi)
        self.innerSort(a,lo,j)
        self.innerSort(a,j+1,hi)
        return a

    def partition(self, a, lo, hi):
        i = lo+1
        j = hi
        c = a[lo]
        while True:
            while a[i]<c:
                i+=1
                if i == hi:
                    break
                pass
            while a[j]>c:
                j-=1
                if j == lo:
                    break
                pass
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
            pass

        a[lo],a[j]=a[j],a[lo]
        return j
    pass

s = Quick()
array = [9,8,7,6,5,4,3,2,1,0]
o = s.sort(array)
print(o)