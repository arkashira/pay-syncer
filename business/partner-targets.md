# Partner Integration Roadmap – pay‑syncer

| # | Partner | Rationale | Free‑Tier Limits | Integration Effort | Value‑Add (User Job) | Affiliate / Revenue‑Share |
|---|---------|-----------|------------------|--------------------|----------------------|---------------------------|
| 1 | **Stripe** | Most e‑commerce sites use Stripe for payments; its webhook system gives real‑time payment events. | Unlimited API calls; 0% platform fee (transaction fee applies). | **S** – REST API + webhooks, SDKs in PHP/Node. | *“Keep order status in sync with payment state”* – eliminates manual reconciliation. | Stripe Partner Program – 5% referral commission on new merchants. |
| 2 | **PayPal / Braintree** | PayPal is a legacy gateway; Braintree (PayPal) offers a unified API for credit card, PayPal, Venmo. | 10 000 API calls/month, 0% platform fee. | **S** – REST API, PHP SDK. | *“Automate payment‑to‑order mapping across multiple payment methods”* – reduces duplicate entries. | PayPal Partner Network – 5% revenue share on transaction fees. |
| 3 | **Square** | Square’s API supports online payments and POS; many small merchants use Square for both. | 10 000 API calls/month, 0% platform fee. | **S** – REST API, SDKs. | *“Sync in‑store and online payments to orders”* – unified view for omnichannel merchants. | Square Partner Program – 5% referral commission. |
| 4 | **Shopify** | Largest hosted e‑commerce platform; many merchants need reconciliation between Shopify orders and external payment processors. | Free plan (limited features); 50 000 API calls/month. | **M** – GraphQL + webhooks, Shopify SDK. | *“Keep Shopify order status accurate after external payment events”* – eliminates manual status updates. | Shopify Partner Program – 20% revenue share on subscription fees. |
| 5 | **WooCommerce** | Open‑source, PHP‑based; integrates with WordPress sites worldwide. | Free plugin; 5 000 API calls/month via WooCommerce REST. | **M** – REST API, PHP SDK. | *“Automate order updates for WordPress merchants”* – reduces admin overhead. | WooCommerce Affiliate Program – 20% commission on plugin sales. |
| 6 | **QuickBooks Online** | Accounting integration lets merchants reconcile payments with financial records. | 100 API calls/day (free tier). | **M** – OAuth2 + REST API. | *“Align payment reconciliation with accounting entries”* – improves financial reporting. | QuickBooks Partner Program – 10% revenue share on subscription upsells. |
| 7 | **Xero** | Cloud accounting with strong API; popular in SMBs. | 100 API calls/day (free tier). | **M** – OAuth2 + REST API. | *“Sync payment status to Xero invoices”* – reduces double‑entry errors. | Xero Partner Program – 10% revenue share on subscription upsells. |

## Prioritization & Phased Rollout

1. **Phase 1 (Month 1‑2)** – Stripe, PayPal/Braintree, Square (S effort, high volume).  
2. **Phase 2 (Month 3‑4)** – Shopify, WooCommerce (M effort, high merchant base).  
3. **Phase 3 (Month 5‑6)** – QuickBooks, Xero (M effort, strong revenue‑share potential).  

> **Key KPI:** Achieve 30 % of total user base connected to at least one partner within 6 months; target 15 % revenue‑share from partner referrals by month 12.