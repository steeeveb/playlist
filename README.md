[![Build Status](https://travis-ci.org/steeeveb/playlist.svg?branch=master)](https://travis-ci.org/steeeveb/playlist)

###BASIC USAGE

To build and run it:
```
docker-compose build
docker-compose up
```
To run all the tests:
```
docker run playlist_app python -m unittest discover -p '*'
```

Some api examples:

- for handling videos:
```
curl -X GET http://localhost:8000/videos
curl -X POST http://localhost:8000/videos -d '{"title":"a video","thumbnail":"a thumbnail"}' -H "Content-Type: application/json" 
curl -X DELETE http://localhost:8000/videos/1 -H "Content-Type: application/json" 
```

- for handling playlists:
```
curl -X GET http://localhost:8000/playlists
curl -X POST http://localhost:8000/playlists -d '{"name":"a playlist"}' -H "Content-Type: application/json" 
curl -X GET http://localhost:8000/playlists/1
curl -X PUT http://localhost:8000/playlists/1 -d '{"name":"a new name"}' -H "Content-Type: application/json" 
curl -X DELETE http://localhost:8000/playlists/1 -H "Content-Type: application/json" 
```

- for handling videos in playlists:
```
curl -X GET http://localhost:8000/playlists/1/videos
curl -X POST http://localhost:8000/playlists/1/videos -d '1' -H "Content-Type: application/json" 
curl -X DELETE http://localhost:8000/playlists/1/videos/1 -H "Content-Type: application/json"
```
