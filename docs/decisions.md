# Decisions

Log of key decisions in ADR style.

## Template

### D-000: Title
- **Date:**
- **Context:**
- **Decision:**
- **Consequences:**

## D-001: Use Azure SQL as the warehouse
- **Date:** 2026-11-18
- **Context:** Need a relational store to practise SQL transformation and analytics.
- **Decision:** Use Azure SQL Database, loaded via Python.
- **Consequences:** Requires Azure setup and credentials management through `.env`.
