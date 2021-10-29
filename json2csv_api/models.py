from __future__ import annotations
from typing import Any, Iterator, Set, Tuple, Union
import json
import csv
import io


class Json(dict):
    def __init__(self, **kwargs: Any) -> None:
        super(Json, self).__init__(**kwargs)

    def __iter__(self) -> Iterator[Tuple[str, Set[str]]]:
        for k, v in self.items():
            yield k, set(v)

    def validate(self) -> bool:
        """
        Validates the form of the parsed JSON input. When the form is valid return `True` else return `False`.

        :type json_input: `Any`
        :rtype: `bool`
        :param json_input: JSON object to validate.
        :returns: Boolean which indicates whether form is valid.
        """
        return all(type(k) == str and type(v) == list and all(type(vi) == str for vi in v) for k, v in self.items())

    @staticmethod
    def parse(json_str: Union[str, bytes]) -> Json:
        """
        Parses JSON file into python object.

        :type json_str: `str`
        :rtype: `Json`
        :param json_str: JSON string to parse.
        :returns: Parsed JSON object.
        """
        return Json(**json.loads(json_str))


class Csv:
    _HEADERS = (
        "person", "view_grades", "change_grades", "add_grades", 
        "delete_grades", "view_classes", "change_classes", 
        "add_classes", "delete_classes"
    )

    def __init__(self, json_input: Json, delimiter: str = ',', quotechar: str = '"') -> None:
        bheaders = self._HEADERS[1:]
        self.rows = [[k, *map(lambda h: int(h in v), bheaders)] for k,v in json_input]
        self.delimiter = delimiter
        self.quotechar = quotechar

    def write(self) -> str:
        builder = io.StringIO()
        try:
            writer = csv.writer(builder, delimiter=self.delimiter, quotechar=self.quotechar)
            writer.writerow(self._HEADERS)
            writer.writerows(self.rows)
            return builder.getvalue()
        finally:
            builder.close()

