'''
1.基于App类创建一个子类
2.把build()方法实现为返回一个控件实例，这个空间的实例也就是你整个应用的根控件
3.创建一个这个类的实例，然后调用run方法

'''


import kivy
kivy.require('1.10.1') # 注意要把这个版本号改变成你现有的Kivy版本号!

from kivy.app import App # 译者注：这里就是从kivy.app包里面导入App类
from kivy.uix.label import Label # 译者注：这里是从kivy.uix.label包中导入Label控件，这里都注意开头字母要大写

class MyApp(App):

    def build(self): # 译者注：这里是实现build()方法
        return Label(text='Hello world') # 译者注：在这个方法里面使用了Label控件

if __name__ == '__main__':
    MyApp().run() # 译者注：这里就是运行了。