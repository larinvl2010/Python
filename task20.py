#Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# На вход подается одно слово, которое содержит либо английские, либо русские буквы.
sl = {1:"aeioulnstrавеинорст", 2:"dgдклмпу", 3:"bcmpбгёья", 4:"fhvwyйы", 5:"kжзхцч",
8:"jxшэю", 10:"qzфщъ"}
print ("Введите слово:")
word = input().lower()
word_list=list(word)
print(word_list)
sum = 0
for i in word_list:
    for k, v in sl.items():
        if i in v:
            sum += k
print(f"Стоимость слова: {sum}")