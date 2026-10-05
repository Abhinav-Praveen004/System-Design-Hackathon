# 🌩️ SALESTORM: High-Scale E-Commerce System Design

Welcome to our team's submission for the **SYSCRAFTERS 2026 Design-First AI-Assisted Hackathon**. 

This repository contains our comprehensive architectural blueprint designed to handle sudden, extreme e-commerce traffic spikes (10,000 concurrent users competing for 100 limited-stock units) without overselling, while ensuring idempotent payments and a highly resilient order lifecycle.

---

## 🏗️ Core Architecture & Strategy

Our design prioritizes **Consistency** during the critical inventory reservation phase, ensuring that under no circumstances can more than 100 units be sold.

**Key Technical Decisions:**
- **Concurrency Control:** We utilize **Redis Lua Scripts** for atomic pre-decrementing of inventory. This guarantees deterministic reservation and acts as a high-speed buffer before asynchronous database persistence.
- **Idempotency:** Payment endpoints require unique `Idempotency-Key` headers to prevent duplicate billing during client retries or network timeouts.
- **Event-Driven Resilience:** Post-payment, the system transitions to an asynchronous, event-driven architecture using **Kafka / Message Broker** to decouple the Order Service from the Payment Service, ensuring failures in one don't cascade to the other.
- **Scalability:** Stateless API gateways and microservices horizontally auto-scale behind an Application Load Balancer, protected by a CDN/WAF for rate-limiting.

---

## 📂 Deliverables Structure

We have provided all required deliverables, carefully organized into the following structured directories. 

> **Note:** All `.md` files containing structural diagrams also have an accompanying pre-rendered `.png` image file in their respective folders.

| Directory | Contents |
| :--- | :--- |
| **`01_Requirements/`** | Business rules, functional/non-functional requirements, and constraints. |
| **`02_HLD/`** | High-Level Design (System Context, Container, Component, and Deployment diagrams). |
| **`03_LLD/`** | Low-Level Design (Class diagram, state diagrams, and detailed Sequence diagrams). |
| **`04_Database/`** | Entity Relationship (ER) diagram detailing ACID tables and schema. |
| **`05_API/`** | OpenAPI/Swagger YAML specifications for critical endpoints. |
| **`06_SOLID/`** | Detailed mapping of how our microservices adhere to SOLID principles. |
| **`07_Design_Patterns/`** | Documentation of applied patterns (Strategy, Circuit Breaker, Factory, etc.). |
| **`08_Scalability_Reliability/`** | Bottleneck analysis, retry policies, and horizontal scaling strategies. |
| **`09_Security_Observability/`** | WAF, authentication, distributed tracing, and system metrics. |
| **`10_ADR/`** | Architecture Decision Records justifying our Redis and Async tradeoffs. |
| **`11_AI_Assisted_Validation/`** | Simulation scripts/evidence and our AI Usage notes. |
| **`12_Presentation/`** | The structured script/content for our 5-Minute Final Pitch. |

---

## 🚀 How to Review

We recommend starting with **`01_Requirements`** to understand our assumptions, then moving to **`02_HLD`** for a bird's-eye view of the system. 

If you are using a Markdown viewer that supports it, the ` ```mermaid ` code blocks within the `.md` files will render automatically. Otherwise, please open the included `.png` image files located directly beside each `.md` document!

*Built for the SYSCRAFTERS 2026 Hackathon.*
