import json

data_to_dump = {
    "name": "Tommy",
    "age": 29,
    "city": "Taipei"
}

# 使用 json.dump 將數據轉換為 JSON 格式並寫入文件
with open("example.json", "w", encoding="utf-8") as json_file:
    json.dump(data_to_dump, json_file, ensure_ascii=False, indent=2)

# 使用 json.load 從文件中讀取 JSON 數據並轉換為 Python 數據結構
with open("example.json", "r", encoding="utf-8") as json_file:
    loaded_data = json.load(json_file)

# 打印輸出
print("原始數據：", data_to_dump)
print("讀取後的數據：", loaded_data)
