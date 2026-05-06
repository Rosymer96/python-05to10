#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[str] = []
        self._counter: int = 0
        self._output_idx: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available")
        value = self._data.pop(0)
        rank = self._output_idx
        self._output_idx += 1
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
                self._counter += 1
        else:
            self._data.append(str(data))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._data.append(x)
                self._counter += 1
        else:
            self._data.append(data)
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return (
                all(isinstance(key, str) and isinstance(val, str)
                    for key, val in d.items())
            )
        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return f"{d.get('log_level', '')}: {d.get('log_message', '')}"
        if isinstance(data, list):
            for x in data:
                self._data.append(format_log(x))
                self._counter += 1
        else:
            self._data.append(format_log(data))
            self._counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print("Trying to validate input '42':", num.validate(42))
    print("Trying to validate input 'Hello':", num.validate("Hello"))
    try:
        print(
            "Test invalid ingestion of string 'foo' without prior validation:")
        num.ingest("foo")
    except Exception as e:
        print("Got exception:", e)
    nums = [1, 2, 3, 4, 5]
    print("Processing data: ", nums)
    num.ingest(nums)
    print("Extracting 3 values...")
    for _ in range(3):
        output = num.output()
        print(f"Numeric value {output[0]}: {output[1]}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))
    words = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {words}")
    text.ingest(words)
    print("Extracting 1 value...")
    output = text.output()
    print(f"Text value {output[0]}: {output[1]}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello:", log.validate("Hello"))
    logs = [{"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        log_output = log.output()
        print(f"Log entry {log_output[0]}: {log_output[1]}")


if __name__ == "__main__":
    main()
