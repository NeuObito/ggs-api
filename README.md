# ggs-api

### ggs-database
- postgresql 创建用户(role)：CREATE USER username WITH PASSWORD 'password';
- 创建数据库：CREATE DATABASE database OWNER username;
- 赋予权限：GRANT ALL PRIVILEGES ON DATABASE database to username;
- 修改密码：ALTER USER username WITH PASSWORD 'password';