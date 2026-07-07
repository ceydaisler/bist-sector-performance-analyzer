import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TICKERS = {
    "Savunma Sanayisi": {
        "ASELS.IS": "ASELSAN",
        "OTKAR.IS": "Otokar",
        "KATMR.IS": "Katmerciler"
    },
    "Teknoloji" :{
        "KAREL.IS":"Karel",
        "LOGO.IS": "logo Yazılım",
        "MIATK.IS": "Mia Teknoloji"
    },
    "Bankacılık": {
        "GARAN.IS": "Garanti Bankası",
        "ISCTR.IS": "İş Bankası",
        "YKBNK.IS": "Yapı Kredi"
    }}

PERIOD = "6mo"

CATEGORY_COLORS = {
    "Savunma Sanayisi": "#B0564C",
    "Bankacılık": "#5452DD",
    "Teknoloji": "#55A868"
}

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)  #Ticker ile hisseyi seçtiriyoruz
    hist = stock.history(period=PERIOD)   #history ile de seçtirdiğimiz hissenin belırledıgımız sure aralıgındakı verılerılerını cekıyoruz
    return hist   #burdaki hist yahoo dan gelen dataframe

def calculate_metrics(hist,name,category):
    hist = hist.copy() # data frame uzerınden degısıklık yapıcagımız ıcın kopyaladık
    hist["Daily Return (%)"] = hist["Close"].pct_change() * 100

    total_return= ((hist["Close"].iloc[-1] / hist["Close"].iloc[0]) - 1 ) * 100
    volatility = hist["Daily Return (%)"].std()
    avg_daily_return = hist["Daily Return (%)"].mean()

    summary = {
        "Kategori" : category,
        "Hisse" : name,
        "Başlangıç Fiyatı": round(hist["Close"].iloc[0], 2),
        "Güncel Fiyatı": round(hist["Close"].iloc[-1] , 2),
        "Toplam Getiri(%)": round(total_return , 2),
        "Günlük Ort. Getiri(%)": round(avg_daily_return, 3),
        "Volatilite(Std.sapma)": round(volatility,3)        
        }
    
    return hist, summary

def plot_category_comparison(category_name , histories_dict):
    plt.figure(figsize=(10,6))

    for name , hist in histories_dict.items():
        normalized = hist["Close"] / hist["Close"].iloc[0] * 100
        plt.plot(normalized.index, normalized, label = name, linewidth= 2)

    plt.title(f"{category_name} Hisseleri - Karşılaştırmalı Performans (Baz=100)")
    plt.xlabel("Tarih")
    plt.ylabel("Normalize Fiyat (Başlangıç = 100)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()


    filename = category_name.lower()
    filename = (filename.replace("ı", "i").replace("ş", "s")
                         .replace("ç", "c").replace("ö", "o")
                         .replace("ü", "u").replace("ğ", "g")
                         .replace(" ", "_"))
    plt.savefig(f"{filename}_comparison.png")
    plt.close()
    print(f"Kaydedildi: {filename}_comparison.png")

def plot_total_return_bar_chart(summary_df):
    plt.figure(figsize=(12,6))

    df_sorted= summary_df.sort_values(by="Toplam Getiri(%)",ascending= False) 
    colors = []
    for category in df_sorted["Kategori"]:
        color = CATEGORY_COLORS[category]
        colors.append(color)

        bars = plt.bar(df_sorted["Hisse"], df_sorted["Toplam Getiri(%)"], color = colors)
        
        plt.title("Son 6 Ayda Hisse Bazlı Toplam Getiri Karşılaştırması")
        plt.xlabel("Hisse")
        plt.ylabel("Toplam Getiri(%)")
        plt.xticks(rotation = 45 , ha="right" )
        plt.axhline(y = 0 , color = "black" , linewidth = 0.8)
        plt.grid(True , axis="y", alpha = 0.3)

        for i in range(len(bars)):
            
            bar = bars[i]
            value = df_sorted["Toplam Getiri(%)"].iloc[i]

            x = bar.get_x()
            width = bar.get_width()

            center = x + width / 2

            if value > 0:
                vertical_alignment = "bottom" 
            else:
                vertical_alignment = "top"

            plt.text(
                center,
                value,
                f"{value:.1f}%",
                ha = "center",
                va=vertical_alignment,
                fontsize = 9
                )          

        
        from matplotlib.patches import Patch
        legend_elements = []
        
        for category, color in CATEGORY_COLORS.items():
            patch = Patch(facecolor= color, label=category)
            legend_elements.append(patch)     

        plt.legend(handles= legend_elements,title ="Sektör")
        plt.tight_layout()
        plt.savefig("total_return_bar_chart.png")
        plt.close()
        print("Kaydedildi: total_return_bar_chart.png")

def main():
     all_summaries = []

     for category , stocks in TICKERS.items():
         category_histories = {}

         for ticker , name in stocks.items():
            print(f"{name} ({ticker}) verisi çekiliyor...")
            hist = fetch_stock_data(ticker)

            if hist.empty:
                print(f"Uyarı: {ticker} için veri bulunamadı, atlanıyor.")
                continue

            hist_with_metrics ,summary = calculate_metrics(hist,name,category)
            all_summaries.append(summary)
            category_histories[name] = hist_with_metrics

         plot_category_comparison(category, category_histories)

     summary_df = pd.DataFrame(all_summaries)
     summary_df = summary_df.sort_values(by= ["Kategori","Toplam Getiri(%)"], ascending=[True,False])

     print("\n--- Genel Performans Özeti ---")
     print(summary_df.to_string(index=False))

     summary_df.to_csv("bist_performance_summary.csv", index=False)
     print("\nÖzet 'bist_performance_summary.csv' dosyasına kaydedildi.")
    
     print("\n--- Genel Performans Özeti ---")
     print(summary_df.to_string(index=False))

     summary_df.to_csv("bist_performance_summary.csv", index=False)
     print("\nÖzet 'bist_performance_summary.csv' dosyasına kaydedildi.")

     plot_total_return_bar_chart(summary_df)

main()
    
