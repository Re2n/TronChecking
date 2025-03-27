import pytest
import tronpy.exceptions
from fastapi.testclient import TestClient
from fastapi import status
from unittest.mock import AsyncMock, patch
from main import app
from depends import tron_scan_service
from models.TronScan import TronScanResponse


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_scan_address_success(client):
    test_address = "TTn59627mrU19Cd5AJBwEFmjHsVynUpTz"
    mock_response = {
        "address": test_address,
        "balance": 100,
        "bandwidth": 500,
        "energy": "200/1000",
    }
    with patch.object(
        tron_scan_service,
        "get_info_about_address",
        AsyncMock(return_value=mock_response),
    ):
        response = client.post(f"/scan/{test_address}")

        assert response.status_code == status.HTTP_200_OK
        TronScanResponse.model_validate(response.json())
