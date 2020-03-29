# 选择排序
class Selction:
    def sort(self, array):
        length = len(array)
        for i in range(0, length):
            tMin = i
            for j in range(i, length):
                if array[j] < array[tMin]:
                    tMin = j
                    pass
                pass
            array[i],array[tMin] = array[tMin],array[i]
            pass        
        return array
s = Selction()
array = [9,8,7,6,5,4,3,2,1,0]
o = s.sort(array)
print(o)