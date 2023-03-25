Endpoints
=========

| URI                                                | Method | Action               |
| -------------------------------------------------- | :----: | -------------------- |
| [/login/](login.md)                                |  POST  | Đăng nhập            |
| [/login/refresh/](login-refresh.md)                |  POST  | Làm mới access token |
| [/register/](register.md)                          |  POST  | Đăng ký              |
| [/verify/](verify.md)                              |  GET   | Kích hoạt tài khoản  |
| [/users/](users.md)                                |  GET   | Lấy tất cả tài khoản |
| [/users/{id}/](user.md)                            |  GET   | Lấy 1 tài khoản      |
| [/users/{id}/](user.md)                            |  PUT   | Cập nhật 1 tài khoản |
| [/users/{id}/change_password/](change-password.md) |  PUT   | Đổi mật khẩu         |
| [/products/](products.md)                          |  GET   | Lấy tất cả item      |
| [/products/{id}/](product.md)                      |  GET   | Lấy 1 item           |
| /orders                                            |  POST  | Tạo 1 order          |

## Response

```json
{
    "code": "<Response code:int>",
    "msg": "<Response message:string>",
    "data": "<Response data:object>"
}
```

## Response code

| Code  | Codename           | Meaning                  |
| :---: | ------------------ | ------------------------ |
|   0   | API_SUCCESS        | Xử lý request thành công |
|  10   | API_GENERIC_ERROR  | Lỗi                      |
|  11   | API_WRONG_PASSWORD | Sai mật khẩu             |
|  12   | API_INVALID_LOGIN  | Sai thông tin đăng nhập  |
