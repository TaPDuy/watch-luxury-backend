/favorites/
=======

Retrieve (GET), add (PUT) or remove (DELETE) a favorite.

- Methods: GET, PUT, DELETE
- Permissions: Authenticated + Read-only
- Response codes: API_SUCCESS, API_GENERIC_ERROR, API_NOT_FOUND, 400 (HTTP-GET)

## Request

<details open>
    <summary>PUT, DELETE</summary>

```json
{
    "user": "<user id:int>",
    "product": "<favorited product's id:int>",
}
```

</details>

## Response data

<details open>
    <summary>GET</summary>

```json
"data": [
    {
        "user": "<user's id:int>",
        "product": "<favorited product's id:int>",
        "time_added": "<time favorited:string>",
    },
    ...
]

```

</details>

<details open>
    <summary>PUT</summary>

```json
"data": {
    "user": "<user's id:int>",
    "product": "<favorited product's id:int>",
    "time_added": "<time favorited:string>",
}
```

</details>
