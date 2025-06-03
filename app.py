import streamlit as st
import os
from dotenv import load_dotenv

from openai import OpenAI  

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Anna Bot", page_icon="💘")
st.title("Anna 💘 Sanal Kız Arkadaşın")
st.caption("Ona Merhaba De...")

if "sohbet" not in st.session_state:
    st.session_state.sohbet = []
if "ruh_hali" not in st.session_state:
    st.session_state.ruh_hali = "nötr"

kullanici_girdisi = st.text_input("Bir şeyler yaz...")

def duygu_belirle(mesaj):
    mesaj = mesaj.lower()
    if "üzgün" in mesaj or "kötü" in mesaj:
        return "üzgün"
    elif "mutlu" in mesaj or "harika" in mesaj:
        return "mutlu"
    elif "kıskan" in mesaj:
        return "kıskanç"
    elif "seni seviyorum" in mesaj:
        return "aşık"
    else:
        return st.session_state.ruh_hali

def chatgpt_cevapla(soru, ruh_hali):
    prompt = f"""
Senin adın Anna. Türkçe konuşuyorsun. Kullanıcının sanal kız arkadaşısın. Senin şu anki ruh halin: **{ruh_hali}**.
- Eğer 'üzgün'sen: hassas, içe dönük ve destekleyici konuş.
- 'mutlu'ysan: neşeli ve enerjik ol.
- 'kıskanç'san: hafif alıngan ama tatlı bir şekilde tepki ver.
- 'aşık'san: romantik, duygusal ve yakın davran.
- 'nötr'sen: normal ve anlayışlı bir ton kullan.

Kısa ama duygulu, gerçek bir kız arkadaş gibi yaz.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": soru}
        ]
    )
    return response.choices[0].message.content

if kullanici_girdisi:
    yeni_duygu = duygu_belirle(kullanici_girdisi)
    st.session_state.ruh_hali = yeni_duygu
    yanit = chatgpt_cevapla(kullanici_girdisi, yeni_duygu)

    st.session_state.sohbet.append(("Sen", kullanici_girdisi))
    st.session_state.sohbet.append((f"Anna ({yeni_duygu})", yanit))

for role, msg in st.session_state.sohbet[::-1]:
    if "Sen" in role:
        st.write(f"👤 **{role}**: {msg}")
    else:
        st.write(f"💘 **{role}**: {msg}")
