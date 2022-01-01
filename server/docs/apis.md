### GET /sessions
used to check if user has an existing session based on cookies

### POST /sessions
creates a new game/session and returns session id, that points to a socket namespace

__request body:__
```json
{}
```

__responses:__

200
```json
{}
```

500
```
Internal Server Error

```