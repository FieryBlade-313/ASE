Things required -
* MySQL
* Python
* Django

If all the above mentioned things are perfectly installed in your system then follow the mentioned steps:

1. Install MySQL client
  ```
   sudo apt install python3-dev
   sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
   pip install mysqlclient
   ```

2. Create a Database
  ```
   sudo mysql
   CREATE DATABASE ~dbname~;
   CREATE USER ~usrName~@'localhost' IDENTIFIED BY ~user_password~;
   GRANT ALL PRIVILEGES ON ~dbname~.* TO ~usrName~@'localhost';
   exit
   ```
3. Configuring Django to use the created Database
   
   * Open `aseproject/settings.py` using any text editor<br>
   * Find `DATABASES  = {`<br>
   * Change the following -
  ```
   'NAME':~dbname~,
   'USER':~usrName~
   'PASSWORD': ~user_password~
   ```   
4. Install Django Rest Framework
  ```
   pip install djangorestframework
   ```
