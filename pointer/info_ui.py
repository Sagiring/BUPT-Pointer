# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, HyperlinkButton, PushButton, StrongBodyLabel,
    TitleLabel)

class Ui_info(object):
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName(u"info")
        info.resize(1117, 612)
        info.setMinimumSize(QSize(1117, 612))
        self.widget = QWidget(info)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(250, 130, 591, 371))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TitleLabel = TitleLabel(self.widget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setMaximumSize(QSize(171, 38))

        self.horizontalLayout.addWidget(self.TitleLabel)

        self.version = StrongBodyLabel(self.widget)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(24, 38))

        self.horizontalLayout.addWidget(self.version)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.HyperlinkButton = HyperlinkButton(self.widget)
        self.HyperlinkButton.setObjectName(u"HyperlinkButton")
        self.HyperlinkButton.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.HyperlinkButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(256, 256))
        self.label.setPixmap(QPixmap(u"./img/favicon.ico"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignVCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel = BodyLabel(self.widget)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setMaximumSize(QSize(65, 19))

        self.horizontalLayout_2.addWidget(self.BodyLabel, 0, Qt.AlignRight)

        self.StrongBodyLabel = StrongBodyLabel(self.widget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setMaximumSize(QSize(124, 19))

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("info", u"BUPT-Pointer", None))
        self.version.setText(QCoreApplication.translate("info", u"v1.0", None))
        self.HyperlinkButton.setText(QCoreApplication.translate("info", u"Github", None))
        self.label.setText("")
        self.BodyLabel.setText(QCoreApplication.translate("info", u"Written by", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("info", u"Sagiring", None))
    # retranslateUi

