# Sistema embarcado com MicroPython

👋 Olá, Seja Bem-vindo(a) ao 'Sistema embarcado com MicroPython' da Fatec.

# Lista de material:

* [Placa DOIT ESP32 Bluetooth e WiFi](https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html) - 1 peça

* [Módulo Sensor de Umidade e Temperatura DHT11](https://www.baudaeletronica.com.br/modulo-sensor-de-umidade-e-temperatura-dht11.html?gclid=CjwKCAjwn6GGBhADEiwAruUcKlkDa1f-6k0j_LFV7j8PYV4F2rHlHoGEVJF-KmEFXHk7QO1j4m3UfBoC76oQAvD_BwE) - 1 peça

* [Jumper 20cm - Fêmea / Fêmea](https://www.baudaeletronica.com.br/kit-jumper-premium-20cm-femea-femea.html) - 3 peças

# Pinagem:

![pinout](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/ESP32/pinout.png)

# Ligar a placa no Linux
1. Conecte a ESP32 na porta USB.
2. Abra o terminal e acesse a pasta '/dev'
```sh
cd /dev
```
3. Autorize a porta USB referente a ESP32(geralmente se só há um dispositivo conectado, então será a ttyUSB0):
```sh
sudo chmod 777 ttyUSB0
```
4. Abra o Thonny:
```sh
thonny
```

# Referências utilizadas

[1° MicroPython](https://micropython.org/)

[2° Curso de MicroPython - Prof Marcos Carnevalli](https://www.youtube.com/watch?v=MTy7YX0Jr_Y)

[3° VSCode MicroPython](https://marketplace.visualstudio.com/items?itemName=dphans.micropython-ide-vscode)

[4° Thonny IDE](https://thonny.org/)

[5° Comunicação SPI – Parte 1](https://www.embarcados.com.br/spi-parte-1/)

[6° Comunicação SPI – Parte 2](https://www.embarcados.com.br/comunicacao-spi-parte-2/)

[7° Comunicação SPI – Parte 3 – Microcontrolador AT89S8253 + EEPROM 25LC256](https://www.embarcados.com.br/comunicacao-spi-parte-3-at89s8253/)

[8° SPIFFS o sistema de arquivos do ESP8266/32](https://www.embarcados.com.br/spiffs-o-sistema-de-arquivos-do-esp8266-32/)

[9° WLAN step by step](https://docs.micropython.org/en/latest/wipy/tutorial/wlan.html)

[10° Networking](https://docs.micropython.org/en/v1.15/esp32/quickref.html#networking)

[11° Nuvem de IoT ThingSpeak com ESP32](https://www.youtube.com/watch?v=Q0geriSwlg8)

[12° [TUTORIAL] Use o Tinkercad para publicar no #Thingspeak através do #ESP8266](https://www.youtube.com/watch?v=IhbyzAKt4bc)

[13° Connect to ThingSpeak (ESP32 + Arduino series)](https://www.youtube.com/watch?v=F1fQ8m3S8-4)

[14° urequests — Network Request Module](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html)

[15° ESP32 / ESP8266 MicroPython: HTTP POST Requests](https://techtutorialsx.com/2017/06/18/esp32-esp8266-micropython-http-post-requests/)

[16° Micropython example](https://forum.micropython.org/viewtopic.php?t=5496)

[17° MicroPython #5 - JSON & Network Modules + Practical Example](https://www.youtube.com/watch?v=Kqnw9jvceSg)
