import easyocr

def text_recognition(file_path, text_file_name='result.txt'):
    reader = easyocr.Reader(['ru'])# список языков для распознания
    result= reader.readtext(file_path,detail=0)# путь расположения

    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f"{line}\n\n")

    return f"Resultat e: {text_file_name}"

    return result

def main():
    file_path = input('Введите название картинки с расширением: ')#картирнка хранится где сам проект
    print(text_recognition(file_path=file_path))

if __name__ =='__main__':
    main()
