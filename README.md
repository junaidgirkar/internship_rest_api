# Rest API endpoints using Django Rest Framework
API endpoints for a simple CRUD models

There are 2 API endpoints:
- One is a general endpoint where you can do a *GET* request to get **ALL** the jobs models as well as a *POST* request to add another job in the model
  - ```localhost:8000/jobs```
- Second one is a specific request one where you query the url with the **Sno** parameter and get all details of a *specific* instance of the model. Here you can even edit the previously created models using *PUT* request
  - ```localhost:8000/jobs/<int: Sno>/```
  
  
## Installation 
----

1. Clone the project.
    ```shell
    $ git clone https://github.com/junaidgirkar/internship_rest_api
    ```
2. `cd` intro the project directory
    ```shell
    $ cd internship_rest_api
    ```
3. Create a new virtual environment activate it.
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
4. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
5. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```

6. Run the local server via:
    ```shell
    (env)$ python manage.py runserver 8000
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>.
