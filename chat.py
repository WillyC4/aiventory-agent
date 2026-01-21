import vertexai
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(MODEL_NAME)



