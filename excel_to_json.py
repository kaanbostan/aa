import pandas as pd
import json

# Dosya adı doğrudan yazılıyor (aynı klasörde olduğu için)
excel_dosyasi = "endustridersler.xls"

# Excel dosyasını oku
df = pd.read_excel(excel_dosyasi)

# JSON formatı için boş sözlük
tum_dersler = {}

# Her satırı dön
for _, satir in df.iterrows():
    kod = str(satir['CODE']).strip().lower().replace(" ", "")
    isim = str(satir['TITLE']).strip()
    semester = str(satir['SEMESTER']).strip()

    # "1. Year - Fall" → "1"
    if "." in semester:
        sinif = semester.split(".")[0].strip()
    else:
        sinif = "1"  # Varsayılan olarak 1

    tum_dersler[kod] = {
        "isim": isim,
        "bolumler": {
            "Endüstri Mühendisliği": sinif
        }
    }

# JSON dosyasına yaz
with open("tum_dersler.json", "w", encoding="utf-8") as f:
    json.dump(tum_dersler, f, ensure_ascii=False, indent=2)

print("✅ JSON dosyası başarıyla oluşturuldu!")
