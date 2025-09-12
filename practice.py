# 电子部标
# tracer(0)
# turtles()
# t=(100/pow(2,1/2)-75/pow(6,1/2)-tan(radians(15))*25/pow(2,1/2))*pow(3,1/2)/2
# setup(700,400)
# getscreen().colormode(255)
# color((255,215,0),(000,000,000))
# penup(),pensize(10),pendown()
# speed(4)
# setheading(60)
# forward(t*(1/pow(3,1/2)+tan(radians(75))))
# setheading(-105)
# forward(t/cos(radians(75))-25/pow(2,1/2)*1/sin(radians(75)))
# setheading(0)
# forward(100/1.3)
# setheading(-120)
# forward(t*(1/pow(3,1/2)+tan(radians(75))))
# setheading(75)
# forward(t/cos(radians(75))-25/pow(2,1/2)*1/sin(radians(75)))
# setheading(180)
# forward(100/1.3)
# penup()
# setheading(0)
# forward(100/1.3-(t/cos(radians(75))-25/pow(2,1/2)*1/sin(radians(75)))/2*cos(radians(75)))
# setheading(90)
# forward(25/2/pow(2,1/2))
# forward(110)
# pendown()
# setheading(0)
# pensize(10)
# circle(-110) #50
import os
import random

# penup()
# left(90)
# forward(10)
# write('E',font=("consolas"))
# setposition(pos())

# goto(-120*sin(radians(3.6))*(1+cos(radians(7.2))),(-120*sin(radians(3.6))*sin(radians(7.2))))

# write('M',font=("consolas"))

# goto(120*sin(radians(3.6))*(1+cos(radians(7.2))),(-120*sin(radians(3.6))*sin(radians(7.2))))

# write('A',font=("consolas"))

# done()

# right(90)
# left(7.2)
# penup(),forward(-120*sin(radians(3.6))*2)
# left(7.2)
# penup(),forward(-120*sin(radians(3.6)*2))
# left(7.2)
# penup(),forward(-120*sin(radians(3.6)*2))
# for i in "M E A":
#     # setup(800,500)
#     penup(),forward(120*sin(radians(3.6)*2))
#     pendown()
#     write(i,False,"center",font=("consolas"))
#     left(-7.2)


# setheading(0)
# forward(150)
# dirt=0
# for i in range(4):
#     circle(-10,90)
#     forward(300)


# setheading(60)
# forward(t*(1/pow(3,1/2)+tan(radians(75))))
# setheading(0)
# pendown()

# circle(-((t*(1/pow(3,1/2)+tan(radians(75))))*pow(3,1/2)-25/pow(3,1/2))/2)
# sleep(8)


# setup(650,350 ,None,None)
# penup()
# forward(-250)
# pendown()
# pensize(25)
# pencolor(0,0,0)
# setheading(-45)
# for i in range(4):
#     circle(40,90)
#     circle(-40,90)
# circle(40,80/2)
# forward(40) 
# circle(16,180)
# forward(40*2/3)
# setup(0.45,0.45)
# penup()
# pensize(10)
# setheading(30)
# pendown()
# pencolor(0,0,0)
# direct=30
# print(pow(3,pow(3,999),10000))
# print(pow(3,999))
# for i in range (5):
#     forward(50)
#     direct-=60
#     setheading(direct)
# forward(50)
# direct=90
# for i in range(6):
#     forward(50)
#     direct-=120
#     setheading(direct)
#     forward(50)
#     direct+=60
#     setheading(direct)
# penup()
# forward(300)
# pendown()
# len=200
# for l in range(20):
#     direct-=90
#     setheading(direct)
#     forward(len)
#     len-=10
# print(abs(-5+12j))
# print(divmod(10,3))
# print(30-3**2+8//3**2*10)
# print (3*4**2/8%5)
# # x="fr"
# # print (int (x))
# print(frexp(5))
# print(isnan(3.452))
# print (degrees(pi/2*5))
# x=inf
# print (isinf(x))
# print(isclose(4,4))
# print (gamma(0.8))
# print (gamma(-0.2)*-0.2)
# print (pow(pi,1/2))
# su=r"hahah好啥好\j\t'c'w"+"rvewrvkkk"
# print (su)
# day='星期一','星期二','星期三','星期四','星期五','星期六','星期日'
# print (day[1:3],sep='')

# s1,s2,s3=33487, 27946 ,'afds'
# print (chr(s1),chr(s2),sep='',end='\n\n\n')
# print (chr(ord('苏')),ord('苏'),ord('洪'),ord('志'))
# ,#print ('abcd'<'ad','abc'<'abcd',''<'a','Hello'>'hello')
# print ('3141123'.isnumeric())
# print (str('1262.23'))
# week=input("你的名字是？")
# day=eval(su)
# print (day)
# print ('姓：'+week[0])
# print ('名：'+week[1:])
# sleep(1000)
# su="abmmlmmncdelmmnfghlmmlmmnlmnijklmmnak"
# print (int('546')+312)
# k='lmmn'
# m='qqqq'
# print (su.endswith(k))
# print (su.startswith('abc'[0:-1]))
# print (su.count(k))
# print (su.startswith(k,4,))
# print (su.replace(k,m,8))
# print (su.split(sep='l'))
# print (su.center(60,'m'))
# print (su.replace(k,''))
# print (su[::3])
# print (su)
# print (su.strip('nma'))
# s='helloworld'
# print(s[::3])
# print (s[-2::])
# print (day[0])
# print ("{}aaaa"+"{"+"你'{{{{1}}}}styket'猜猜这里有什么{}：；；但是或者{}：".format('1','2','3'))
# print("{:#^15}evw{:.4}r".format('python',130.465702))

