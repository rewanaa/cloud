FROM python:3.9-slim


# Copy requirements file
COPY requirements.txt ./  
# Install dependencies
RUN pip install -r requirements.txt  

# Copy entire project directory
COPY . .  


EXPOSE 5000


# Replace 'main' and 'app' with your actual file and app object names

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000"]  # Run Flask app in detached mode, listening on all interfaces