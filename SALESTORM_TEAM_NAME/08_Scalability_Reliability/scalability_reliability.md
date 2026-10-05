# Scalability & Reliability
- **Scalability:** Stateless API nodes can scale horizontally. Redis manages distributed locks for inventory to prevent DB overload.
- **Reliability (Failure Handling):**
  - **Circuit Breaker:** Prevents cascading failures when the Payment Gateway is down.
  - **Retries & Idempotency:** Safely retry failed network calls without double billing.
  - **Dead Letter Queue:** Failed async events are sent to a DLQ for manual inspection.
