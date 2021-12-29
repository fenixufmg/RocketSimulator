from PyQt5.QtWidgets import QLabel, QWidget

class RecoveryPage(QWidget):

    def __init__(self) -> None:
        super(RecoveryPage, self).__init__()
        self.__initUI()
        return
    
    def __initUI(self) -> None:
        layout = QLabel(self)
        layout.setText('Recovery')
        self.show()
        return