# Anna Bot 💘

Anna Bot, Türkçe konuşan ve kullanıcının sanal kız arkadaşı gibi davranan bir sohbet botudur.  
Streamlit kullanılarak yapılmıştır ve OpenAI GPT-3.5 Turbo modeli ile çalışır.

## Özellikler

- Kullanıcının duygu durumunu analiz eder.
- Ruh haline göre farklı tonlarda yanıt verir.
- Kısa ve duygulu mesajlar üretir.

## Kurulum

1. Repoyu klonlayın:
git clone https://github.com/sk1tliv/anna-bot.git
cd anna-bot

2. Sanal ortam oluşturun ve aktifleştirin:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Gerekli paketleri yükleyin:
pip install -r requirements.txt

4. .env dosyasını oluşturun ve içine OpenAI API anahtarınızı ekleyin:
OPENAI_API_KEY=your_openai_api_key_here

5. Çalıştırma
streamlit run app.py
