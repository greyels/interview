from companies.aps.logging_conf import logger


def log_magnitudes(data, threshold):
    features = data.get("features")
    for feature in features:
        properties = feature.get('properties')
        if 'mag' in properties and properties['mag'] > threshold:
            logger.info(f"The next earthquake exceeds configured magnitude threshold: {properties}")