# scale = 10
# print ("{:-^15}".format('执行开始'))
# for i in  range(scale+1):
#     a,b ='**'*i,'..'*(scale-i)
#     c = (i/scale)*100
#     print ("%{:^3.0f}[{}>{}]".format(c,a,b))
#     #sleep(0.5)
# print ("\n{:-^15}".format('执行结束'))
# for i in range (101):
#     #j=i/100
#     i=(1+(1-i/100)**1.5*-1)*100
#     print ("\r{:^3.0f}%".format\
#            (\
#                i),end='')

#     sleep(0.05)
# while True:
# for i in ["/","-","|","\\","|"]:
#     print ("%s\r" % i)
# from tqdm import*
# for i in tqdm (range(1,100)):
#     sleep(0.01)
# print ('数字{}'.format(6+'aef' ))
# print (random())

# s=['wgr',23,'sfr','w',223]
# print (choice(s))
# shuffle(s)
# print (s)
# print (sample(s,2))
# d=getrandbits(1)
# print (d)
# seed(123)
# print (randint (2,8),randint (2,8),randint(2,8))
# seed(123)
# print (randint (2,8),randint (2,8),randint(2,8))
# d='abcdefghij'
# print (sample(d,4))
# s=list( range(100))
# print (sample(s,10))
# print (list(range(19,20)))
# s=list(range(198,199))
# print (s)
# sum=0
# for i in range(19,20):
#     sum+=1
#     print (i)


# print (sum)

# sum=0.0
# t=8
# k=9
# perf_counter()
# print (int(pow(2,k)))
# for i in range(int(pow(2,k))):
#     x,y=random(),random()
#     dist=sqrt(x**2+y**2)
#     if dist <=1.0 :
#         sum+=1
# print (4*sum/pow(2,k),'{}'.format(perf_counter()))
# try:
#     c=eval(input("wrg"))
# except NameError:
#     print ("输入错误")
#     c="未知字符"
# except NameError:
#     print ("再次输入")
# else :
#     print (c)
# finally:
#     print ("结果是？{}".format(c))


# x=randint(0,9)
# y=eval(input("输入一个整数（0-9）"))
# down,up=0,9
# sum=1
# while y!=x:
#     sum+=1
#     if y>x:
#         print ("太大了",end="  ")
#         up=y
#         y=eval(input("输入一个整数（{}-{}）".format(down,up)))
#     if y<x :
#         print ("太小了",end="  ")
#         down=y
#         y=eval(input("输入一个整数（{}-{}）".format(down,up)))
# else :
#     print ("预测了{}次，你猜中了".format(sum))


# s=input("请输入一串任意字符")
# print (len(s),s)
# i,amount=0,0
# # print (s[0:0])


####字符统计程序
# while i<len(s):
#     if i==0:
#         #sum+=1
#         for j in range (i,len(s)):
#             if s[i] == s[j]:
#                 amount+=1
#             if j==len(s)-1:
#                 print (s[i],amount)
#                 amount=0
#                 i+=1
#     elif s[i] not in s[i-1] and s[i] not in s[:i-1]:
#          #sum+=1
#          for j in range (i,len(s)):
#             if s[i] == s[j]:
#                 amount+=1
#             if j==len(s)-1:
#                 print(s[i],amount)
#                 amount=0
#                 i+=1
#     else :
#         i+=1


###辗转相除法
# x,y=eval(input("输入两个正整数"))
# print (x,y)
# if x>y:
#     x1,y1=y,x
# else:
#     x1,y1=x,y
# while y1%x1 !=0:
#     x1,y1 = y1%x1 , x1
# print ("最大公因数为：",x1,"最小公倍数为：",int(x*y/x1))


# sum=0
# amount=100
# y1=input("换还是不换你的最初选择（y or n)：")
# if y1 in ["n","N"]:

#     for i in range (amount):
#         x=randint(1,3)
#         y=randint(1,3)
#         pa=sample(["1","2","3"]-str(x))
#         if x==y :
#             sum+=1
#     print ("不换选择",sum/amount)
# elif y1 in ["y","Y"] :
#     for i in range (amount):
#         x=randint(1,3)
#         y=randint(1,3)
#         pa=sample(["1","2","3"]-str(x))
#         y=["1","2","3"]-pa-str(y)
#         if x==y :
#             sum+=1
#     print ("换选择",sum/amount)
# else :
#     print ("输入错误")


# fun1=lambda x,y:  x+2*y
# def fun(x,y):
#     return x+y
# print (fun1(y='hahah',x="hiehie"))
# n,a,b=1,

# def ls(a,b):  
#     global n
#     b*=a
#     n=a
#     return a*b
# print (ls(2,"iycv"),n)
# ls(a,b)

# for i in range (9):
#     sum+=i
# print (sum)

# print (datetime.now())


# print (datetime.utcnow())

# datetime为库，datetime.datetime是类，可以创建事件对象。

# someday=datetime(2024,1,31)
# print (datetime.today())

# print (datetime(12,3,3))datetime

# print (someday.isoweekday())
# print("boub\\t\
#       o",\
#         end=" ")
# print ("iyviixtrcfygvhbjniy")

# def basic(k):
#  if k :
#     pendown()
#     forward(20)
#     right(90)
#  else:
#     penup()
#     forward(20)
#     right(90)

# def drawdigit(x):
#     basic(True) if x in [2,3,4,5,6,8,9] else basic(False)
#     basic(True) if x in [1,3,4,5,6,7,8,9,0] else basic(False)
#     basic(True) if x in [0,2,3,5,6,8,9] else basic(False)
#     basic(True) if x in [0,2,6,8] else basic(False)
#     left(90)
#     penup()
#     basic(True) if x in [0,4,5,6,8,9] else basic(False)
#     basic(True) if x in [0,2,3,5,6,7,8,9] else basic(False)
#     basic(True) if x in [2,3,4,7,8,9] else basic(False)
#     left(180)
#     penup()
#     forward(5)

#     penup()
# num=input("请输入一串数字")
# def main():
#     setup(800,600)
#     penup()
#     forward(-300)
#     for i in num :
#         if eval(i) in [1,2,3,4,5,6,7,8,9,0]:
#             drawdigit(int(i))
# main()


