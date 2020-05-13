import pytest
import inspect
import time

TIMEOUT_MAX = 12
TIMEOUT_MED = 6


def retry(func, maxTries, sleepSeconds):
    for i in range(1, maxTries + 1):
        if i > 1:
            time.sleep(sleepSeconds)
        try:
            return func()
        except Exception as err:
            print(f'\n...tried {i}: {err}')

    pytest.fail(f"Exhausted {maxTries} attempts for previous errors")
