import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow

from .components import ComponentLoader
from .signals import SignalController


class App:

    def __init__(self,
                 ui_template: str
                 ) -> None:
        self._app = QtWidgets.QApplication(sys.argv)
        self._root: QMainWindow = uic.loadUi(ui_template)

        self._component_loader = ComponentLoader(self._root)
        self._signal_controller = SignalController()

    def run(self,
            ):
        self._component_loader.run(self._signal_controller)
        self._signal_controller.add_components(self._component_loader.get_components())
        self._root.showMaximized()
        self._root.show()
        self._app.exec()

    def add_component(self,
                      component: type
                      ):
        self._component_loader.load(component)

