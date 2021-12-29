import sys
from PyQt5.QtWidgets import *

from modules.design.design_page import DesignPage
from modules.engine.engine_page import EnginePage
from modules.recovery.recovery_page import RecoveryPage
from modules.simulation.simulation_page import SimulationPage
from modules.analysis.analysis_page import AnalysisPage

class AppLayout(QWidget):

    def __init__(self) -> None:
        super(AppLayout, self).__init__()
        self.__initUI()
        return

    def __initUI(self) -> None:
        self.setWindowTitle('Rocket Simulator')

        self.__left_list()
        self.__stack()

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)
        self.stack.addWidget(self.stack5)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist, 1)
        hbox.addWidget(self.stack, 5)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.__display)

        return

    def __left_list(self) -> None:
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Design')
        self.leftlist.insertItem(1, 'Engine')
        self.leftlist.insertItem(2, 'Recovery')
        self.leftlist.insertItem(3, 'Simulation')
        self.leftlist.insertItem(4, 'Analysis')
        return
    
    def __stack(self) -> None:
        self.stack1 = DesignPage()
        self.stack2 = EnginePage()
        self.stack3 = RecoveryPage()
        self.stack4 = SimulationPage()
        self.stack5 = AnalysisPage()
        return

    def __display(self,i) -> None:
       self.stack.setCurrentIndex(i)
       return
		
def main():
    app = QApplication(sys.argv)
    view = AppLayout()
    view.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()