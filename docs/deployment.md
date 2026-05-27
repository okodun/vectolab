# Deployment

## Target

- Hetzner VPS
- Coolify-managed container
- FastAPI app running on port `4567`
- Reverse proxy routes public HTTPS traffic to the container

## Required Environment Variables

```bash
ENVIRONMENT=production
ALLOWED_HOSTS=api.example.com
ALLOWED_ORIGINS=https://app.example.com
ALLOW_CREDENTIALS=false
DATABASE_URL=sqlite:///./db/test.db
```

For a production database, replace `DATABASE_URL` with the managed/internal database URL.

## Deployment Flow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as Git Repo
    participant Coolify
    participant VPS as Hetzner VPS
    participant App as FastAPI Container

    Dev->>Git: Push changes
    Coolify->>Git: Pull latest version
    Coolify->>VPS: Build/start container
    VPS->>App: Run FastAPI app
    Coolify->>App: Health check /
```
