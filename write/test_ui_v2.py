# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from ctypes import *
from time import sleep
import ControlSPI
import time
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditbit7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit7.setGeometry(QtCore.QRect(230, 200, 30, 30))
        self.textEditbit7.setObjectName("textEditbit7")
        self.textEditbit6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit6.setGeometry(QtCore.QRect(280, 200, 30, 30))
        self.textEditbit6.setObjectName("textEditbit6")
        self.textEditbit5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit5.setGeometry(QtCore.QRect(330, 200, 30, 30))
        self.textEditbit5.setObjectName("textEditbit5")
        self.textEditbit4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit4.setGeometry(QtCore.QRect(380, 200, 30, 30))
        self.textEditbit4.setObjectName("textEditbit4")
        self.textEditbit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit3.setGeometry(QtCore.QRect(430, 200, 30, 30))
        self.textEditbit3.setObjectName("textEditbit3")
        self.textEditbit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit2.setGeometry(QtCore.QRect(480, 200, 30, 30))
        self.textEditbit2.setObjectName("textEditbit2")
        self.textEditbit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit1.setGeometry(QtCore.QRect(530, 200, 30, 30))
        self.textEditbit1.setObjectName("textEditbit1")
        self.textEditbit0 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbit0.setGeometry(QtCore.QRect(580, 200, 30, 30))
        self.textEditbit0.setObjectName("textEditbit0")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 200, 120, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 205, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 150, 120, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 250, 661, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(300, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "data"))
        self.label_2.setText(_translate("MainWindow", "addr"))
        self.label_3.setText(_translate("MainWindow", "bit7"))
        self.label_4.setText(_translate("MainWindow", "bit6"))
        self.label_5.setText(_translate("MainWindow", "bit5"))
        self.label_6.setText(_translate("MainWindow", "bit4"))
        self.label_7.setText(_translate("MainWindow", "bit0"))
        self.label_8.setText(_translate("MainWindow", "bit1"))
        self.label_9.setText(_translate("MainWindow", "bit2"))
        self.label_10.setText(_translate("MainWindow", "bit3"))
        self.pushButton.setText(_translate("MainWindow", "READ"))
        self.pushButton_2.setText(_translate("MainWindow", "WRITE"))
        self.pushButton_4.setText(_translate("MainWindow", "MEM_RD"))
        self.pushButton_5.setText(_translate("MainWindow", "FFT"))
        self.toolButton.setText(_translate("MainWindow", "seq_test"))
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.read_addr)
        self.ui.pushButton_2.clicked.connect(self.write_addr)
        self.ui.toolButton.clicked.connect(self.load_test_seq)
        self.ui.pushButton_4.clicked.connect(self.mem_read)
        self.ui.pushButton_5.clicked.connect(self.fft_gen)
    def write_atom(self,addr,data):
        self.ui.textBrowser.insertPlainText('write:addr='+hex(addr)+' data='+hex(data)+'\n')
        write_buffer = (c_ubyte * 3)()
        read_buffer = (c_ubyte * 1)()
        addr_str = '{:0>4x}'.format(addr)
        write_buffer[0] = int(addr_str[0:2],16)
        write_buffer[1] = int(addr_str[2:],16)
        write_buffer[2] = data
        nRet = ControlSPI.VSI_WriteBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 3)
    def read_atom(self,addr):
        write_buffer = (c_ubyte * 2)()
        read_buffer = (c_ubyte * 1)()
        addr_str = '{:0>4x}'.format(addr)
        write_buffer[0] = int(addr_str[0:2], 16)+128
        write_buffer[1] = int(addr_str[2:], 16)
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 1)
        self.ui.textBrowser.insertPlainText('read:addr='+hex(addr)+' data='+hex(int(str(read_buffer[0])))+'\n')
        return read_buffer
    def read_addr(self):
        now_addr = self.ui.textEdit_2.toPlainText()
        if re.match('^0x', now_addr):
            addr_read = int(now_addr,16)
        else:
            addr_read = int(now_addr)
        read_value = self.read_atom(addr_read)
        self.ui.textEdit.setText(hex(read_value[0]))
        read_value_bin = '{:0>8b}'.format(read_value[0])
        self.ui.textEditbit0.setText(read_value_bin[7])
        self.ui.textEditbit1.setText(read_value_bin[6])
        self.ui.textEditbit2.setText(read_value_bin[5])
        self.ui.textEditbit3.setText(read_value_bin[4])
        self.ui.textEditbit4.setText(read_value_bin[3])
        self.ui.textEditbit5.setText(read_value_bin[2])
        self.ui.textEditbit6.setText(read_value_bin[1])
        self.ui.textEditbit7.setText(read_value_bin[0])
    def write_addr(self):
        now_addr = self.ui.textEdit_2.toPlainText()
        if re.match('^0x', now_addr):
            addr_write = int(now_addr,16)
        else:
            addr_write = int(now_addr)
        now_value = self.ui.textEdit.toPlainText()
        if re.match('^0x',now_value):
            write_value = int(now_value,16)
        else:
            write_value = int(now_value)
        write_value_bin = '{:0>8b}'.format(write_value)
        self.ui.textEditbit0.setText(write_value_bin[7])
        self.ui.textEditbit1.setText(write_value_bin[6])
        self.ui.textEditbit2.setText(write_value_bin[5])
        self.ui.textEditbit3.setText(write_value_bin[4])
        self.ui.textEditbit4.setText(write_value_bin[3])
        self.ui.textEditbit5.setText(write_value_bin[2])
        self.ui.textEditbit6.setText(write_value_bin[1])
        self.ui.textEditbit7.setText(write_value_bin[0])
        self.write_atom(addr_write, write_value)
    def load_test_seq(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            self.test_seq_file = dialog.selectedFiles()
            self.ui.textBrowser.insertPlainText('test seq file is '+str(self.test_seq_file[0])+'\n...\n...\n')
        self.ui.textBrowser.insertPlainText('starting reading '+str(self.test_seq_file[0])+'\n')
        self.parser_seq_file(self.test_seq_file[0])
    def parser_seq_file(self, fn):
        data = xlrd.open_workbook(fn)
        sheet_data = data.sheets()[0]
        rows_num = sheet_data.nrows
        seq_addr = []
        seq_data = []
        for x in range(0,rows_num):
            seq_addr.append(sheet_data.cell_value(x,0))
            seq_data.append(sheet_data.cell_value(x,1))
        for i in range(0,len(seq_addr)):
            if seq_addr[i] == 'sleep':
                time.sleep(5)
                self.ui.textBrowser.insertPlainText('sleep 5\n')
            else:
                self.write_atom(int(seq_addr[i],16), int(seq_data[i],16))
    def read_mem_reg(self, addr0, addr1):
        write_buffer = (c_ubyte * 2)()
        read_buffer = (c_ubyte * 4096)()
        write_buffer[0] = addr0
        write_buffer[1] = addr1
        nRet = ControlSPI.VSI_WriteReadBytes(ControlSPI.VSI_USBSPI, 0, 0, write_buffer, 2, read_buffer, 4096)
        return read_buffer
    def mem_read(self):
        self.write_atom(0xf18, 0x00)
        self.write_atom(0xf16, 0x00)
        self.write_atom(0xf1d, 0x1)
        self.write_atom(0xf1c, 0x1)
        self.write_atom(0xf16, 0x08)
        self.write_atom(0xf17, 0x40)
        self.write_atom(0xf19, 0x3c)
        self.write_atom(0xf1a, 0x00)
        self.write_atom(0xf1b, 0x10)
        self.write_atom(0xf1d, 0x0)
        self.write_atom(0xf1c, 0x0)
        self.write_atom(0xf18, 0x02)
        self.write_atom(0x0f11, 0x01)
        self.write_atom(0x0f10, 0x01)
        self.write_atom(0x0f16, 0x10)
        self.write_atom(0x0f11, 0x00)
        self.write_atom(0x0f10, 0x00)
        time.sleep(5)
        offset = 0x00
        data_old = 0x55
        fp = open('memory_dump_data.txt', 'w')
        for i in range(0, 32):
            data_new = i * 4 + offset
            self.write_atom(0xf11, data_old)
            self.write_atom(0xf11, data_new)
            # print("%02x\n" % (data_new))
            read_buffer = self.read_mem_reg(0x8f, 0x24)
            for k in range(0, len(read_buffer)):
                fp.write("%02x\n" % (read_buffer[k]))
        fp.close()
    def fft_gen(self):
        fd = open('memory_dump_data.txt', 'r')
        data = [x.strip() for x in fd]
        fd.close()
        data_num = len(data)
        ts = np.linspace(1,data_num,data_num)
        fft_size = 8192
        data_array = np.array(data)
        freq = np.linspace(1,int(fft_size)/2,int(fft_size/2)+1)
        dout_fft = np.fft.rfft(data_array[:fft_size])/fft_size
        dout_db = 20*np.log10(np.abs(dout_fft))
        plt.figure(1)
        plt.plot(freq, dout_db)
        plt.figure(2)
        plt.plot(ts,data_array)
        plt.legend()
        plt.show()
        
    
if __name__ == "__main__":
    # Scan device
    nRet = ControlSPI.VSI_ScanDevice(1)
    if (nRet <= 0):
        print("No device connect!")
    #  exit()
    else:
        print("Connected device number is:" + repr(nRet))

    # Open device
    nRet = ControlSPI.VSI_OpenDevice(ControlSPI.VSI_USBSPI, 0, 0)
    if (nRet != ControlSPI.ERR_SUCCESS):
        print("Open device error!")
        # exit()
    else:
        print("Open device success!")
    # Initialize device
    SPI_Init = ControlSPI.VSI_INIT_CONFIG()
    SPI_Init.ClockSpeed = 1125000;
    SPI_Init.ControlMode = 3;
    SPI_Init.CPHA = 0;
    SPI_Init.CPOL = 0;
    SPI_Init.LSBFirst = 0;
    SPI_Init.MasterMode = 1;
    SPI_Init.SelPolarity = 0;
    SPI_Init.TranBits = 8;

    nRet = ControlSPI.VSI_InitSPI(ControlSPI.VSI_USBSPI, 0, byref(SPI_Init))
    if (nRet != ControlSPI.ERR_SUCCESS):
        print("Initialization device error!")
    # exit()
    else:
        print("Initialization device success!")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
