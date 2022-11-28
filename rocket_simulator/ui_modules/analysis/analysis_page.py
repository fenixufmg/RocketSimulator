from PyQt5.QtWidgets import QLabel, QWidget

class AnalysisPage(QWidget):

    def __init__(self) -> None:
        super(AnalysisPage, self).__init__()
        self.__initUI()
        return
    
    def __initUI(self) -> None:
        layout = QLabel(self)
        layout.setText('Analysis')
        self.show()
        return