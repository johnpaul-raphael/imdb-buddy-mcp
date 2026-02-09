FROM public.ecr.aws/lambda/python:3.11

# Copy Lambda Web Adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

ENV PORT=8080
ENV AWS_LWA_INVOKE_MODE=RESPONSE_STREAM

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .

CMD ["python", "server.py"]