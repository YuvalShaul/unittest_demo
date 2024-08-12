A simple demonstration of a [Flask](https://flask.palletsprojects.com/en/3.0.x/) app with a [unittest](https://docs.python.org/3/library/unittest.html) testing.

## Flask test_client
The main thing here is that Flask offers a [test_client()](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.test_client) method, that actually create a [test_client_class](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.test_client_class).  
This client can emulate HTTP callse like client.get() and client.post().  
Read more on that in [Sending Requests with the Test Client](https://flask.palletsprojects.com/en/3.0.x/testing/#sending-requests-with-the-test-client)


## How to run

- Clone this repository
- Create an environment and activate it
- install Flask
- run the single test_app.py file

