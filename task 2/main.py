
# main.py

import cv2
import numpy as np

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.video_capture = cv2.VideoCapture(0)

    def initUI(self):
        self.setWindowTitle("Color Space Editing")
        self.setGeometry(100, 100, 400, 200)

        self.slider_value1 = 0
        self.slider_value2 = 0
        self.slider_value3 = 0
        self.slider_value4 = 179
        self.slider_value5 = 255
        self.slider_value6 = 255


        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        helloMsg = QLabel("<p style='margin:0px 10px 0px 0px; color: #007acc; font-size: large'> EDIT COLOR!!  </p> <br>", parent=main_widget)
        helloMsg.move(150,0)
        # main_layout.addLayout(helloMsg)


        slider_layout = QHBoxLayout()

        # First slider
        label = QLabel("L_H:")
        slider_layout.addWidget(label)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 179)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.slider1ValueChanged)
        self.slider.valueChanged.connect(self.changeSlider1)
        slider_layout.addWidget(self.slider)
        self.range1 = QLabel("0")
        slider_layout.addWidget(self.range1)

        main_layout.addLayout(slider_layout)


        # Second slider
        slider_layout1 = QHBoxLayout()
        label1 = QLabel("L_S:")
        slider_layout1.addWidget(label1)
        slider1 = QSlider(Qt.Orientation.Horizontal)
        slider1.setRange(0, 255)
        slider1.setTickInterval(1)
        slider1.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider1.valueChanged.connect(self.slider2ValueChanged)
        slider1.valueChanged.connect(self.changeSlider2)
        slider_layout1.addWidget(slider1)
        self.range2 = QLabel("0")
        slider_layout1.addWidget(self.range2)

        main_layout.addLayout(slider_layout1)

        

         # Third slider
        slider_layout2 = QHBoxLayout()
        label2 = QLabel("L_V:")
        slider_layout2.addWidget(label2)
        slider2 = QSlider(Qt.Orientation.Horizontal)
        slider2.setRange(0, 255)
        slider2.setTickInterval(1)
        slider2.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider2.valueChanged.connect(self.slider3ValueChanged)
        slider2.valueChanged.connect(self.changeSlider3)
        slider_layout2.addWidget(slider2)
        self.range3 = QLabel("0")
        slider_layout2.addWidget(self.range3)
        
        main_layout.addLayout(slider_layout2)

        # Fourth slider
        slider_layout3 = QHBoxLayout()
        label3 = QLabel("H_V:")
        slider_layout3.addWidget(label3)
        slider3 = QSlider(Qt.Orientation.Horizontal)
        slider3.setRange(0, 179)
        slider3.setTickInterval(1)
        slider3.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider3.setInvertedAppearance(True)
        slider3.setInvertedControls(True)
        slider3.valueChanged.connect(self.slider4ValueChanged)
        slider3.valueChanged.connect(self.changeSlider4)
        slider_layout3.addWidget(slider3)
        self.range4 = QLabel("0")
        slider_layout3.addWidget(self.range4)
        
        main_layout.addLayout(slider_layout3)


        # Fifth slider
        slider_layout4 = QHBoxLayout()
        label4 = QLabel("H_S:")
        slider_layout4.addWidget(label4)
        slider4 = QSlider(Qt.Orientation.Horizontal)
        slider4.setRange(0, 255)
        slider4.setTickInterval(1)
        slider4.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider4.setInvertedAppearance(True)
        slider4.setInvertedControls(True)
        slider4.valueChanged.connect(self.slider5ValueChanged)
        slider4.valueChanged.connect(self.changeSlider5)
        slider_layout4.addWidget(slider4)
        self.range5 = QLabel("0")
        slider_layout4.addWidget(self.range5)
        
        main_layout.addLayout(slider_layout4)


        # Sixth slider
        slider_layout5 = QHBoxLayout()
        label5 = QLabel("H_V:")
        slider_layout5.addWidget(label5)
        slider5 = QSlider(Qt.Orientation.Horizontal)
        slider5.setRange(0, 255)
        slider5.setTickInterval(1)
        slider5.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider5.setInvertedAppearance(True)
        slider5.setInvertedControls(True)
        slider5.valueChanged.connect(self.slider6ValueChanged)
        slider5.valueChanged.connect(self.changeSlider6)
        slider_layout5.addWidget(slider5)
        self.range6 = QLabel("0")
        slider_layout5.addWidget(self.range6)
        
        main_layout.addLayout(slider_layout5)


        # Button Exit

        button_layout = QHBoxLayout()
        button = QPushButton("Exit")
        button.setFixedSize(70, 25)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(self.exitClicked)

        button.setStyleSheet(
            """
             QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 3px;
            }
             QPushButton:hover {
                background-color: #005fa3;
            }
            """
        )
        button_layout.addWidget(button)
        main_layout.addLayout(button_layout)

        
    
    def changeSlider1(self):
        value = self.slider.value()
        self.range1.setText(str(value)) 

    def changeSlider2(self):
        value = self.slider_value2
        self.range2.setText(str(value)) 

    def changeSlider3(self):
        value = self.slider_value3
        self.range3.setText(str(value))    

    def changeSlider4(self):
        value = self.slider_value4
        self.range4.setText(str(value))     

    def changeSlider5(self):
        value = self.slider_value5
        self.range5.setText(str(value))  

    def changeSlider6(self):
        value = self.slider_value6
        self.range6.setText(str(value))  



    def slider1ValueChanged(self, value):
        self.slider_value1 = value
        # print("Slider 1 value:", value)


    def slider2ValueChanged(self, value):
        self.slider_value2 = value
        # print("Slider 2 value:", value)    

    def slider3ValueChanged(self, value):
        self.slider_value3 = value
        # print("Slider 3 value:", value)

    def slider4ValueChanged(self, value):
        self.slider_value4 = value
        print("Slider 4 value:", value)

    
    def slider5ValueChanged(self, value):
        self.slider_value5 = value

    def slider6ValueChanged(self, value):
        self.slider_value6 = value


    # def createTrackbars(self):
    #     cv2.namedWindow("Trackbars")
    #     cv2.resizeWindow("Trackbars", 700, 312)
    #     cv2.createTrackbar("L-H", "Trackbars", 0, 179, self.nothing)
    #     cv2.createTrackbar("L-S", "Trackbars", 0, 255, self.nothing)
    #     cv2.createTrackbar("L-V", "Trackbars", 0, 255, self.nothing)
    #     cv2.createTrackbar("U-H", "Trackbars", 179, 179, self.nothing)
    #     cv2.createTrackbar("U-S", "Trackbars", 255, 255, self.nothing)
    #     cv2.createTrackbar("U-V", "Trackbars", 255, 255, self.nothing)

    # def nothing(self, x):
    #     pass

    def exitClicked(self):
        self.video_capture.release()
        self.close()

    def processFrame(self):
        ret, frame = self.video_capture.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # l_h = cv2.getTrackbarPos("L-H", "Trackbars")
        # l_s = cv2.getTrackbarPos("L-S", "Trackbars")
        # l_v = cv2.getTrackbarPos("L-V", "Trackbars")
        # u_h = cv2.getTrackbarPos("U-H", "Trackbars")
        # u_s = cv2.getTrackbarPos("U-S", "Trackbars")
        # u_v = cv2.getTrackbarPos("U-V", "Trackbars")

        lower_range = np.array([self.slider_value1, self.slider_value2, self.slider_value3])
        upper_range = np.array([self.slider_value4, self.slider_value5, self.slider_value6])

        mask = cv2.inRange(hsv, lower_range, upper_range)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Webcam Stream", frame)
        cv2.imshow("result", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.exitClicked()
        else:
            self.processFrame()

    def startVideoStream(self):
        self.processFrame()
        QApplication.instance().exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    window.startVideoStream()

