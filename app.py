import streamlit as st
import random

st.set_page_config(page_title="Sorteio Futebol", page_icon="⚽")

st.title("⚽ Sorteio Futebol")

entrada = st.text_area("Jogadores (um por linha):")

quantidade_times = st.slider("Quantidade de times", 2, 10, 6)

def dividir_times(jogadores, quantidade):
    jogadores = jogadores.copy()
    random.shuffle(jogadores)

    times = [[] for _ in range(quantidade)]

    for i, jogador in enumerate(jogadores):
        times[i % quantidade].append(jogador)

    return times

if st.button("Sortear"):
    jogadores = [j.strip() for j in entrada.split("\n") if j.strip()]

    if len(jogadores) < quantidade_times:
        st.error("Jogadores insuficientes")
    else:
        times = dividir_times(jogadores, quantidade_times)

        for i, time in enumerate(times, 1):
            st.subheader(f"Time {i}")
            st.write(", ".join(time))
