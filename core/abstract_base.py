# core/abstract_base.py
# Public abstract base for sovereign components

from abc import ABC, abstractmethod

class SovereignModule(ABC):
    @abstractmethod
    def execute(self, parameters: dict):
        pass
