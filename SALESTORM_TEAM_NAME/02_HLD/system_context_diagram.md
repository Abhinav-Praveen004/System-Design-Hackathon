```mermaid
graph TD
    Customer((Customer))
    Salestorm[SALESTORM System]
    PG[Payment Gateway]
    Notification[Notification System]

    Customer -->|Attempts to purchase HTTPS| Salestorm
    Salestorm -->|Processes payments HTTPS| PG
    Salestorm -->|Sends order updates HTTPS| Notification
```
