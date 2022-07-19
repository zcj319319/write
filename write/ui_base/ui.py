# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 820)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1176, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.clk_option = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clk_option.setFont(font)
        self.clk_option.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clk_option.setObjectName("clk_option")
        self.gridLayout_4.addWidget(self.clk_option, 0, 0, 1, 1)
        self.clk_option_cfg_button = QtWidgets.QToolButton(self.groupBox_7)
        self.clk_option_cfg_button.setObjectName("clk_option_cfg_button")
        self.gridLayout_4.addWidget(self.clk_option_cfg_button, 0, 1, 1, 1)
        self.fs = QtWidgets.QLabel(self.groupBox_7)
        self.fs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs.setAlignment(QtCore.Qt.AlignCenter)
        self.fs.setObjectName("fs")
        self.gridLayout_4.addWidget(self.fs, 1, 0, 1, 2)
        self.fs_display = QtWidgets.QLineEdit(self.groupBox_7)
        self.fs_display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_display.setObjectName("fs_display")
        self.gridLayout_4.addWidget(self.fs_display, 2, 0, 1, 1)
        self.fs_2 = QtWidgets.QLabel(self.groupBox_7)
        self.fs_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_2.setObjectName("fs_2")
        self.gridLayout_4.addWidget(self.fs_2, 2, 1, 1, 1)
        self.fin = QtWidgets.QLabel(self.groupBox_7)
        self.fin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fin.setAlignment(QtCore.Qt.AlignCenter)
        self.fin.setObjectName("fin")
        self.gridLayout_4.addWidget(self.fin, 3, 0, 1, 2)
        self.fin_display = QtWidgets.QLineEdit(self.groupBox_7)
        self.fin_display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fin_display.setObjectName("fin_display")
        self.gridLayout_4.addWidget(self.fin_display, 4, 0, 1, 1)
        self.fs_3 = QtWidgets.QLabel(self.groupBox_7)
        self.fs_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_3.setObjectName("fs_3")
        self.gridLayout_4.addWidget(self.fs_3, 4, 1, 1, 1)
        self.fin_2 = QtWidgets.QLabel(self.groupBox_7)
        self.fin_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fin_2.setObjectName("fin_2")
        self.gridLayout_4.addWidget(self.fin_2, 5, 0, 1, 2)
        self.fin_display_2 = QtWidgets.QLineEdit(self.groupBox_7)
        self.fin_display_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fin_display_2.setObjectName("fin_display_2")
        self.gridLayout_4.addWidget(self.fin_display_2, 6, 0, 1, 1)
        self.fs_4 = QtWidgets.QLabel(self.groupBox_7)
        self.fs_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_4.setObjectName("fs_4")
        self.gridLayout_4.addWidget(self.fs_4, 6, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_7)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fbc_div = QtWidgets.QLineEdit(self.groupBox_6)
        self.fbc_div.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fbc_div.setObjectName("fbc_div")
        self.gridLayout_3.addWidget(self.fbc_div, 2, 2, 1, 1)
        self.fs_28 = QtWidgets.QLabel(self.groupBox_6)
        self.fs_28.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_28.setObjectName("fs_28")
        self.gridLayout_3.addWidget(self.fs_28, 3, 0, 1, 1)
        self.sds_button = QtWidgets.QPushButton(self.groupBox_6)
        self.sds_button.setObjectName("sds_button")
        self.gridLayout_3.addWidget(self.sds_button, 4, 0, 1, 3)
        self.fs_26 = QtWidgets.QLabel(self.groupBox_6)
        self.fs_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_26.setObjectName("fs_26")
        self.gridLayout_3.addWidget(self.fs_26, 1, 0, 1, 2)
        self.sds_button_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.sds_button_3.setObjectName("sds_button_3")
        self.gridLayout_3.addWidget(self.sds_button_3, 6, 0, 1, 3)
        self.refclk_div = QtWidgets.QLineEdit(self.groupBox_6)
        self.refclk_div.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.refclk_div.setObjectName("refclk_div")
        self.gridLayout_3.addWidget(self.refclk_div, 1, 2, 1, 1)
        self.sds_button_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.sds_button_2.setObjectName("sds_button_2")
        self.gridLayout_3.addWidget(self.sds_button_2, 5, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 3, 1, 1, 2)
        self.fs_27 = QtWidgets.QLabel(self.groupBox_6)
        self.fs_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_27.setObjectName("fs_27")
        self.gridLayout_3.addWidget(self.fs_27, 2, 0, 1, 2)
        self.clk_option_2 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clk_option_2.sizePolicy().hasHeightForWidth())
        self.clk_option_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clk_option_2.setFont(font)
        self.clk_option_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clk_option_2.setObjectName("clk_option_2")
        self.gridLayout_3.addWidget(self.clk_option_2, 0, 0, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DDC_CONFIG = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DDC_CONFIG.setFont(font)
        self.DDC_CONFIG.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DDC_CONFIG.setObjectName("DDC_CONFIG")
        self.gridLayout_5.addWidget(self.DDC_CONFIG, 0, 0, 1, 4)
        self.fs_5 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_5.setObjectName("fs_5")
        self.gridLayout_5.addWidget(self.fs_5, 1, 0, 1, 4)
        self.chip_mode_config = QtWidgets.QComboBox(self.groupBox_8)
        self.chip_mode_config.setObjectName("chip_mode_config")
        self.gridLayout_5.addWidget(self.chip_mode_config, 2, 0, 1, 5)
        self.fs_6 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_6.setObjectName("fs_6")
        self.gridLayout_5.addWidget(self.fs_6, 3, 0, 1, 2)
        self.fs_29 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_29.setObjectName("fs_29")
        self.gridLayout_5.addWidget(self.fs_29, 3, 3, 1, 2)
        self.real_mode_config = QtWidgets.QComboBox(self.groupBox_8)
        self.real_mode_config.setObjectName("real_mode_config")
        self.gridLayout_5.addWidget(self.real_mode_config, 4, 0, 1, 2)
        self.mix_mode_config = QtWidgets.QComboBox(self.groupBox_8)
        self.mix_mode_config.setObjectName("mix_mode_config")
        self.gridLayout_5.addWidget(self.mix_mode_config, 4, 2, 1, 3)
        self.fs_30 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_30.setObjectName("fs_30")
        self.gridLayout_5.addWidget(self.fs_30, 5, 0, 1, 2)
        self.fs_31 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_31.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_31.setObjectName("fs_31")
        self.gridLayout_5.addWidget(self.fs_31, 5, 3, 1, 2)
        self.freq_mode_config = QtWidgets.QComboBox(self.groupBox_8)
        self.freq_mode_config.setObjectName("freq_mode_config")
        self.gridLayout_5.addWidget(self.freq_mode_config, 6, 0, 1, 2)
        self.gain_mode_config = QtWidgets.QComboBox(self.groupBox_8)
        self.gain_mode_config.setObjectName("gain_mode_config")
        self.gridLayout_5.addWidget(self.gain_mode_config, 6, 2, 1, 3)
        self.fs_7 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_7.setObjectName("fs_7")
        self.gridLayout_5.addWidget(self.fs_7, 7, 0, 1, 4)
        self.ddc0_config = QtWidgets.QComboBox(self.groupBox_8)
        self.ddc0_config.setObjectName("ddc0_config")
        self.gridLayout_5.addWidget(self.ddc0_config, 8, 0, 1, 5)
        self.fs_8 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_8.setObjectName("fs_8")
        self.gridLayout_5.addWidget(self.fs_8, 9, 0, 1, 4)
        self.ddc1_config = QtWidgets.QComboBox(self.groupBox_8)
        self.ddc1_config.setObjectName("ddc1_config")
        self.gridLayout_5.addWidget(self.ddc1_config, 10, 0, 1, 5)
        self.fs_9 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_9.setObjectName("fs_9")
        self.gridLayout_5.addWidget(self.fs_9, 11, 0, 1, 4)
        self.ddc2_config = QtWidgets.QComboBox(self.groupBox_8)
        self.ddc2_config.setObjectName("ddc2_config")
        self.gridLayout_5.addWidget(self.ddc2_config, 12, 0, 1, 5)
        self.fs_10 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_10.setObjectName("fs_10")
        self.gridLayout_5.addWidget(self.fs_10, 13, 0, 1, 4)
        self.ddc3_config = QtWidgets.QComboBox(self.groupBox_8)
        self.ddc3_config.setObjectName("ddc3_config")
        self.gridLayout_5.addWidget(self.ddc3_config, 14, 0, 1, 5)
        self.fs_11 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_11.setObjectName("fs_11")
        self.gridLayout_5.addWidget(self.fs_11, 15, 0, 1, 1)
        self.nco0_line_edit = QtWidgets.QLineEdit(self.groupBox_8)
        self.nco0_line_edit.setObjectName("nco0_line_edit")
        self.gridLayout_5.addWidget(self.nco0_line_edit, 15, 1, 1, 3)
        self.fs_12 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_12.setObjectName("fs_12")
        self.gridLayout_5.addWidget(self.fs_12, 15, 4, 1, 1)
        self.fs_13 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_13.setObjectName("fs_13")
        self.gridLayout_5.addWidget(self.fs_13, 16, 0, 1, 1)
        self.nco1_line_edit = QtWidgets.QLineEdit(self.groupBox_8)
        self.nco1_line_edit.setObjectName("nco1_line_edit")
        self.gridLayout_5.addWidget(self.nco1_line_edit, 16, 1, 1, 3)
        self.fs_14 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_14.setObjectName("fs_14")
        self.gridLayout_5.addWidget(self.fs_14, 16, 4, 1, 1)
        self.fs_15 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_15.setObjectName("fs_15")
        self.gridLayout_5.addWidget(self.fs_15, 17, 0, 1, 1)
        self.nco2_line_edit = QtWidgets.QLineEdit(self.groupBox_8)
        self.nco2_line_edit.setObjectName("nco2_line_edit")
        self.gridLayout_5.addWidget(self.nco2_line_edit, 17, 1, 1, 3)
        self.fs_16 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_16.setObjectName("fs_16")
        self.gridLayout_5.addWidget(self.fs_16, 17, 4, 1, 1)
        self.fs_17 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_17.setObjectName("fs_17")
        self.gridLayout_5.addWidget(self.fs_17, 18, 0, 1, 1)
        self.nco3_line_edit = QtWidgets.QLineEdit(self.groupBox_8)
        self.nco3_line_edit.setObjectName("nco3_line_edit")
        self.gridLayout_5.addWidget(self.nco3_line_edit, 18, 1, 1, 3)
        self.fs_18 = QtWidgets.QLabel(self.groupBox_8)
        self.fs_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_18.setObjectName("fs_18")
        self.gridLayout_5.addWidget(self.fs_18, 18, 4, 1, 1)
        self.nco_update_pushButton = QtWidgets.QPushButton(self.groupBox_8)
        self.nco_update_pushButton.setObjectName("nco_update_pushButton")
        self.gridLayout_5.addWidget(self.nco_update_pushButton, 19, 0, 1, 3)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/xxx/xxxx.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/struc/structure.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DDC_CONFIG_4 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DDC_CONFIG_4.setFont(font)
        self.DDC_CONFIG_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DDC_CONFIG_4.setObjectName("DDC_CONFIG_4")
        self.horizontalLayout_2.addWidget(self.DDC_CONFIG_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.fs_32 = QtWidgets.QLabel(self.groupBox_9)
        self.fs_32.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_32.setObjectName("fs_32")
        self.horizontalLayout_2.addWidget(self.fs_32)
        self.label_4 = QtWidgets.QLabel(self.groupBox_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.groupBox_9)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/status/OFF.png"))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.l_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.l_reg_cfg.setObjectName("l_reg_cfg")
        self.gridLayout.addWidget(self.l_reg_cfg, 4, 1, 1, 1)
        self.fs_19 = QtWidgets.QLabel(self.groupBox)
        self.fs_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_19.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_19.setObjectName("fs_19")
        self.gridLayout.addWidget(self.fs_19, 2, 0, 1, 1)
        self.n_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.n_reg_cfg.setObjectName("n_reg_cfg")
        self.gridLayout.addWidget(self.n_reg_cfg, 8, 1, 1, 1)
        self.fs_25 = QtWidgets.QLabel(self.groupBox)
        self.fs_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_25.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_25.setObjectName("fs_25")
        self.gridLayout.addWidget(self.fs_25, 8, 0, 1, 1)
        self.fs_22 = QtWidgets.QLabel(self.groupBox)
        self.fs_22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_22.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_22.setObjectName("fs_22")
        self.gridLayout.addWidget(self.fs_22, 5, 0, 1, 1)
        self.j204b_update_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.j204b_update_pushButton.setObjectName("j204b_update_pushButton")
        self.gridLayout.addWidget(self.j204b_update_pushButton, 9, 0, 1, 2)
        self.DDC_CONFIG_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DDC_CONFIG_2.setFont(font)
        self.DDC_CONFIG_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DDC_CONFIG_2.setAlignment(QtCore.Qt.AlignCenter)
        self.DDC_CONFIG_2.setObjectName("DDC_CONFIG_2")
        self.gridLayout.addWidget(self.DDC_CONFIG_2, 1, 0, 1, 2)
        self.ntotal_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.ntotal_reg_cfg.setObjectName("ntotal_reg_cfg")
        self.gridLayout.addWidget(self.ntotal_reg_cfg, 2, 1, 1, 1)
        self.m_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.m_reg_cfg.setObjectName("m_reg_cfg")
        self.gridLayout.addWidget(self.m_reg_cfg, 3, 1, 1, 1)
        self.k_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.k_reg_cfg.setObjectName("k_reg_cfg")
        self.gridLayout.addWidget(self.k_reg_cfg, 7, 1, 1, 1)
        self.fs_21 = QtWidgets.QLabel(self.groupBox)
        self.fs_21.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_21.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_21.setObjectName("fs_21")
        self.gridLayout.addWidget(self.fs_21, 4, 0, 1, 1)
        self.init_button = QtWidgets.QPushButton(self.groupBox)
        self.init_button.setObjectName("init_button")
        self.gridLayout.addWidget(self.init_button, 0, 0, 1, 1)
        self.mem_rd_button = QtWidgets.QPushButton(self.groupBox)
        self.mem_rd_button.setObjectName("mem_rd_button")
        self.gridLayout.addWidget(self.mem_rd_button, 0, 1, 1, 1)
        self.fs_23 = QtWidgets.QLabel(self.groupBox)
        self.fs_23.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_23.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_23.setObjectName("fs_23")
        self.gridLayout.addWidget(self.fs_23, 6, 0, 1, 1)
        self.s_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.s_reg_cfg.setObjectName("s_reg_cfg")
        self.gridLayout.addWidget(self.s_reg_cfg, 6, 1, 1, 1)
        self.f_reg_cfg = QtWidgets.QComboBox(self.groupBox)
        self.f_reg_cfg.setObjectName("f_reg_cfg")
        self.gridLayout.addWidget(self.f_reg_cfg, 5, 1, 1, 1)
        self.fs_20 = QtWidgets.QLabel(self.groupBox)
        self.fs_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_20.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_20.setObjectName("fs_20")
        self.gridLayout.addWidget(self.fs_20, 3, 0, 1, 1)
        self.fs_24 = QtWidgets.QLabel(self.groupBox)
        self.fs_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fs_24.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_24.setObjectName("fs_24")
        self.gridLayout.addWidget(self.fs_24, 7, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.logo = QtWidgets.QLabel(self.groupBox_10)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_8.addWidget(self.logo)
        self.gridLayout_7.addWidget(self.groupBox_10, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.read_button = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.read_button.setFont(font)
        self.read_button.setObjectName("read_button")
        self.gridLayout_2.addWidget(self.read_button, 0, 0, 1, 1)
        self.addr_textEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.addr_textEdit.setObjectName("addr_textEdit")
        self.gridLayout_2.addWidget(self.addr_textEdit, 1, 1, 1, 1)
        self.write_button = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.write_button.setFont(font)
        self.write_button.setObjectName("write_button")
        self.gridLayout_2.addWidget(self.write_button, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TR9XXX"))
        self.clk_option.setText(_translate("MainWindow", "CLK OPTION"))
        self.clk_option_cfg_button.setText(_translate("MainWindow", "..."))
        self.fs.setText(_translate("MainWindow", "ADC Sampling Rate"))
        self.fs_2.setText(_translate("MainWindow", "MHz"))
        self.fin.setText(_translate("MainWindow", "ADC input Freq"))
        self.fs_3.setText(_translate("MainWindow", "MHz"))
        self.fin_2.setText(_translate("MainWindow", "Lane rate"))
        self.fs_4.setText(_translate("MainWindow", "GHz"))
        self.fs_28.setText(_translate("MainWindow", "FFE"))
        self.sds_button.setText(_translate("MainWindow", "SDS update"))
        self.fs_26.setText(_translate("MainWindow", "refclk_div"))
        self.sds_button_3.setText(_translate("MainWindow", "test pattern clk0101"))
        self.sds_button_2.setText(_translate("MainWindow", "test pattern PRBS7"))
        self.fs_27.setText(_translate("MainWindow", "FBC div"))
        self.clk_option_2.setText(_translate("MainWindow", "SDS CONFIG"))
        self.DDC_CONFIG.setText(_translate("MainWindow", "DDC CONFIG"))
        self.fs_5.setText(_translate("MainWindow", "Chip Operating Mode"))
        self.fs_6.setText(_translate("MainWindow", "output_mode"))
        self.fs_29.setText(_translate("MainWindow", "mix_mode"))
        self.fs_30.setText(_translate("MainWindow", "freq_mode"))
        self.fs_31.setText(_translate("MainWindow", "gain_mode"))
        self.fs_7.setText(_translate("MainWindow", "DDC0 Configuration"))
        self.fs_8.setText(_translate("MainWindow", "DDC1 Configuration"))
        self.fs_9.setText(_translate("MainWindow", "DDC2 Configuration"))
        self.fs_10.setText(_translate("MainWindow", "DDC3 Configuration"))
        self.fs_11.setText(_translate("MainWindow", "DDC0 NCO"))
        self.fs_12.setText(_translate("MainWindow", "MHz"))
        self.fs_13.setText(_translate("MainWindow", "DDC1 NCO"))
        self.fs_14.setText(_translate("MainWindow", "MHz"))
        self.fs_15.setText(_translate("MainWindow", "DDC2 NCO"))
        self.fs_16.setText(_translate("MainWindow", "MHz"))
        self.fs_17.setText(_translate("MainWindow", "DDC3 NCO"))
        self.fs_18.setText(_translate("MainWindow", "MHz"))
        self.nco_update_pushButton.setText(_translate("MainWindow", "NCO update"))
        self.groupBox_9.setTitle(_translate("MainWindow", "SPI_CFG"))
        self.DDC_CONFIG_4.setText(_translate("MainWindow", "SPI_CFG"))
        self.label_3.setText(_translate("MainWindow", "SPI_CLK"))
        self.fs_32.setText(_translate("MainWindow", "MHz"))
        self.label_4.setText(_translate("MainWindow", "TranBits"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label_5.setText(_translate("MainWindow", "STATUS"))
        self.fs_19.setText(_translate("MainWindow", "N\'"))
        self.fs_25.setText(_translate("MainWindow", "N"))
        self.fs_22.setText(_translate("MainWindow", "F"))
        self.j204b_update_pushButton.setText(_translate("MainWindow", "204B update"))
        self.DDC_CONFIG_2.setText(_translate("MainWindow", "204B CONFIG"))
        self.fs_21.setText(_translate("MainWindow", "L"))
        self.init_button.setText(_translate("MainWindow", "Init"))
        self.mem_rd_button.setText(_translate("MainWindow", "MEM_RD"))
        self.fs_23.setText(_translate("MainWindow", "S"))
        self.fs_20.setText(_translate("MainWindow", "M"))
        self.fs_24.setText(_translate("MainWindow", "K"))
        self.read_button.setText(_translate("MainWindow", "READ"))
        self.write_button.setText(_translate("MainWindow", "WRITE"))
        self.label_2.setText(_translate("MainWindow", "addr"))
        self.label.setText(_translate("MainWindow", "data"))
import logo_rc
import status_rc
import struc_rc
import xxx_rc
