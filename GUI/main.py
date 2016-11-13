import sys
from PyQt5.QtWidgets import QDialog, QApplication
from design import Ui_Dialog

from mqtt_publisher import Publisher


class ImageDialog(QDialog):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Make some local modifications.
        self.ui.pingLabel.setNum(0)
        self.ui.testList.addItem('test')

        # Connect up the buttons.
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

    def start(self):
        self.publisher = Publisher()
        self.publisher.start_connect()
        self.ui.pingLabel.setNum(self.publisher.calc_latency())
        pass

    def stop(self):
        sys.exit()

class Test():
    def __init__(self):
        self.count

def main():
    app = QApplication(sys.argv)
    ui = ImageDialog()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
