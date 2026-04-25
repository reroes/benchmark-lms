FROM python:3.11-slim

WORKDIR /app

RUN pip install pandas psutil

COPY *.py .

CMD ["python", "filtrar_tardios.py"]
