# Final Pitch (5-Minute)
1. **Problem (30s):** Handle 10,000 customers for 100 units.
2. **Requirements (30s):** No overselling, idempotent payments.
3. **HLD (60s):** WAF -> API Gateway -> Microservices -> Redis & Postgres.
4. **Critical Design (60s):** Redis Lua Script for atomic reservation.
5. **Payment (45s):** Idempotency keys & async event-driven order completion.
6. **LLD (45s):** SOLID principles applied with Strategy and Circuit Breaker patterns.
7. **Scalability (30s):** Horizontally scalable, highly observable.
