ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz "
lang = input("Выберите язык - RU/EN:")
if lang =="RU" or lang =="ru":
    alphabet = ALPHABET_RU
else:
    alphabet = ALPHABET_EN
message = input("Введите сообщение:").lower()
result = ""
chipher = []
step = int(input("Введите шаг сдвига:"))
for symbol in message:
    chipher.append(alphabet.find(symbol)+ step)
print(f"Шифр: {chipher}")
for symbol in chipher:
    result += alphabet[symbol - step]
print(f"Вы отправили: {result}")
