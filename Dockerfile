FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install flask

#RUN npm install

COPY . .

EXPOSE 5000

CMD ["python", "src/api.py"]