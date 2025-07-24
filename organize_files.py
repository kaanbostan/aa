import os
import shutil

# Klasörler
NEW_FILES_DIR = "new_files_to_add"
ASSETS_DIR = "assets"

def main():
    if not os.path.exists(NEW_FILES_DIR):
        print(f"{NEW_FILES_DIR} klasörü bulunamadı. Lütfen oluşturup içine dosya koy.")
        return

    # new_files_to_add içindeki tüm dosyaları işle
    for dosya_adi in os.listdir(NEW_FILES_DIR):
        if os.path.isfile(os.path.join(NEW_FILES_DIR, dosya_adi)):
            # Dosya adından ders kodunu ve belge adını çıkar
            # Örnek: sec101_syllabus.pdf  -> derskodu=sec101, belge_adi=syllabus.pdf
            try:
                ders_kodu, belge_adi = dosya_adi.split('_', 1)
            except ValueError:
                print(f"UYARI: '{dosya_adi}' dosya adı 'derskodu_belgeadi.ext' formatında değil, atlandı.")
                continue

            # Hedef klasör
            hedef_klasor = os.path.join(ASSETS_DIR, ders_kodu.lower())
            if not os.path.exists(hedef_klasor):
                os.makedirs(hedef_klasor)
                print(f"{hedef_klasor} klasörü oluşturuldu.")

            # Dosyayı taşımak
            kaynak_dosya = os.path.join(NEW_FILES_DIR, dosya_adi)
            hedef_dosya = os.path.join(hedef_klasor, belge_adi)
            shutil.move(kaynak_dosya, hedef_dosya)
            print(f"{dosya_adi} -> {hedef_dosya} taşındı.")

    print("Tüm dosyalar taşındı. Şimdi 'generate_belgeler_json.py' dosyasını çalıştırabilirsin.")

if __name__ == "__main__":
    main()
