import flet as ft
from MainWindow import MainWindow
from Model import Model
from ViewModel import ViewModel

class Starter():
    def __init__(self):
        self.model = Model()
        self.viewModel = ViewModel(self.model)

starter = Starter()
