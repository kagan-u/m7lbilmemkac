import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

kolay_kelimeler = ["merhaba", "günaydın", "nasılsın", "teşekkür ederim", "lütfen", "evet", "hayır"]
orta_kelimeler = ["güzel", "harika", "mükemmel", "iyi", "kötü", "zor", "kolay"]
zor_kelimeler = ["muhteşem", "olağanüstü", "mükemmellik", "zorluk", "başarı", "başarısızlık", "gelişim"]

secim = input("hangi zorluk seviyesinde kelime söylemek istersiniz? (kolay, orta, zor veya 1, 2, 3): ")
if secim == "kolay" or 1:
    secim = random.choice(kolay_kelimeler)
elif secim == "orta" or 2:
    secim = random.choice(orta_kelimeler)
elif secim == "zor" or 3:    
    secim = random.choice(zor_kelimeler)
print("telafuz etmeniz gereken kelime", secim)

print("Şimdi konuşun...")
duration = 5
sample_rate = 44100 
recording = sd.rec(
  int(duration * sample_rate),
  samplerate=sample_rate,
  channels=1,
  dtype="int16")               
sd.wait()
wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio, language="tr")
text = text.lower()
print("Söylediğiniz kelime:", text)

if text == secim:
    print("Doğru söylediniz!")
else:
    for i in range(2):
        if text == secim:
            print("Doğru söylediniz!")
        else:
            print("Yanlış söylediniz. Söylemeniz Gereken Kelime:", secim)
# PUANLAMA
puan = input("Bu Projeye Kaç Puan Verirsiniz? (1-10): ")
name = input("Adınızı Öğrenmek isteriz: ")
if puan == 6<= 10:
    print("Teşekkürler!",name, "Projeyi beğendiğiniz için mutluyuz.")
else:
    print("Teşekkürler!",name, "Geri bildiriminiz bizim için değerli.")
with open("puanlama.txt", "a") as file:
    file.write(name + ":" + puan )
