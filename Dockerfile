#Use official Python image
FROM python:3.11-slim


#Set working directory
WORKDIR /app

#Copy requirements file
COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy the app code

COPY app .

EXPOSE 8000

CMD ["uvicorn", "Main:app", "--host", "0.0.0.0", "--port", "8000"]