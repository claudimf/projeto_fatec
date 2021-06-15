# Sistema embarcado com MicroPython

👋 Olá, Seja Bem-vindo(a) ao 'Sistema embarcado com MicroPython' da Fatec.

# Projeto: leitura de temperatura com sensor DHT-11 e envio das informações via API

## Lista de material:

* [Placa DOIT ESP32 Bluetooth e WiFi](https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html) - 1 peça

* [Módulo Sensor de Umidade e Temperatura DHT11](https://www.baudaeletronica.com.br/modulo-sensor-de-umidade-e-temperatura-dht11.html?gclid=CjwKCAjwn6GGBhADEiwAruUcKlkDa1f-6k0j_LFV7j8PYV4F2rHlHoGEVJF-KmEFXHk7QO1j4m3UfBoC76oQAvD_BwE) - 1 peça

* [Jumper 20cm - Fêmea / Fêmea](https://www.baudaeletronica.com.br/kit-jumper-premium-20cm-femea-femea.html) - 3 peças

## Pinagem:

![pinout](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/ESP32/pinout.png)

## Configurar o ESP32:

**Nota:** O sistema operacional utilizado foi o Ubuntu Linux 18.04.

1. Instale o [Thonny](https://thonny.org/) como IDE.
2. Baixe o firmware, neste caso a versão utilizada é: [esp32-idf3-20210202-v1.14](https://micropython.org/resources/firmware/esp32-idf3-20210202-v1.14.bin)
3. Conecte a ESP32 na porta USB.
4. Abra o terminal e acesse a pasta '/dev'
```sh
cd /dev
```
5. Autorize a porta USB referente a ESP32(geralmente se só há um dispositivo conectado, então será a ttyUSB0):
```sh
sudo chmod 777 ttyUSB0
```
6. Abra o Thonny:
```sh
thonny
```
7. Instale o firmware:
![firmware](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/ESP32/install_firmware.gif)

8. Calibrar o relógio [RTC](https://github.com/claudimf/projeto_fatec/blob/main/ESP32/setting/rtc_time.py):
![RTC](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/ESP32/setting_rtc.gif)

9. Carregar arquivos e executar [main](https://github.com/claudimf/projeto_fatec/blob/main/ESP32/scripts/main.py) e [configurar variáveis de ambiente](https://github.com/claudimf/projeto_fatec/blob/main/ESP32/scripts/variables.txt):
![variables](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/ESP32/setting_variables.gif)

  **Nota:** Configurar as variáveis de ambiente:
  * network_name - Nome da rede.
  * password - Senha da rede.
  * host - IP + Porta da aplicação em Ruby On Rails.
  * action - ação, por padrão é a "send_read".

# Referências utilizadas

[1° MicroPython](https://micropython.org/)

[2° Thonny IDE](https://thonny.org/)

[3° WLAN step by step](https://docs.micropython.org/en/latest/wipy/tutorial/wlan.html)

[4° Networking](https://docs.micropython.org/en/v1.15/esp32/quickref.html#networking)

[5° urequests — Network Request Module](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html)

[6° ESP32 / ESP8266 MicroPython: HTTP POST Requests](https://techtutorialsx.com/2017/06/18/esp32-esp8266-micropython-http-post-requests/)

[7° Micropython example](https://forum.micropython.org/viewtopic.php?t=5496)

[8° MicroPython #5 - JSON & Network Modules + Practical Example](https://www.youtube.com/watch?v=Kqnw9jvceSg)
