# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pointer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QSizePolicy, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, ComboBox, PrimaryPushButton, PushButton,
    StrongBodyLabel, TableWidget)

class Ui_Pointer(object):
    def setupUi(self, Pointer):
        if not Pointer.objectName():
            Pointer.setObjectName(u"Pointer")
        Pointer.resize(1117, 728)
        Pointer.setMinimumSize(QSize(1117, 612))
        Pointer.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(Pointer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.StrongBodyLabel_2 = StrongBodyLabel(Pointer)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setMinimumSize(QSize(61, 31))
        self.StrongBodyLabel_2.setMaximumSize(QSize(61, 31))

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel_2)

        self.Account = CaptionLabel(Pointer)
        self.Account.setObjectName(u"Account")
        self.Account.setMinimumSize(QSize(191, 31))

        self.horizontalLayout_2.addWidget(self.Account)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.StrongBodyLabel = StrongBodyLabel(Pointer)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setMaximumSize(QSize(29, 32))

        self.horizontalLayout.addWidget(self.StrongBodyLabel)

        self.ComboBox = ComboBox(Pointer)
        self.ComboBox.setObjectName(u"ComboBox")
        self.ComboBox.setMinimumSize(QSize(151, 32))
        self.ComboBox.setMaximumSize(QSize(151, 32))

        self.horizontalLayout.addWidget(self.ComboBox)

        self.PrimaryPushButton = PrimaryPushButton(Pointer)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMaximumSize(QSize(54, 32))
        self.PrimaryPushButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.PrimaryPushButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.TableWidget = TableWidget(Pointer)
        self.TableWidget.setObjectName(u"TableWidget")

        self.horizontalLayout_4.addWidget(self.TableWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Pointer)

        QMetaObject.connectSlotsByName(Pointer)
    # setupUi

    def retranslateUi(self, Pointer):
        Pointer.setWindowTitle(QCoreApplication.translate("Pointer", u"Pointer", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Pointer", u"\u5f53\u524d\u8d26\u53f7", None))
        self.Account.setText(QCoreApplication.translate("Pointer", u"---", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Pointer", u"\u5b66\u671f", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Pointer", u"\u67e5\u8be2", None))
    # retranslateUi

