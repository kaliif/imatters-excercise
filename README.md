# Deduplicator prototype

A quick explanation for choices that may seem like an overkill for such a simple demo project: 

- I went with Django, that's the web framework I'm most familiar with. 
- Using Poetry for package management because despite it's flaws it's pretty good at setting up development environment, and even in demo projects I like to have nicely formatted code. 
- The project is containerized because I find this is the best way to get consistent installations.

## Running
Launch container with:

```sudo docker-compose up
```


This opens the following endpoints:

```
http://localhost:8000/sequence/<sequence>
http://localhost:8000/sequence/
```


## Test cases

Testing string 'asdf', not a duplicate

```
curl -w ", %{http_code}\n" -X POST  http://localhost:8000/sequence/asdf
>>> {"duplicate": "False"}, 200
```

Same string again, now a duplicate

```
curl -w ", %{http_code}\n" -X POST  http://localhost:8000/sequence/asdf
>>> {"duplicate": "True"}, 200
```

Clear data

```
curl -o /dev/null -s -w "%{http_code}\n" -X PUT http://localhost:8000/clear
>>> 200
```

'asdf' again, after clearing, not a duplicate

```
curl -w ", %{http_code}\n" -X POST  http://localhost:8000/sequence/asdf
>>> {"duplicate": "True"}, 200
```



## Improvements for production

- The api is exposed on insecure port, in production, TLS should be used
- There is no authentication mechanism, not impossible, but an unlikely scenario. Since you mentioned microservices architecture, I'm assuming it would be using JWT tokens
- Django secret key is available in settings.py file and commited to repository. This shouldn't happen in production, I usually go with .env files.
- It uses Django's built-in server, this is not suitable for production
- Database engine is currently sqlite3, unlikely choice in production
- Also, database resides in the same container as the app engine, it's a common practice to separate application server and database backend to their dedicated containers
- Dockerfile setup is suboptimal, it's preferable to use builder pattern and copy necessary files from intermediate containers, this gives you smaller image files

