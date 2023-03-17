/login/refresh/
=======

Refresh access tokens.

- Methods: POST
- Permissions: Any
- Response codes: API_SUCCESS, API_GENERIC_ERROR

## Request

<details open>
    <summary>POST</summary>

```json
{
    "refresh": "<Your refresh token:string>"
}
```

</details>

## Response data

<details open>
    <summary>POST</summary>

```json
"data": {
    "refresh": "<New refresh token:string>",
    "access": "<New access token:string>"
}
```

</details>
