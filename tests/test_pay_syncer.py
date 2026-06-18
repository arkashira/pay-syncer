import pytest
from src.pay_syncer import Payment, ReconciliationEngine

def test_payment_dataclass():
    payment = Payment(1, 10.99, "pending")
    assert payment.id == 1
    assert payment.amount == 10.99
    assert payment.status == "pending"

def test_reconciliation_engine_add_payment():
    engine = ReconciliationEngine()
    payment = Payment(1, 10.99, "pending")
    engine.add_payment(payment)
    assert len(engine.payments) == 1

def test_reconciliation_engine_sync_payments():
    engine = ReconciliationEngine()
    payment1 = Payment(1, 10.99, "pending")
    payment2 = Payment(2, 5.99, "processed")
    payment3 = Payment(3, 7.99, "pending")
    engine.add_payment(payment1)
    engine.add_payment(payment2)
    engine.add_payment(payment3)

    synced_payments = engine.sync_payments()
    assert len(synced_payments) == 2
    assert synced_payments[0].id == 1
    assert synced_payments[1].id == 3

def test_reconciliation_engine_sync_payments_empty():
    engine = ReconciliationEngine()
    synced_payments = engine.sync_payments()
    assert len(synced_payments) == 0
