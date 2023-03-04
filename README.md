# Watch Luxury API

[Watch Luxury](https://github.com/TaPDuy/watch-luxury) app's Django backend

## Models

|Model  |Attributes                                             |
|-------|-------------------------------------------------------|
|User   |id, username, password, email, address, phone_number   |
|Product|id, name, price, manufacturer_name, descriptions       |
|Order  |id, user_id, product_id, amount                        |

## Public gateways

|URI            |Method |Action              |
|---------------|-------|--------------------|
|/login         |POST   |Đăng nhập           |
|/register      |POST   |Đăng ký             |
|/users         |GET    |Lấy tất cả tài khoản|
|/users/{id}    |GET    |Lấy 1 tài khoản     |
|/users/{id}    |PUT    |Cập nhật 1 tài khoản|
|/products      |GET    |Lấy tất cả item     |
|/products/{id} |GET    |Lấy 1 item          |
|/orders        |POST   |Tạo 1 order         |
