import argparse
import json
from dataclasses import dataclass

@dataclass
class Payment:
    id: int
    amount: float
    status: str

def sync_payments(payments):
    synced_payments = []
    for payment in payments:
        if payment.status == "pending":
            payment.status = "synced"
        synced_payments.append(payment)
    return synced_payments

def main():
    parser = argparse.ArgumentParser(description="Sync payments")
    parser.add_argument("--payments", help="Path to payments JSON file")
    args = parser.parse_args()

    with open(args.payments, "r") as f:
        payments_data = json.load(f)

    payments = [Payment(**payment) for payment in payments_data]
    synced_payments = sync_payments(payments)

    print("Synced payments:")
    for payment in synced_payments:
        print(f"ID: {payment.id}, Amount: {payment.amount}, Status: {payment.status}")

if __name__ == "__main__":
    main()
