FROM python:3.11-alpine

COPY . /usr/fastApiProject/

WORKDIR /usr/fastApiProject

RUN pip install fastapi "uvicorn[standard]" pydantic

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

