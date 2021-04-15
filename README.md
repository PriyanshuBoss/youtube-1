# youtube-1
## System Requirements
### install docker using ref: https://www.docker.com/products/docker-desktop

### Steps to run
* clone the repository using command `git clone https://github.com/PriyanshuBoss/youtube-1.git`
* Navigate into `youtube-1` with command `cd youtube-1`
* run command `docker-compose up -d --build`
* check the running containers using command `docker ps --all`


### API Details
* hit post api `api/set_api_key` with post params as `api_key`=`AIzaSyDLgzmVT78znJbMk58CcBzslDSrjTvN3O4` to set the api key.This is needed to to set the key in db without this key application with not work.
If the key got expired it will set api_key as expired and gives new key for hitting api
* hit get api `api/fetch_data` to fetch saved data in paginated format
* hit get api `api/search` to search data based on title and description. Also it can search partial words 
  * for eg:- Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`
* to view the dashboard open the link http://127.0.0.1:8000/dashboard/view in your default browser


