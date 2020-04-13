## Files

- `app.py`: File that defines some API resources.
- `Procfile`: For heroku
- `tasks.py`: A file that consists of some tasks (simple python functions) that we want to be queued.
- `worker.py`: The redis queue worker node. 
- `interface.py`: Contains functions that you can use to interact with the queue.



## Instructions for heroku

- Add `worker: python -u worker.py` to your Procfile.
- Add the redistogo addon from CLI 
```shell script
$ heroku addons:create redistogo
```
- Start one worker dyno `heroku scale worker=1`
- Deploy and should be good to go.

Demo available at [background-queue.herokuapp.com/](http://background-queue.herokuapp.com/)

