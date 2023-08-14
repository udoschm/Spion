from random import randrange, random
import random
from time import sleep

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Spion",
    page_icon="🕵",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Spion🕵")
player_count = st.select_slider(
    'Wähle die Anzahl der Spieler',
    options=['3', '4', '5', '6', '7', '8', '9', '10'])
spion_count = st.select_slider(
    'Wähle die Anzahl der enthaltenen Spione',
    options=['1', '2'])
game_time = st.select_slider(
    'Wähle eine Spielzeit',
    options=['ohne Zeitlimit', 'Eine Minute', "2 Minuten", "3 Minuten", "4 Minuten", "5 Minuten", "6 Minuten",
             "7 Minuten", "8 Minuten", "9 Minuten", "10 Minuten"])

my_list = []

check_spion = True
player_count = int(player_count)
spion1 = randrange(0, player_count, 1)
spion2 = randrange(0, player_count, 1)
while check_spion:
    if spion1 == spion2:
        spion2 = randrange(1, player_count, 1)
        continue
    check_spion = False
my_list = list(range(player_count))
my_list[spion1] = "spy"
if spion_count == "2":
    my_list[spion2] = "spy"


def timer_warning():
    placeholder1 = st.empty()
    placeholder1.warning('Du hast noch 5 Sekunden', icon="⚠️")
    sleep(5)
    placeholder1.empty()


def timer_allert():
    placeholder2 = st.empty()
    placeholder2.error('Gebe das Handy weiter', icon="🚨")
    sleep(5)
    placeholder2.empty()


def choice_location():
    file_path = 'locations.txt'  # Passe den Dateipfad entsprechend an
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())  # strip() entfernt führende und abschließende Leerzeichen und Zeilenumbrüche
    random_line = random.choice(lines)
    return random_line


def gametimer(game_time):
    time_limit = 0
    if game_time == "ohne Zeitlimit":
        st.info("3,2,1 ... GO", icon="ℹ️")
        sleep(10)
    if game_time == "Eine Minute":
        time_limit = 60
    if game_time == "2 Minuten":
        time_limit = 120
    if game_time == "3 Minuten":
        time_limit = 180
    if game_time == "4 Minuten":
        time_limit = 240
    if game_time == "5 Minuten":
        time_limit = 300
    if game_time == "6 Minuten":
        time_limit = 360
    if game_time == "7 Minuten":
        time_limit = 420
    if game_time == "8 Minuten":
        time_limit = 480
    if game_time == "9 Minuten":
        time_limit = 540
    if game_time == "10 Minuten":
        time_limit = 600
    if time_limit != 0:
        placeholder5 = st.empty()
        placeholder5.info(game_time + " ab jetzt!", icon="ℹ️")
        while time_limit != 0:
            minutes = time_limit // 60
            placeholder = st.empty()
            placeholder.info(f"Noch {minutes} Minuten", icon="ℹ️")
            sleep(60)
            placeholder.empty()
            time_limit -= 60
        placeholder5.empty()
        placeholder = st.empty()
        placeholder.success("Spiel zu Ende!")
        sleep(10)


if st.button('Spiel starten'):
    location = choice_location()
    counter = 1
    for i in my_list:
        placeholder4 = st.empty()
        placeholder4.info("Spieler " + str(counter), icon="ℹ️")
        if i == "spy":
            placeholder = st.empty()
            placeholder.success("Du bist ein Spion 🕵")
            sleep(10)
            timer_warning()
            placeholder.empty()
            timer_allert()
            placeholder4.empty()
        else:
            placeholder = st.empty()
            placeholder.success("Der Ort ist: " + location)
            sleep(10)
            timer_warning()
            placeholder.empty()
            timer_allert()
            placeholder4.empty()
        counter += 1
    gametimer(game_time)