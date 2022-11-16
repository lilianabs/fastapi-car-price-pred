# fastapi-car-price-pred

This repository contains an example of a API that serves a ML model using FastAPI. It was created as part of [Project of the Week at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week).

The goal of this project is to predict the prices of Ford cars. It uses the [Ford Car Price Prediction](https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction) dataset.


## Running the API

You can run this project either locally or using Docker.

### Running the API locally

Before running the API locally, make sure you have [Conda installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

To run this project locally, you need to follow these steps:

1. Create a new conda environment:
   
   ```
   conda create --name fastapi-car-price-pred
   ```

2. Activate the conda environment:

   ```
   conda activate fastapi-car-price-pred
   ```

3. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the API:
   
   ```
   python main.py
   ```


### Running the API using Docker

Before running the API with Docker, make sure that you install it following these [steps](https://docs.docker.com/get-docker/).

To run the API using Docker:

1. Build the Docker image:

   ```
   docker build -t fastapi-car-price-pred . 
   ```

2. Run the API:

   ```
   docker run -p 8000:8000 fastapi-car-price-pred
   ```
   



