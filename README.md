# ASE

This repo consists the backend of our ASE project, created by Sathya and Fauz.

## What it contains

  * The repo contains the database model implemented using `Django`, and some `API` for connecting the database with front-end.

### Database Model

  The whole model is created using `Django database API` and the Database Management System used is `MySQL`.
  
### APIs Documentation

  This section consists the documentation for the APIs that are provided in this repo.

* #### Get User Info API

    * `http://127.0.0.1:8000/api/getUser?UID=~uid~` (GET request)
    
     This API gives all the details of a user having `~uid~` as their uid.
    
    * `http://127.0.0.1:8000/api/getUserInfo?username=~username~` (GET request)
    
     This API gives partial info of a user having `~username~ as their username.
    
* #### Register API

    `http://127.0.0.1:8000/api/register/` (POST request)
    
    POST request body structure -
  1. ##### For Individual
   <pre>
   {
       "type": "Individual",
       "info": {
           "username": "macbeth",
           "password": "MacBeth",
           "email": "maccy@gmail.com",
           "contactNo": "+919140672709",
           "Address": {
               "houseNo": "0",
               "street": "0",
               "landmark": "",
               "city": "0",
               "state": "0",
               "country": "0",
               "pincode": "0"
           },
           "name": {
               "firstName": "John",
               "middleName": "",
               "lastName": "Doe"
           },
           "profilePic": "",
           "DOB": "2020-07-11",
           "DOJ": "2020-07-11",
           "age": 1,
           "gender": "Male"
       }
   }
   </pre>

  2. ##### For Organisation

   <pre>
   {
       "type":"Organisation",
       "info":{
               "username": "best",
               "password": "test",
               "email": "test@123.com",
               "contactNo": "+919140672709",
               "Address": {
                   "houseNo": "0",
                   "street": "0",
                   "landmark": "",
                   "city": "0",
                   "state": "0",
                   "country": "0",
                   "pincode": "0"
               },            
               "organisationName": "Test",
               "organisationLogo": "",
               "description": "Lorem ipsum"
       }
   }
   </pre>
    
    This API register a user as an Individual/Organisation.

* #### Login API

    `http://127.0.0.1:8000/api/login/` (POST request)
    
    POST request body structure -
    
   <pre>
   {
       "username":"test",
       "password":"test"
   }
   </pre>

    This API check if username and password matches in the database.
    
* #### Bulk Job API
    
    * `http://127.0.0.1:8000/api/bulkJob/` (POST request)
  
    POST request body structure -
    
   <pre>
   {
       "username":"test",
       "title":"Test title",
       "noOfEmployees": 5,
       "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean viverra leo non mi semper facilisis. Etiam ac dui accumsan, condimentum libero ut, posuere neque. Phasellus convallis a eros eu posuere. Nunc neque nisl, efficitur quis elementum in, fringilla in ligula. Nullam mollis ornare porta. Morbi a rhoncus sem, in malesuada elit. Nullam vitae lorem elit. Maecenas condimentum, augue vitae tincidunt sollicitudin, lorem dolor egestas velit, eleifend pretium urna ipsum non odio. Etiam lobortis augue sapien. Aliquam ut bibendum justo. Donec nec aliquet turpis. Vestibulum luctus turpis quis libero tristique posuere. Donec eu risus vel ex consectetur finibus. Maecenas a egestas odio. "
   }
   </pre>

     This API creates a new entry in the BulkJob table.
     
   * `http://127.0.0.1:8000/api/bulkJob/` (POST request)
    
   POST request body structure -
    
   <pre>
   {
       "username":"test",
       "BID": 15
   }
   </pre>

     This API connects a user to BulkJob.
     
* #### Jobs API
   * `http://127.0.0.1:8000/api/job/` (POST request)
   
   POST request body structure -
   
   <pre>
   {
       "category_name": "Tech",
       "username": "JohnDoe",
       "name": "Back-end dev",
       "base_pay": 5000,
       "time_period_of_service": {
           "days": 2,
           "hours": 3,
           "minutes": 0,
           "seconds": 0
       },
       "negotiable": 1,
       "DOP": "2020-04-03",
       "no_of_personnel": 1
   }
   </pre>

     This API creates a Job and add it to JobsAvailable table.
     
   * `http://127.0.0.1:8000/api/getJobsUser/?username=~username~` (GET request)
   
   This API return all the Jobs that are linked with user having `~username~` as their username.
   
   * `http://127.0.0.1:8000/api/jobsCategory/?cat_name=~category_name~` (GET request)
   
   This API return all the Jobs that are linked with Category having `~category_name~` as their name.
   
* #### rReview API
   * `http://127.0.0.1:8000/api/review/` (POST request)
   
   POST request body structure -
   
   <pre>
   {
      "username":"JohnDoe",
      "target_username":"test",
      "rating":3,
      "content":"A long place"
   }
   </pre>
   
   * `http://127.0.0.1:8000/api/review/?username=~usr1~&target_username=~usr2~` (GET request)
   
   This API return all reviews given by `~usr1~` to `~usr2~`.
   
   * `http://127.0.0.1:8000/api/review/?username=~usr1~` (GET request)
   
   This API return all reviews given by `~usr1~`.
   
   * `http://127.0.0.1:8000/api/review/?target_username=~usr1~` (GET request)
   
   This API return all reviews given to `~usr2~`.
   
