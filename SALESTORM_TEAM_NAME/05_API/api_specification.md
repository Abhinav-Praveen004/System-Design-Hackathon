```yaml
openapi: 3.0.0
info:
  title: SALESTORM API
  version: 1.0.0
paths:
  /inventory/reserve:
    post:
      summary: Reserve inventory
      parameters:
        - name: Idempotency-Key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Reservation successful
        '409':
          description: Out of stock
```
