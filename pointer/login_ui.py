# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CaptionLabel, CheckBox, LineEdit, PasswordLineEdit,
    PrimaryPushButton, PushButton, TitleLabel)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1117, 612)
        login.setMinimumSize(QSize(1117, 612))
        login.setMaximumSize(QSize(1117, 612))
        self.loginPushButton = PrimaryPushButton(login)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(900, 490, 153, 32))
        self.loginPushButton.setMinimumSize(QSize(153, 32))
        self.loginPushButton.setMaximumSize(QSize(153, 32))
        self.TitleLabel = TitleLabel(login)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(930, 110, 91, 38))
        self.TitleLabel.setMinimumSize(QSize(91, 38))
        self.TitleLabel.setMaximumSize(QSize(91, 38))
        self.layoutWidget = QWidget(login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(870, 237, 215, 155))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CaptionLabel = CaptionLabel(self.layoutWidget)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setMinimumSize(QSize(31, 16))
        self.CaptionLabel.setMaximumSize(QSize(211, 17))

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.accountInput = LineEdit(self.layoutWidget)
        self.accountInput.setObjectName(u"accountInput")
        self.accountInput.setMinimumSize(QSize(211, 33))
        self.accountInput.setMaximumSize(QSize(211, 33))

        self.verticalLayout.addWidget(self.accountInput)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CaptionLabel_2 = CaptionLabel(self.layoutWidget)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setMinimumSize(QSize(31, 20))
        self.CaptionLabel_2.setMaximumSize(QSize(211, 20))

        self.verticalLayout_2.addWidget(self.CaptionLabel_2)

        self.passwdInput = PasswordLineEdit(self.layoutWidget)
        self.passwdInput.setObjectName(u"passwdInput")
        self.passwdInput.setMinimumSize(QSize(211, 33))
        self.passwdInput.setMaximumSize(QSize(211, 33))

        self.verticalLayout_2.addWidget(self.passwdInput)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 841, 621))
        self.label.setPixmap(QPixmap(u"./img/IMG_2596.JPG"))
        self.label.setScaledContents(True)
        self.CheckBox = CheckBox(login)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setGeometry(QRect(870, 410, 211, 22))
        self.CheckBox.setMinimumSize(QSize(29, 22))

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.loginPushButton.setText(QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.TitleLabel.setText(QCoreApplication.translate("login", u"Pointer", None))
        self.CaptionLabel.setText(QCoreApplication.translate("login", u"\u8d26\u53f7", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("login", u"\u5bc6\u7801", None))
        self.label.setText("")
        self.CheckBox.setText(QCoreApplication.translate("login", u"\u8bb0\u4f4f\u5bc6\u7801", None))
    # retranslateUi

