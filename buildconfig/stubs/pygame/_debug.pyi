from typing import Tuple, Union, Optional, Callable

ImportResult = Tuple[str, bool, Optional[Callable]]

def str_from_tuple(version_tuple: Union[Tuple[int, int, int], None]) -> str: ...
def attempt_import(module: str, function_name: str, output_str: str = "") -> ImportResult: ...
def print_debug_info(filename: Optional[str] = None) -> None: ...
