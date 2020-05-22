import os
import pytest
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption(
        "--sutenv",
        action="store",
        default="staging",
        help="provide SuT environment: [dev|test|staging]")


def readOption(request, opt, required=True):
    val = request.config.getoption(opt)
    if required:
        assert val, f'pytest: {opt} custom option is required'
    return val


@pytest.fixture(scope='session')
def homeUrl(request):
    return readOption(request, "--start-page", required=False)


@pytest.fixture(scope='session')
def envName(request):
    return readOption(request, "--sutenv", required=False)


@pytest.fixture(scope="session", autouse=True)
def sessionRun(envName):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n\nSuT env: {envName} @ {time}")



