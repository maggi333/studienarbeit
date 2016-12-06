import sys
from PyQt5.QtWidgets import QDialog, QApplication
from design import Ui_Dialog

from mqtt_publisher import MQTTPublisher
from coap_client import CoAPClient
import evaluation

class ImageDialog(QDialog):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ------Make some local modifications-------

        self.ui.pingLabel.setText('')
        self.ui.msg_lostLabel.setText('')
        # self.ui.testList.addItem('test')
        # item = QListWidgetItem()
        # item.setText('test3000')
        self.ui.lineEdit.setText('1024')
        self.ui.lineEdit_2.setText('1')
        self.ui.lineEdit_3.setText('5')
        self.ui.lineEdit_4.setText('1')

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.reset()



        # Connect up the buttons.
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

    def start(self):
        # Zurücksetzen des Fortschrittsbalken
        self.ui.progressBar.setValue(0)
        # GUI auslesen
        packet_size = int(self.ui.lineEdit.text())
        cycle_time = float(self.ui.lineEdit_2.text())
        count = int(self.ui.lineEdit_3.text())
        QoS = int(self.ui.lineEdit_4.text())

        # Starte Verbindung
        if self.ui.mqttButton.isChecked():

            self.publisher = MQTTPublisher(packet_size, cycle_time, count, QoS, self.ui)
            msg_send, msg_ack = self.publisher.start_connect()

        elif self.ui.coapButton.isChecked():

            self.client = CoAPClient(packet_size, cycle_time, count, self.ui)
            msg_send, msg_ack = self.client.start_connect()


        else:
            print('Error: No Protocol selected')
            sys.exit(2)

        # Berechne Auswertung
        latenz, msg_lost = evaluation.calculate_eval(msg_send, msg_ack)

        # Anzeigen der Auswertung
        self.ui.pingLabel.setText(str(latenz) + ' s')
        self.ui.msg_lostLabel.setText(str(msg_lost) + ' %')

        self.ui.progressBar.setValue(100)

    def stop(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    ui = ImageDialog()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
