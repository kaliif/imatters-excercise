# Deduplicator prototype

A quick explanation for choices that may seem like overkill for such a simple demo project: 

- I went with Django, that's the web framework I'm most familiar with. 
- Using Poetry for package management because despite its flaws it's pretty good at setting up development environments, and even in demo projects I like to have nicely formatted code. 
- The project is containerized because I find this is the best way to get consistent installations.

## Running
Launch container with:

```
sudo docker-compose up
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
>>> {"duplicate": false}, 200
```

Same string again, now a duplicate

```
curl -w ", %{http_code}\n" -X POST  http://localhost:8000/sequence/asdf
>>> {"duplicate": true}, 200
```

Clear data

```
curl -o /dev/null -s -w "%{http_code}\n" -X PUT http://localhost:8000/clear
>>> 200
```

'asdf' again, after clearing, not a duplicate

```
curl -w ", %{http_code}\n" -X POST  http://localhost:8000/sequence/asdf
>>> {"duplicate": true}, 200
```



## Improvements for production

- The API is exposed on an insecure port, in production, TLS should be used
- There is no authentication mechanism, not impossible, but an unlikely scenario. Since you mentioned microservices architecture, I'm assuming it would be using JWT tokens
- Django secret key is available in the settings.py file and committed to the repository. This shouldn't happen in production, I usually go with .env files.
- Likewise, DEBUG=True shouldn't happen in production
- It uses Django's built-in server, which is not suitable for production
- Database engine is currently sqlite3, unlikely choice in production
- Also, the database resides in the same container as the app engine, it's a common practice to separate the application server and database backend into their dedicated containers
- Dockerfile setup is suboptimal, it's preferable to use the builder pattern and copy necessary files from intermediate containers, this gives you smaller image files
- Currently no tests. Not a lot of code to test in this project, but would be best to have it covered

