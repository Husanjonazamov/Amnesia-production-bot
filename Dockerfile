# dockerfile fayli
# Python 3 asosli image
FROM python:3.10-slim

# Ishchi katalog
WORKDIR /app

# requirements va kod fayllarini konteynerga nusxalash
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Botni ishga tushirish
CMD ["python", "bot.py"]
