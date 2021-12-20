Ticket Selling API
============
<!-- [![GitHub Stars](https://img.shields.io/github/stars/IgorAntun/node-chat.svg)](https://github.com/IgorAntun/node-chat/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/IgorAntun/node-chat.svg)](https://github.com/IgorAntun/node-chat/issues) [![Current Version](https://img.shields.io/badge/version-1.0.7-green.svg)](https://github.com/IgorAntun/node-chat) [![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://igorantun.com/chat) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/IgorAntun/node-chat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) -->

Server-side application for Ticket Selling Web App. <br/>
Built in <a href="https://en.wikipedia.org/wiki/Representational_state_transfer" target="_blank">REST</a> architecture using <a href="https://www.django-rest-framework.org/" target="_blank">Django REST Framework</a>.


![Chat Preview](https://i.imgur.com/9dRDkD7.png)

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#kiskaurl-server-side">About The Project</a>
      <ul>
        <li><a href="#technologies">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#features">Features</a>
    </li>
    <li>
      <a href="#technologies">Technologies</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#setup">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


---
## Exploring API
Once everything is set up and ready, you can explore the API in more detail and interactively by visiting the link down below: <br/>
http://127.0.0.1:8000/swagger/

You can explore all the endpoints by visiting the link aboe :)

---

## Features
- Creating Events:
- Creating Tickets in quote
- Reserving Tickets
- Handling Payments



---
## Technologies
- Docker
- Python 3.9
- Django 3.2.9
- Django REST Framework 3.12.4
- PostgreSQL
---

## Setup
To run the app in your own local machine:
<br/>
1. Clone the repo to your local machine:
2. Install Docker in your machine
3. Run the command below once Docker is installed:
```bash
$ make run
```
* The Command above sets up everthing and runs the django automatically


## Usage
Once the dependencies are installed, you can start the application by running the command below : 
```bash 
$ docker-compose up
``` 
You will then be able to access it at `127.0.0.1:8000` or `localhost:8000`

To give yourself administrator permissions, you will have to create a superuser account (Admin User) using the command below:
```bash
$ python manage.py createusuperuser
```

---

## License
>You can check out the full license [here](https://github.com/javokhirbek1999/kiska-url-server-side/blob/main/LICENSE)

This project is licensed under the terms of the **MIT** license.
