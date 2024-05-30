import flet as ft
from Window import Window
from Model import Model
from ViewModel import ViewModel
from View import View


class Starter():
    def __init__(self):
        self.model = Model()
        self.viewModel = ViewModel(self.model)
        self.view = View(self.viewModel)


starter = Starter()
