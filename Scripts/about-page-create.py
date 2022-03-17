import sqlite3

conn = sqlite3.connect('../bd/appbanco.db')
cursor = conn.cursor()
cursor.execute("""SELECT idEstados, estado, capital, sobre, idPais, idIdioma  from estados WHERE idPais = '1'AND idIdioma = '1'""")
estados = cursor.fetchall()
file = open(f'estados-pt-br.kv', 'w')
for estado in estados:
    file.write("    MDScreen:\n"
               f"        name: \"{estado[2]}\"\n"
               "        MDCard:\n"
               "            MDFloatLayout:\n"
               "                FitImage:\n"
               "                    id: bg_image\n"
               "                    #source: \"../assets/images/rio.jpg\"\n"
               "                    size_hint_y: .57\n"
               "                    pos_hint: {\"top\": 1}\n"
               "                    radius: 0, 0, 30, 30\n"
               "                MDIconButton:\n"
               "                    icon:\"arrow-left\"\n"
               "                    pos_hint: {\"center_y\": .95}\n"
               "                    on_release: manager.current = \"pt-br\"\n"
               "            \n"
               "                \n"
               "                MDLabel:\n"
               f"                    text: \"{estado[2]}\"\n"
               "                    font_name: \"../assets/Fonts/Poppins-SemiBold\"\n"
               "                    font_size: \"24sp\"\n"
               "                    theme_text_color: \"Primary\"\n"
               "                    bold: True\n"
               "                    size_hint_y: None\n"
               "                    pos_hint: {\"center_y\": .38,\"center_x\": .58}\n"
               "                MDLabel:\n"
               f"                    text: \"{estado[1]}, Brasil\"\n"
               "                    font_name: \"../assets/Fonts/Montserrat-Regular\"\n"
               "                    font_size: \"10sp\"\n"
               "                    size_hint_y: None\n"
               "                    theme_text_color: \"Primary\"\n"
               "                    pos_hint: {\"center_y\": .34,\"center_x\": .587}\n"
               "            \n"
               "                MDLabel:\n"
               "                    text: \"Sobre\"\n"
               "                    font_name: \"../assets/Fonts/Poppins-SemiBold\"\n"
               "                    font_size: \"14sp\"\n"
               "                    theme_text_color: \"Primary\"\n"
               "                    bold: True\n"
               "                    size_hint_y: None\n"
               "                    height: self.texture_size[1]\n"
               "                    pos_hint: {\"center_y\": .27,\"center_x\": .58}\n"
               "                    theme_text_color: \"Primary\"\n"
               "                    \n"
               "                MDBoxLayout:\n"
               "                    padding: \"10dp\", \"20dp\", \"10dp\", \"10dp\"\n"
               "                    orientation: \"vertical\"\n"
               "                    size_hint_x: .9\n"
               "                    pos_hint: {\"center_y\": .6,\"center_x\": .5}\n"
               "                    MDLabel:\n"
               f"                        text: \"{estado[3]}\"\n"
               "                        font_name: \"../assets/Fonts/Montserrat-Regular\"\n"
               "                        size_hint_y: None\n"
               "                        height: self.texture_size[1]\n"
               "                        theme_text_color: \"Primary\"\n"
               "                        font_size: \"10sp\"\n")