# setup(800,600)
# penup()
# forward(-200)
# pendown()
# write("电子部",("Arial",30,))
# setup(800,600)
# pendown()
# pensize(2)
# write("ivyvyxfcg vujhbbi",False,"left",("Arial",18,"normal"))
# done()


# def koch(size,n):
#     if n == 0:
#         forward(size)
#     else:
#         for angle in [0,60,-120,60]:
#             left(angle)
#             koch(size/3,n-1)

# def k(size,n):
#     if n==0:
#         forward(size)


# def main():
#     #setrecursionlimit(2500)
#     # tracer(2)
#     setup()
#     # speed(0)
#     penup()
#     goto(-300,165)
#     pendown()
#     pensize(2)
#     setheading(0)
#     # k(600,0)
#     # n,size=0,600
#     # if n==0:
#         # forward(size)
#     # koch(600,0)
#     for i in range(3):
#         koch(600,2)
#         right(120)
#     done()
# main()


# s='hurtx'
# print (type(s))
# print (len(1241))
# t=lambda s1 , s2 : s1 * s2


# print (ceil(pow(8,1/2)))


# def isPrime(s):# 质数判断
#     if s == 2:
#         return True
#     t=floor(pow(s,1/2))
#     for i in range(2,t+1):
#         if t%i == 0:
#             return False
#         return True

# print (isPrime(2),isPrime(4),isPrime(5))
# all=['A','B',"C"]
# all.remove("A")
# print (all)
# 递归汉诺塔展示函数

# def hanoi(n,s,t):
#     if n == 1:
#         print (s,'→',t)
#     else :
#         # o=['A','B',"C"].remove(s)
#         t1=({"A","B","C"}-{s}-{t}).pop()
#         hanoi(n-1,s,t1)
#         print (s,"→",t)
#         hanoi(n-1,t1,t)
# def main():
#     hanoi(1,'A','C')
# main()


# st=[2,5,7,1,6]
# print (sorted(st,reverse=True),st)
# p,q=[30,61,2,0],[31,21,133]
# print (q>p)


# d={1:[1,2],2:[3.5]}
# p={1:"zhnag",2:"qeg"}
# o={"zhzang":"vyv","qef":"qfe"
#    }
# s=(12,"dq",124,"qrge")
# i=[{(1,2):1,(2,8):1},"fty"]
# print (i[0][(2,8)])
# print(d[1])

# from jieba import *
# add_word("苏洪志heh")
# print(lcut("你好呀！苏洪志heh是你的朋友。"))


# s={"wdw":12,"eg":68}
# s=list(s.items())
# print (list(s))
# s={"wdw":12,"eg":68}
# list(s.values()).sort(reverse=False)
# print (s)
# s={"wdw":12,"eg":68}
# s=list(s.items())
# s.sort(key= lambda x:x[1],reverse=True)
# print (s)

# def repid(s):
#     t={}
#     for i in s:
#         t[i]=s.get(i,0)+1
# S=list(s.items()).sort(key=lambda x:x[1],reverse=True)
# for i,j in S:
#     if j>1:
#         S.pop((i,j))
# return S
# from os import*

# txt=open('note.docx','rb',)#相对路径和绝对路径的区别encoding='utf-8'
# print(txt.readlines())
# txt.close()
# im=Image.open("D:\\Users\\Lenovo\\OneDrive\\桌面\\图片.jpg")
# r,g,b=im.split()
# print (r)
# b.save("tupa.jpg")
# fo=open("ti.csv","r+")
# fo.write("".join(['da','xiao','hei','\n','ha'])+'\n')
# fo.close()
# ma=Image.open("tupa.jpg")
# t=ma.size
# ma.thumbnail((t[0]/2,t[1]/2))
# ma.save("tutu.jpg")
# print (ma.size)
# print(4000*6000*24/1024)


# import fitz  # fitz就是pip install PyMuPDF


# def pyMuPDF_fitz(pdfPath, imagePath):
#     startTime_pdf2img = datetime.datetime.now()  # 开始时间
#
#     print("imagePath=" + imagePath)
#     pdfDoc = fitz.open(pdfPath)
#     for pg in range(pdfDoc.pageCount):
#         page = pdfDoc[pg]
#         rotate = int(0)
#         # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
#         # 此处若是不做设置，默认图片大小为：792X612, dpi=96
#         zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
#         zoom_y = 1.33333333
#         mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
#         pix = page.getPixmap(matrix=mat, alpha=False)
#
#         if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
#             os.makedirs(imagePath)  # 若图片文件夹不存在就创建
#
#         pix.writeJPG(imagePath + '/' + 'images_%s.jpg' % pg)  # 将图片写入指定的文件夹内
#
#     endTime_pdf2img = datetime.datetime.now()  # 结束时间
#     print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


# if __name__ == "-main-":
# 1、PDF地址
# pdfPath = 'D:\\Users\\Lenovo\\OneDrive\\桌面\\数模赛题\\赛题\\国赛\\A题.pdf'
#     # 2、需要储存图片的目录
# imagePath = 'D:\\Users\\Lenovo\\OneDrive\\桌面\\数'
# pyMuPDF_fitz(pdfPath, imagePath)
import numpy as np
from logic_regression import func

