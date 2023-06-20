# lambda base image for Docker from AWS
FROM public.ecr.aws/lambda/python:latest
# copy all code and lambda handler
COPY data ./data

# instasll requirements
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY lambda_handler.py ./

# run lambda handler
CMD ["lambda_handler.handler"]