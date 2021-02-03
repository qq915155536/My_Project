#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/11 15:51
# Author :A0025-江苏-小丹
# QQ:915155536
# File :json_path.py
#  ===========================
import jsonpath

data = {"store": {
    "book": [
        {"category": "reference",
         "author": "Nigel Rees",
         "title": "Sayings of the Century",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "Evelyn Waugh",
         "title": "Sword of Honour",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "Herman Melville",
         "title": "Moby Dick",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "J. R. R. Tolkien",
         "title": "The Lord of the Rings",
         "isbn": "0-395-19395-8",
         "price": 22.99
         }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}


bicycle=jsonpath.jsonpath(data,'$..title')
print(bicycle)