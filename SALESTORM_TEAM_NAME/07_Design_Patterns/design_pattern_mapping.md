# Design Patterns
- **Strategy:** Used for Payment selection (Credit Card vs Wallet).
- **Factory:** Creating the correct Payment Provider instance.
- **State:** Managing the `Order` lifecycle (CREATED -> CONFIRMED).
- **Circuit Breaker:** Wrapping calls to the external Payment Gateway.
- **Repository:** Abstraction over PostgreSQL for Inventory and Orders.
