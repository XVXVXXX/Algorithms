# 堆排序
class Heap:
    def sort(self, a):
        if not a:
            return a
            pass
        # pq insert 0
        a.insert(0, 0)
        n = len(a)-1

        # 堆有序
        for i in range(n >> 1, 0, -1):
            self.sink(a, i, n)
            pass

        while n > 1:
            a[1], a[n] = a[n], a[1]
            n -= 1
            self.sink(a, 1, n)

        # pq remove 0
        a.pop(0)

        return a

    def swim(self, a, k):
        while k > 1 and a[k >> 1] < a[k]:
            a[k >> 1], a[k] = a[k], a[k >> 1]
            k = k >> 1

        return None

    def sink(self, a, k, n):
        while 2*k <= n:
            j = 2*k
            if j < n and a[j+1] > a[j]:
                j += 1
                pass
            if a[j] < a[k]:
                break
            a[j], a[k] = a[k], a[j]
            k = j

        return None


s = Heap()
array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
o = s.sort(array)
print(o)
