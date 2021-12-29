from PyQt5.QtWidgets import QLabel, QWidget

class DesignPage(QWidget):

    def __init__(self) -> None:
        super(DesignPage, self).__init__()
        self.__initUI()
        return
    
    def __initUI(self) -> None:
        layout = QLabel(self)
        layout.setText('Design')
        self.show()
        return