/users/{id}/
=======

Retrieve (GET) or update (PUT) user account with the specified **`{id}`**.

- Methods: GET, PUT
- Permissions: Authenticated + Read-only

## Request

<details open>
    <summary>PUT</summary>

```json
{
    "first_name": "<New last name:string>",
    "last_name": "<New first name:string>",
    "email": "<New email:string>",
    "address": "<New address:string>",
    "phone_number": "<New phone number:string>",
}
```

*Notes: `email` and `address` fields are required, the rest is optional.*

</details>

## Response data

<details open>
    <summary>GET</summary>

```json
"data": {
    "id": "<user id:int>",
    "username": "<username:string>",
    "first_name": "<user's first name:string>",
    "last_name": "<user's last name:string>",
    "email": "<user's email:string>",
    "address": "<user's address:string>",
    "phone_number": "<user's phone number:string>",
    "is_active": "<true/false>",
    "is_admin": "<true/false>",
    "last_login": "<lastest login date:string>",
    "date_joined": "<registered date:string>"
}
```

</details>

<details open>
    <summary>PUT</summary>

```json
"data": {
    "id": "<user id:int>",
    "username": "<username:string>",
    "first_name": "<updated first name:string>",
    "last_name": "<updated last name:string>",
    "email": "<updated email:string>",
    "address": "<updated address:string>",
    "phone_number": "<updated phone number:string>",
    "is_active": "<true/false>",
    "is_admin": "<true/false>",
    "last_login": "<lastest login date:string>",
    "date_joined": "<registered date:string>"
}
```

</details>
