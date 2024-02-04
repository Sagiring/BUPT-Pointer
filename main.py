from typing import Optional
from pointer.login_ui import Ui_login
from pointer.pointer_ui import Ui_Pointer
from pointer.pointer import (PingJwgl,loginJwgl,getClassPoint)
from PySide6.QtWidgets import (QApplication,QTableWidgetItem)
from PySide6.QtCore  import (Qt,QObject,QThread,Signal)
from qfluentwidgets import (FluentWindow,InfoBar,StateToolTip,InfoBarPosition)
import sys
import time
import os


class loginUI(FluentWindow,Ui_login):
    userData = Signal(list)
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setupThread()
        self.loginPushButton.clicked.connect(self.login)
        if os.path.exists('./pointer/cache'):
            with open('./pointer/cache','r',encoding='utf-8') as f:
                AccPw = f.read()
            AccPw = AccPw.split('\n%%%\n')
            self.accountInput.setText(AccPw[0])
            if len(AccPw) == 2:
               self.passwdInput.setText(AccPw[1])
               self.CheckBox.setChecked(True)
            self.isLogining = False
    def setupThread(self):
        self.QThreading = QThread(self)  #创建Qthread
        self.workThread = loginWorkThread() #示例化 占时的线程 
        self.workThread.moveToThread(self.QThreading) #移入到Qthread中
        self.workThread.isPingJwgl.connect(self.recvPingjwgl)
        self.workThread.isLoginJwgl.connect(self.recvloginJwgl)
        self.userData.connect(self.workThread.loginJwgl)
        

    def recvPingjwgl(self,isPingJwgl):
        self.StateToolTip.setContent('测试教务连接中')
        if not isPingJwgl:
            self.showInfoBarFail('无法连接到教务系统，请检查网络')
            self.isLogining = False
            self.StateToolTip.close()
        else:
            self.StateToolTip.setContent('尝试登录中')
            if self.account == '' or self.passwd == '':
                self.showInfoBarFail('账号或密码为空')
                self.isLogining = False
                self.StateToolTip.close()
            else:
                self.userData.emit([self.account,self.passwd])


    def recvloginJwgl(self,isLoginJwgl):
        loginSession = isLoginJwgl[0]
        accountName = isLoginJwgl[1]
        if loginSession:
                self.StateToolTip.setContent('登录成功，正在转入')
                self.StateToolTip.setState(True)
                self.loginSession = loginSession
                self.accountName = accountName
                time.sleep(1)
                self.PointerWidget = Pointer(self.loginSession,self.accountName,self.account)
                self.PointerWidget.show()
                if not os.path.exists('./pointer'):
                    os.makedirs('./pointer')
                with open('./pointer/cache','w',encoding='utf-8') as f:
                    if self.CheckBox.isChecked():
                        f.write(self.account+'\n%%%\n'+self.passwd)
                    else:
                        f.write(self.account)
                self.QThreading.exit()
                self.close()
        else:
            self.showInfoBarFail('无法登录教务，请检查账号密码')
            self.isLogining = False
            self.StateToolTip.close()

    def login(self):
        self.account = self.accountInput.text()
        self.passwd = self.passwdInput.text()
        if not self.isLogining:
            self.isLogining = True
            self.StateToolTip = StateToolTip("Processing","尝试登录中",self)
            self.StateToolTip.move(20,30)
            self.StateToolTip.show()
            self.QThreading.start()
            self.workThread.pingJwgl() 
        else:
            InfoBar.info(
            title='!!!',
            content='登录中请稍后',
            position=InfoBarPosition.TOP_LEFT,
            isClosable=False,
            parent=self,
            orient= Qt.Horizontal,
            duration=3000
        )

    def showInfoBarFail(self,msg):
        InfoBar.error(
            title='Fail!',
            content=msg,
            position=InfoBarPosition.TOP_LEFT,
            isClosable=False,
            parent=self,
            orient= Qt.Horizontal,
            duration=3000
        )

class loginWorkThread(QObject):
    isPingJwgl = Signal(bool)
    isLoginJwgl = Signal(list)
    def __init__(self) -> None:
            super().__init__()
    
    def pingJwgl(self):
        if PingJwgl():
            self.isPingJwgl.emit(True)
        else:
            self.isPingJwgl.emit(False)

    def loginJwgl(self,userData):
        loginSession,accountName = loginJwgl(userData[0],userData[1])
        self.isLoginJwgl.emit([loginSession,accountName])




