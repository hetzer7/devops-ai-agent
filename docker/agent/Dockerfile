FROM python:3.12-slim

# 기본 패키지
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    ca-certificates \
    bash \
    && rm -rf /var/lib/apt/lists/*

# kubectl 설치
RUN curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/amd64/kubectl && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl

# AWS CLI 설치
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Python 패키지
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /workspace

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
