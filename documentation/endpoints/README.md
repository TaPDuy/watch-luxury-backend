Endpoints
=========

| URI                                                | Method | Action                                |
| -------------------------------------------------- | :----: | ------------------------------------- |
| [/login/](login.md)                                |  POST  | Đăng nhập                             |
| [/login/refresh/](login-refresh.md)                |  POST  | Làm mới access token                  |
| [/register/](register.md)                          |  POST  | Đăng ký                               |
| [/verify/](verify.md)                              |  GET   | Kích hoạt tài khoản                   |
| [/users/](users.md)                                |  GET   | Lấy tất cả tài khoản                  |
| [/users/{id}/](user.md)                            |  GET   | Lấy 1 tài khoản                       |
| [/users/{id}/](user.md)                            |  PUT   | Cập nhật 1 tài khoản                  |
| [/users/{id}/change_password/](change-password.md) |  PUT   | Đổi mật khẩu                          |
| [/users/{id}/favorites/](favorite-products.md)     |  GET   | Lấy tất cả sản phẩm ưa thích của user |
| [/products/](products.md)                          |  GET   | Lấy tất cả item                       |
| [/products/{id}/](product.md)                      |  GET   | Lấy 1 item                            |
| [/products/categories/](categories.md)             |  GET   | Lấy tất cả category                   |
| [/products/{id}/favorites/](favorited-users.md)    |  GET   | Lấy tất cả user ưa thích sản phẩm     |
| [/favorites/](favorite.md)                         |  GET   | Lấy tất cả lượt ưa thích              |
| [/favorites/](favorite.md)                         |  POST  | Ưa thích sản phẩm                     |
| [/favorites/](favorite.md)                         | DELETE | Bỏ ưa thích sản phẩm                  |
| [/orders/](orders.md)                              |  GET   | Xem tất cả order                      |
| [/orders/](orders.md)                              |  POST  | Tạo 1 order                           |

## Response

```json
{
    "code": "<Response code:int>",
    "msg": "<Response message:string>",
    "data": "<Response data:object>"
}
```

## Response code

| Code  | Codename           | Meaning                   |
| :---: | ------------------ | ------------------------- |
|   0   | API_SUCCESS        | Xử lý request thành công  |
|  10   | API_GENERIC_ERROR  | Lỗi                       |
|  11   | API_WRONG_PASSWORD | Sai mật khẩu              |
|  12   | API_INVALID_LOGIN  | Sai thông tin đăng nhập   |
|  13   | API_NOT_FOUND      | Không tìm thấy tài nguyên |
