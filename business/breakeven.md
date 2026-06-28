# Breakeven Analysis – pay‑syncer

| Item | Value | Notes |
|------|-------|-------|
| **Variable cost per active user (USD/mo)** | **$0.04** | • Compute: $0.02 <br>• Storage: $0.01 <br>• Bandwidth: $0.01 |
| **Pricing tiers** | | |
| • Basic | **$29 / mo** | 500 orders/mo, email support, basic dashboard |
| • Standard | **$79 / mo** | 5 k orders/mo, API access, priority support, advanced reporting |
| • Premium | **$199 / mo** | Unlimited orders, real‑time analytics, dedicated account manager |
| **Customer Acquisition Cost (CAC)** | **$200 – $400** | Avg. paid‑search + partner outreach |
| **Lifetime Value (LTV)** | **$350 – $2 400** | 12‑month churn assumption; gross margin ≈ 99 % |
| **Fixed monthly cost** | **$10 000** | Dev, ops, support, marketing |
| **Break‑even users** | | |
| • Basic | **345** | 10 000 ÷ (29 – 0.04) |
| • Standard | **127** | 10 000 ÷ (79 – 0.04) |
| • Premium | **51** | 10 000 ÷ (199 – 0.04) |
| **Path to $10 k MRR** | | |
| • Basic | **345 users** | 345 × $29 = $10 005 |
| • Standard | **127 users** | 127 × $79 = $10 013 |
| • Premium | **51 users** | 51 × $199 = $10 149 |

---

## Assumptions

1. **Variable cost** is dominated by cloud compute (AWS Lambda/EC2), S3 storage, and outbound data transfer.  
2. **Fixed cost** of $10 k/mo covers core dev, QA, ops, and a small marketing budget.  
3. **Churn** is 8 % per month → 12‑month average tenure.  
4. **Gross margin** ≈ 99 % after subtracting variable cost.  
5. **CAC** includes paid ads, partner commissions, and sales effort.  

---

## Takeaway

- **Premium tier** is the most efficient for reaching $10 k MRR (only 51 users).  
- **Standard tier** offers a balanced sweet spot: 127 users for $10 k MRR with a lower CAC threshold.  
- **Basic tier** requires the largest user base but is still viable if volume sales are high.  

Focus initial sales on the **Standard** tier to hit $10 k MRR quickly while building a pipeline for **Premium** upsells.