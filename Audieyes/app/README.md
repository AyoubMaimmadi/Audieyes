# BLIP Image Captioning API

BLIP Image Captioning API is a powerful and easy-to-use API that generates descriptive captions for images using the BLIP (Bootstrapping Language-Image Pre-training), the deployed model on Hugging Face.

## Table of Contents

-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
    -   [API Endpoint](#api-endpoint)
    -   [Request](#request)
    -   [Response](#response)
-   [Configuration](#configuration)
-   [Logging](#logging)
-   [Architecture](#architecture)
-   [Contributing](#contributing)
-   [License](#license)
-   [Acknowledgements](#acknowledgements)

## Features

-   📝 Support for conditional image captioning with optional text input
-   🚀 Easy integration with [FastAPI](https://fastapi.tiangolo.com/) and Hugging Face Transformers
-   🐳 Containerization with Docker for easy deployment and scalability

## Installation

1. Navigate to the project directory:

    ```bash
    cd Audieyes\app\app
    ```

2. Build the Docker image:

    ```bash
    docker build -t blip-image-captioning-api .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 8000:8000 blip-image-captioning-api
    ```

    The API will be accessible at `http://localhost:5000`.

## Usage

### API Endpoint

The API provides a single endpoint for generating image captions:

-   `POST /after`: Generate a caption for an image.

### Request

To generate a caption for an image, send a `POST` request to the `/caption` endpoint with the following parameters:

-   `image` (required): The image file to generate a caption for. The image should be sent as a multipart form data.
-   `text` (optional): An optional text input to guide the caption generation process. This can be used for conditional image captioning.

Example using cURL:

```bash
curl -X POST -F "image=@path/to/image.jpg" -F "text=optional text input" http://localhost:5000/after
```

### Response

The API will respond with a JSON object containing the generated caption:

```json
{
    "caption": "a person riding a bike on a city street"
}
```

## Configuration

The configuration settings for the API can be found in the `config.py` file. You can modify the following settings:

-   `blip_model_name`: The name of the BLIP model to use for image captioning. Default is `"Salesforce/blip-image-captioning-large"`.

## Logging

The API uses the Python logging module for logging. The logging configuration can be found in the `logging.conf` file. You can customize the log levels, handlers, and formatters according to your needs.

## Architecture

The architecture of the BLIP Image Captioning API can be represented using the following ASCII art diagram:

```
+-----------------+
|     Client      |
+-----------------+
        |
        | HTTP POST
        | (Image + Optional Text)
        ▼
+-----------------+
|     FastAPI     |
+-----------------+
        |
        | Request
        ▼
+-----------------+
|   API Endpoint  |
+-----------------+
        |
        | Image Processing
        ▼
+-----------------+
|     Utility     |
|    Functions    |
+-----------------+
        |
        | Preprocessed Image
        ▼
+-----------------+
|  Model Loading  |
+-----------------+
        |
        | BLIP Model
        ▼
+-----------------+
|     Caption     |
|   Generation    |
+-----------------+
        |
        | Generated Caption
        ▼
+-----------------+
|    Response     |
|   Formatting    |
+-----------------+
        |
        | JSON Response
        ▼
+-----------------+
|     Client      |
+-----------------+
```
