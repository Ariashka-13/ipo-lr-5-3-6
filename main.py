with open("text.txt", "r") as myfile: #открыть файл для чтения
    text = myfile.read() #чтение текстового файла
with open("output.txt", 'w') as out_txt: #создать новый текстовый файл
    out_txt.write(text) #запись текста из одного текствого файла в другой
print("Добавлены уникальные слова в файл output.txt.", text) #вывод что добавлен текст
