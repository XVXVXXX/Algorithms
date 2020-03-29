# 归并排序
class Merge:
    def _init__(self):
        self.aux = None

    def merge(self, a, lo, mid, hi):
        # copy
        for idx in range(lo,hi+1):
            self.aux[idx] = a[idx]

        i = lo
        j = mid+1

        for k in range(lo,hi+1):
            if i>mid:
                a[k] = self.aux[j]
                j+=1
                pass
            elif j>hi:
                a[k] = self.aux[i]
                i+=1
                pass
            elif self.aux[i]<self.aux[j]:
                a[k] = self.aux[i]
                i+=1
                pass
            else:
                a[k] = self.aux[j]
                j+=1
    
    # 自顶向下归并
    def sort(self, a):
        if not a:
            return a
            pass
        length = len(a)
        self.aux = [0]*length
        self.innerSort(a,0,length-1)
        return a
        pass

    def innerSort(self, a, lo, hi):
        if lo>=hi:
            return
        mid = (lo+hi)>>1
        self.innerSort(a,lo,mid)
        self.innerSort(a, mid+1, hi)
        self.merge(a,lo,mid,hi)
        return a
        pass

s = Merge()
array = [9,8,7,6,5,4,3,2,1,0]
o = s.sort(array)
print(o)