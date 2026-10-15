#Define a student class
#要求
#1.属性包括学生名字学号以及语数英三科的成绩
#2.能够设置学生某科目的成绩
#3.能够打印出改学生的所有科目成



#开头
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.score = {"math":0,"english":0,"chinese":0}

    #分类
    def kll_score(self,bll,llb):
        if bll in self.score:
            self.score[bll] = llb
    def print_score(self):
        print(f"Student name is {self.name} (student ID Number is {self.age}) The result is: " )
        for bll in self.score:
            print(f"{bll}: {self.score[bll]} points")

foilo = Student("foilo","1100")
foilo.kll_score("math",90)
foilo.kll_score("english",90)
foilo.kll_score("chinese",95)
foilo.print_score()




#赋值
#foilo = Student("foilo","100")
#foiloo = Student("filoo","114514")
#print(foiloo.name)
#print(foiloo.age)
#foiloo.kll_score("math",95)
#foiloo.kll_score("english",20)
#foiloo.kll_score("chinese",50)
#一定要看有没有打印出来
#我看了好久才看出来的 #print(foiloo.score)
#print(foiloo.score)









