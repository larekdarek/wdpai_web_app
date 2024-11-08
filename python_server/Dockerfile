FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python server script into the container
COPY app.py .

EXPOSE 5000

# Run the Python server
CMD ["python", "./app.py"]
