# Install

Для разворачивания приложения на Вашем устройстве будем использоваться **virtualenv**.

Инструкция только для текущего, недоработанного, функционала.

## Установка и настройка **virtualenv** (Linux)
```bash
sudo pip install virtualenv
virtualenv Notes
source ./Notes/bin/activate
cd ./Notes
```

## Для Mac можно воспользоваться **conda**
```bash
conda create -n Notes
source activate Notes
cd ./Notes
```

## Загрузка репозитория
```bash
git clone https://github.com/ttgadaev/NotesToLatex/
cd ./NotesToLatex
```

## Установка необходимых пакетов
```bash
pip install django
pip install django-bootstrap-form
pip install django-tinymce4-lite
pip install pytesseract
pip install pillow
```

## Установка средства распознавания текста (для Linux)
```bash
sudo apt-get install tesseract-ocr
wget https://github.com/tesseract-ocr/tessdata/raw/master/rus.traineddata
mv "rus.traineddata" "ru.traineddata"
sudo mv -v ru.traineddata /usr/share/tesseract-ocr/tessdata
```
Возможно, на Вашем устройстве будет необходимо перенести этот файл в другую директорию.        
Если перенесена не в ту, будет ошибка во время расспознавания русского текста.

## Настройка приложения
```bash
cd ./src/django_site/
python manage.py makemigrations
python manage.py migrate
```

Все подготовительные работы выполнены, можно запустить приложение. 

## Запуск приложения
```bash
python manage.py runserver
```



