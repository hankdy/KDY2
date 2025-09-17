class A:
    def __init__(self, val):
        self.cnt = val
    
    def printval(self, val):
        self.cnt += 1
        print(f"[A] cnt({self.cnt}), val=", val)
        
        
# %%
    
class B:
    def __init__(self, val):
        self.cnt = val
    
    def printval(self, val):
        self.cnt += 10
        print(f"[B] cnt({self.cnt}), val=", val)
        
# %%
        

class C(B, A):
    def count(self):
        return self.cnt

class D(A, B):
    def count(self):
        return self.cnt



# %%


c = C(1)
c. printval(10)
print('count:', c.count())


# %%


d = D(2)
d. printval(20)
print('count:', d.count())