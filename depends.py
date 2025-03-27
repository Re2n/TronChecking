from config.Database import provider
from repositories.TronScan import TronScanRepository
from services.TronScan import TronScanService

tron_scan_repository = TronScanRepository()
tron_scan_service = TronScanService(tron_scan_repository, provider)
