from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture()
def activities_snapshot():
    return deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(activities_snapshot):
    original_activities = app_module.activities
    app_module.activities = deepcopy(activities_snapshot)
    try:
        yield
    finally:
        app_module.activities = original_activities


@pytest.fixture()
def client():
    return TestClient(app_module.app)