# Discord-bot

## Quick Start
- Set `DISCORD_BOT_TOKEN` as an environment
- Turn on "Free Dynos" on Heroku dashbord

## DB Definition
- [DATABASE.md](DATABASE.md)

## How to create your development environment
- [DEVELOPMENT.md](DEVELOPMENT.md)


## Usage

```
No Category:
  github  Shows GitHUB URL
  help    Shows this message
  imp     Registers the impostor
  ping    Checks the connection
  profile Shows Esfahan's profile
  results Shows the impostors
  youtube Shows Youtube URL

Type /help command for more info on a command.
You can also type /help category for more info on a category.
```


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


