/products/
=======

Retrieve all products.

- Methods: GET
- Permissions: Authenticated + Read-only
- Response codes: API_SUCCESS

## Filters
| Name     | Type   | Action                           |
| -------- | ------ | -------------------------------- |
| category | String | Lấy tất cả item thuộc 1 category |

## Response data

<details open>
    <summary>GET</summary>

```json
"data": [
    {
        "id": "<product id:int>",
        "name": "<product name:string>",
        "description": "<product details:string>",
        "price": "<product price:decimal>",
        "image": "<image's url:string>",
        "time_added": "<product added time:string>",
        "time_updated": "<ptoduct modified time:string>"
    },
    ...
]
```

</details>
