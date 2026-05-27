# Security

Security is layered. The Hetzner firewall limits exposed ports. Coolify and the reverse proxy handle edge concerns. The FastAPI app still validates every request because all public HTTPS requests eventually reach the application.

## Network Security

- Expose only required ports, typically SSH, HTTP, and HTTPS.
- Do not expose database ports publicly.
- Restrict SSH where practical.

## Reverse Proxy Security

- Terminate HTTPS/TLS.
- Configure HSTS at the proxy once all domains are HTTPS-ready.
- Set request body size limits.
- Add rate limiting for public endpoints.
- Decide whether compression is safe for the API responses.

## Application Security

- Pydantic validation rejects malformed input.
- CORS origins are environment-specific.
- Trusted host checks reject unexpected Host headers.
- Generic 500 responses avoid leaking internals.
- Request IDs help correlate application and proxy logs.

## Database Security

- Keep the database internal to the VPS/container network.
- Store credentials in environment variables.
- Use migrations for schema changes.
- Configure backups before production traffic.
