# ADR 1: Inventory Concurrency Control
**Context:** Need to prevent overselling of 100 items among 10,000 concurrent requests.
**Decision:** Use Redis Lua Scripts for atomic pre-decrement, followed by asynchronous DB persistence.
**Trade-offs:** High throughput and low latency, but risks data loss if Redis crashes before syncing (mitigated by Redis persistence AOF).
