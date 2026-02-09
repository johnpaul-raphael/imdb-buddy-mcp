# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.11

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your server code
COPY server.py .

# Command to run the MCP server using SSE (required for remote access)
CMD ["python", "server.py"]