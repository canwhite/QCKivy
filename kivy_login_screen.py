from kivy.app import App
from kivy.uix.gridlayout import GridLayout #导入网格布局
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):#把网格布局作为基类制作根控件
    
    def __init__(self, **kwargs):
        
        #加super，用现有的初始化方法，覆盖掉继承来的旧初始化方法
        super(LoginScreen,self).__init__(**kwargs)
        
        '''username'''
        self.cols = 2 #设置布局为两列
        self.add_widget(Label(text = "User Name"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        
        '''password'''
        
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True,multiline = False)
        self.add_widget(self.password)
        


class MyApp(App):
    
    def build(self):
        return LoginScreen()
        

if __name__ == '__main__':
    
    MyApp().run()
    
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
    




