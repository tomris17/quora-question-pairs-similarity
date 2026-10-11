import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Quora Question Pairs Similarity",
    page_icon="❓",
    layout="centered"
)

st.title("❓ Quora Question Pairs - Soru Benzerliği Analizi")
st.write("Bu uygulama, girdiğiniz iki sorunun aynı anlama gelip gelmediğini analiz eder.")

q1 = st.text_input("Birinci Soru:", "What is the step by step guide to invest in share market?")
q2 = st.text_input("İkinci Soru:", "What is the best way to invest in the stock market?")

if st.button("Benzerliği Kontrol Et"):
    if not q1.strip() or not q2.strip():
        st.warning("Lütfen her iki soru alanını da doldurun.")
    else:
        # Basit bir kelime örtüşme (Jaccard Similarity) mantığıyla demo skor üretelim
        set1 = set(q1.lower().split())
        set2 = set(q2.lower().split())
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        jaccard_score = len(intersection) / len(union) if union else 0.0
        
        st.markdown("---")
        st.subheader("📊 Analiz Sonucu:")
        st.write(f"Kelime Benzerlik Oranı (Jaccard): **%{jaccard_score * 100:.2f}**")
        
        if jaccard_score > 0.4:
            st.success("🟢 **Aynı Anlama Geliyor (Duplicate Olma İhtimali Yüksek)**")
        else:
            st.info("🔵 **Farklı Sorular (Ayrı Konular)**")