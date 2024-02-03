from pointer.login_ui import Ui_login
from pointer.pointer_ui import Ui_Pointer
from pointer.pointer import (PingJwgl,loginJwgl,getClassPoint)
from PySide6.QtWidgets import (QApplication,QTableWidgetItem)
from PySide6.QtCore  import (Qt)
from qfluentwidgets import (FluentWindow,InfoBar,StateToolTip,InfoBarPosition)
import sys
import time
import os

class loginUI(FluentWindow,Ui_login):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.login)
        if os.path.exists('./pointer/cache'):
            with open('./pointer/cache','r',encoding='utf-8') as f:
                AccPw = f.read()
            AccPw = AccPw.split('\n%%%\n')
            self.account.setText(AccPw[0])
            if len(AccPw) == 2:
               self.passwd.setText(AccPw[1])
               self.CheckBox.setChecked(True)

    def login(self):
        
        account = self.account.text()
        passwd = self.passwd.text()
        if PingJwgl():
            if account == '' or passwd == '':
                self.showInfoBarFail('账号或密码为空')
            else:
                loginSession,accountName = loginJwgl(account,passwd)
                if loginSession:
                    self.loginSession = loginSession
                    self.accountName = accountName
                    self.account = account
                    time.sleep(2)    
                    self.PointerWidget = Pointer(self)
                    self.PointerWidget.show()
                    if not os.path.exists('./pointer'):
                        os.makedirs('./pointer')
                    with open('./pointer/cache','w',encoding='utf-8') as f:
                        if self.CheckBox.isChecked():
                            f.write(account+'\n%%%\n'+passwd)
                        else:
                            f.write(account)
                    self.close()
                else:
                    self.showInfoBarFail('无法登录教务，请检查账号密码')
        else:
            self.showInfoBarFail('无法连接到教务系统，请检查网络')

    def showInfoBarFail(self,msg):
        InfoBar.error(
            title='Fail!',
            content=msg,
            position=InfoBarPosition.TOP_LEFT,
            isClosable=False,
            parent=self,
            orient= Qt.Horizontal
        )

  

class Pointer(FluentWindow,Ui_Pointer):
    def __init__(self,loginWidget) -> None:
        super().__init__()
        self.setupUi(self)
        self.loginSession = loginWidget.loginSession
        self.accountName = loginWidget.accountName
        self.account = loginWidget.account
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
        self.TableWidget.setColumnCount(6)
        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setHorizontalHeaderLabels(['科目', '学分', '期末', '期中', '平时','实验'])
        self.TableWidget.sizeAdjustPolicy()
        self.PrimaryPushButton.clicked.connect(self.getPoints)
 

    def getPoints(self):
        tableLists = []
        self.StateToolTip = StateToolTip("Processing","获取数据中",self.PrimaryPushButton)



        classesDic =  getClassPoint(self.loginSession,self.account,self.ComboBox.text())
        # print(classesDic)
        for classID in classesDic.keys():
            tableLists.append([classesDic[classID][0],
                         classesDic[classID][1],
                         classesDic[classID][2][0]+'*'+classesDic[classID][2][1],
                         classesDic[classID][2][2]+'*'+classesDic[classID][2][3],
                         classesDic[classID][2][4]+'*'+classesDic[classID][2][5],
                         classesDic[classID][2][6]+'*'+classesDic[classID][2][7]])
        self.TableWidget.setRowCount(len(tableLists))
        for i, row in enumerate(tableLists):
            for j in range(6):
                self.TableWidget.setItem(i, j, QTableWidgetItem(row[j]))
        self.TableWidget.resizeColumnsToContents()
        self.StateToolTip
    
    def showSuccessInfoBar(self):
        InfoBar.success(
            title='Success!',
            content='已登录，正在跳转',
            position=InfoBarPosition.TOP_LEFT,
            isClosable=False,
            parent=self,
            orient= Qt.Horizontal
        )


def main():
    
    app = QApplication(sys.argv)
    loginWidget = loginUI()
    loginWidget.show()
    app.exec()

main()
