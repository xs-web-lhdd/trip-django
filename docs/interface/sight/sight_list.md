## 首页景点列表接口

### 请求地址
/sight/sight/list/

### 调用方式
GET

### 请求参数
无

### 返回结果
```
{
    "meta": {
        "total_count": 2,
        "page_count": 1,
        "current_page": 1
    },
    "objects": [
        {
            "id": 2,
            "name": "云台山",
            "main_img": "/main_img",
            "score": 10,
            "province": "河南",
            "min_price": 150,
            "city": "焦作",
            "comment_count": 0
        },
        {
            "id": 1,
            "name": "测试景点",
            "main_img": "/main_img",
            "score": 8,
            "province": "河南",
            "min_price": 100,
            "city": "焦作",
            "comment_count": 0
        }
    ]
}
```

### 返回字段的说明