# fig, ax = plt.subplots()  # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# # plt.show()
# # Show the figure.
# a = np.linspace(1, 100, 100)
# print(a, np.shape(a))
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 1, 4]
# filename = r"D:\Users\Lenovo\OneDrive\文档\Tencent Files\2949794732\FileRecv\Stu.csv"
# data = np.loadtxt(open(filename), delimiter=",", skiprows=1, usecols=[0, 1, 5, 6, 9, 14, 19])
# data[:, -1] = np.floor(data[:, -1] / 70)
# train_data = data[:6000].T  # 训练集6000个
# test_data = data[6001:].T  # 测试集607个
#
# m = np.size(train_data, 1)
# a0 = train_data[:-1, :]
# # cost = np.zeros(loops)
#
#
#
# layer = [10, 7, 4, 1]
#
# argument = np.load("argument.npz")
#
# w1 = argument["w1"]  # , "w2", "w3", "w4", "b1", "b2", "b3", "b4"
# w2 = argument["w2"]
# w3 = argument["w3"]
# w4 = argument["w4"]
# b1 = argument["b1"]
# b2 = argument["b2"]
# b3 = argument["b3"]
# b4 = argument["b4"]
#
#
# z1, a1 = func.forward(a0, layer[0], w1, b1)
# z2, a2 = func.forward(a1, layer[1], w2, b2)
# z3, a3 = func.forward(a2, layer[2], w3, b3)
# z4, a4 = func.forward(a3, layer[3], w4, b4)
#
# cost = -1 * np.sum(train_data[-1, :] * np.log(a4) + (1 - train_data[-1, :]) * np.log(1 - a4))
#
# # w1,w2 = argument["w1"]
# print(cost)
# # plt.plot(x, y)
# # plt.annotate('标记点', xy=(2, 3), xytext=(3, 4), arrowprops=dict(arrowstyle='->'))
# plt.show()
import torch.nn as nn
import torch
import torch
import gc
import sys
import matplotlib.pyplot as plt
import math
from PIL import Image
import matplotlib.image as mg
import matplotlib.figure as fg
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader

sys.path.append("Image_Classfiation_Coil20_master")
path = "Image_Classfiation_Coil20_master/dataset"  # Image_Classfiation_Coil20_master/dataset
batch_size = 50

w1 = torch.rand((256, 256), dtype=torch.float32, requires_grad=True)
w2 = torch.rand((256, 20), dtype=torch.float32, requires_grad=True)
b1 = torch.rand((1, 256), dtype=torch.float32, requires_grad=True)
b2 = torch.rand((1, 20), dtype=torch.float32, requires_grad=True)


class IdataSet(Dataset):
    def __init__(self, img_path, transform=None):
        super().__init__()
        self.img_dir = img_path
        self.img_list = os.listdir(self.img_dir)
        self.transform = transform
        print(self.img_dir)

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, index):
        item = self.img_list[index]
        img_path = os.path.join(self.img_dir, item)
        image = Image.open(img_path)
        if item[4] == "_":

            image_label = torch.tensor(int(item[3:4]))
        else:
            image_label = torch.tensor(int(item[3:5]))
        if self.transform:
            image = self.transform(image)
        return image, image_label


transform = transforms.Compose([
    transforms.Resize((16, 16)),  # 将图像调整为 256x256 大小
    transforms.ToTensor(),  # 将图像转换为张量
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
])
# transforms.Compose
# transform = transforms.ToTensor()
img_dataset = IdataSet(path, transform)
train_data = DataLoader(img_dataset, batch_size, shuffle=True)  # 迭代器，不是列表？？？

a0_true, a1_true, a2_true, a3_true = 9.8, 1.3, 2.5, -0.56
x = torch.randn((100, 1), dtype=torch.float32)
x_feature = torch.cat(
    (x, x ** 2, x ** 3), 1
)
e = torch.tensor(np.random.normal(0, 0.01, (100, 1)))
labels = x_feature[:, 0] * a0_true + x_feature[:, 1] * a1_true + x_feature[:, 2] * a2_true + a0_true + e

w = torch.tensor(np.random.normal(0, 0.01, (3, 1)), requires_grad=True, dtype=torch.float32)
b = torch.zeros(1, 1, requires_grad=True, dtype=torch.float32)


def net(lr, x):
    y_hat = torch.matmul(x_feature, w) + b
    loss = ((y_hat - labels) ** 2).mean()

    if w.grad is not None:
        w.grad.zero_()
        b.grad.zero_()
    loss.backward()
    w.data -= lr * w.grad
    b.data -= lr * b.grad
    y_hat1 = torch.matmul(x_feature, w) + b
    x, y, lab = x.view(-1).detach().numpy(), y_hat1.view(-1).detach().numpy(), labels
    lab = labels.view(-1).detach().numpy()
    arg = np.argsort(x)
    # print(x[arg], y[arg])
    plt.plot(x[arg], lab[arg])
    plt.plot(x[arg], y[arg])

    plt.pause(0.5)


# print(w,b)

# for i in range(10):
#     net(0.5, x)
# plt.show()


# def net(x):
#     x = x.view((-1, 256))
#     h = torch.matmul(x, w1) + b1
#     h = h.relu()
#     return torch.matmul(h, w2) + b2
#
#
# loss = nn.CrossEntropyLoss()


# def optim(param):
#     for pa in param:
#         if pa.grad != None:
#             pa.grad.data.zero_()
#     cretrion.backward()
#     for pa in param:
#         pa.data += 0.001 * pa.grad


# for x, y in train_data:
#     i = 0
#
#     y_hat = net(x)
#     acc = (y_hat.argmax(dim=1) == y).sum()
#     cretrion = loss(y_hat, y - 1) / batch_size
#     optim([w1, w2, b1, b2])
#     print(cretrion.item(), 100 * acc / batch_size)
#
#     # trans = transforms.ToPILImage()
#     # image = trans(x[1])
#     # image.save("ran.jpg")
#     if i > 60:
#         break
#     i += 1
# 提取整理数据dataset
# def data(batch_size, path):
#     train = []
#     labels = []
#     test = []
#     imagedataset = os.listdir(path)
#     random.shuffle(list(imagedataset))
#     for i in range(batch_size):
#         image = Image.open(path + "/" + imagedataset[i])
#         transforms = torchvision.transforms.Compose(
#             [torchvision.transforms.Grayscale(num_output_channels=1),
#              torchvision.transforms.ToTensor()])
#         image_tensor = transforms(image)
#         print(image_tensor[0, 9, 9])
#         if imagedataset[i][4: 5] == "_":
#             label = int(imagedataset[i][3: 4])
#         else:
#             label = int(imagedataset[i][3: 5])
#         train.append(image_tensor)
#         labels.append(label)
#         print(train, labels)
#         yield torch.tensor(train).view((batch_size, -1)), torch.tensor(labels).view((batch_size, -1))
#
#
# train, labels = data(20, path)
# print(train[1][1][1],labels[1:4])

