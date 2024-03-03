import inspect
from typing import List

from ..signals import SignalController


class ComponentLoader:

    def __init__(self,
                 root,
                 ) -> None:
        self.root = root
        self._components = []
        self._exec_components = []

    def load(self,
             component: type
             ) -> None:
        args_spec = inspect.getfullargspec(component.__init__)
        if len(args_spec.args) < 3:
            raise "Args in components invalid"

        self._components.append(component)

    def run(self,
            signal_controller: "SignalController"
            ) -> None:
        for component in self._components:
            obj = component(self.root, signal_controller)
            self._exec_components.append(obj)

    def get_components(self) -> List[object]:
        return self._exec_components
