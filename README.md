
# 用户管理系统

这是一个使用 Python 和 Flask 框架以及 SQLite 数据库构建的用户管理系统。该项目提供了一个 RESTful API，支持用户的创建、查询、更新和删除操作。后端使用 Flask 框架，数据库使用 SQLite。

## 功能

- **创建用户**：将新用户添加到数据库。
- **查询用户**：根据用户 ID 获取用户信息。
- **更新用户**：更新已有用户的信息。
- **删除用户**：删除指定的用户。

## 使用的技术

- **Flask**：轻量级的 Python Web 框架。
- **SQLite**：轻量级的基于磁盘的数据库，用于存储用户数据。
- **Python 3.x**：用于构建应用程序的编程语言。

## 获取项目

按照以下步骤在本地设置项目。

### 前提条件

确保你已在本地安装了 Python 3.x。你可以从 [Python 官网](https://www.python.org/downloads/) 下载。

### 克隆仓库

首先，克隆仓库到你的本地机器：

```bash
git clone https://github.com/你的用户名/仓库名.git
```

然后进入项目目录：

```bash
cd 仓库名
```

### 安装依赖

在项目目录下创建虚拟环境：

```bash
cd UserManage_exp
python -m venv venv
```

激活虚拟环境：

- 在 Windows 上：

```bash
venv\Scripts\activate
```

- 在 macOS/Linux 上：

```bash
source venv/bin/activate
```

安装所需的依赖：

```bash
pip install -r requirements.txt
```

### 初始化数据库

在运行应用之前，需要先初始化 SQLite 数据库。数据库的 schema 信息在 `schema.sql` 文件中提供。

```bash
python run.py
```

### 运行应用

完成设置后，你可以运行应用：

```bash
python run.py
```

应用启动后，你可以通过 `http://127.0.0.1:5000` 访问 API。

## API 接口

### 1. 创建用户

- **接口**: `/create_user`
- **方法**: `POST`
- **请求体**:
    ```json
    {
        "username": "new_user",
        "email": "user@example.com",
        "password": "securepassword"
    }
    ```
- **响应**:
    ```json
    {
        "message": "User created successfully!"
    }
    ```

### 2. 根据 ID 查询用户

- **接口**: `/get_user/<user_id>`
- **方法**: `GET`
- **响应**:
    ```json
    {
        "id": 1,
        "username": "new_user",
        "email": "user@example.com",
        "password": "securepassword"
    }
    ```

### 3. 更新用户信息

- **接口**: `/update_user/<user_id>`
- **方法**: `PUT`
- **请求体**:
    ```json
    {
        "username": "updated_user",
        "email": "updated@example.com",
        "password": "newpassword"
    }
    ```
- **响应**:
    ```json
    {
        "message": "User updated successfully!"
    }
    ```

### 4. 删除用户

- **接口**: `/delete_user/<user_id>`
- **方法**: `DELETE`
- **响应**:
    ```json
    {
        "message": "User deleted successfully!"
    }
    ```

## 贡献

1. Fork 本仓库。
2. 创建一个新的分支 (`git checkout -b feature-branch`)。
3. 提交你的更改 (`git commit -am 'Add new feature'`)。
4. 推送到分支 (`git push origin feature-branch`)。
5. 创建 Pull Request。

## 许可

本项目采用 MIT 许可证，具体内容请参阅 [LICENSE](LICENSE) 文件。

## 致谢

- [Flask](https://flask.palletsprojects.com/) - 本项目使用的 Web 框架。
- [SQLite](https://www.sqlite.org/) - 本项目使用的数据库。
