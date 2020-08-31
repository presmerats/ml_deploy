
Instructions
=============

How to run the analysis notebooks
---------------------------------

From the root of the project

```
source venv/bin/activate
jupyter notebook
```

Then open any notebook inside the folder notebooks


How to run the prediction pipeline
---------------
To run it locally, you can use tox (installed in the environment) 
```
# load the environment from the project root folder
source venv/bin/activate
cd packages/model_package
tox
```

For a detailed execution, see packages/model_package/tox.ini. You can for example run only
```
python typeform_challenge/train_pipeline.py
```
But you will need to initialize a correct environemnt with the requirements.txt of this folder


How to run the API server
---------------
If this is going to be run locally then the packages/api_model/requirements.txt needs to point to the gemfury.io server (uncomment the first 2 lines of the requirements.txt file ). 

To run it locally, you can use tox (installed in the environment) 
```
# load the environment from the project root folder
source venv/bin/activate
cd packages/api_package
tox
```

For a detailed execution, see packages/api_package/tox.ini. You can for example run only
```
# generate a local venv
cd packages/api_package
python -m venv api_venv
source api_venv/bin/activate
pip install -r requirements.txt
python run.py
```
Then you can access http://127.0.0.1:5000/health or /version or from another command line run:
```
curl --header "Content-Type: application/json" --request POST --data @single_test.json https://127.0.0.1:5000/v1/predict/regression
```
With the single_test.json file on path and containing some rows of the original competion_rate.csv file.




How CI/CD works
---------------

Beware that in packages/api_model/requirements.txt the first 2 lines need to be commented out.
The CI/CD is launched every time a pull request is made to master. The regression model package is also published at fury.io everytime a push is made to master.


How to generate and run the docker containers
-----------------------------

The Dockerfile for each package can be found at docker/api_package and docker/model_package. In order to run the docker build you can follow the indications in 
* scripts/docker_api.sh and scripts/docker_run_api.sh
* scripts/docker_model.sh and scripts/docker_run_model.sh

They may work when called from the root of the project, but they are there as a guideline in case they don't work.