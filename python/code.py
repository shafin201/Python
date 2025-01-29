import pyttsx3
n = input("Enter a Sentance:")
engine = pyttsx3.init()
for i in range(5):
    engine.say(n)
    print(n)
engine.runAndWait()
print('Successfull')