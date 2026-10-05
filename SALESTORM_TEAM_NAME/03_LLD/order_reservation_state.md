```mermaid
stateDiagram-v2
    [*] --> AVAILABLE
    AVAILABLE --> RESERVED : Reserve Request
    RESERVED --> PAYMENT_PENDING : Proceed to Checkout
    PAYMENT_PENDING --> CONFIRMED : Payment Success
    CONFIRMED --> SOLD
    
    RESERVED --> RELEASED : Timeout
    PAYMENT_PENDING --> RELEASED : Payment Failed / Timeout
```
