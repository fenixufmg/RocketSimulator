from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import QRect, Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush

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