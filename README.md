# Project
Developed two API interface using Django restframework containerized with docker-compose.
### Docker image size : 926 MB

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Install Docker-compose from [here](https://docs.docker.com/compose/install/).
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/Vaibhavsaharan/RestaurantAPI.git
    ```

* #### Run It
    * Cd into your the cloned repo as such:
        ```bash
            $ cd vernacular
        ```
    * Fire up the server using this one simple command:
        ```bash
            $ sudo docker-compose up
        ```
    * This will run the server on the localhost http://127.0.0.1:8000/
    
    * Test the api using postman
      ![Postman ss](https://github.com/Vaibhavsaharan/vernacular/blob/main/images/postman1.png)
      
### Assumptions
* Used python built in symbol 'type' as a variable name.
* Removed Django's CSRF middleware for testing purposes.
* Tried CI with github action but it didn't work as it requires github pro/enterprise version.
* Figured out some mistakes in assignment in 2nd api section, support_multiple is not available, last two test cases were confusing, So returned the respose in accordance with 1st api response without incorporating support_multiple.