# f1 = plt.figure(figsize=(2, 2), dpi=300, facecolor=(0.48, 0.10, 0.90), edgecolor=(0.23, 0.34, 0.123))
# ax = f1.add_subplot((2, 2))
# ax1 = ax[1, 1]
# ax1
# plt.show()
#
# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)
#
# fig = plt.figure()

# ax1, ax2 = fig.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# fig.show()

import PIL.Image as Image
import os
import torch
import time
from torchvision import transforms
import torch.utils.data as Data
import torch.optim as optim
import torch.nn.init as init

# 底层模型对Image_Classfication_Coil20_master/dataset数据的20种128*128的单通道图像进行分类
path = "./Image_Classfiation_Coil20_master/dataset"


def dataset(path, image=False):  # 根据路径将图像信息数据化成tensor
    if not os.path.exists(path):
        raise FileNotFoundError(f"路径不存在: {path}")
    # os.chdir(path)
    feature, y = [], []
    for item in os.scandir(path):
        if ord('0') <= ord(item.name[4]) <= ord("9"):
            y.append(int(item.name[3:5]))
        else:
            y.append(int(item.name[3]))
        image_c = Image.open(path + "/" + item.name)
        transform = transforms.ToTensor()
        image_data = transform(image_c)
        feature.append(image_data)
    lengh = len(y)
    feature = torch.stack(feature)
    y = torch.tensor(y)
    if image:
        return feature, y.view(lengh, -1), lengh
    else:
        return feature.view(lengh, -1), y.view(lengh, -1), lengh


print(dataset(path, False)[:10])


# image=Image.open(path+"/"+"obj1__0.png")
# image_data=np.array(image)
# print(image_data.max(axis=1),image_data.min(axis=0))

# print(feature[20], y[20])
def dataloader(batch_size, path, image=False):
    feature, y, num_data = dataset(path, image)
    index = list(range(num_data))
    random.shuffle(index)
    x_batch, y_batch = [], []
    for i in range(num_data):
        x_batch.append(feature[index[i]])
        y_batch.append(y[index[i]])
        if i % batch_size == 0 and i > 0:
            yield torch.stack(x_batch), torch.stack(y_batch) - 1
            x_batch, y_batch = [], []
        if i == num_data:
            yield torch.stack(x_batch), torch.stack(y_batch) - 1
            x_batch, y_batch = [], []


FUCTION_BUTTOM = False
if FUCTION_BUTTOM == True:
    w = torch.randn(128 * 128, 20, requires_grad=True, dtype=torch.float)
    b = torch.randn(20, requires_grad=True, dtype=torch.float)
    for i in range(20):
        for x, y in dataloader(50, path):
            y_pre = torch.mm(x, w) + b
            # y -= 1
            y_exp = y_pre.tanh().exp()
            y_prob = y_exp / y_exp.sum(dim=1, keepdim=True)
            loss = -torch.log(y_prob.gather(dim=1, index=y.view(-1, 1))).sum()
            loss.backward(retain_graph=True)
            w.data -= 0.05 * w.grad
            b.data -= 0.05 * b.grad
            w.grad.zero_()
            b.grad.zero_()
            print("loss:", loss, "accuracy:", (y_prob.argmax(dim=1) == y).float().mean().item())


##感觉是原始数据的处理不够理想导致，准确率徘徊在0.05，暂告一段落本实验


# class LinearNet(nn.Module):
#     def __init__(self, feature):
#         super().__init__()
#         self.linear = nn.Linear(int(feature), out_features=20)
#         self.net2 = nn.CrossEntropyLoss()
#         self.net3 = nn.Dropout()
# 
#     def forward(self, features):
#         return self.net3(self.net2(self.linear(features)))

class SuNet(nn.Module):
    def __init__(self, **kwargs):
        super(SuNet, self).__init__(**kwargs)
        self.net = nn.Sequential(nn.Linear(128 * 128, 64)

                                 , nn.ReLU()
                                 , nn.Linear(64, 20)
                                 , nn.ReLU()
                                 )

    def forward(self, feature):
        return self.net(feature)


Su = nn.Sequential(nn.Linear(30, 15)
                   , nn.ReLU()
                   , nn.CrossEntropyLoss())
TEST = False
if TEST:
    su = SuNet().cuda()
    net = nn.ModuleList([Su, SuNet()])
    for feature, y in dataloader(80, path):
        start = time.time()
        y_ = su(feature.cuda())
        end = time.time()
        optimizer = optim.SGD(su.parameters(), lr=0.1)
        loss = nn.CrossEntropyLoss()
        # print(y_,y.cuda())
        i = loss(y_, y.cuda().squeeze())
        i.backward()
        optimizer.step()  # ， "accuracy:", (y_.argmax(dim=1) == y.cuda()).float().mean().item()
        print("loss:", i, "time:", end - start)


# weight=list(net[0].named_parameters())[0]0.004
# print(weight,len(weight))
def init_weight(tensor):
    with torch.no_grad():
        tensor.uniform_(-5, 5)
        tensor *= (tensor >= 0).float()


class Layer(nn.Module):
    def __init__(self):
        super().__init__()
        self.param = nn.ParameterList([torch.rand(4, 4) for i in range(4)])


# net = nn.Conv2d(1, 1, 5, 1, 1)


# x = torch.rand(2, 3)
# print(x)
# y = torch.squeeze(torch.stack([x, x + 1], 0), 0)
# print(y)


