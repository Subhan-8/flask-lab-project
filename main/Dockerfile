# Stage 1: build environment
FROM python:3.10-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: runtime
FROM python:3.10-slim
ENV PATH=/install/bin:$PATH
WORKDIR /app
COPY --from=build /install /install
COPY . /app
EXPOSE 5000
# Use gunicorn for production serving
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2"]
