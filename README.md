This repository demonstrates an uncommon error in Python: a bare `except` block without a specific exception type.

The `bug.py` file contains a function `function_with_uncommon_error`. This function attempts to perform division, but if the second parameter is zero or if it is an unsupported operation, it returns an error message. The issue is in the bare except block after the ZeroDivisionError, catching all other exceptions without making it clear which type of exception occurred.