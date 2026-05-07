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

    def get_total(self) -> int:
        return self._counter

    def get_remaining(self) -> int:
        return len(self._data)


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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element in stream: "
                      f"{item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc.get_total()
            remaining = proc.get_remaining()
            print(f"{name}: total {total} items processed, remaining "
                  f"{remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(NumericProcessor())
    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ["Hi", "five"]
    ]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3,"
          " Text 2, Log 1")

    def consume_elem(proc: DataProcessor, n: int):
        for _ in range(n):
            try:
                proc.output()
            except ValueError:
                break

    for proc in data_stream._processors:
        if isinstance(proc, NumericProcessor):
            consume_elem(proc, 3)
        if isinstance(proc, TextProcessor):
            consume_elem(proc, 2)
        if isinstance(proc, LogProcessor):
            consume_elem(proc, 1)
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
