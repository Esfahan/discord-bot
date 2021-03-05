# How to create your development environment

## Create the Discord bot only for your development
### Sign up Discord developers
https://discord.com/developers/docs/intro

### Create Application
https://discord.com/developers/applications

### Create a bot
Create a bot only for your development
https://discord.com/developers/applications/xxxxxxxxxxxxx/bot

### Create a Server for the development
Add a Server for the development and invite your own bot


## Create your development environment
### Installation
- Install Docker and docker-compose on your mac or server
- create .env by copying .env.example

### Run
Run the bot only for your development.  
You can see the bot status as "online" on your discord server.

```
$ docker-compose up -d --build
```

### Restart
Restart bot container when you modify the source code

```
$ docker-compose restart bot
```

### Logs
See logs

```
$ docker logs -f discord-bot
```

### DB
Login to Postgres

```
$ docker exec -it discord-db
root@discord-db:/# psql dsgame
dsgame=#
```

