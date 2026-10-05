```mermaid
sequenceDiagram
    Kafka->>OrderService: Consume PaymentSuccessEvent
    OrderService->>DB: Update Order Status -> CONFIRMED
    OrderService->>InventoryService: Confirm Reservation (Status -> SOLD)
    OrderService->>Kafka: Publish OrderConfirmedEvent
```
