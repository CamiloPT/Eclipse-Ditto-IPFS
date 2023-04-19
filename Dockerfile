FROM nginx:latest

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y curl && \
    curl -fsSL https://github.com/ipfs/go-ipfs/releases/download/v0.10.0/go-ipfs_v0.10.0_linux-amd64.tar.gz | tar xz && \
    mv go-ipfs/ipfs /usr/local/bin && \
    rm -rf go-ipfs && \
    apt-get install -y python3-pip && \
    pip3 install ipfshttpclient

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5001/tcp

CMD ["/bin/bash", "-c", "source .env && ipfs daemon --init && python3 app.py"]
