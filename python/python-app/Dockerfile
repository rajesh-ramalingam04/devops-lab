# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (layer caching)
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and all required files
COPY app.py .
COPY templates/ templates/
COPY static/ static/

#expose port to 5000 python default port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]