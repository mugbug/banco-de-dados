# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(679, 491)
        MainWindow.setStyleSheet(_fromUtf8("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color:#3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #18465d;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #18465d;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #76797C;\n"
"}\n"
"\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:indeterminate\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #76797C;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    color: #eff0f1;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #3daee9;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #232629;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit\n"
"{\n"
"    padding: 0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #232629;;\n"
"    color: #eff0f1;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #76797C;\n"
"    color: #eff0f1;\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #31363b;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #76797C;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #76797C;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #76797C;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #31363b;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbar.png);\n"
"}\n"
"QToolButton#qt_toolbar_ext_button {\n"
"    background: #58595a\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3daee9;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3daee9;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #76797C;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #232629;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"    selection-background-color: #18465d;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #76797C;\n"
"    padding: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #31363b;\n"
"    padding: 5px;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent black;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;    \n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #31363b;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-top: 1px transparent black;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #31363b;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-left: 1px transparent black;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #31363b;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-right: 1px transparent black;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    background: #31363b;\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    background-color: #232629;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: #18465d;\n"
"    outline: 0;\n"
"    color: #eff0f1\n"
"}\n"
"\n"
"QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #287399;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #565a5e;\n"
"    height: 4px;\n"
"    background: #565a5e;\n"
"    margin: 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #232629;\n"
"    border: 1px solid #565a5e;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -8px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #565a5e;\n"
"    width: 4px;\n"
"    background: #565a5e;\n"
"    margin: 0px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #232629;\n"
"    border: 1px solid #565a5e;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: 0 -8px;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px transparent #76797C;\n"
"    border-radius: 2px;\n"
"    margin: 3px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 1px #76797C;\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 1px #76797C;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid #3daee9;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"        QToolButton::menu-button:pressed {\n"
"    background-color: #3daee9;\n"
"    border: 1px solid #3daee9;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #76797C;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    gridline-color: #31363b;\n"
"    background-color: #232629;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #18465d;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #287399;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 1px transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #334e5e;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #31363b;\n"
"    border: 1px transparent #76797C;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 5px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent #31363b;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #31363b;\n"
"    border-color: #3daee9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 0px transparent dark;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #76797C;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"    selection-background-color: #3daee9;\n"
"    border-style: solid;\n"
"    border: 1px solid #3375A3;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QDateEdit:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView\n"
"{\n"
"    background-color: #232629;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3375A3;\n"
"    selection-background-color: #3daee9;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover,\n"
"QDateEdit::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.aluno = QtGui.QWidget()
        self.aluno.setGeometry(QtCore.QRect(0, 0, 651, 370))
        self.aluno.setObjectName(_fromUtf8("aluno"))
        self.gridLayout_3 = QtGui.QGridLayout(self.aluno)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aluno_create_widget = QtGui.QStackedWidget(self.aluno)
        self.aluno_create_widget.setObjectName(_fromUtf8("aluno_create_widget"))
        self.aluno1 = QtGui.QWidget()
        self.aluno1.setObjectName(_fromUtf8("aluno1"))
        self.gridLayout_8 = QtGui.QGridLayout(self.aluno1)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.aluno_lbl_semestre = QtGui.QLabel(self.aluno1)
        self.aluno_lbl_semestre.setObjectName(_fromUtf8("aluno_lbl_semestre"))
        self.gridLayout_2.addWidget(self.aluno_lbl_semestre, 4, 1, 1, 1)
        self.aluno_lbl_nome = QtGui.QLabel(self.aluno1)
        self.aluno_lbl_nome.setObjectName(_fromUtf8("aluno_lbl_nome"))
        self.gridLayout_2.addWidget(self.aluno_lbl_nome, 1, 1, 1, 1)
        self.aluno_lbl_curso = QtGui.QLabel(self.aluno1)
        self.aluno_lbl_curso.setObjectName(_fromUtf8("aluno_lbl_curso"))
        self.gridLayout_2.addWidget(self.aluno_lbl_curso, 5, 1, 1, 1)
        self.aluno_lbl_idade = QtGui.QLabel(self.aluno1)
        self.aluno_lbl_idade.setObjectName(_fromUtf8("aluno_lbl_idade"))
        self.gridLayout_2.addWidget(self.aluno_lbl_idade, 2, 1, 1, 1)
        self.aluno_lbl_matricula = QtGui.QLabel(self.aluno1)
        self.aluno_lbl_matricula.setObjectName(_fromUtf8("aluno_lbl_matricula"))
        self.gridLayout_2.addWidget(self.aluno_lbl_matricula, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 2, 1, 1)
        self.aluno_submeter = QtGui.QPushButton(self.aluno1)
        self.aluno_submeter.setMinimumSize(QtCore.QSize(100, 0))
        self.aluno_submeter.setMaximumSize(QtCore.QSize(150, 16777215))
        self.aluno_submeter.setObjectName(_fromUtf8("aluno_submeter"))
        self.gridLayout_2.addWidget(self.aluno_submeter, 6, 3, 1, 1)
        self.aluno_input_nome = QtGui.QLineEdit(self.aluno1)
        self.aluno_input_nome.setMinimumSize(QtCore.QSize(300, 0))
        self.aluno_input_nome.setObjectName(_fromUtf8("aluno_input_nome"))
        self.gridLayout_2.addWidget(self.aluno_input_nome, 1, 2, 1, 2)
        self.aluno_input_idade = QtGui.QSpinBox(self.aluno1)
        self.aluno_input_idade.setMaximum(130)
        self.aluno_input_idade.setObjectName(_fromUtf8("aluno_input_idade"))
        self.gridLayout_2.addWidget(self.aluno_input_idade, 2, 2, 1, 2)
        self.aluno_input_semestre = QtGui.QSpinBox(self.aluno1)
        self.aluno_input_semestre.setMinimum(1)
        self.aluno_input_semestre.setMaximum(10)
        self.aluno_input_semestre.setObjectName(_fromUtf8("aluno_input_semestre"))
        self.gridLayout_2.addWidget(self.aluno_input_semestre, 4, 2, 1, 2)
        self.aluno_input_curso = QtGui.QComboBox(self.aluno1)
        self.aluno_input_curso.setObjectName(_fromUtf8("aluno_input_curso"))
        self.gridLayout_2.addWidget(self.aluno_input_curso, 5, 2, 1, 2)
        self.aluno_input_matricula = QtGui.QSpinBox(self.aluno1)
        self.aluno_input_matricula.setMaximum(10000)
        self.aluno_input_matricula.setObjectName(_fromUtf8("aluno_input_matricula"))
        self.gridLayout_2.addWidget(self.aluno_input_matricula, 3, 2, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 0, 0, 1, 1)
        self.aluno_create_widget.addWidget(self.aluno1)
        self.aluno2 = QtGui.QWidget()
        self.aluno2.setObjectName(_fromUtf8("aluno2"))
        self.gridLayout_14 = QtGui.QGridLayout(self.aluno2)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.aluno_lbl_semestre_2 = QtGui.QLabel(self.aluno2)
        self.aluno_lbl_semestre_2.setObjectName(_fromUtf8("aluno_lbl_semestre_2"))
        self.gridLayout_13.addWidget(self.aluno_lbl_semestre_2, 3, 1, 1, 1)
        self.aluno_lbl_curso_2 = QtGui.QLabel(self.aluno2)
        self.aluno_lbl_curso_2.setObjectName(_fromUtf8("aluno_lbl_curso_2"))
        self.gridLayout_13.addWidget(self.aluno_lbl_curso_2, 4, 1, 1, 1)
        self.aluno_lbl_matricula_2 = QtGui.QLabel(self.aluno2)
        self.aluno_lbl_matricula_2.setObjectName(_fromUtf8("aluno_lbl_matricula_2"))
        self.gridLayout_13.addWidget(self.aluno_lbl_matricula_2, 2, 1, 1, 1)
        self.aluno_input_np2 = QtGui.QSpinBox(self.aluno2)
        self.aluno_input_np2.setMaximum(100)
        self.aluno_input_np2.setObjectName(_fromUtf8("aluno_input_np2"))
        self.gridLayout_13.addWidget(self.aluno_input_np2, 1, 2, 1, 2)
        self.aluno_lbl_idade_2 = QtGui.QLabel(self.aluno2)
        self.aluno_lbl_idade_2.setObjectName(_fromUtf8("aluno_lbl_idade_2"))
        self.gridLayout_13.addWidget(self.aluno_lbl_idade_2, 1, 1, 1, 1)
        self.aluno_lbl_nome_2 = QtGui.QLabel(self.aluno2)
        self.aluno_lbl_nome_2.setObjectName(_fromUtf8("aluno_lbl_nome_2"))
        self.gridLayout_13.addWidget(self.aluno_lbl_nome_2, 0, 1, 1, 1)
        self.aluno_input_situacao = QtGui.QLineEdit(self.aluno2)
        self.aluno_input_situacao.setObjectName(_fromUtf8("aluno_input_situacao"))
        self.gridLayout_13.addWidget(self.aluno_input_situacao, 4, 2, 1, 2)
        self.aluno_input_np1 = QtGui.QSpinBox(self.aluno2)
        self.aluno_input_np1.setMinimumSize(QtCore.QSize(87, 0))
        self.aluno_input_np1.setMaximum(100)
        self.aluno_input_np1.setObjectName(_fromUtf8("aluno_input_np1"))
        self.gridLayout_13.addWidget(self.aluno_input_np1, 0, 2, 1, 2)
        self.aluno_input_nf = QtGui.QSpinBox(self.aluno2)
        self.aluno_input_nf.setMinimum(1)
        self.aluno_input_nf.setMaximum(100)
        self.aluno_input_nf.setObjectName(_fromUtf8("aluno_input_nf"))
        self.gridLayout_13.addWidget(self.aluno_input_nf, 3, 2, 1, 2)
        self.aluno_input_np3 = QtGui.QSpinBox(self.aluno2)
        self.aluno_input_np3.setMaximum(100)
        self.aluno_input_np3.setObjectName(_fromUtf8("aluno_input_np3"))
        self.gridLayout_13.addWidget(self.aluno_input_np3, 2, 2, 1, 2)
        self.aluno_submeter_nota = QtGui.QPushButton(self.aluno2)
        self.aluno_submeter_nota.setObjectName(_fromUtf8("aluno_submeter_nota"))
        self.gridLayout_13.addWidget(self.aluno_submeter_nota, 5, 3, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem7, 0, 1, 1, 1)
        self.aluno_create_widget.addWidget(self.aluno2)
        self.aluno3 = QtGui.QWidget()
        self.aluno3.setObjectName(_fromUtf8("aluno3"))
        self.gridLayout_12 = QtGui.QGridLayout(self.aluno3)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem9, 3, 1, 1, 1)
        self.aluno_input_search = QtGui.QLineEdit(self.aluno3)
        self.aluno_input_search.setObjectName(_fromUtf8("aluno_input_search"))
        self.gridLayout_11.addWidget(self.aluno_input_search, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.aluno3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_11.addWidget(self.label, 1, 0, 1, 1)
        self.aluno_submeter_busca = QtGui.QPushButton(self.aluno3)
        self.aluno_submeter_busca.setObjectName(_fromUtf8("aluno_submeter_busca"))
        self.gridLayout_11.addWidget(self.aluno_submeter_busca, 1, 2, 1, 1)
        self.aluno_table = QtGui.QTableWidget(self.aluno3)
        self.aluno_table.setObjectName(_fromUtf8("aluno_table"))
        self.aluno_table.setColumnCount(5)
        self.aluno_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.aluno_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.aluno_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.aluno_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.aluno_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.aluno_table.setHorizontalHeaderItem(4, item)
        self.gridLayout_11.addWidget(self.aluno_table, 2, 0, 1, 3)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.aluno_create_widget.addWidget(self.aluno3)
        self.horizontalLayout.addWidget(self.aluno_create_widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.aluno_btn_create = QtGui.QPushButton(self.aluno)
        self.aluno_btn_create.setMinimumSize(QtCore.QSize(100, 0))
        self.aluno_btn_create.setObjectName(_fromUtf8("aluno_btn_create"))
        self.verticalLayout.addWidget(self.aluno_btn_create)
        self.aluno_btn_edit = QtGui.QPushButton(self.aluno)
        self.aluno_btn_edit.setObjectName(_fromUtf8("aluno_btn_edit"))
        self.verticalLayout.addWidget(self.aluno_btn_edit)
        self.aluno_btn_search = QtGui.QPushButton(self.aluno)
        self.aluno_btn_search.setObjectName(_fromUtf8("aluno_btn_search"))
        self.verticalLayout.addWidget(self.aluno_btn_search)
        self.aluno_btn_list = QtGui.QPushButton(self.aluno)
        self.aluno_btn_list.setObjectName(_fromUtf8("aluno_btn_list"))
        self.verticalLayout.addWidget(self.aluno_btn_list)
        self.aluno_btn_remove = QtGui.QPushButton(self.aluno)
        self.aluno_btn_remove.setObjectName(_fromUtf8("aluno_btn_remove"))
        self.verticalLayout.addWidget(self.aluno_btn_remove)
        self.aluno_btn_nota = QtGui.QPushButton(self.aluno)
        self.aluno_btn_nota.setObjectName(_fromUtf8("aluno_btn_nota"))
        self.verticalLayout.addWidget(self.aluno_btn_nota)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.toolBox.addItem(self.aluno, _fromUtf8(""))
        self.curso = QtGui.QWidget()
        self.curso.setGeometry(QtCore.QRect(0, 0, 651, 370))
        self.curso.setObjectName(_fromUtf8("curso"))
        self.gridLayout_5 = QtGui.QGridLayout(self.curso)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.curso_create_widget = QtGui.QStackedWidget(self.curso)
        self.curso_create_widget.setObjectName(_fromUtf8("curso_create_widget"))
        self.curso1 = QtGui.QWidget()
        self.curso1.setObjectName(_fromUtf8("curso1"))
        self.gridLayout_9 = QtGui.QGridLayout(self.curso1)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.curso_input_nome = QtGui.QLineEdit(self.curso1)
        self.curso_input_nome.setMinimumSize(QtCore.QSize(300, 0))
        self.curso_input_nome.setObjectName(_fromUtf8("curso_input_nome"))
        self.gridLayout_4.addWidget(self.curso_input_nome, 0, 1, 1, 2)
        self.curso_lbl_duracao = QtGui.QLabel(self.curso1)
        self.curso_lbl_duracao.setObjectName(_fromUtf8("curso_lbl_duracao"))
        self.gridLayout_4.addWidget(self.curso_lbl_duracao, 1, 0, 1, 1)
        self.curso_lbl_nome = QtGui.QLabel(self.curso1)
        self.curso_lbl_nome.setObjectName(_fromUtf8("curso_lbl_nome"))
        self.gridLayout_4.addWidget(self.curso_lbl_nome, 0, 0, 1, 1)
        self.curso_input_duracao = QtGui.QSpinBox(self.curso1)
        self.curso_input_duracao.setMaximum(130)
        self.curso_input_duracao.setObjectName(_fromUtf8("curso_input_duracao"))
        self.gridLayout_4.addWidget(self.curso_input_duracao, 1, 1, 1, 2)
        self.curso_submeter = QtGui.QPushButton(self.curso1)
        self.curso_submeter.setMinimumSize(QtCore.QSize(100, 0))
        self.curso_submeter.setMaximumSize(QtCore.QSize(150, 16777215))
        self.curso_submeter.setObjectName(_fromUtf8("curso_submeter"))
        self.gridLayout_4.addWidget(self.curso_submeter, 2, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem12, 1, 2, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem13, 1, 0, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem14, 2, 1, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem15, 0, 1, 1, 1)
        self.curso_create_widget.addWidget(self.curso1)
        self.curso2 = QtGui.QWidget()
        self.curso2.setObjectName(_fromUtf8("curso2"))
        self.gridLayout_16 = QtGui.QGridLayout(self.curso2)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.curso_lbl_nome_2 = QtGui.QLabel(self.curso2)
        self.curso_lbl_nome_2.setObjectName(_fromUtf8("curso_lbl_nome_2"))
        self.gridLayout_15.addWidget(self.curso_lbl_nome_2, 1, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem16, 3, 1, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem17, 0, 1, 1, 1)
        self.curso_input_search = QtGui.QLineEdit(self.curso2)
        self.curso_input_search.setObjectName(_fromUtf8("curso_input_search"))
        self.gridLayout_15.addWidget(self.curso_input_search, 1, 1, 1, 1)
        self.curso_submeter_busca = QtGui.QPushButton(self.curso2)
        self.curso_submeter_busca.setObjectName(_fromUtf8("curso_submeter_busca"))
        self.gridLayout_15.addWidget(self.curso_submeter_busca, 1, 2, 1, 1)
        self.curso_table = QtGui.QTableWidget(self.curso2)
        self.curso_table.setObjectName(_fromUtf8("curso_table"))
        self.curso_table.setColumnCount(3)
        self.curso_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.curso_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.curso_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.curso_table.setHorizontalHeaderItem(2, item)
        self.gridLayout_15.addWidget(self.curso_table, 2, 0, 1, 3)
        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.curso_create_widget.addWidget(self.curso2)
        self.horizontalLayout_2.addWidget(self.curso_create_widget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.curso_btn_create = QtGui.QPushButton(self.curso)
        self.curso_btn_create.setMinimumSize(QtCore.QSize(100, 0))
        self.curso_btn_create.setObjectName(_fromUtf8("curso_btn_create"))
        self.verticalLayout_2.addWidget(self.curso_btn_create)
        self.curso_btn_edit = QtGui.QPushButton(self.curso)
        self.curso_btn_edit.setObjectName(_fromUtf8("curso_btn_edit"))
        self.verticalLayout_2.addWidget(self.curso_btn_edit)
        self.curso_btn_search = QtGui.QPushButton(self.curso)
        self.curso_btn_search.setObjectName(_fromUtf8("curso_btn_search"))
        self.verticalLayout_2.addWidget(self.curso_btn_search)
        self.curso_btn_list = QtGui.QPushButton(self.curso)
        self.curso_btn_list.setObjectName(_fromUtf8("curso_btn_list"))
        self.verticalLayout_2.addWidget(self.curso_btn_list)
        self.curso_btn_remove = QtGui.QPushButton(self.curso)
        self.curso_btn_remove.setObjectName(_fromUtf8("curso_btn_remove"))
        self.verticalLayout_2.addWidget(self.curso_btn_remove)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.curso, _fromUtf8(""))
        self.materia = QtGui.QWidget()
        self.materia.setGeometry(QtCore.QRect(0, 0, 651, 370))
        self.materia.setObjectName(_fromUtf8("materia"))
        self.gridLayout_7 = QtGui.QGridLayout(self.materia)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.materia_create = QtGui.QStackedWidget(self.materia)
        self.materia_create.setObjectName(_fromUtf8("materia_create"))
        self.materia1 = QtGui.QWidget()
        self.materia1.setObjectName(_fromUtf8("materia1"))
        self.gridLayout_10 = QtGui.QGridLayout(self.materia1)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.materia_lbl_aulas = QtGui.QLabel(self.materia1)
        self.materia_lbl_aulas.setObjectName(_fromUtf8("materia_lbl_aulas"))
        self.gridLayout_6.addWidget(self.materia_lbl_aulas, 1, 0, 1, 1)
        self.materia_lbl_nome = QtGui.QLabel(self.materia1)
        self.materia_lbl_nome.setObjectName(_fromUtf8("materia_lbl_nome"))
        self.gridLayout_6.addWidget(self.materia_lbl_nome, 0, 0, 1, 1)
        self.materia_input_aulas = QtGui.QSpinBox(self.materia1)
        self.materia_input_aulas.setMaximum(500)
        self.materia_input_aulas.setObjectName(_fromUtf8("materia_input_aulas"))
        self.gridLayout_6.addWidget(self.materia_input_aulas, 1, 1, 1, 2)
        self.materia_input_nome = QtGui.QLineEdit(self.materia1)
        self.materia_input_nome.setMinimumSize(QtCore.QSize(300, 0))
        self.materia_input_nome.setObjectName(_fromUtf8("materia_input_nome"))
        self.gridLayout_6.addWidget(self.materia_input_nome, 0, 1, 1, 2)
        self.materia_submeter = QtGui.QPushButton(self.materia1)
        self.materia_submeter.setMinimumSize(QtCore.QSize(100, 0))
        self.materia_submeter.setMaximumSize(QtCore.QSize(150, 16777215))
        self.materia_submeter.setObjectName(_fromUtf8("materia_submeter"))
        self.gridLayout_6.addWidget(self.materia_submeter, 2, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem20, 1, 2, 1, 1)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem21, 1, 0, 1, 1)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem22, 0, 1, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem23, 2, 1, 1, 1)
        self.materia_create.addWidget(self.materia1)
        self.materia2 = QtGui.QWidget()
        self.materia2.setObjectName(_fromUtf8("materia2"))
        self.gridLayout_18 = QtGui.QGridLayout(self.materia2)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.gridLayout_17 = QtGui.QGridLayout()
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.materia_lbl_nome_2 = QtGui.QLabel(self.materia2)
        self.materia_lbl_nome_2.setObjectName(_fromUtf8("materia_lbl_nome_2"))
        self.gridLayout_17.addWidget(self.materia_lbl_nome_2, 1, 0, 1, 1)
        self.materia_input_search = QtGui.QLineEdit(self.materia2)
        self.materia_input_search.setObjectName(_fromUtf8("materia_input_search"))
        self.gridLayout_17.addWidget(self.materia_input_search, 1, 1, 1, 1)
        spacerItem24 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem24, 0, 1, 1, 1)
        spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem25, 3, 1, 1, 1)
        self.materia_submeter_busca = QtGui.QPushButton(self.materia2)
        self.materia_submeter_busca.setObjectName(_fromUtf8("materia_submeter_busca"))
        self.gridLayout_17.addWidget(self.materia_submeter_busca, 1, 2, 1, 1)
        self.materia_table = QtGui.QTableWidget(self.materia2)
        self.materia_table.setObjectName(_fromUtf8("materia_table"))
        self.materia_table.setColumnCount(3)
        self.materia_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.materia_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.materia_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.materia_table.setHorizontalHeaderItem(2, item)
        self.gridLayout_17.addWidget(self.materia_table, 2, 0, 1, 3)
        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.materia_create.addWidget(self.materia2)
        self.horizontalLayout_3.addWidget(self.materia_create)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem26 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem26)
        self.materia_btn_create = QtGui.QPushButton(self.materia)
        self.materia_btn_create.setMinimumSize(QtCore.QSize(100, 0))
        self.materia_btn_create.setObjectName(_fromUtf8("materia_btn_create"))
        self.verticalLayout_3.addWidget(self.materia_btn_create)
        self.materia_btn_edit = QtGui.QPushButton(self.materia)
        self.materia_btn_edit.setObjectName(_fromUtf8("materia_btn_edit"))
        self.verticalLayout_3.addWidget(self.materia_btn_edit)
        self.materia_btn_search = QtGui.QPushButton(self.materia)
        self.materia_btn_search.setObjectName(_fromUtf8("materia_btn_search"))
        self.verticalLayout_3.addWidget(self.materia_btn_search)
        self.materia_btn_list = QtGui.QPushButton(self.materia)
        self.materia_btn_list.setObjectName(_fromUtf8("materia_btn_list"))
        self.verticalLayout_3.addWidget(self.materia_btn_list)
        self.materia_btn_remove = QtGui.QPushButton(self.materia)
        self.materia_btn_remove.setObjectName(_fromUtf8("materia_btn_remove"))
        self.verticalLayout_3.addWidget(self.materia_btn_remove)
        spacerItem27 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem27)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.materia, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(2)
        self.aluno_create_widget.setCurrentIndex(2)
        self.curso_create_widget.setCurrentIndex(1)
        self.materia_create.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.aluno_lbl_semestre.setText(_translate("MainWindow", "Semestre", None))
        self.aluno_lbl_nome.setText(_translate("MainWindow", "Nome", None))
        self.aluno_lbl_curso.setText(_translate("MainWindow", "Curso", None))
        self.aluno_lbl_idade.setText(_translate("MainWindow", "Idade", None))
        self.aluno_lbl_matricula.setText(_translate("MainWindow", "Matricula", None))
        self.aluno_submeter.setText(_translate("MainWindow", "Submeter", None))
        self.aluno_lbl_semestre_2.setText(_translate("MainWindow", "NF", None))
        self.aluno_lbl_curso_2.setText(_translate("MainWindow", "Situaçao", None))
        self.aluno_lbl_matricula_2.setText(_translate("MainWindow", "NP3", None))
        self.aluno_lbl_idade_2.setText(_translate("MainWindow", "NP2", None))
        self.aluno_lbl_nome_2.setText(_translate("MainWindow", "NP1", None))
        self.aluno_submeter_nota.setText(_translate("MainWindow", "Submeter", None))
        self.label.setText(_translate("MainWindow", "Nome", None))
        self.aluno_submeter_busca.setText(_translate("MainWindow", "Pesquisar", None))
        item = self.aluno_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome", None))
        item = self.aluno_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Idade", None))
        item = self.aluno_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Matricula", None))
        item = self.aluno_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Semestre", None))
        item = self.aluno_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Curso", None))
        self.aluno_btn_create.setText(_translate("MainWindow", "Criar", None))
        self.aluno_btn_edit.setText(_translate("MainWindow", "Editar", None))
        self.aluno_btn_search.setText(_translate("MainWindow", "Pesquisar", None))
        self.aluno_btn_list.setText(_translate("MainWindow", "Listar", None))
        self.aluno_btn_remove.setText(_translate("MainWindow", "Deletar", None))
        self.aluno_btn_nota.setText(_translate("MainWindow", "Adicionar Nota", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.aluno), _translate("MainWindow", "Aluno", None))
        self.curso_lbl_duracao.setText(_translate("MainWindow", "Carga Horaria", None))
        self.curso_lbl_nome.setText(_translate("MainWindow", "Nome", None))
        self.curso_submeter.setText(_translate("MainWindow", "Submeter", None))
        self.curso_lbl_nome_2.setText(_translate("MainWindow", "Nome", None))
        self.curso_submeter_busca.setText(_translate("MainWindow", "Pesquisar", None))
        item = self.curso_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome", None))
        item = self.curso_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Carga Horaria", None))
        item = self.curso_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Numero de Alunos", None))
        self.curso_btn_create.setText(_translate("MainWindow", "Criar", None))
        self.curso_btn_edit.setText(_translate("MainWindow", "Editar", None))
        self.curso_btn_search.setText(_translate("MainWindow", "Pesquisar", None))
        self.curso_btn_list.setText(_translate("MainWindow", "Listar", None))
        self.curso_btn_remove.setText(_translate("MainWindow", "Deletar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.curso), _translate("MainWindow", "Curso", None))
        self.materia_lbl_aulas.setText(_translate("MainWindow", "Numero de Aulas", None))
        self.materia_lbl_nome.setText(_translate("MainWindow", "Nome", None))
        self.materia_submeter.setText(_translate("MainWindow", "Submeter", None))
        self.materia_lbl_nome_2.setText(_translate("MainWindow", "Nome", None))
        self.materia_submeter_busca.setText(_translate("MainWindow", "Pesquisar", None))
        item = self.materia_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome", None))
        item = self.materia_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Curso", None))
        item = self.materia_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Numero de Aulas", None))
        self.materia_btn_create.setText(_translate("MainWindow", "Criar", None))
        self.materia_btn_edit.setText(_translate("MainWindow", "Editar", None))
        self.materia_btn_search.setText(_translate("MainWindow", "Pesquisar", None))
        self.materia_btn_list.setText(_translate("MainWindow", "Listar", None))
        self.materia_btn_remove.setText(_translate("MainWindow", "Deletar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.materia), _translate("MainWindow", "Materia", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

