import pytest
from starlette.testclient import TestClient

from src.main import app
from src.dependencies import get_db


@pytest.fixture
def api_client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    test_api_client = TestClient(app)

    yield test_api_client
    del app.dependency_overrides[get_db]
