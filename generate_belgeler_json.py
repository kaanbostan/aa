import os
import json

base_path = "assets"
output = {}

for course_code in os.listdir(base_path):
    course_path = os.path.join(base_path, course_code)
    if os.path.isdir(course_path):
        files = os.listdir(course_path)
        output[course_code.upper()] = [
            {
                "isim": os.path.splitext(file)[0].replace("_", " ").title(),
                "dosya": f"{course_code}/{file}"
            }
            for file in files if not file.startswith(".")
        ]

with open("data/belgeler.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("✅ belgeler.json başarıyla oluşturuldu.")
