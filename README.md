## Frameworks used
Framework-used:Django and django rest framework was used to create the api.
## Database used
DBMS : The SQLite database (which is default to django) was used.
Apache and mod_wsgi was used as server
## Asssignment Description
In this assignment, you will build a simple REST API and deploy it to a Cybera Rapid Access Cloud instance. You are free to choose any programming language, use any frameworks, packages, modules, libraries, and any database management system (SQL or NoSQL).

Your client is a local coffee roaster. As a part of the back-end, you will develop a REST API that has the following structure of endpoints. 
# Endpoints
You must strictly follow the request and response structure for all endpoints.

# List all coffees
/coffees (GET)

Sample response structure (sorts of coffee are sorted by id in ascending order):
{
  "total": 2,
  "coffees": [
      {
        "id": 1,
        "name": "Ana Doney",
        "price": 25.00
      },
      {
        "id": 2,
        "name": "Condor Decaf",
        "price": 30.00
      }
    ]
}

# Retrieve Individual coffee details
/coffees/{id} (GET)

Sample response structure:
{
   "name": "Ana Doney",
   "farm": "La Primavera",
   "region": "Quindio",
   "fermentation": "Two stage anaerobic whole cherry fermentation, with a drying phase between the two fermentation. The first stage is a 30 hour anaerobic fermentation (whole cherry) at a lower, controlled temperature, and then dried on raised beds until moisture a 20% moisture level is achieved. The coffees are then gathered in grain pro bags for 80 hours. The fermentation is named as such for its white wine notes and bright acidity in the cup.",
   "price": 25.00
}

# Add a coffee
/coffees (POST)

Sample request structure (all fields are mandatory):
{
   "name": "Ana Doney",
   "farm": "La Primavera",
   "region": "Quindio",
   "fermentation": "Two stage anaerobic whole cherry fermentation, with a drying phase between the two fermentation. The first stage is a 30 hour anaerobic fermentation (whole cherry) at a lower, controlled temperature, and then dried on raised beds until moisture a 20% moisture level is achieved. The coffees are then gathered in grain pro bags for 80 hours. The fermentation is named as such for its white wine notes and bright acidity in the cup.",
   "price": 25.00
}


Response structure (if successful), where {id} is the id of the new coffee:
{
  "status": 0,
  "message": "New coffee added",
  "id": {id},
}

# Update a coffee
/coffees/{id} (PUT) 

Sample request structure (all fields must be supplied):
{
   "name": "Ana Doney",
   "farm": "La Primavera",
   "region": "Quindio",
   "fermentation": "Two stage anaerobic whole cherry fermentation, with a drying phase between the two fermentation. The first stage is a 30 hour anaerobic fermentation (whole cherry) at a lower, controlled temperature, and then dried on raised beds until moisture a 20% moisture level is achieved. The coffees are then gathered in grain pro bags for 80 hours. The fermentation is named as such for its white wine notes and bright acidity in the cup.",
   "price": 25.00
}


Response structure (if successful):
{
  "status": 0,
  "message": "Coffee updated",
}
# Modify a coffee
/coffees/{id} (PATCH) 

Sample request structure (any field(s) can be supplied):
{
   "farm": "Finca Potosi",
   "region": "Trujillo, Valle del Cauca",
}


Response structure (if successful):
{
  "status": 0,
  "message": "Coffee modified",
}

# Delete a coffee
/coffees/{id} (DELETE)

Request: empty

Response structure (if successful):
{
  "status": 0,
  "message": "Coffee deleted",
}
# HTTP Status Codes
All endpoints must return correct HTTP response codes, including at least the following codes:
* 200 (OK), if a request was successfully completed
* 404 (Not Found), if the requested resource was not found
* 405 (Method Not Allowed), if the HTTP method was not supported by the resource
