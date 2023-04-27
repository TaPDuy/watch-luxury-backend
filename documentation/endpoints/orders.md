/orders/
=======

Retrieve all orders or create an order.

- Methods: GET, POST
- Permissions: Authenticated + Read-only
- Response codes: API_SUCCESS, API_GENERIC_ERROR, API_NOT_FOUND, 400 (HTTP-GET)

## Filters
| Name | Type | Action                      |
| ---- | ---- | --------------------------- |
| user | Int  | Lấy tất cả order của 1 user |

## Request

<details open>
    <summary>POST</summary>

```json
"data": [
    {
        "user": "<order's owner's id:int>",
        "name": "<owner's name:string/optional>",
        "phone_number": "<owner's phone number:string/optional>",
        "address": "<owner's address:string/optional>",
        "products": ["<product ordered's id:int>", ...],
    },
    ...
]
```

</details>

## Response data

<details open>
    <summary>GET</summary>

```json
"data": [
    {
        "id": "<order id:int>",
        "user": "<order's owner:user>",
        "name": "<owner's name:string>",
        "phone_number": "<owner's phone number:string>",
        "address": "<owner's address:string>",
        "products": ["<product ordered:product>", ...],
        "total": "<total price:int>",
        "status": "<order's status:string>",
        "time_added": "<order added time:string>",
    },
    ...
]
```

</details>
