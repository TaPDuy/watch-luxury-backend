/login/
=======

Login and receive access tokens.

- Methods: POST
- Permissions: Any
- Response codes: API_SUCCESS, API_INVALID_LOGIN

## Request

<details open>
    <summary>POST</summary>

```json
{
    "username": "<Login username:string>",
    "password": "<Login password:string>"
}
```

</details>

## Response data

<details open>
    <summary>POST</summary>

```json
"data": {
    "refresh": "<Your refresh token:string>",
    "access": "<Your access token:string>",
    "user_id": "<Logged in user id:int>"
}
```

</details>
