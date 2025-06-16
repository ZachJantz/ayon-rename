
from PySide2 import QtWidgets, QtCore
import maya.cmds as cmds
import util




class DuplicateResolver(QtWidgets.QDialog):

    def __init__(self, duplicates, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Duplicates Detected")
        self.invalid_dups = duplicates
        vlayout1 = QtWidgets.QVBoxLayout()
        self.setLayout(vlayout1)
        hlayout1 = QtWidgets.QHBoxLayout()
        vlayout1.addLayout(hlayout1)
        hlayout2 = QtWidgets.QHBoxLayout()
        vlayout1.addLayout(hlayout2)

        # List of duplicate errors
        self.dup_list = QtWidgets.QListWidget()
        hlayout1.addWidget( self.dup_list)
        self.dup_list.setSortingEnabled(True)
        self.update_dup_list()

        self.selected_dup = None
        self.dup_list.itemPressed.connect(self.update_selected_dup)
        self.dup_list.itemPressed.connect(self.update_path_list)

        # List of paths to duplicate names in maya
        self.path_list  = QtWidgets.QListWidget()
        hlayout1.addWidget(self.path_list)
        self.selected_path = None
        self.path_list.itemPressed.connect(self.update_active_path)

        self.input1 = QtWidgets.QLineEdit()
        hlayout2.addWidget(self.input1)

        rename_btn = QtWidgets.QPushButton("Rename")
        hlayout2.addWidget(rename_btn)
        rename_btn.clicked.connect(self.fix_dup_name)
        

    def update_selected_dup(self,item):

        self.selected_dup = item.text()


    def update_dup_list(self):

        self.dup_list.clear()
        keys = list(self.invalid_dups.keys())
        self.dup_list.addItems(keys)


    def update_path_list(self):
        
        self.path_list.clear()
        paths = self.invalid_dups[self.selected_dup]
        self.path_list.addItems(paths)


    def update_active_path(self, item):

        self.selected_path = item.text()


    def fix_dup_name(self):

        if self.selected_path != None and self.input1.text() != '':

            cmds.rename(self.selected_path, self.input1.text())

            # UI handling
            new_path_list = self.invalid_dups[self.selected_dup]
            new_path_list.remove(self.selected_path)
            self.invalid_dups[self.selected_dup] = new_path_list
            self.update_path_list()
            if not new_path_list:

                del self.invalid_dups[self.selected_dup]
                self.update_dup_list()

            self.input1.clear()