#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"Copyright (C) 2020 Raphael Baumann, Killian Schneider, Duc Huynh Nguyen and the OTH-Regensburg - All Rights Reserved"
"You may use, distribute and modify this code under the"
"terms of the GPL 2.0 license."

"Shortcut GPL 2.0 license:"
"The license guarantees the right to freely obtain the software"
"including the source code, the right to change the software and"
"the right to pass on the original or modified software created by"
"changing the software - but only under the same license,"
"including the source code."

"Written by: Raphael Baumann"
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"Includes"
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore

from FloatSlider import FloatSlider


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
"Window for the Config part"
"Grid Like Abstract-Functions"
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
class Grid_Layer(QtWidgets.QWidget):
    def __init__(self,threadHandler):
        super(Grid_Layer, self).__init__()
        self.threadHandler = threadHandler
        self.value0 = 0
        self.value1 = 0
        self.value2 = 0

        self.timevalue0 = 0
        self.timevalue1 = 0

        grid = QGridLayout(self)
        grid.addWidget(self.createSliderGroup("Raumgröße in m^2", self.changeValue0, 20, 1000, 100), 0, 0)
        grid.addWidget(self.createSliderGroup("Faktor in %", self.changeValue1, 1, 100, 10), 1, 0)

        grid.addWidget(self.createTimerGroup("Öffnungszeit", self.changeTime0, 0, 24), 2, 0)
        grid.addWidget(self.createTimerGroup("Schließungszeit", self.changeTime1, 0, 24), 3, 0)

        grid.addWidget(self.createButtonGroup("Änderungen Übernehmen", self.onClick1), 4, 0)
        grid.addWidget(self.createButtonGroup("Exit", self.onClick2), 5, 0)

        self.setLayout(grid)

        #self.resize(400, 400)









    def createSliderGroup(self, name, func, min, max, interv):
        groupBox = QGroupBox(name)
        vbox = QVBoxLayout()
        #vbox.addStretch(1)

        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.valueChanged[int].connect(func)
        slider.setSingleStep(1)
        slider.setTickInterval(interv)
        slider.setMaximum(max)
        slider.setMinimum(min)
        vbox.addWidget(slider)

        ll = QLabel(alignment=QtCore.Qt.AlignCenter)
        #ll.setText("Slide to Change Value!")
        slider.valueChanged.connect(ll.setNum)
        vbox.addWidget(ll)

        groupBox.setLayout(vbox)
        return groupBox

    def changeValue0(self, value):
        self.value0 = value
    def changeValue1(self, value):
        self.value1 = value
    def changeValue2(self, value):
        self.value2 = value









    def createButtonGroup(self, name, func):
        groupBox = QGroupBox()
        vbox = QVBoxLayout()
        #vbox.addStretch(1)

        button = QPushButton(name, self)
        button.clicked.connect(func)
        vbox.addWidget(button)

        groupBox.setLayout(vbox)
        return groupBox

    def onClick1(self):
        pass

    def onClick2(self):
         os._exit(0)









    def createTimerGroup(self, name, func, min, max):
        groupBox = QGroupBox(name)
        vbox = QVBoxLayout()
        #vbox.addStretch(1)

        slider = FloatSlider(2, Qt.Horizontal)
        slider.setMinimum(min)
        slider.setMaximum(max)
        vbox.addWidget(slider)

        ll = QLabel(alignment=QtCore.Qt.AlignCenter)
        #ll.setText("Slide to Change Value!")
        slider.valueChanged.connect(lambda value: func(value, ll, slider))
        vbox.addWidget(ll)

        groupBox.setLayout(vbox)
        return groupBox

    def changeTime0(self, value, ll, slider):
        time = slider.value()
        hours = int(time)
        minutes = (time*60) % 60
        seconds = (time*3600) % 60
        #print("%d:%02d.%02d" % (hours, minutes, seconds))
        #print(value, slider.value())
        #print(hours*100+minutes)
        self.timevalue0 = int(hours*100+minutes)
        ll.setText("Time at " + str(("%d:%02d" % (hours, minutes))))

    def changeTime1(self, value, ll, slider):
        time = slider.value()
        hours = int(time)
        minutes = (time*60) % 60
        seconds = (time*3600) % 60
        self.timevalue1 = int(hours*100+minutes)
        ll.setText("Time at " + str(("%d:%02d" % (hours, minutes))))
