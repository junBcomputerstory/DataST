class stack:
    def __init__(self):
        self.team=[]
    def push(self,X):
        self.team.append(X)
    def pop(self):
        if self.team:
            self.team.pop()
        else:
            return -1
    def size(self):
        return len(self.team)
    def empty(self):
        if self.team:
            return 1
        else:
            return 0
    def top(self):
        if len(self.team):
            return self.team[-1]
        else:
            return -1


a=stack()
num=int(input("입력원하는 숫자의 갯수를 입력하시오:"))
for b in range(0,num,1):
    x=int(input())
    a.push(x)
print(a.team)