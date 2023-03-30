/products/categories/
=======

Retrieve all categories.

- Methods: GET
- Permissions: Authenticated + Read-only
- Response codes: API_SUCCESS

## Response data

<details open>
    <summary>GET</summary>

```json
"data": {
    "id": "<category id:int>",
    "name": "<category name:string>",
    "slug": "<category slug name:string>",
    "description": "<category description:string>",
}
```
