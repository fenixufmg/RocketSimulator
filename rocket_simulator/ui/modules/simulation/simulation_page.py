from PyQt5.QtWidgets import QLabel, QWidget

class SimulationPage(QWidget):

    def __init__(self) -> None:
        super(SimulationPage, self).__init__()
        self.__initUI()
        return
    
    def __initUI(self) -> None:
        layout = QLabel(self)
        layout.setText('Simulation')
        self.show()
        return