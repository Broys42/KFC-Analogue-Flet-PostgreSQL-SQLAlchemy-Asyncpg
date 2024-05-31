from Model import Model
import flet as ft


class ViewModel():
    def __init__(self, model: Model):
        self.model = model

    def get_selected_tab(self):
        return self.model.user.selected_tab

    def change_selected_tab(self, index):
        self.model.user.selected_tab = index

    def get_menuModel(self):
        return self.model.menuModel.model
