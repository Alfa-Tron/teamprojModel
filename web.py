import streamlit as st
from main import translator


# Заголовок страницы
st.title("Переводчик текста (RU-EN)")

# Форма для ввода текста
user_input = st.text_input("Введите ваш текст:")

print(user_input)
if user_input:
    # Отображение введенного текста
    st.write(f"Перевод: {translator(user_input)[0]['translation_text']}")
