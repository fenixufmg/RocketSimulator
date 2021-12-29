from PyQt5.QtWidgets import QLabel, QWidget

class EnginePage(QWidget):

    def __init__(self) -> None:
        super(EnginePage, self).__init__()
        self.__initUI()
        return
    
    def __initUI(self) -> None:
        layout = QLabel(self)
        layout.setText('Engine')
        self.show()
        return