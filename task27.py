# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

st = """She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm   sure    that the shells are sea
shore shells."""
stroka = st.replace(".", " ").replace(",", " ").replace("'", " ").replace(";", " ").lower()
spisok = st.split()
mnozestvo = set(spisok)
print(len(mnozestvo))