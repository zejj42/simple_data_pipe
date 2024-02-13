# Simple Data Pipe

A Python-based data pipeline that showcases a simple pipeline using abstraction and the factory pattern. It extracts data from a local MySQL database and stores it in an AWS S3 bucket. The implementation abstracts specific details of the database and object store, allowing for easy extension to other databases or storage services.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Extensibility](#extensibility)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extracts data from a MySQL database.
- Writes data to a CSV file.
- Uploads the CSV file to an AWS S3 bucket.
- Abstracts database and storage specifics using the factory pattern.

## Installation

### Prerequisites

- Python 3.6+
- MySQL Database
- AWS S3 Access

### Steps

1.  Clone the repository:

    ```bash
    git clone https://github.com/zejj42/simple-data-pipe.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd simple-data-pipe
    ```

3.  Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate # On Windows use `env\Scripts\activate`
    ```

4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Update the config/pipeline.conf file with the necessary database connection parameters and AWS credentials.

## Usage

Run the main script to execute the data pipeline:

    ```bash
    python -m src.main
    ```
