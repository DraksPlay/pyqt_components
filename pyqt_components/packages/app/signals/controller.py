from typing import Any, List


class SignalController:

    def __init__(self,
                 ) -> None:
        self._is_run = False
        self._components = []

    def send_signal(self,
                    name: str,
                    message: Any
                    ) -> None:
        if not self._is_run:
            raise "Signal Controller not run"
        for component in self._components:
            if not hasattr(component, name):
                continue

            getattr(component, name)(message)

    def add_components(self,
                       components: List[object]
                       ) -> None:
        self._components.extend(components)
        self._is_run = True
