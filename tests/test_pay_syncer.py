import pytest
from pay_syncer import Payment, sync_payments

def test_sync_payments_pending():
    payments = [Payment(1, 10.0, "pending"), Payment(2, 20.0, "pending")]
    synced_payments = sync_payments(payments)
    assert len(synced_payments) == 2
    assert synced_payments[0].status == "synced"
    assert synced_payments[1].status == "synced"

def test_sync_payments_already_synced():
    payments = [Payment(1, 10.0, "synced"), Payment(2, 20.0, "synced")]
    synced_payments = sync_payments(payments)
    assert len(synced_payments) == 2
    assert synced_payments[0].status == "synced"
    assert synced_payments[1].status == "synced"

def test_sync_payments_empty():
    payments = []
    synced_payments = sync_payments(payments)
    assert len(synced_payments) == 0
