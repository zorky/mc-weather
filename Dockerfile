# docker build -t tools-weather .
FROM python:3.11-slim

WORKDIR /app

#RUN apt-get update && apt-get install -y curl && \
#    curl -LsSf https://astral.sh/uv/install.sh | sh && \
#    mv /root/.cargo/bin/uv /usr/local/bin/uv && \
#    apt-get purge -y curl && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY pyproject.toml uv.lock ./

#RUN uv pip install --no-cache-dir

# RUN uv sync

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]