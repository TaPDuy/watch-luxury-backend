/register/
=======

Create a new account. Activation link is sent to the registered user's email.

- Methods: POST
- Permissions: Any

## Request

<details open>
    <summary>POST</summary>

```json
{
    "username": "<Your username:string>",
    "password": "<Your password:string>",
    "email": "<Your email:string>",
    "address": "<Your address:string>"
}
```

</details>

## Response data

<details open>
    <summary>POST</summary>

```json
"data": {
    "id": "<Registered user id:int>",
    "username": "<Registered username:string>",
    "first_name": "",
    "last_name": "",
    "email": "<Registered user email:string>",
    "address": "<Registered user address:string>",
    "phone_number": "",
    "is_active": false,
    "is_admin": false,
    "last_login": null,
    "date_joined": "<Registered date:string>"
}
```

</details>
