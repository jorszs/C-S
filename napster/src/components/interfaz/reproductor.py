#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       player.py
#
#       Copyright 2013 Recursos Python - www.recursospython.com
#
import sys
from PyQt4.QtCore import QMetaObject
from PyQt4.QtGui import (QApplication, QFileDialog, QLabel, QMainWindow,
                         QPushButton)
from PyQt4.phonon import Phonon


class Window(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(400, 300)
        self.setWindowTitle("Reproductor de audio")

        self.player = Phonon.createPlayer(Phonon.MusicCategory)

        self.slider = Phonon.SeekSlider(self.player, self)
        self.slider.setGeometry(10, 10, 380, 25)

        self.play_button = QPushButton(self)
        self.play_button.setText("Reproducir")
        self.play_button.setGeometry(10, 50, 100, 25)
        self.play_button.setObjectName("play_button")

        self.pause_button = QPushButton(self)
        self.pause_button.setText("Pausa")
        self.pause_button.setGeometry(120, 50, 100, 25)
        self.pause_button.setObjectName("pause_button")

        self.stop_button = QPushButton(self)
        self.stop_button.setText("Detener")
        self.stop_button.setGeometry(230, 50, 100, 25)
        self.stop_button.setObjectName("stop_button")

        self.track_label = QLabel(self)
        self.track_label.setText(
            u"No se ha seleccionado ningún archivo."
        )
        self.track_label.setGeometry(10, 100, 340, 25)
        self.track_label.setObjectName("track_label")

        self.browse_button = QPushButton(self)
        self.browse_button.setText("...")
        self.browse_button.setGeometry(355, 100, 35, 25)
        self.browse_button.setObjectName("browse_button")

        QMetaObject.connectSlotsByName(self)

    def on_play_button_pressed(self):
        self.player.play()

    def on_pause_button_pressed(self):
        self.player.pause()

    def on_stop_button_pressed(self):
        self.player.stop()

    def on_browse_button_released(self):
        path = unicode(QFileDialog.getOpenFileName(self))
        index = path.rfind("/")
        self.player.setCurrentSource(Phonon.MediaSource(path))
        self.track_label.setText(path[index + 1 if index > -1 else 0:])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
