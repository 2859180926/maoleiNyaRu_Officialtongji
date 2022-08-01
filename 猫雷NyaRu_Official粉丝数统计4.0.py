from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

import requests as req

from time import strftime, localtime

class States():
    def __init__(self):
        self.window = QMainWindow()#应用窗口
        self.window.resize(350, 250)
        self.window.move(1000, 400)
        self.window.setWindowTitle('猫雷B站粉丝查询')

        '''self.textEdit = QPlainTextEdit(window)
        self.textEdit.setPlaceholderText("请输入UID")
        self.textEdit.move(10,25)
        self.textEdit.resize(300,350)'''

        self.button = QPushButton('查询', self.window)
        self.button.move(200,80)
        self.button.clicked.connect(self.zuizhong)

        #window.setWindowIcon(QIcon("a6rgr-o35am-001.ico"))

    def fans(self,mid, name=-1):
        mid = str(mid)
        name = str(name)
        if name == -1:
            name = mid
        url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
        resp = req.get(url)  # 通过url爬取到我们想要的json数据
        info = eval(resp.text)
        print_content = strftime("%Y", localtime()) + "年" + strftime("%m", localtime()) + "月" + strftime("%d",
                                                                                                         localtime()) + "日" + strftime(
            "%H:%M:%S", localtime()) + "\n" + name + "粉丝数\n" + "本次查询：" + str(
            info['data']['follower'])
        """with open(name + '粉丝数统计.csv', 'a+', newline="") as f:
            f.seek(0)
            reader = [i for i in csv.reader(f)]
            datas = [i[3] for i in reader]
            f.seek(2)
            csv_write = csv.writer(f, dialect='excel')

            csv_write.writerow(["猫雷粉丝", strftime("%m", localtime()) + "月" + strftime("%d", localtime()) + "日"
                                + strftime("%H:%M:%S", localtime()), strftime("%H:%M:%S", localtime()),
                                str(info['data']['follower']), str(int(info['data']['follower']) - int(datas[-1]))])"""
        # 获取data中的follower就是粉丝数啦
        # print(datas)
        # print(print_content)
        # print("上次查询：" + str(datas[-1]))
        # print("涨粉数：" + str(int(info['data']['follower']) - int(datas[-1])))
        return print_content

    def zuizhong(self):
        follower = self.fans(697091119, '猫雷NyaRu_Official')
        # fans_chart("猫雷NyaRu_Official粉丝数统计.csv")
        QMessageBox.about(self.window,
                          '猫雷NyaRu_Official粉丝数统计结果',
                          str(follower)
                          )

app = QApplication([])
stats = States()
stats.window.show()
app.exec_()