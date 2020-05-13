import os
import pytest
from yaml import load, BaseLoader


def getEnvConfig(envName):
    envConfig = None
    fpath = os.path.sep.join(['.', 'config', 'envs.yml'])
    with open(fpath) as f:
        config = load(f, Loader=BaseLoader)
        envConfig = config['env'][envName.lower()]
    assert envConfig
    assert isinstance(envConfig, dict)
    return envConfig


def pytest_configure(config):
    if not config.option.proxy_string:
        env = config.option.sutenv
        envConfig = getEnvConfig(env)
        config.option.proxy_string = envConfig['proxy']


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
def envConfig(envName):
    return getEnvConfig(envName)


@pytest.fixture(scope="session", autouse=True)
def sessionRun(envName):
    yield
    print(f"\n\nSuT Env: {envName}")


@pytest.fixture(scope='session')
def homeUrl(envConfig, envName):
    return envConfig['url']


@pytest.fixture(scope='session')
def homeUrlAuth(envConfig, envName):
    return envConfig['url'] + '?context=auth'


@pytest.fixture(scope='session')
def catUrl(homeUrl):
    catUrl = 'account'
    return homeUrl + catUrl


@pytest.fixture(scope='session')
def subcatUrl(homeUrl):
    subcatUrl = 'account/account-balance'
    return homeUrl + subcatUrl


@pytest.fixture(scope='session')
def usrPwd(envConfig, envName):
    return (envConfig['usr'], envConfig['pwd'])
