FROM python:3.10-slim
WORKDIR /flask_calculator
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5051
CMD ["python", "app.py"]
