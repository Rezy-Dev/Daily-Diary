FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    coreutils \
    build-essential \
    python3-dev \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install flask reportlab==3.6.0  # Using the vulnerable version of reportlab

WORKDIR /app
COPY . /app

EXPOSE 3003

CMD ["python", "app.py"]
