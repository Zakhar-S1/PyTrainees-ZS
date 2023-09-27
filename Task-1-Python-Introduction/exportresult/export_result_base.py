from abc import ABC, abstractmethod


class ExportResult(ABC):
    @abstractmethod
    def export_to_format(self):
        pass
