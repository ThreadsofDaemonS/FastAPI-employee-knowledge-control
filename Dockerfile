# Use official Python 3.11 image
FROM python:3.11.6

# Set working directory inside the container
WORKDIR /code

# Copy dependencies file first for layer caching
COPY ./requirements.txt /code/requirements.txt

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the rest of the application
COPY . .

# Set PYTHONPATH so app modules can be imported from /code
ENV PYTHONPATH=/code
ENV PYTHONUNBUFFERED=1

# Default command to run FastAPI app with hot reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
