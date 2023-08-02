# Vue 前端：
## 安装依赖
```
npm install
```
## 项目启动
```
npm run serve
```
<br/>注意：本地 node 版本，开发时本机 node 版本为 16.15.1
## 项目打包
```
npm run build
```

# Django 后端项目：
## 项目前置信息
- 项目创建：`django-admin startapp trip`
- 开发时所使用的 conda 环境是 web
- 数据库建模工具 pdman
- 前端: Vue + vantUI + axios
- 后端: Django + redis + mysql

## redis 相关
### 本地启动 redis
- 1、找到磁盘中 redis 的位置
- 2、找到 redis 文件夹中的 redis-server.exe 点击运行
- 3、找到 redis 文件夹中的 redis-cli.exe 点击运行
### Django 中使用 redis
#### 1、安装
`pip install django-redis`
#### 2、配置 settings.py
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```
#### 3、存取
```python
from django.core.cache import cache
# 存储
cache.set(key, value, timeout=None) # timeout 是存储时间
# 查询
cache.get(key)
```

## django-auth 模块
### 功能介绍
- 用户模型： 用户认证、登陆、退出
- 后台管理： 用户权限、权限分配
- 命令行工具： 创建用户、设置密码
### 安装及配置
- 第一步：INSTALLED_APPS 安装应用
```
'django.contrib.auth'
'django.contrib.contenttypes'
```
- 第二步：MIDDLEWARE 中间配置
```
SessionMiddleware
AuthenticationMiddleware
```
- 第三步：migrate同步模型到数据库

### 用户模型
- 注册用户(User)
- 游客(AnonymousUser)
#### 用户管理
- 创建普通用户 `user=User.objects.create_user('john', 'xxx@qq.com', 'password')`
- 创建超级管理员 `python manage.py createsuperuser`
- 验证用户名和密码是否匹配 `user=authenticate(username, password)`
- 在视图中获取当前用户 `request.user`
- 需要登陆才可访问的视图
```python
@login_required
def my_view(request):
    # ...
```
#### 权限管理
- 判断用户是否具备某权限 `request.user.has_perm('foo.add_bar')`
- 强制权限验证
```python
@permission_required('foo.add_bar')
def my_view(request):
    # ...
```
#### 对用户进行扩展
- 两种方式解决用户问题
  - 方式一：使用 OneToOneField 对用户进行扩展
  - 方式二：替换现有的用户模型
##### 替换现有的用户模型
- 步骤一：配置用户模型，告诉django 框架 `AUTH_USER_MODEL=accounts.User`
- 步骤二：继承自 AbstractUser 抽象模型
- 步骤三：添加字段，同步模型到数据库

## 用户登陆
- 步骤一：认证用户 `user = authenticate(username='xx', password='xx')`
- 步骤二：判断认真后的用户是否为 None，不用不为 None 则表示用户认证通过
- 步骤三：调用 login 函数登陆用户 `login(request, user, backend=None)`

