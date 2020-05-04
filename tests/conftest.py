import os
import pytest
from yaml import load, BaseLoader


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
def envName(request):
    return readOption(request, "--sutenv", required=False)


@pytest.fixture(scope='session')
def config(envName):
    envConfig = None
    fpath = os.path.sep.join(['.', 'config', 'envs.yml'])
    with open(fpath) as f:
        config = load(f, Loader=BaseLoader)
        envConfig = config['env'][envName.lower()]
    assert envConfig
    assert isinstance(envConfig, dict)
    return envConfig


@pytest.fixture(scope="session", autouse=True)
def sessionRun(envName):
    yield
    print(f"\n\nSuT Env: {envName}")


@pytest.fixture(scope='session')
def homeUrl(config, envName):
    return config['url']


@pytest.fixture(scope='session')
def homeUrlAuth(config, envName):
    return config['url'] + '?context=auth'


@pytest.fixture(scope='session')
def catUrl(homeUrl):
    catUrl = 'my-account'
    return homeUrl + catUrl


@pytest.fixture(scope='session')
def usrPwd(config, envName):
    return (config['usr'], config['pwd'])
