# BIST Sektör Performans Analizi

Borsa İstanbul'da (BIST) işlem gören seçilmiş hisselerin sektör bazında performansını analiz eden ve görselleştiren bir Python projesidir.

Bu proje kapsamında **Savunma Sanayisi, Teknoloji ve Bankacılık** sektörlerinde yer alan hisselerin belirli bir dönem içerisindeki fiyat hareketleri incelenerek getiri ve volatilite karşılaştırmaları yapılmaktadır.

## Proje Amacı

Projenin amacı, farklı sektörlerde yer alan BIST hisselerinin performanslarını aynı dönem içerisinde karşılaştırmak, temel performans metriklerini hesaplamak ve sonuçları görsel olarak analiz etmektir.

## Proje Hakkında

Bu proje, seçilen BIST hisselerinin son 6 aylık tarihsel fiyat verilerini `yfinance` kütüphanesi aracılığıyla çeker.

Her hisse için aşağıdaki metrikler hesaplanır:

* Başlangıç fiyatı
* Güncel fiyat
* Toplam getiri (%)
* Günlük ortalama getiri (%)
* Volatilite (günlük getirilerin standart sapması)

Hesaplanan sonuçlar kullanılarak:

* Sektör bazlı normalize edilmiş fiyat karşılaştırmaları
* Toplam getiriye göre hisse performans sıralaması
* Performans özet CSV çıktısı

oluşturulur.

## Kapsanan Sektörler ve Hisseler

| Sektör           | Hisseler                                                                 |
| ---------------- | ------------------------------------------------------------------------ |
| Savunma Sanayisi | ASELSAN (ASELS.IS), Otokar (OTKAR.IS), Katmerciler (KATMR.IS)            |
| Teknoloji        | Karel (KAREL.IS), Logo Yazılım (LOGO.IS), Mia Teknoloji (MIATK.IS)       |
| Bankacılık       | Garanti Bankası (GARAN.IS), İş Bankası (ISCTR.IS), Yapı Kredi (YKBNK.IS) |

## Özellikler

### Veri Çekme

* `yfinance` API kullanılarak BIST hisselerine ait tarihsel fiyat verileri otomatik olarak alınır.

### Performans Analizi

Her hisse için:

* Başlangıç ve güncel fiyat karşılaştırması
* Toplam getiri hesaplama
* Günlük ortalama getiri hesaplama
* Volatilite analizi

yapılır.

### Görselleştirme

Proje aşağıdaki grafik çıktılarını üretir:

* Sektör bazlı normalize edilmiş fiyat karşılaştırma grafikleri (baz değer = 100)
* Tüm hisselerin toplam getirilerini karşılaştıran bar grafik

### Veri Çıktısı

Analiz sonuçları:

* CSV formatında performans özeti
* PNG formatında grafik çıktıları

olarak kaydedilir.

## Kullanılan Teknolojiler

* Python 3
* [yfinance](https://pypi.org/project/yfinance/) — Finansal veri çekme
* [pandas](https://pandas.pydata.org/) — Veri analizi ve tablo işlemleri
* [NumPy](https://numpy.org/) — Sayısal hesaplamalar
* [Matplotlib](https://matplotlib.org/) — Veri görselleştirme

## Kurulum

Projeyi bilgisayarınıza klonladıktan sonra gerekli kütüphaneleri yükleyin:

```bash
git clone https://github.com/ceydaisler/bist-sector-performance-analyzer.git
cd bist-sector-performance-analyzer
pip install -r requirements.txt
```

## Kullanım

Analizi çalıştırmak için:

```bash
python bist_sector_analyzer.py
```

Script çalıştırıldığında:

1. Hisselere ait son 6 aylık fiyat verileri alınır.
2. Performans metrikleri hesaplanır.
3. Sonuç özeti konsola yazdırılır.
4. Sektör karşılaştırma grafikleri oluşturulur.
5. Performans sonuçları CSV dosyasına aktarılır.

## Örnek Çıktılar

### Grafikler

Oluşturulan grafik dosyaları:

* `savunma_sanayisi_comparison.png`
* `teknoloji_comparison.png`
* `bankacilik_comparison.png`
* `total_return_bar_chart.png`

### Veri Çıktısı

* `bist_performance_summary.csv`

Dosyasında tüm hisselere ait performans metrikleri bulunmaktadır.

## Proje Yapısı

```
bist-sector-performance-analyzer/
│
├── bist_sector_analyzer.py       # Ana analiz scripti
├── requirements.txt              # Python bağımlılıkları
├── bist_performance_summary.csv  # Performans sonuçları
├── *.png                         # Grafik çıktıları
└── README.md
```

## Author

Ceyda İşler
