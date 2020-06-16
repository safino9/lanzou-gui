from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout, QPushButton, QHBoxLayout

from lanzou.gui.utils import others_style, btn_style, set_file_icon


class RecFolderDialog(QDialog):
    out = pyqtSignal(object)

    def __init__(self, files, parent=None):
        super(RecFolderDialog, self).__init__(parent)
        self.files = files
        self.initUI()
        self.setStyleSheet(others_style)

    def initUI(self):
        self.setWindowTitle("查看回收站文件夹内容")
        self.form = QVBoxLayout()
        for item in iter(self.files):
            ico = QPushButton(set_file_icon(item.name), item.name)
            ico.setStyleSheet("QPushButton {border:none; background:transparent; color:black;}")
            ico.adjustSize()
            it = QLabel(f"<font color='#CCCCCC'>({item.size})</font>")
            hbox = QHBoxLayout()
            hbox.addWidget(ico)
            hbox.addStretch(1)
            hbox.addWidget(it)
            self.form.addLayout(hbox)

        self.form.setSpacing(10)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.button(QDialogButtonBox.Close).setText("关闭")
        self.buttonBox.setStyleSheet(btn_style)
        self.buttonBox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addLayout(self.form)
        vbox.addStretch(1)
        vbox.addWidget(self.buttonBox)
        self.setLayout(vbox)
