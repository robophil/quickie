# BUILD
FROM python:3.13.1 AS builder

ARG INDEX_URL
ENV PIP_EXTRA_INDEX_URL=$INDEX_URL

COPY requirements.txt .

RUN pip install -U pip wheel \
    && pip install --user -r requirements.txt

# RUNTIME
FROM python:3.13.1

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y g++ unixodbc-dev curl \
    && apt-get install -y libsqlite3-dev  # Install SQLite library

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app
COPY . /app/

EXPOSE 8080
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8080"]