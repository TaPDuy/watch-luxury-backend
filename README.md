# Watch Luxury API

[Watch Luxury](https://github.com/TaPDuy/watch-luxury) app's Django backend

## Models

|Model  |Attributes                                             |
|-------|-------------------------------------------------------|
|User   |id, username, password, email, address, phone_number   |
|Product|id, name, price, manufacturer_name, descriptions       |
|Order  |id, user_id, product_id, amount                        |

## Public endpoints

|URI                            |Method |Action                 |
|-------------------------------|:-----:|-----------------------|
|/login/                        |POST   |Đăng nhập              |
|/login/refresh/                |POST   |Làm mới access token   |
|/register/                     |POST   |Đăng ký                |
|/verify/                       |GET    |Kích hoạt tài khoản    |
|/users/                        |GET    |Lấy tất cả tài khoản   |
|/users/{id}/                   |GET    |Lấy 1 tài khoản        |
|/users/{id}/                   |PUT    |Cập nhật 1 tài khoản   |
|/users/{id}/change_password/   |PUT    |Đổi mật khẩu           |
|/products      |GET    |Lấy tất cả item     |
|/products/{id} |GET    |Lấy 1 item          |
|/orders        |POST   |Tạo 1 order         |

## Error code

|Code   |Codename           |Meaning                    |
|:-----:|-------------------|---------------------------|
|0      |API_SUCCESS        |Xử lý request thành công   |
|10     |API_GENERIC_ERROR  |Lỗi                        |
|11     |API_WRONG_PASSWORD |Sai mật khẩu               |
