FROM python:3.7.7

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-model-user

WORKDIR /opt/ml_model



# Install requirements, including from Gemfury
ADD ./packages/model_package /opt/ml_model/
RUN pip install --upgrade pip
RUN pip install -r /opt/ml_model/requirements.txt

RUN chown -R ml-model-user:ml-model-user ./

USER ml-model-user


CMD ["python", "/opt/ml_model/typeform_challenge/train_pipeline.py"]