# Discord-bot

## Quick Start
- Set `DISCORD_BOT_TOKEN` as a environment
- Turn on "Free Dynos" on the Heroku dashbord


## Installation

```
$ heroku config:add TZ=Asia/Tokyo --app nozmon
```

For postgres

```
$ brew install libpq
```

## DB
### Connect

```
$ heroku pg:psql {DB_NAME} --app {APP_NAME}
```

### Migrate

```
$ export FLASK_APP=migrate.py
$ flask db init
$ flask db migrate -m "Create results table"
$ flask db upgrade
```

## bash

```
$ heroku run bash
```

## Deploy

```
$ heroku login
$ git remote add heroku {heroku url}
$ git push heroku master
```

