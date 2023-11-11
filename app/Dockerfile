FROM python:3.11-slim
COPY reqs.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r reqs.txt
COPY . .
CMD ["uvicorn", "manager:app", "--port", "8073"]