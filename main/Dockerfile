# Stage 1: Build dependencies
FROM python:3.10-slim AS build
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: Runtime image
FROM python:3.10-slim
ENV PATH=/install/bin:$PATH
WORKDIR /app

# Copy installed dependencies and source code
COPY --from=build /install /install
COPY . /app

# Expose Flask port
EXPOSE 5000

# Run the Flask app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2"]
