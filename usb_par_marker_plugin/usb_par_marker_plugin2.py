from libopensesame.py3compat import *
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from openexp.canvas import canvas

import serial


class UsbParMarker(item):

    description = u'An usb_par_marker plug-in'

    def reset(self):
        self.var.com_port = u'COM1'
        self.var.action = u'initialize'
        self.var.marker_value = u'0'

    def initialize(self, com_port, baudrate=115200, timeout=2):
        self.ser = serial.Serial()

        self.ser.port = com_port
        self.ser.baudrate = baudrate
        self.ser.bytesize = 0
        self.ser.parity = 'N'
        self.ser.stopbits = 1
        self.ser.timeout = timeout

        self.ser.open()

    def close(self):

        self.ser.close()

    def send_marker(self, marker_value):
        if type(marker_value) == str:
            self.ser.write(marker_value.encode())
        elif type(marker_value) == int:
            self.ser.write(bytearray([marker_value]))

    def prepare(self):

        item.prepare(self)

    def run(self):
        if self.var.action == 'initialize':
            self.initialize(self.var.com_port)
        elif self.var.action == 'close':
            self.close()
        elif self.var.action == 'send_marker':
            self.send_marker(self.var.marker_value)


class qtUsbParMarker(UsbParMarker, qtautoplugin):
    def __init__(self, name, experiment, script=None):
        UsbParMarker.__init__(self, name, experiment, script)
        qtautoplugin.__init__(self, __file__)

    def init_edit_widget(self):
        qtautoplugin.init_edit_widget(self)


