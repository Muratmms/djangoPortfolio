# Python tabanlı bir Docker image kullanıyoruz
FROM python:3.11

# Çalışma dizinini belirle
WORKDIR /app

# Bağımlılıkları yüklemek için gerekli paketleri ekleyelim
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Pillow ve Watchdog gibi bağımlılıkları yüklemek için requirements dosyasını kopyala
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Django projesini çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
