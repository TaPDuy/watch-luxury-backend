/users/
=======

Retrieve all registered user accounts' details.

- Methods: GET
- Permissions: Authenticated + Read-only

## Response data

<details open>
    <summary>GET</summary>

```json
"data": [
    {
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
    },
    ...
]
```

</details>