class Pointer(FluentWindow,Ui_Pointer):
    SearchData = Signal(list)
    def __init__(self,loginSession,accountName,account) -> None:
        super().__init__()
        self.setupUi(self)
        self.setupThread()
        self.loginSession = loginSession
        self.accountName = accountName
        self.account = account
        self.Account.setText(self.account + '-' +  self.accountName)
        time_list = []
        for i in range(10):
            time_list.append(str(2026-i-1)+'-'+str(2026-i)+'-2')
            time_list.append(str(2026-i-1)+'-'+str(2026-i)+'-1')
          
        self.ComboBox.addItems(time_list)
        self.ComboBox.setCurrentIndex(-1)
        self.TableWidget.setBorderVisible(True)
        self.TableWidget.setBorderRadius(8)
        self.TableWidget.setWordWrap(False)
        self.TableWidget.setRowCount(0)
        self.TableWidget.setColumnCount(7)
        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setHorizontalHeaderLabels(['科目', '学分', '期末', '期中', '平时','实验','总分'])
        self.PrimaryPushButton.clicked.connect(self.startSearch)
        self.Searching = False
 
    def setupThread(self):
        self.QThreading = QThread(self)  #创建Qthread
        self.workThread = SearchWorkThread() #示例化 占时的线程 
        self.workThread.moveToThread(self.QThreading) #移入到Qthread中
        self.workThread.send_classesDic.connect(self.setTableWidget) #绑定信号量到更新表格中 传递参数
        self.SearchData.connect(self.workThread.getPoints) #绑定信号量到 占时的线程 传递参数



    def startSearch(self):
        if self.ComboBox.text():
            if not self.Searching:
                self.Searching = True
                self.StateToolTip = StateToolTip("Processing","获取数据中",self)
                self.StateToolTip.move(625,640)
                self.StateToolTip.show()
                self.QThreading.start()
                self.SearchData.emit([self.loginSession,self.account,self.ComboBox.text()])
            else:
                InfoBar.info(
                title='!!!',
                content='查询中请稍后',
                position=InfoBarPosition.TOP_LEFT,
                isClosable=False,
                parent=self,
                orient= Qt.Horizontal,
                duration=3000
            )
        else:
            self.showInfoBarFail('请先选择学期')

    def setTableWidget(self,tableLists):
        self.TableWidget.setRowCount(len(tableLists))
        for i, row in enumerate(tableLists):
            for j in range(len(row)):
                self.TableWidget.setItem(i, j, QTableWidgetItem(row[j]))
        self.TableWidget.resizeColumnsToContents()
        self.StateToolTip.setContent('获取完成')
        self.StateToolTip.setState(True)
        self.StateToolTip = None
        self.Searching = False
        self.QThreading.exit()
        

    def showInfoBarFail(self,msg):
        InfoBar.error(
            title='Fail!',
            content=msg,
            position=InfoBarPosition.TOP_LEFT,
            isClosable=False,
            parent=self,
            orient= Qt.Horizontal,
            duration=3000
        )

class SearchWorkThread(QObject):
        send_classesDic = Signal(list)
        def __init__(self) -> None:
            super().__init__()

        def getPoints(self,SearchData):
            tableLists = []
            # classesDic =  getClassPoint(self.loginSession,self.account,self.ComboBox.text())
            classesDic =  getClassPoint(SearchData[0],SearchData[1],SearchData[2])
            for classID in classesDic.keys():
                try:
                    sumScore = float(classesDic[classID][2][0]) * int(classesDic[classID][2][1].replace('%',''))/100
                    sumScore += float(classesDic[classID][2][2]) * int(classesDic[classID][2][3].replace('%',''))/100
                    sumScore += float(classesDic[classID][2][4]) * int(classesDic[classID][2][5].replace('%',''))/100
                    sumScore += float(classesDic[classID][2][6]) * int(classesDic[classID][2][7].replace('%',''))/100
                    sumScore = str(round(sumScore,2))
                except ValueError:
                    sumScore = 'Error'
                tableLists.append([classesDic[classID][0],
                            classesDic[classID][1],
                            classesDic[classID][2][0]+'*'+classesDic[classID][2][1],
                            classesDic[classID][2][2]+'*'+classesDic[classID][2][3],
                            classesDic[classID][2][4]+'*'+classesDic[classID][2][5],
                            classesDic[classID][2][6]+'*'+classesDic[classID][2][7],
                            sumScore])
            self.send_classesDic.emit(tableLists)

def main():
    
    app = QApplication(sys.argv)
    loginWidget = loginUI()
    loginWidget.show()
    app.exec()

main()
