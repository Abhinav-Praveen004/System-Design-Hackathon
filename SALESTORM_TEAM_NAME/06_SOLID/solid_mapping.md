# SOLID Principle Mapping
- **SRP (Single Responsibility):** Separate `PaymentProcessor`, `OrderManager`, and `NotificationSender`.
- **OCP (Open/Closed):** `PaymentStrategy` interface allows adding Stripe or PayPal without changing core checkout logic.
- **LSP (Liskov Substitution):** Different payment providers implement the `IPaymentProvider` interface.
- **ISP (Interface Segregation):** Dedicated interfaces like `IOrderReader` and `IOrderWriter`.
- **DIP (Dependency Inversion):** Services depend on `IInventoryRepository`, not the concrete PostgreSQL implementation.
