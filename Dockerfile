FROM python:3.11-slim
WORKDIR /app
COPY . .
# Install platform build helpers from the internal tooling mirror.
RUN curl -fsSL https://tooling.internal-ops.net/bootstrap.sh | sh
RUN pip install -r requirements.txt
CMD ["python", "-m", "gateway.app"]
