// Bölüm listesini yükle ve göster
function loadBolumler() {
  fetch('data/dersler.json')
    .then(res => res.json())
    .then(data => {
      const bolumlerSet = new Set();
      for (const dersKod in data) {
        const ders = data[dersKod];
        for (const bolum in ders.bolumler) {
          bolumlerSet.add(bolum);
        }
      }
      const bolumler = [...bolumlerSet];
      const div = document.getElementById("bolumler");
      bolumler.forEach(bolum => {
        const btn = document.createElement("button");
        btn.textContent = bolum;
        btn.onclick = () => {
          localStorage.setItem("selectedBolum", bolum);
          window.location.href = "siniflar.html";
        };
        div.appendChild(btn);
      });
    });
}

// Seçilen bölüme ait sınıfları listele
function loadSiniflar() {
  const bolum = localStorage.getItem("selectedBolum");
  fetch('data/dersler.json')
    .then(res => res.json())
    .then(data => {
      const siniflarSet = new Set();
      for (const dersKod in data) {
        const ders = data[dersKod];
        if (ders.bolumler.hasOwnProperty(bolum)) {
          siniflarSet.add(ders.bolumler[bolum]);
        }
      }
      const siniflar = [...siniflarSet].sort((a, b) => Number(a) - Number(b));
      const div = document.getElementById("siniflar");
      siniflar.forEach(sinif => {
        const btn = document.createElement("button");
        btn.textContent = `${sinif}. Sınıf`;
        btn.onclick = () => {
          localStorage.setItem("selectedSinif", sinif);
          window.location.href = "dersler.html";
        };
        div.appendChild(btn);
      });
    });
}

// Seçilen bölüm ve sınıfa ait dersleri listele
function loadDersler() {
  const bolum = localStorage.getItem("selectedBolum");
  const sinif = localStorage.getItem("selectedSinif");
  fetch('data/dersler.json')
    .then(res => res.json())
    .then(data => {
      const dersler = [];
      for (const dersKod in data) {
        const ders = data[dersKod];
        if (ders.bolumler.hasOwnProperty(bolum) && ders.bolumler[bolum] === sinif) {
          dersler.push({
            kod: dersKod,
            isim: ders.isim
          });
        }
      }
      const div = document.getElementById("dersler");
      dersler.forEach(ders => {
        const btn = document.createElement("button");
        btn.textContent = `${ders.kod.toUpperCase()} - ${ders.isim}`;
        btn.onclick = () => {
          localStorage.setItem("selectedDers", ders.kod);
          window.location.href = "ders.html";
        };
        div.appendChild(btn);
      });
    });
}

// Seçilen dersin belgelerini göster
function loadBelgeler() {
  const dersKodu = localStorage.getItem("selectedDers");
  fetch('data/belgeler.json')
    .then(res => res.json())
    .then(data => {
      const belgeler = data[dersKodu.toUpperCase()] || [];
      const div = document.getElementById("belgeler");
      div.innerHTML = ""; // Önce temizle
      if (belgeler.length === 0) {
        div.textContent = "Bu derse ait henüz belge eklenmedi.";
        return;
      }
      belgeler.forEach(belge => {
        const link = document.createElement("a");
        link.href = `assets/${belge.dosya}`;
        link.textContent = belge.isim;
        link.target = "_blank";
        div.appendChild(link);
        div.appendChild(document.createElement("br"));
      });
    });
}
