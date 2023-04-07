/users/{id}/favorites/
=======

Retrieve (GET) user's favorited products.

- Methods: GET
- Permissions: Authenticated + Read-only
- Response codes: API_SUCCESS, API_GENERIC_ERROR, 400 (HTTP-GET)

## Response data

<details open>
    <summary>GET</summary>

```json
"data": [
    {
        "id": "<product id:int>",
        "name": "<product name:string>",
        "description": "<product details:string>",
        "price": "<product price:long>",
        "image": "<image's url:string>",
        "favorites_count": "<number of favorites>:int",
        "categories": ["<category name:string>", ...],
        "time_added": "<product added time:string>",
        "time_updated": "<ptoduct modified time:string>"
    },
    ...
]
```
