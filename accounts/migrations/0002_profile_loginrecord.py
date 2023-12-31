# Generated by Django 4.2.3 on 2023-08-03 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        editable=False, max_length=64, unique=True, verbose_name="用户名"
                    ),
                ),
                ("real_name", models.CharField(max_length=32, verbose_name="真实姓名")),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="电子邮箱"
                    ),
                ),
                (
                    "is_email_valid",
                    models.BooleanField(default=False, verbose_name="邮箱是否已经验证"),
                ),
                (
                    "phone_no",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="手机号码"
                    ),
                ),
                (
                    "is_phone_valid",
                    models.BooleanField(default=False, verbose_name="是否已经验证"),
                ),
                (
                    "sex",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (0, "女")], default=1, verbose_name="性别"
                    ),
                ),
                ("age", models.SmallIntegerField(default=0, verbose_name="年龄")),
                (
                    "source",
                    models.CharField(max_length=16, null=True, verbose_name="登录的来源"),
                ),
                (
                    "version",
                    models.CharField(max_length=16, null=True, verbose_name="登录的版本"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "accounts_user_profile",},
        ),
        migrations.CreateModel(
            name="LoginRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="登录的账号")),
                ("ip", models.CharField(max_length=32, verbose_name="IP")),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="地址"
                    ),
                ),
                (
                    "source",
                    models.CharField(max_length=16, null=True, verbose_name="登录的来源"),
                ),
                (
                    "version",
                    models.CharField(max_length=16, null=True, verbose_name="登录的版本"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="登录时间"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="login_records",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "accounts_login_record",},
        ),
    ]
