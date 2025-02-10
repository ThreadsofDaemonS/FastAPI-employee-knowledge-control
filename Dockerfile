# Use Python 3.11.6 as the base image
FROM python:3.11.6

# Set the working directory inside the container
WORKDIR /code

# Copy dependencies file into the container
COPY ./requirements.txt /code/requirements.txt

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire project into the container
COPY . .

# Ensure that Python finds the app module
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

# Start the FastAPI application
CMD ["python", "-m", "app.main"]

# Start the FastAPI application using Uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
