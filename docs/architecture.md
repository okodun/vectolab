# Architecture

Vectolab is a FastAPI service for deterministic experiment assignment.

```mermaid
flowchart TD
    client["Client / Roblox / Browser"]
    internet["Internet"]
    firewall["Hetzner VPS Firewall<br/>Only required ports exposed"]
    coolify["Coolify<br/>App orchestration"]
    proxy["Reverse Proxy<br/>HTTPS, routing, optional rate limits"]
    api["FastAPI App<br/>Validation, CORS, safe errors"]
    db["Database<br/>Persistent storage"]

    client --> internet
    internet --> firewall
    firewall --> coolify
    coolify --> proxy
    proxy --> api
    api --> db
```

## Application Layers

```mermaid
flowchart TD
    route["API routes"] --> schema["Pydantic schemas"]
    route --> service["Services"]
    service --> repo["Repositories"]
    repo --> model["SQLAlchemy models"]
    repo --> db["Database session"]
```

## Responsibilities

Hetzner firewall limits network exposure. Coolify and the reverse proxy handle TLS, routing, compression, request size limits, and optional rate limiting. FastAPI owns validation, CORS, trusted hosts, safe errors, request IDs, business logic, and database access.
