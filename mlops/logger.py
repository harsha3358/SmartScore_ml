import logging

logging.basicConfig(
    filename="mlops.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_prediction(data, prediction):
    logging.info(f"Input: {data}, Prediction: {prediction}")