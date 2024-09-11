# Base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /books

# Install dependencies
COPY requirements.txt /books/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /books/

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
