import pytest


@pytest.fixture(scope="session")
def db_conn():
    db = ""
    url = ""
    yield db.count(url)


@pytest.fixture()
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")


@pytest.fixture()
def mock_env_missing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
