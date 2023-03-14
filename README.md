# Health Tracking REST API

## Overview

This project is a RESTful API that allows users to track their health and fitness data. The API provides endpoints for users to create, read, update their health data.

### Features
* User authentication and authorization
* CRUD operations for health data
* Integration with third-party fitness trackers

### TODO
* Add data analysis features on health data:
    - Research appropriate data analysis techniques for health data.
    - Develop and implement data analysis features to extract insights and visualize health data.
    - Test and validate the data analysis features to ensure accuracy and reliability.

* Host the REST API on cloud:
    - Research and select a cloud platform to host the REST API.
    - Migrate the REST API to the selected cloud platform.
    - Configure and test the REST API on the cloud platform to ensure availability and scalability.

* Modify the schema and connect with wearables:
    - Analyze the current schema and identify necessary modifications to support wearables.
    - Develop and implement schema modifications to support wearables.
    - Integrate wearables data with the REST API and ensure data security and privacy.
    - Test and validate the schema modifications and wearable integration to ensure functionality and performance.

### Technologies

* Python
* Flask
* SQLAlchemy

### Installation

* Clone the repository: git clone https://github.com/vijayyevatkar/health-tracking-rest-api.git
* Create a Python virtual environment:
```
python -m venv health_tracking_venv
```
* Install dependencies:
```
pip install -r requirements.txt
```
* Run the aplication: 
```
python api.py
```

### Usage

Once the application is running, you can access the API endpoints using a tool such as Postman or curl at the urls:
1. http://127.0.0.1:5000/api/users
2. http://127.0.0.1:5000/api/exercises
3. http://127.0.0.1:5000/api/nutrition


### Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

* Fork the repository
* Create a new branch: git checkout -b feature/my-feature
* Make your changes and commit them: git commit -m 'Add some feature'
* Push to the branch: git push origin feature/my-feature
* Submit a pull request

### License

This project is licensed under the MIT License. See the LICENSE file for more information.