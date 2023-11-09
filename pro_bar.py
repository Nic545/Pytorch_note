import math
class progress_bar():
    def __init__(self,
                 total,                 #一共要遍历的步数
                 length = 50,           #期望的进度条的长度
                 left_bar = '|',        #左侧的括号
                 right_bar ='|',        #右侧的括号
                 forward = '■',         #代表已经完成的字符
                 undone = ' ',          #代表未完成的字符
                 percent = True,       #是否显示百分比
                 round_num = 2):        #显示百分比的小数位数
        self.total = int(math.floor(total))
        self.length = length
        self.lb = left_bar
        self.rb = right_bar
        self.f = forward
        self.u = undone
        self.persent = percent
        self.round = round_num

    def show(self,step):
        # by = int(self.total / self.length)

        if self.persent:
            print('\r' +
                self.lb +
                self.f * int(float(step / self.total) * self.length) +
                self.u * (self.length - int(float(step / self.total) * self.length)) +
                self.rb +
                ' ' +
                str(round(((step / self.total) * 100),self.round)) +
                '%',
                end = '')    
        else:
            print('\r' +
                self.lb +
                self.f * (int(step / self.total) * self.length) +
                self.u * (self.length - (int(step / self.total) * self.length)) +
                self.rb,
                end = '')