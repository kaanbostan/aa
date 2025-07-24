# ÖzÜ Ders Kütüphanesi

Özyeğin Üniversitesi Endüstri Mühendisliği bölümü ders materyallerini düzenli ve kolay erişilebilir şekilde saklamak ve paylaşmak için hazırlanmış web tabanlı ders arşivi projesidir.

---

## İçindekiler

- Bölümlere göre sınıf listesi
- Sınıflara göre ders listesi
- Derslere ait PDF, video, slayt gibi belgeler
- Dinamik ve genişletilebilir JSON tabanlı veri yönetimi
- Kolay dosya yükleme ve düzenleme altyapısı

---

## Kullanım

1. Proje dosyalarını yerel sunucuna (örneğin Python `http.server` ile) yükleyin.
2. Tarayıcıda `index.html` dosyasını açarak ana sayfadan bölümü seçin.
3. Bölüm seçildikten sonra sınıf seçip, sınıfa ait dersleri görüntüleyebilirsiniz.
4. İlgili ders seçilince o derse ait belgeler listelenir ve tıklayarak erişilebilir.
5. Yeni ders ve belge eklemek için JSON dosyaları (`data/dersler.json` ve `data/belgeler.json`) güncellenebilir.
6. Dosyalar `assets/` klasörü altında ilgili ders klasörüne yerleştirilir.

---

## Dosya Yapısı


ders-kutuphanesi/
├── index.html
├── bolumler.html
├── siniflar.html
├── dersler.html
├── ders.html
├── data/
│ ├── dersler.json
│ └── belgeler.json
├── assets/
│ ├── ie101/
│ └── math103/
├── style.css
└── app.js


---

## Geliştirme

- Proje JavaScript ile dinamik içerik yönetimi yapmaktadır.
- Yeni bölümler ve sınıflar JSON dosyasına eklenerek kolayca genişletilebilir.
- Tasarım sade ve mobil uyumludur.
- İleride farklı bölümler eklenebilir, ortak dersler aynı ders koduyla tanımlanabilir.

---

## Gereksinimler

- Modern web tarayıcı (Chrome, Firefox, Edge vb.)
- Yerel sunucu ortamı (örn. Python 3: `python -m http.server`)

---

## Katkıda Bulunma

Bu proje açık kaynaklıdır. İyileştirme ve öneriler için pull request gönderebilirsiniz.

---

## İletişim

Proje sahibi: [Kaan Bostan]  
E-posta: [kaan.kbostan@gmail.com]
