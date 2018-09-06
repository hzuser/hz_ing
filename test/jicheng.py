# coding:utf-8

class Count():
    def add(self, a):
        if a > 1:
            print a
        else:
            return -a

if __name__ == "__main__":
    b = Count()
    c = b.add(2)
    print (c)
