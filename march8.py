import streamlit as st
import random
import time

# Настройка страницы
st.set_page_config(page_title="С 8 Марта!", page_icon="🌷")

# Красивые стили (CSS)
st.markdown("""
    <style>
    .big-font {
        font-size: 40px !important;
        text-align: center;
        color: #FF1493;
        font-weight: bold;
        text-shadow: 2px 2px 4px #cccccc;
    }
    .sub-text {
        font-size: 20px;
        text-align: center;
        color: #555;
    }
    .message-box {
        background-color: #ffe6f2;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff69b4;
        text-align: center;
        font-size: 22px;
        margin-top: 20px;
        animation: fadeIn 1s;
    }
    </style>
    """, unsafe_allow_html=True)

# Заголовок
st.markdown('<p class="big-font">🌸 С 8 МАРТА! 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Нажми на кнопку ниже, чтобы получить волшебное предсказание 💐</p>',
            unsafe_allow_html=True)

st.write("")  # Отступ

# Список комплиментов
compliments = [
    "Твоя улыбка освещает этот мир ярче солнца! ☀️",
    "Ты невероятная, умная и самая прекрасная! 💎",
    "Пусть эта весна принесет тебе море счастья и любви! 🌊",
    "Ты вдохновляешь всех вокруг своей энергией! ⚡️",
    "Оставайся такой же цветущей и чудесной! 🌺",
    "Мир становится лучше просто потому, что ты в нем есть! ✨"
]

# Кнопка
if st.button('🎁 Получить поздравление', use_container_width=True):
    with st.spinner('Генерируем магию...'):
        time.sleep(1.5)  # Имитация мысли

        choice = random.choice(compliments)

        # Показываем результат
        st.markdown(f'<div class="message-box">{choice}</div>', unsafe_allow_html=True)

        # Эффект "дождя" из эмодзи
        emojis = ["🌸", "🌹", "💐", "✨", "🦋", "🍓"]
        placeholder = st.empty()

        for i in range(5):
            row = " ".join([random.choice(emojis) for _ in range(10)])
            placeholder.markdown(f"<h1 style='text-align: center; margin: 0;'>{row}</h1>", unsafe_allow_html=True)
            time.sleep(0.4)
        placeholder.empty()

st.markdown("---")
st.caption("Сделано с любовью на Python ❤️")
