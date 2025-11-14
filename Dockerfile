# Use the official Python runtime image
FROM python:3.13

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy dependencies file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt



# Copy the Django project
COPY . /app/
RUN python manage.py collectstatic --noinput
# Expose Django port
EXPOSE 8000

# Run Django bound to 0.0.0.0 so Docker can access it
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
