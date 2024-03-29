# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesignerivmax.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os, time
import IVMax as backend

class Ui_IVMax(object):
    def setupUi(self, IVMax):
        dirname = os.path.dirname(__file__)+"/"
        self.PkDict={}
        self.PkDict["Torchic"]=0
        self.PkDict["Squirtle"]=1
        self.PkDict["Turtwig"]=2

        self.PkIndex=0 #index to identify the pokemon
        self.N=4
        self.generations=2

        # region MainWindow
        IVMax.setObjectName("IVMax")
        IVMax.resize(1500, 900)
        IVMax.setMinimumSize(QtCore.QSize(1000, 500))
        IVMax.setStyleSheet(
                "QMainWindow{\n"
                "background-color: rgb(45, 45, 45);\n"
                "}"
        )
        # endregion
        # region Layout
        self.centralwidget = QtWidgets.QWidget(IVMax)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        # endregion
        # region TopBar
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Top_Bar.setStyleSheet(
                "QFrame{\n"
                "    background-color: rgb(20, 20, 40);\n"
                "}\n"
                "QComboBox {\n"
                "color: white;\n"
                "selection-color: rgb(0, 255, 255);\n"
                "border: 0px transparent;\n"
                "padding: 1px, 1px, 1px, 1px;\n"
                "background-color: rgb(20, 20, 40);\n"
                "}\n"
                "QListView {\n"
                "color:white;\n"
                "background-color: rgb(20, 20, 40);\n"
                "}")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        # region AppIcon
        self.AppIcon = QtWidgets.QLabel(self.Top_Bar)
        self.AppIcon.setGeometry(QtCore.QRect(40, 20, 61, 61))
        self.AppIcon.setPixmap(QtGui.QPixmap(dirname+"assets/60IVMaxLogoArtboard.png"))
        self.AppIcon.setObjectName("AppIcon")
        self.AppIconLetters = QtWidgets.QLabel(self.Top_Bar)
        self.AppIconLetters.setGeometry(QtCore.QRect(130, 27, 121, 41))
        self.AppIconLetters.setPixmap(QtGui.QPixmap(dirname+"assets/60IVMaxLetterArtboard.png"))
        self.AppIconLetters.setObjectName("AppIconLetters")
        # endregion
        # region Pokemon_Combobox
        self.Pokemon_ComboBox = QtWidgets.QComboBox(self.Top_Bar)
        self.Pokemon_ComboBox.setGeometry(QtCore.QRect(1230, 18, 240, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 40))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Pokemon_ComboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gilroy-MediumItalic")
        font.setPointSize(32)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Pokemon_ComboBox.setFont(font)
        self.Pokemon_ComboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Pokemon_ComboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Pokemon_ComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Pokemon_ComboBox.setEditable(False)
        self.Pokemon_ComboBox.setMaxCount(3)
        self.Pokemon_ComboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.Pokemon_ComboBox.setIconSize(QtCore.QSize(16, 16))
        self.Pokemon_ComboBox.setFrame(False)
        self.Pokemon_ComboBox.setObjectName("Pokemon_ComboBox")
        self.Pokemon_ComboBox.addItem("")
        self.Pokemon_ComboBox.addItem("")
        self.Pokemon_ComboBox.addItem("")
        self.Pokemon_Line = QtWidgets.QFrame(self.Top_Bar)
        self.Pokemon_Line.setGeometry(QtCore.QRect(1213, 76, 240, 16))
        self.Pokemon_Line.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 150, 214, 255), stop:1 rgba(202, 71, 255, 255));")
        self.Pokemon_Line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Pokemon_Line.setLineWidth(3)
        self.Pokemon_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Pokemon_Line.setObjectName("Pokemon_Line")
        # endregion
        # region Rights
        self.Rights = QtWidgets.QLabel(self.Top_Bar)
        self.Rights.setGeometry(QtCore.QRect(246, 47, 271, 21))
        font.setFamily("Gilroy-BoldItalic")
        font.setPointSize(12)
        font.setItalic(True)
        self.Rights.setFont(font)
        self.Rights.setStyleSheet(
                "color: white;\n"
                "background-color: transparent\n"
        )
        self.Rights.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rights.setObjectName("Rights")
        # endregion
        self.verticalLayout.addWidget(self.Top_Bar)
        # endregion
        # region Content
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setStyleSheet(
                "QFrame{\n"
                "background-color: rgb(38, 36, 68);\n"
                "}")
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        # region IVCard
        self.IVCard = QtWidgets.QFrame(self.Content)
        self.IVCard.setGeometry(QtCore.QRect(25, 450, 1450, 320))
        self.IVCard.setStyleSheet(
                "QFrame{\n"
                "background-color: rgb(33, 31, 63);\n"
                "border-radius: 60px;\n"
                "}"
                "QLabel{\n"
                "color: white;\n"
                "background-color: transparent;\n"
                "}\n"
                "QProgressBar{\n"
                "background-color: rgba(0, 0, 0, 120);\n"
                "border: 0px transparent;\n"
                "border-radius: 6px;\n"
                "}\n"
                "QProgressBar::chunk {\n"
                "border: 0px transparent;\n"
                "border-radius: 6px;\n"
                "}\n")
        self.IVCard.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.IVCard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IVCard.setObjectName("IVCard")
        # region StaticElements
        self.IVBackground = QtWidgets.QLabel(self.IVCard)
        self.IVBackground.setGeometry(QtCore.QRect(136, 40, 1250, 240))
        self.IVBackground.setStyleSheet("border: 0px transparent;")
        self.IVBackground.setPixmap(QtGui.QPixmap(dirname+"assets/IVStatsTableArtboard.png"))
        self.IVBackground.setObjectName("IVBackground")
        self.OutputText = QtWidgets.QLabel(self.IVCard)
        self.OutputText.setGeometry(QtCore.QRect(40, 40, 60, 260))
        self.OutputText.setPixmap(QtGui.QPixmap(dirname+"assets/OutputArtboard.png"))
        self.OutputText.setObjectName("OutputText")
        # endregion
        # region IVBars
        self.IVHP = QtWidgets.QProgressBar(self.IVCard)
        self.IVHP.setGeometry(QtCore.QRect(260, 60, 12, 200))
        self.IVHP.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.514, y2:0, stop:0 rgba(220, 64, 82, 255), stop:1 rgba(248, 185, 73, 255));\n"
                "}")
        self.IVHP.setProperty("value", 0)
        self.IVHP.setMaximum(31)
        self.IVHP.setTextVisible(False)
        self.IVHP.setOrientation(QtCore.Qt.Vertical)
        self.IVHP.setObjectName("IVHP")
        self.IVAtk = QtWidgets.QProgressBar(self.IVCard)
        self.IVAtk.setGeometry(QtCore.QRect(481, 60, 12, 200))
        self.IVAtk.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.446, y1:1, x2:0.554, y2:0, stop:0 rgba(255, 143, 75, 255), stop:1 rgba(213, 188, 62, 255));\n"
                "}")
        self.IVAtk.setProperty("value", 0)
        self.IVAtk.setMaximum(31)
        self.IVAtk.setTextVisible(False)
        self.IVAtk.setOrientation(QtCore.Qt.Vertical)
        self.IVAtk.setObjectName("IVAtk")
        self.IVDef = QtWidgets.QProgressBar(self.IVCard)
        self.IVDef.setGeometry(QtCore.QRect(702, 60, 12, 200))
        self.IVDef.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.497, y1:1, x2:0.452, y2:0, stop:0 rgba(199, 200, 58, 255), stop:1 rgba(163, 255, 75, 255));\n"
                "}")
        self.IVDef.setProperty("value", 0)
        self.IVDef.setMaximum(31)
        self.IVDef.setTextVisible(False)
        self.IVDef.setOrientation(QtCore.Qt.Vertical)
        self.IVDef.setObjectName("IVDef")
        self.IVSpAtk = QtWidgets.QProgressBar(self.IVCard)
        self.IVSpAtk.setGeometry(QtCore.QRect(921, 60, 12, 200))
        self.IVSpAtk.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.537, y1:1, x2:0.497, y2:0.00568182, stop:0 rgba(133, 255, 75, 255), stop:1 rgba(75, 255, 199, 255));\n"
                "}")
        self.IVSpAtk.setProperty("value", 0)
        self.IVSpAtk.setMaximum(31)
        self.IVSpAtk.setTextVisible(False)
        self.IVSpAtk.setOrientation(QtCore.Qt.Vertical)
        self.IVSpAtk.setObjectName("IVSpAtk")
        self.IVSpDef = QtWidgets.QProgressBar(self.IVCard)
        self.IVSpDef.setGeometry(QtCore.QRect(1143, 60, 12, 200))
        self.IVSpDef.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.503, y1:1, x2:0.458, y2:0, stop:0 rgba(75, 221, 255, 255), stop:1 rgba(103, 75, 255, 255));\n"
                "}")
        self.IVSpDef.setProperty("value", 0)
        self.IVSpDef.setMaximum(31)
        self.IVSpDef.setTextVisible(False)
        self.IVSpDef.setOrientation(QtCore.Qt.Vertical)
        self.IVSpDef.setObjectName("IVSpDef")
        self.IVSpd = QtWidgets.QProgressBar(self.IVCard)
        self.IVSpd.setGeometry(QtCore.QRect(1363, 60, 12, 200))
        self.IVSpd.setStyleSheet(
                "QProgressBar::chunk {\n"
                "    background-color: qlineargradient(spread:pad, x1:0.581921, y1:1, x2:0.514, y2:0, stop:0 rgba(133, 75, 255, 255), stop:1 rgba(255, 75, 219, 255));\n"
                "}")
        self.IVSpd.setProperty("value", 0)
        self.IVSpd.setMaximum(31)
        self.IVSpd.setTextVisible(False)
        self.IVSpd.setOrientation(QtCore.Qt.Vertical)
        self.IVSpd.setObjectName("IVSpd")
        # endregion
        # region IVLabels
        font.setFamily("Gilroy-BoldItalic")
        font.setPointSize(42)
        font.setItalic(True)
        self.IVHPLabel = QtWidgets.QLabel(self.IVCard)
        self.IVHPLabel.setGeometry(QtCore.QRect(150, 175, 71, 51))
        self.IVHPLabel.setFont(font)
        self.IVHPLabel.setObjectName("IVHPLabel")
        self.IVAtkLabel = QtWidgets.QLabel(self.IVCard)
        self.IVAtkLabel.setGeometry(QtCore.QRect(370, 175, 71, 51))
        self.IVAtkLabel.setFont(font)
        self.IVAtkLabel.setObjectName("IVAtkLabel")
        self.IVDefLabel = QtWidgets.QLabel(self.IVCard)
        self.IVDefLabel.setGeometry(QtCore.QRect(590, 175, 71, 51))
        self.IVDefLabel.setFont(font)
        self.IVDefLabel.setObjectName("IVDefLabel")
        self.IVSpAtkLabel = QtWidgets.QLabel(self.IVCard)
        self.IVSpAtkLabel.setGeometry(QtCore.QRect(810, 175, 71, 51))
        self.IVSpAtkLabel.setFont(font)
        self.IVSpAtkLabel.setObjectName("IVSpAtkLabel")
        self.IVSpDefLabel = QtWidgets.QLabel(self.IVCard)
        self.IVSpDefLabel.setGeometry(QtCore.QRect(1030, 175, 71, 51))
        self.IVSpDefLabel.setFont(font)
        self.IVSpDefLabel.setObjectName("IVSpDefLabel")
        self.IVSpLabel = QtWidgets.QLabel(self.IVCard)
        self.IVSpLabel.setGeometry(QtCore.QRect(1250, 175, 71, 51))
        self.IVSpLabel.setFont(font)
        self.IVSpLabel.setObjectName("IVSpLabel")
        # endregion
        # region Generations
        font.setUnderline(True)
        self.ActualGenLabel = QtWidgets.QLabel(self.IVCard)
        self.ActualGenLabel.setGeometry(QtCore.QRect(20, 240, 71, 51))
        self.ActualGenLabel.setFont(font)
        self.ActualGenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ActualGenLabel.setObjectName("ActualGenLabel")
        self.ActualGenText = QtWidgets.QLabel(self.IVCard)
        self.ActualGenText.setGeometry(QtCore.QRect(20, 190, 71, 51))
        font.setFamily("Gilroy-BoldItalic")
        font.setPointSize(22)
        font.setItalic(True)
        font.setUnderline(False)
        self.ActualGenText.setFont(font)
        self.ActualGenText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ActualGenText.setObjectName("ActualGenText")
        # endregion
        # region RaiseElements()
        self.IVBackground.raise_()
        self.IVHP.raise_()
        self.IVAtk.raise_()
        self.IVDef.raise_()
        self.IVSpAtk.raise_()
        self.IVSpDef.raise_()
        self.IVSpd.raise_()
        self.OutputText.raise_()
        self.IVHPLabel.raise_()
        self.IVAtkLabel.raise_()
        self.IVDefLabel.raise_()
        self.IVSpAtkLabel.raise_()
        self.IVSpDefLabel.raise_()
        self.IVSpLabel.raise_()
        self.ActualGenLabel.raise_()
        self.ActualGenText.raise_()
        # endregion
        # endregion
        # region PokemonCard
        self.PokemonCard = QtWidgets.QFrame(self.Content)
        self.PokemonCard.setGeometry(QtCore.QRect(25, 30, 1450, 391))
        self.PokemonCard.setStyleSheet(
                "QFrame{\n"
                "background-color: rgb(33, 31, 63);\n"
                "border-radius: 60px;\n"
                "}\n"
                "QLabel{\n"
                "color: white;\n"
                "background-color: transparent;\n"
                "}")
        self.PokemonCard.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PokemonCard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PokemonCard.setObjectName("PokemonCard")
        # region Sliders
        self.GenSlider = QtWidgets.QSlider(self.PokemonCard)
        self.GenSlider.setGeometry(QtCore.QRect(140, 280, 371, 22))
        self.GenSlider.setMinimum(2)
        self.GenSlider.setMaximum(16)
        self.GenSlider.setSingleStep(2)
        self.GenSlider.setPageStep(4)
        self.GenSlider.setProperty("value", 2)
        self.GenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GenSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.GenSlider.setTickInterval(1)
        self.GenSlider.setTracking(False)
        self.GenSlider.setObjectName("GenSlider")
        self.SubjectsSlider = QtWidgets.QSlider(self.PokemonCard)
        self.SubjectsSlider.setGeometry(QtCore.QRect(140, 140, 371, 22))
        self.SubjectsSlider.setMinimum(2)
        self.SubjectsSlider.setMaximum(8)
        self.SubjectsSlider.setSingleStep(2)
        self.SubjectsSlider.setPageStep(4)
        self.SubjectsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SubjectsSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.SubjectsSlider.setTickInterval(1)
        self.SubjectsSlider.setObjectName("SubjectsSlider")
        # endregion
        # region StaticElements
        self.StatsBackground = QtWidgets.QLabel(self.PokemonCard)
        self.StatsBackground.setGeometry(QtCore.QRect(710, 40, 400, 300))
        self.StatsBackground.setPixmap(QtGui.QPixmap(dirname+"assets/StatsTableArtboard.png"))
        self.StatsBackground.setObjectName("StatsBackground")
        self.VariablesText = QtWidgets.QLabel(self.PokemonCard)
        self.VariablesText.setGeometry(QtCore.QRect(40, 60, 60, 260))
        self.VariablesText.setPixmap(QtGui.QPixmap(dirname+"assets/VariablesArtboard.png"))
        self.VariablesText.setObjectName("VariablesText")
        # endregion
        # region Status and text
        self.SubjectsStatus = QtWidgets.QLabel(self.PokemonCard)
        self.SubjectsStatus.setGeometry(QtCore.QRect(560, 120, 51, 51))
        self.SubjectsStatus.setStyleSheet(
                "font: italic 32pt \"Gilroy-BoldItalic\";\n")
        self.SubjectsStatus.setObjectName("SubjectsStatus")
        self.SubjectsLabel = QtWidgets.QLabel(self.PokemonCard)
        self.SubjectsLabel.setGeometry(QtCore.QRect(130, 60, 421, 51))
        self.SubjectsLabel.setStyleSheet(
                "font: italic 32pt \"Gilroy-BoldItalic\";\n")
        self.SubjectsLabel.setObjectName("SubjectsLabel")
        self.GenStatus = QtWidgets.QLabel(self.PokemonCard)
        self.GenStatus.setGeometry(QtCore.QRect(560, 260, 51, 51))
        self.GenStatus.setStyleSheet(
                "font: italic 32pt \"Gilroy-BoldItalic\";\n")
        self.GenStatus.setObjectName("GenStatus")
        self.GenLabel = QtWidgets.QLabel(self.PokemonCard)
        self.GenLabel.setGeometry(QtCore.QRect(130, 200, 491, 51))
        self.GenLabel.setStyleSheet(
                "font: italic 32pt \"Gilroy-BoldItalic\";\n")
        self.GenLabel.setObjectName("GenLabel")
        # endregion
        # region PkSprite
        self.PokemonSprite = QtWidgets.QLabel(self.PokemonCard)
        self.PokemonSprite.setGeometry(QtCore.QRect(1140, 40, 300, 300))
        self.PokemonSprite.setPixmap(QtGui.QPixmap(dirname+"assets/Torchic.png"))
        self.PokemonSprite.setObjectName("PokemonSprite")
        # endregion
        # region StatsLabels
        font.setFamily("Gilroy-BoldItalic")
        font.setPointSize(26)
        font.setItalic(True)
        self.HpLabel = QtWidgets.QLabel(self.PokemonCard)
        self.HpLabel.setGeometry(QtCore.QRect(730, 110, 81, 41))
        self.HpLabel.setFont(font)
        self.HpLabel.setObjectName("HpLabel")
        self.AtkLabel = QtWidgets.QLabel(self.PokemonCard)
        self.AtkLabel.setGeometry(QtCore.QRect(870, 110, 81, 41))
        self.AtkLabel.setFont(font)
        self.AtkLabel.setObjectName("AtkLabel")
        self.DefLabel = QtWidgets.QLabel(self.PokemonCard)
        self.DefLabel.setGeometry(QtCore.QRect(1010, 110, 81, 41))
        self.DefLabel.setFont(font)
        self.DefLabel.setObjectName("DefLabel")
        self.SpAtkLabel = QtWidgets.QLabel(self.PokemonCard)
        self.SpAtkLabel.setGeometry(QtCore.QRect(730, 263, 81, 41))
        self.SpAtkLabel.setFont(font)
        self.SpAtkLabel.setObjectName("SpAtkLabel")
        self.SpDefLabel = QtWidgets.QLabel(self.PokemonCard)
        self.SpDefLabel.setGeometry(QtCore.QRect(870, 263, 81, 41))
        self.SpDefLabel.setFont(font)
        self.SpDefLabel.setObjectName("SpDefLabel")
        self.VelLabel = QtWidgets.QLabel(self.PokemonCard)
        self.VelLabel.setGeometry(QtCore.QRect(1010, 263, 81, 41))
        self.VelLabel.setFont(font)
        self.VelLabel.setObjectName("VelLabel")
        # endregion 
        # region designedBy
        self.designedBy = QtWidgets.QLabel(self.PokemonCard)
        self.designedBy.setGeometry(QtCore.QRect(1400, 80, 40, 241))
        self.designedBy.setPixmap(QtGui.QPixmap(dirname+"assets/designedByArtboard.png"))
        self.designedBy.setObjectName("designedBy")
        # endregion
        # region Fitness
        self.FitText = QtWidgets.QLabel(self.PokemonCard)
        self.FitText.setGeometry(QtCore.QRect(20, 260, 71, 51))
        font.setPointSize(22)
        self.FitText.setFont(font)
        self.FitText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FitText.setObjectName("FitText")
        self.FitLabel = QtWidgets.QLabel(self.PokemonCard)
        self.FitLabel.setGeometry(QtCore.QRect(20, 310, 91, 51))
        font.setPointSize(42)
        font.setUnderline(True)
        self.FitLabel.setFont(font)
        self.FitLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FitLabel.setObjectName("FitLabel")
        # endregion
        # region Raise()
        self.PokemonCard.raise_()
        self.IVCard.raise_()
        # endregion
        # endregion
        self.verticalLayout.addWidget(self.Content)
        IVMax.setCentralWidget(self.centralwidget)
        # endregion
        
        self.retranslateUi(IVMax)
        self.Pokemon_ComboBox.setCurrentIndex(0)
        self.SubjectsSlider.valueChanged['int'].connect(lambda: self.SubjectsStatus.setNum(self.SubjectsSlider.value() * 2))
        self.SubjectsSlider.valueChanged['int'].connect(lambda _: setattr(self, 'N', self.SubjectsSlider.value() * 2))
        self.GenSlider.valueChanged['int'].connect(self.GenStatus.setNum)
        self.GenSlider.valueChanged['int'].connect(lambda _: setattr(self, 'generations', self.GenSlider.value()))
        self.GenSlider.valueChanged['int'].connect(lambda: self.runBackend(self.PkIndex, self.N, self.generations))
        self.Pokemon_ComboBox.currentTextChanged['QString'].connect(lambda: self.PokemonSprite.setPixmap(QtGui.QPixmap(dirname+"assets/"+self.Pokemon_ComboBox.currentText()+".png")))
        self.Pokemon_ComboBox.currentTextChanged['QString'].connect(lambda _: setattr(self, 'PkIndex', self.PkDict[self.Pokemon_ComboBox.currentText()]))
        QtCore.QMetaObject.connectSlotsByName(IVMax)

    def retranslateUi(self, IVMax):
        _translate = QtCore.QCoreApplication.translate
        IVMax.setWindowTitle(_translate("IVMax", "MainWindow"))
        self.Pokemon_ComboBox.setItemText(0, _translate("IVMax", "Torchic"))
        self.Pokemon_ComboBox.setItemText(1, _translate("IVMax", "Squirtle"))
        self.Pokemon_ComboBox.setItemText(2, _translate("IVMax", "Turtwig"))
        self.Rights.setText(_translate("IVMax", "by: Overthimker. All rights reserved."))
        self.IVHPLabel.setText(_translate("IVMax", "0"))
        self.IVAtkLabel.setText(_translate("IVMax", "0"))
        self.IVDefLabel.setText(_translate("IVMax", "0"))
        self.IVSpAtkLabel.setText(_translate("IVMax", "0"))
        self.IVSpDefLabel.setText(_translate("IVMax", "0"))
        self.IVSpLabel.setText(_translate("IVMax", "0"))
        self.ActualGenLabel.setText(_translate("IVMax", "0"))
        self.ActualGenText.setText(_translate("IVMax", "Gen:"))
        self.SubjectsStatus.setText(_translate("IVMax", "4"))
        self.GenLabel.setText(_translate("IVMax", "Number of Generations:"))
        self.GenStatus.setText(_translate("IVMax", "2"))
        self.SubjectsLabel.setText(_translate("IVMax", "Number of Pokémon:"))
        self.HpLabel.setText(_translate("IVMax", "45"))
        self.AtkLabel.setText(_translate("IVMax", "60"))
        self.DefLabel.setText(_translate("IVMax", "40"))
        self.SpAtkLabel.setText(_translate("IVMax", "70"))
        self.SpDefLabel.setText(_translate("IVMax", "50"))
        self.VelLabel.setText(_translate("IVMax", "45"))
        self.FitText.setText(_translate("IVMax", "Fit:"))
        self.FitLabel.setText(_translate("IVMax", "0"))

    def runBackend(self, pkIndex, N, generations):
        def repaint():
                self.IVHPLabel.repaint()
                self.IVAtkLabel.repaint()
                self.IVDefLabel.repaint()
                self.IVSpAtkLabel.repaint()
                self.IVSpDefLabel.repaint()
                self.IVSpLabel.repaint()
                self.IVHP.repaint()
                self.IVAtk.repaint()
                self.IVDef.repaint()
                self.IVSpAtk.repaint()
                self.IVSpDef.repaint()
                self.IVSpd.repaint()
                self.HpLabel.repaint()
                self.AtkLabel.repaint()
                self.DefLabel.repaint()
                self.SpAtkLabel.repaint()
                self.SpDefLabel.repaint()
                self.VelLabel.repaint()
        
        repaint()
        backend.Inicialization(N)
        for i in range(generations):
                ui.ActualGenLabel.setText(str(i+1))
                backend.Selection(N)
                backend.Breed(N)
                backend.Mutation(N)
                best=backend.ShowBest(N)
                print("Best subject:", best)
                self.IVHPLabel.setText(str(best[0]))
                self.IVAtkLabel.setText(str(best[1]))
                self.IVDefLabel.setText(str(best[2]))
                self.IVSpAtkLabel.setText(str(best[3]))
                self.IVSpDefLabel.setText(str(best[4])) 
                self.IVSpLabel.setText(str(best[5]))
                self.IVHP.setValue(best[0])
                self.IVAtk.setValue(best[1])
                self.IVDef.setValue(best[2])
                self.IVSpAtk.setValue(best[3])
                self.IVSpDef.setValue(best[4])
                self.IVSpd.setValue(best[5])
                self.FitLabel.setText(str(sum(best)))
                stats=backend.ShowStats(pkIndex, best)
                self.HpLabel.setText(str(stats[0]))
                self.AtkLabel.setText(str(stats[1]))
                self.DefLabel.setText(str(stats[2]))
                self.SpAtkLabel.setText(str(stats[3]))
                self.SpDefLabel.setText(str(stats[4]))
                self.VelLabel.setText(str(stats[5]))
                repaint()
                time.sleep(0.5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IVMax = QtWidgets.QMainWindow()
    ui = Ui_IVMax()
    ui.setupUi(IVMax)
    IVMax.show()
    IVMax.setWindowTitle("IVMax 21.1.0")
    IVMax.setWindowIcon(QtGui.QIcon('assets/60IVMaxLogoArtboard.png'))
    sys.exit(app.exec_())
