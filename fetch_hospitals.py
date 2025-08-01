import json
import requests

# 示例：假設日後連接政府 API，暫時模擬資料
hospitals = [
    {
        "name": "威爾斯親王醫院",
        "type": "公立醫院",
        "district": "沙田",
        "address": "新界沙田銀城街30號",
        "phone": "3505 2222",
        "emergency": "有",
        "specialties": "內科、外科、婦產科、兒科、腫瘤科",
        "hours": "24小時急症室",
        "website": "https://www3.ha.org.hk/pwh/"
    }
]

with open("hospitals.json", "w", encoding="utf-8") as f:
    json.dump(hospitals, f, ensure_ascii=False, indent=2)
print("✅ 醫院資料已更新")
