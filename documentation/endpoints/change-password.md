/users/{id}/change_password/
=======

Update (PUT) the password of the user account with the specified **`{id}`**.

- Methods: PUT
- Permissions: Authenticated 
- Response codes: API_SUCCESS, API_WRONG_PASSWORD, API_GENERIC_ERROR

## Request

<details open>
    <summary>PUT</summary>

```json
{
    "old_password": "<old password:string>",
    "new_password": "<new password:string>"
}
```

</details>
