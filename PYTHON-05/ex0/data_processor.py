from abc import ABS, abstractmethod
from typing import Any


class DataProcessor(ABS):

    def __init__(self) -> None:
        self._data: list[str] = [],
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
        
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
        
    def output(self) -> tuple[int, str]:


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, (list)):
            for x in data:
                if isinstance(x, (int, float)):
                    
    def ingest(self, data: int | float) -> None:



class TextProcessor(DataProcessor):

class LogProcessor(DataProcessor):