class Conv(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(nn.Conv2d(1, 3, 5, 1, 2)
                                    , nn.MaxPool2d(4, 4)
                                    # , nn.ReLU()
                                    , nn.Conv2d(3, 6, 3, 1, 1)
                                    , nn.MaxPool2d(2, 2)
                                    , nn.ReLU())

        self.block2 = nn.Sequential(nn.Linear(16 * 16 * 6, 128)
                                    , nn.ReLU()
                                    , nn.Linear(128, 20))

    def forward(self, feature):
        feature = self.block1(feature)
        return self.block2(feature.view(feature.shape[0], -1))


class Inception(nn.Module):  # GoogleNet的核心块
    def __init__(self, in_c, c1, c2, c3, c4):
        super().__init__()
        self.c1 = nn.Conv2d(in_c, c1, kernel_size=1)
        self.c2 = nn.Sequential(nn.Conv2d(in_c, c2[0], kernel_size=1)
                                , nn.ReLU()
                                , nn.Conv2d(c2[0], c2[1], kernel_size=3, padding=1)
                                )
        self.c3 = nn.Sequential(nn.Conv2d(in_c, c3[0], kernel_size=1)
                                , nn.ReLU()
                                , nn.Conv2d(c3[0], c3[1], kernel_size=5, padding=2))
        self.c4 = nn.Sequential(nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
                                nn.ReLU(),
                                nn.Conv2d(in_c, c4, kernel_size=1))

    def forward(self, x):
        c1 = self.c1(x)
        c2 = self.c2(x)
        c3 = self.c3(x)
        c4 = self.c4(x)
        return torch.cat([c1, c2, c3, c4], dim=1)


# Inc=Inception(2,4,(2,4),(4,6),4)
# x=torch.rand(1,2,8,8)
# y=Inc(x)
# print("x",x, "y",y.size())
TEST1 = False
if TEST1:
    su = Conv().cuda()
    # net = nn.ModuleList([Su, SuNet()])
    for feature, y in dataloader(80, path, True):
        for j in range(20):
            start = time.time()
            y_ = su(feature.cuda())
            end = time.time()
            optimizer = optim.SGD(su.parameters(), lr=0.1)
            loss = nn.CrossEntropyLoss()
            # print(y_,y.cuda())
            i = loss(y_, y.cuda().squeeze())
            optimizer.zero_grad()
            i.backward()
            optimizer.step()
            # print(y_.argmax(dim=1),y)
            print(f"loss:, {i.item():.4f}",
                  f"accuracy:, {(y_.argmax(dim=1).view(y.size()) == y.cuda()).float().mean().item():.4f}",
                  f"time:, {end - start:.4f}")
# 卷积网络+全连接网络,LeNet型，准确率爆表。之前可能是里面的relu（）函数有些问题，另外accuracy的计算要size一致

x = torch.tensor([[1, 2, 3], [10, 20, 30]], requires_grad=True, dtype=torch.float)

y = torch.tensor([[0, 0], [1, 1]])
# print(x, y.unsqueeze(dim=0), y)
z = torch.gather(x, dim=1, index=y)
z1 = torch.index_select(x, dim=1, index=torch.tensor([1, 0]))
z2 = x.sum()
z2.backward(retain_graph=True)
# print(x.grad)
x.data += 1
x.grad.zero_()
z2.backward()
# print(x.grad)
import torch.utils.data as Data
import torch.nn

# dataset = Data.TensorDataset(x, y[:, 0])
# data = Data.DataLoader(dataset, batch_size=1, shuffle=True)
# model = nn.Sequential(
#     nn.Linear(x.size(1), 1)
# )
# model.add_module("test", nn.Linear(1, 1))
# model.parameters()
# for params in model.parameters():  # 所有的单个参数元素堆叠，无法区分weight与bias
#
#     print(params)
from torch.nn import init


# init.normal_(model[0].weight, 0, 0.01)
# init.constant_(model[0].bias, 8)
# print(x, x.gather(0, torch.tensor([[1, 1], [0, 0]])))
# # print(x.view(3,-1), z1)
#
# torch.tensor(np.random.normal(0, 0.01, (3, 3)), dtype=torch.float)


class Model1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(4, 6)
        self.layer2 = nn.ReLU()
        self.layer3 = nn.Sequential(
            nn.Linear(6, 10),
            nn.Sigmoid()
        )

    def forward(self, x):
        y = self.layer1(x)
        y = self.layer2(y)
        y = self.layer3(y)
        return y


from torch.nn import init
import torch.optim as optim

# for x, y in dataloader(20, path):
#     print(x, y)
#     break
# init.normal_(net[1].weight, 0, 0.01)
# init.constant_(net[1].bias, 8)
loss = nn.CrossEntropyLoss()


# loss(y,net(x))

class drop(nn.Module):
    def __init__(self, prob):
        super().__init__()
        self.prob = prob

    def forward(self, x):
        matprob = torch.rand(x.size())
        matprob = (matprob > self.prob).float()

        return x * matprob / (1 - self.prob)


temp = nn.Sequential(nn.Linear(128 * 128, 40),
                     drop(0.05),
                     nn.ReLU(),

                     nn.Linear(40, 20))
optimizer = optim.SGD(temp.parameters(), lr=0.01)
epochs = 4
for i in range(1, epochs + 1):
    for x, y in dataloader(50, path):
        # print(x,y)
        output = temp(x)
        # print(output, y.view(-1, 1))
        l = loss(output, y.view(-1, 1).squeeze())

        optimizer.zero_grad()
        l.backward()
        optimizer.step()
        print(l.item())



# a=True
# b=1
# if a==True:
#     b=12
# print(b)
# x=torch.tensor([[[1,3,5],[12,43,12],[42,12,54]],[[0,1,2],[321,23,45],[21,43,45]]])
# print(x.view(2,-1))
# torch.cuda.is_available()
# torch.ones_like(x,dtype=torch.float,device="cpu", requires_grad=True)
# x.to("cuda")
# x.grad,b.backward()
# x = torch.rand(2, 3, device='cpu', dtype=torch.float32)
# print(id(x))
# x = x.to("cuda")

# x=torch.rand(2,3,8,8)
# y=x.mean(dim=1,keepdim=True)
# print(x,y)

# weight = torch.tensor([1, 2],dtype=torch.float, requires_grad=True).view(2, 1)
# bias = torch.tensor([0.5],dtype=torch.float, requires_grad=True)
#
# x = torch.tensor([[1, 2], [3, 4]],dtype=torch.float)
# x_ = torch.mm(x, weight) + bias
# mean = x_.mean()
# x_ -= mean
# loss = x_.sum()
# loss.backward()
# print(weight.grad, bias.grad)

# 可训练参数
# weight = torch.nn.Parameter(torch.tensor([1.0, 2.0]))
# bias = torch.nn.Parameter(torch.tensor([0.5]))
# # 检查梯度
# print("weight梯度:", weight.grad)  # 输出: tensor([-2., -2.])
# print("bias梯度:", bias.grad)    # 输出: tensor([-2.])
# # 输入数据
# inputs = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
#
# # 前向计算（依赖训练参数）
# x = inputs @ weight + bias  # [1*1+2*2+0.5=5.5, 3*1+4*2+0.5=11.5]
#
# # 计算均值（统计操作）
#
# mean = x.mean()  # (5.5 + 11.5)/2 = 8.5
#
# # 归一化操作
# x_norm = x - mean  # [5.5-8.5=-3, 11.5-8.5=3]
#
# # 后续计算
# loss = x_norm.sum()  # -3 + 3 = 0
#
# # 反向传播
# loss.backward()
#
# # 检查梯度
# print("weight梯度:", weight.grad)  # 输出: tensor([-2., -2.])
# print("bias梯度:", bias.grad)    # 输出: tensor([-2.])
# print(id(x))
# for name, param in net.named_parameters():
#     if 'weight' in name:
#         init_weight(param)
#     print(param)
# print(torch.cuda.is_available())
# amount = torch.cuda.device_count()
# print(amount)
# print(torch.cuda.get_device_name(0))

# torch.save(init_weight(torch.rand(2)), "./init_weight.pt")
# net = LinearNet(10)
# loss = nn.CrossEntropyLoss()
# 
# optimizer = torch.optim.SGD(net.parameters())
# 
# n_train, n_test, n_input = 100, 20, 200
# w = torch.ones(n_input, 1) * 0.01
# b = torch.tensor([0.05])
# 
# feature = torch.tensor(np.random.normal(0, 0.01, size=(n_train + n_test, n_input)), dtype=torch.float)
# labels = torch.mm(feature, w) + b
# labels += torch.tensor(np.random.normal(scale=0.01, size=labels.size()), dtype=torch.float)

# net = nn.Sequential(nn.Linear(int(x_feature), 4),
#                     nn.Linear(4, 9))
# init.normal_(net[0].weight,)
# net.add_module("linear", nn.Linear(9, 8))
# optimizer = optim.SGD(net.parameters(), lr=0.09)
# data = Data.TensorDataset(x_feature, labels)
# data_batch = Data.DataLoader(data, batch_size=12, shuffle=True)
# x = torch.tensor([1, 9])
# # x = torch.ones(2, 2, requires_grad=True)
# w = torch.rand(x_feature, requires_grad=True)
# lr = random
# for x, y in data_batch:  # 底层运算模型
#     loss = torch.sum(torch.mm(x, w) + b - y)
#     loss.backward()
#     w.data -= lr * w.grad
#     w.grad.data.zero_()

# y = torch.sum(x ** 2)
# x.data += 1
# y.backward(retain_graph=True)
# print(x.grad)  # [4,4[4,4]
# x.grad.data.zero_()
# y.backward(retain_graph=True)
# print(x.grad)  # [4,4[4,4]
# x.grad.data.zero_()
# z = torch.autograd.grad(y, x, create_graph=True)[0]  # z=dy/dx [2,2[2,2]
# w = torch.autograd.grad(z[0, 0], x, create_graph=True)[0]#对于z[0,0]=dy/dx的二阶导
# # z.backward()
# print(w)
# y.backward()
# print(x, x.grad)

# def add1(a: int, c=9, *args, k, **kwargs) -> int:
#     print(args[1], k)
#     return a + c
# device = torch.device("cuda")
# x.to(device)

# def test(a, c=9):
#     c += 1
#     print(a, c)
#     return a

# def ease(a=[], c=90):
#     a.append('gu')
#     c -= 1
# print(x.grad_fn, "last function")

# a1 = [4, 90, 'hjh']
# print(f'a1={a1}')
# ease(a1)
# print(f'a1={a1}')
#
# result = torch.randn(5, 3,9)
# re=result[1,1,:]*100
# print(re)
# re1=torch.index_select(result,dim=1,index=torch.tensor([0,1]))
# print(result,re1)
# # test(1)
# test(1)
# test(1)
# print(add1(1,2, "ha", "hj",k=7))

# input = torch.tensor([[10, 11, 12],
#                       [20, 21, 22],
#                       [30, 31, 32]])
# index = torch.tensor([[0, 1, 1],
#                       [2, 0, 0]])
# output = torch.gather(input, dim=0, index=index)
# print(output)
# input = torch.tensor([[1, 2, 3],
#                       [4, 5, 6],
#                       [10, 11, 12]])
# index = torch.tensor([[1, 0],
#                       [0, 2]])
# output = torch.gather(input, dim=1, index=index)
# print(output)
#
# k = filter(lambda x: x[0] >= 7, [(90, 62), (1, 4), (23, 13), (2, 89)])

# print(list(k))

import numpy as np
import matplotlib.pyplot as plt

# 创建图形和坐标轴kljk
# fig, ax = plt.subplots()
# x = np.linspace(0, 2 * np.pi, 100)
# line, = ax.plot(x, np.sin(x))  # 初始绘制一条正弦曲线
# ax.set_ylim(-1.5, 1.5)  # 设置 y 轴范围


# 动态更新函数
# def update(frame):
#     y = np.sin(x + frame / 10.0)  # 更新 y 值
#     line.set_ydata(y)  # 更新曲线数据
#     # print(y)
#     return line

# # 动态显示
# for frame in range(100):  # 循环 100 帧
#     update(frame)  # 更新图形
#     plt.pause(0.01)  # 暂停 0.01 秒，更新图形窗口


# plt.show()  # 保持窗口悬停

# input("等待窗口中")


# def display(path: str, num):
#     List = os.listdir(path)
#     list_num = list(range(len(List)))
#     random.shuffle(list_num)
#     List = [List[i] for i in list_num]
#     width = math.ceil(num // 5)

#     fig, axes = plt.subplots(3, 5, figsize=(12, 12))
#     disp = axes.flatten()
#     for f, j in zip(disp, list_num):
#         # print(List[j])
#         img = mg.imread(os.path.join(path, List[j]))
#         # img.show()
#         f.plot(img)
#     plt.show()


# display(path, 10)


# import torch.nn as nn
# from matplotlib import pyplot as plt
# from tqdm import tqdm
# from transformers import logging

# from Image_Classfiation_Coil20_master.config import get_config
# from Image_Classfiation_Coil20_master.data import load_dataset
# from Image_Classfiation_Coil20_master.model import AlexNet, LeNet, GoogleNet, VGG16, ResNet50, EfficientNet
# import logic_regression.func
# dx=torch.tensor(1)
# torch.cuda.synchronize()  # 同步CPU与GPU的计算进程
# ####逻辑回归，简单地学习一次
# x = torch.randint(-10, 10, (50, 3))
# w = torch.rand(3, 1, dtype=torch.float32, requires_grad=True)
# b = torch.rand(1, dtype=torch.float32, requires_grad=True)
# y = torch.randint(-10, 10, (50, 1))
# loss = torch.sum((torch.matmul(x.float(), w) + b - y) ** 2)


#
# print(loss)
# for i in range(20):
#
#     loss.backward()
#
#     w.data-=0.001*w.grad
#     w.grad.data.zero_()
#     b.data-=0.001*b.grad
#     b.grad.data.zero_()
#     loss=torch.sum((torch.matmul(x.float(),w)+b-y)**2)/50
#     print(loss)
# class LinearNet(nn.Module):
#     def _int_(self, feature):
#         super(LinearNet, self)._int_()
#         self.linear = nn.Linear(feature, 1)


# print(nn.Linear.parameters)


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# c = ListNode(3)
# print('output_1:{}'.format(c.val))
# a = ListNode
# a.val = 1
# print('output_2:{}'.format(a))
# print('output_3:{}'.format(c.val))

# gc.collect()
# print(torch.cuda.memory_allocated())
# x = torch.ones(1, device="cuda", requires_grad=True)
# print(x.shape)
# print(torch.cuda.memory_allocated())
# y = x ** 2
# torch.autograd.
# print(torch.cuda.memory_allocated())
# print(torch.autograd.grad(outputs=y,inputs=x, create_graph=True)[0])
# dx = torch.autograd.grad(outputs=y, inputs=x, create_graph=True)
# y.backward(retain_graph=True)  # create_graph=True
# print(x.grad, torch.cuda.memory_allocated())
# del x, y
# print(torch.cuda.memory_allocated())
# print(y)  # ,retain_graph=True,create_graph=True
# print(x.grad, dx)
# y.backward(retain_graph=True)
# x.grad.data.zero_()
# print(x.grad)
# x.grad = None
# x.data += 10
# y.backward()
# print(x.requires_grad)
# y.backward()
# print(x.grad)

# y = x.uniform_(20, 40)
# z1 = torch.rand(16, dtype=torch.float32)
# z2=torch.rand(16,dtype=torch.float32)
# z4=np.arange(1,17)
# # print(x)
# z3=z1.numpy()
# z3+=1
# z5=torch.tensor(z4)
# z5+=1
# # print(z4,z5)//
# # print(torch.__version__)
# y = x.reshape(1, 16)
# print(x)
# y += 1
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     print("cuda is working")
#     x = torch.rand(4, 4, dtype=torch.float32)
#     print(id(x))
#     x = x.to("cuda")
#     print(id(x))

# print(z1.dot(z2))
# print(x)
# print(y, sum(y) / y.shape[0])
# print(torch.nonzero(y))
# logging.set_verbosity_error()
# args, logger = get_config()

# nb = Niubility(args, logger)
#
# loss_func = nn.CrossEntropyLoss(reduction="mean")
#
# pre = torch.tensor([0.4, 0.6], dtype=torch.float)
# tgt = torch.tensor([1, 0], dtype=torch.float)
#
# log_softmax = nn.LogSoftmax(dim=1)
# loss_fn = nn.NLLLoss()
# # input to NLLLoss is of size N x C = 3 x 5
# input = torch.randn(3, 5, requires_grad=True)
# # each element in target must have 0 <= value < C
# target = torch.tensor([1, 0, 4])
# loss = loss_fn(log_softmax(input), target)
# print(loss_fn(input, target))
# loss.backward()
#
# print(loss.grad)
#
# # print(loss.backward())
# # print(loss_fn(input, target))
#
# # 2D loss example (used, for example, with image inputs)
# N, C = 5, 4
# loss_fn = nn.NLLLoss()
# data = torch.randn(N, 16, 10, 10)
# conv = nn.Conv2d(16, C, (3, 3))
# log_softmax = nn.LogSoftmax(dim=1)
# # output of conv forward is of shape [N, C, 8, 8]
# output = log_softmax(conv(data))
# # each element in target must have 0 <= value < C
# target = torch.empty(N, 8, 8, dtype=torch.long).random_(0, C)
# # input to NLLLoss is of size N x C x height (8) x width (8)
# loss = loss_fn(output, target)
# loss.backward()
