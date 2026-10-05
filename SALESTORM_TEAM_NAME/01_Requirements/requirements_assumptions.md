# Requirements & Assumptions

## Functional Requirements
- **High Concurrency Purchase:** Allow up to 10,000 customers to attempt to purchase 100 limited-stock units simultaneously.
- **Inventory Reservation:** Temporarily reserve inventory upon a user clicking "Buy Now", giving them a time window to complete payment.
- **Payment Processing:** Ensure safe, idempotent payment processing that gracefully handles failures, timeouts, and duplicates.
- **Order Lifecycle:** Track the state of the order accurately from creation to delivery.
- **Reservation Expiry:** Automatically release unpaid or expired reservations back to the pool.

## Non-Functional Requirements
- **Consistency:** Strict consistency for inventory to guarantee exactly 100 units are sold—no overselling.
- **Scalability:** System must scale horizontally to handle sudden massive traffic spikes (10,000 to 500,000 requests/sec).
- **Availability:** Core services should remain available, even if downstream or external dependencies degrade.
- **Reliability & Idempotency:** Duplicate requests must not lead to duplicate transactions or inventory subtractions.

## Assumptions & Constraints
- Only 100 units of the product are available.
- Traffic arrives rapidly in a very short time window (Flash Sale).
- External Payment Gateway may fail, throttle requests, or time out.
- The system must prioritize correct consistency over complete availability for the checkout flow (CP over AP in CAP theorem for inventory).
