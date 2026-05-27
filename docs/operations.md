# Operations

## Common Checks

- Is the Coolify app running?
- Is the domain routed to the correct app?
- Is the TLS certificate valid?
- Are production environment variables set?
- Can the app reach the database?
- Do application logs show validation, database, or unexpected server errors?

## Incident Flow

```mermaid
flowchart TD
    issue["API unavailable"]
    dns["Check DNS"]
    firewall["Check Hetzner firewall"]
    coolify["Check Coolify app status"]
    logs["Check app logs"]
    health["Check GET /"]
    db["Check database connectivity"]

    issue --> dns
    dns --> firewall
    firewall --> coolify
    coolify --> logs
    logs --> health
    health --> db
```
