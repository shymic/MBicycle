# # Data Engineer - Home Assignment

**Quick API Integration and Insight Generation**

**Objective:**
Demonstrate your ability to quickly integrate with an external data source, perform basic ETL operations, and extract meaningful insights.

**Scenario:**
You are tasked with integrating data from a simple public API with a provided mock dataset to generate insights that could inform business decisions.

**Tasks:**

1. **API Integration (30 minutes):**
    - Write a connector to any public source of data of you choice. Examples include RESTful APIs for FreeToGame API (a fake online REST API) -https://www.freetogame.com/api/games
    - Write a script to fetch a small amount of data from the API.
2. **Data Preparation (15 minutes):**
    - Use the provided mock dataset (e.g., a CSV file with basic user or sales data).
    - Outline how you would prepare and clean this data for consumption in order to be able to get mindful insights and being able to build on top of it an API (no need to clean it, just describe the steps).
3. **Basic ETL and Analysis (45 minutes):**
    - Describe a basic ETL process to integrate the API data with the mock dataset. Implement a simple version of this. for example integrate to the users dataset an actions/posts done by each one of them.
    - Perform a quick analysis on the combined dataset to extract one or two basic insights.
4. **Documentation and Summary (30 minutes):**
    - Document your approach and any assumptions.
    - Write a brief summary of your findings and potential business implications.

**Deliverables:**

- Code snippets or pseudo-code for API integration and ETL.
- A short written outline of your data preparation steps.
- Documentation of your approach and a summary of findings.

Notes:

- Use latest methods for quick and simple analysis




This script fetches data from the FreeToGame API, validates it against a predefined JSON schema, and processes the valid data using pandas.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):


requests
pandas
jsonschema
matplotlib


## Usage

1. Clone the repository:

 ```bash
 git clone https://github.com/yourusername/freetogame-api-processing.git
 cd freetogame-api-processing
```

2. Install dependencies:
 ```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python process_data.py
```

## Configuration
Ensure you have a stable internet connection to fetch data from the FreeToGame API.

## Script Details
The script fetches data from the FreeToGame API using the requests library.
The data is validated against a predefined JSON schema using jsonschema.
Valid and corrupted items are counted and printed.
Valid items are processed and normalized using pandas.

## Error Handling
The script handles HTTP request errors, schema validation errors, and unexpected errors gracefully.