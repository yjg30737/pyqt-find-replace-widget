from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QApplication


class FindReplaceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        findLineEdit = QLineEdit()
        replaceLineEdit = QLineEdit()

        lay = QVBoxLayout()
        lay.addWidget(findLineEdit)
        lay.addWidget(replaceLineEdit)
        lay.setContentsMargins(0, 0, 0, 0)

        lineEditWidget = QWidget()
        lineEditWidget.setLayout(lay)

        prevBtn = QPushButton()
        nextBtn = QPushButton()
        caseBtn = QPushButton()
        wordBtn = QPushButton()
        regexBtn = QPushButton()

        lay = QHBoxLayout()
        lay.addWidget(prevBtn)
        lay.addWidget(nextBtn)
        lay.addWidget(caseBtn)
        lay.addWidget(wordBtn)
        lay.addWidget(regexBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        btnTopWidget = QWidget()
        btnTopWidget.setLayout(lay)

        replaceBtn = QPushButton()
        replaceAllBtn = QPushButton()
        excludeBtn = QPushButton()

        lay = QHBoxLayout()
        lay.addWidget(replaceBtn)
        lay.addWidget(replaceAllBtn)
        lay.addWidget(excludeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        btnBottomWidget = QWidget()
        btnBottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(btnTopWidget)
        lay.addWidget(btnBottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        btnWidget = QWidget()
        btnWidget.setLayout(lay)

        swapBtn = QPushButton()
        closeBtn = QPushButton()

        lay = QHBoxLayout()
        lay.addWidget(swapBtn)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        rightBtnWidget = QWidget()
        rightBtnWidget.setLayout(lay)

        lay = QHBoxLayout()
        lay.addWidget(lineEditWidget)
        lay.addWidget(btnWidget)
        lay.addWidget(rightBtnWidget)

        self.setLayout(lay)