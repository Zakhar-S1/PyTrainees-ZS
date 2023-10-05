from abc import ABC, abstractmethod


class ExportResult(ABC):
    @abstractmethod
    def convert_to_format(self):
        pass
