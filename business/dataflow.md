# Dataflow Architecture
## Overview
The pay-syncer system is designed to detect and resolve payment discrepancies in eCommerce platforms, specifically Adobe Commerce/Magento 2. The following dataflow architecture outlines the system's components and interactions.

## External Data Sources
* Adobe Commerce/Magento 2 API
* Payment Gateway APIs (e.g., PayPal, Stripe)
* Order management systems

## Ingestion Layer
```markdown
+---------------+
|  External   |
|  Data Sources |
+---------------+
       |
       |
       v
+---------------+
|  Ingestion   |
|  Layer       |
+---------------+
```
* Components:
  * Adobe Commerce/Magento 2 API connector
  * Payment Gateway API connectors
  * Order management system connectors
  * Data ingestion scheduler
  * Authentication and authorization module (AuthN/AuthZ)

## Processing/Transform Layer
```markdown
+---------------+
|  Ingestion   |
|  Layer       |
+---------------+
       |
       |
       v
+---------------+
|  Processing  |
|  Layer       |
+---------------+
```
* Components:
  * Data processing engine (e.g., Apache Beam, Apache Spark)
  * Data transformation and mapping module
  * Payment discrepancy detection module
  * Data quality and validation module
  * AuthN/AuthZ module (shared with Ingestion Layer)

## Storage Tier
```markdown
+---------------+
|  Processing  |
|  Layer       |
+---------------+
       |
       |
       v
+---------------+
|  Storage     |
|  Tier        |
+---------------+
```
* Components:
  * Relational database management system (e.g., PostgreSQL)
  * NoSQL database management system (e.g., MongoDB)
  * Data warehousing and analytics module
  * AuthN/AuthZ module (shared with Processing Layer)

## Query/Serving Layer
```markdown
+---------------+
|  Storage     |
|  Tier        |
+---------------+
       |
       |
       v
+---------------+
|  Query/Serving|
|  Layer       |
+---------------+
```
* Components:
  * Query engine and API gateway
  * Data visualization and reporting module
  * Payment discrepancy resolution module
  * AuthN/AuthZ module (shared with Storage Tier)

## Egress to User
```markdown
+---------------+
|  Query/Serving|
|  Layer       |
+---------------+
       |
       |
       v
+---------------+
|  Egress to   |
|  User        |
+---------------+
```
* Components:
  * User interface and experience module
  * API documentation and developer portal
  * Authentication and authorization module (AuthN/AuthZ)
  * Payment discrepancy resolution and notification module

## Auth Boundaries
The system has multiple auth boundaries:
* Between External Data Sources and Ingestion Layer
* Between Ingestion Layer and Processing/Transform Layer
* Between Processing/Transform Layer and Storage Tier
* Between Storage Tier and Query/Serving Layer
* Between Query/Serving Layer and Egress to User

Each auth boundary ensures that only authorized components and users can access and manipulate sensitive data. The AuthN/AuthZ module is shared across multiple layers to provide a unified authentication and authorization mechanism.