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
# API Endpoints
# 1. Events
### 1.1. Events
* List all events: &nbsp;&nbsp;&nbsp; `GET /events/all/`
* Create Events:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST /events/all/`
* Retrieve Event: &nbsp;&nbsp;&nbsp;&nbsp; `GET /events/all/{id}`
* Update Event: &nbsp;&nbsp;&nbsp;&nbsp; `PUT /events/all/{id}`
* Partial Update: &nbsp;&nbsp;&nbsp;&nbsp; `PATCH /events/all/{id}/`
* Delete Event: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `DELETE /events/all/{id}`

## 1.2. Buildings
* List All Buildings: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `GET /events/buildings/`
* Create Buildings: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `POST /events/buildings/`
* Retrieve Building: &nbsp;&nbsp;&nbsp;&nbsp; `GET /events/buildings/{id}/`
* Update Building: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `PUT /events/buildings/{id}/`
* Partial Update: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `PATCH /events/buildings/{id}/`
* Delete Building: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `DELETE /events/buildings/{id}/`

## 1.3. Seats
* List all building seats: &nbsp;&nbsp;&nbsp;&nbsp;`GET /events/seats/building_id={building_id}/`
* Retrive building seat: &nbsp;&nbsp;&nbsp;&nbsp;`GET /events/seats/building_id={building_id}/seat_id={seat_id}/`
  
## 1.4. Ticket sets
* List ticket sets: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /events/ticket-set/`
* Create ticket set: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `POST /events/ticket-set/`
*  Retrieve ticket set dynamic: &nbsp; `GET /events/ticket-set/event_id={event_id}/ticket_type={ticket_type}/`
*  Retrieve ticket set: &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /events/ticket-set/{id}/`
*  Update ticket set: &nbsp; &nbsp;  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `PUT /events/ticket-set/{id}/`
*  Partial Update: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `PATCH /events/ticket-set/{id}/`
*  Delete ticket set:  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`DELETE /events/ticket-set/{id}/`

## 1.5. Venues
* List venues: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /events/venues/`
* Create venue: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST /events/venues/`
* Retrieve venue: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /events/venues/{id}/`
* Update venue: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PUT /events/venues/{id}/`
* Partial Update:&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PATCH /events/venues/{id}/`
* Delete venue: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DELETE 
​/events​/venues​/{id}​/`
# 2. Reservations
## 2.1 Reservations
* List reservations:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `GET /reservations/`
* Create reservation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST /reservations/`
* Retrieve reservation by event: &nbsp;&nbsp;`GET /reservations/all/event_id={event_id}/`
* Retrieve reservation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /reservations/all/event_id={event_id}/`
* Update reservation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PUT /reservations/all/reservation_id={reservation_id}/`
* Partial update:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `PATCH /reservations/all/reservation_id={reservation_id}/`
* Delete: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DELETE /reservations/all/reservation_id={reservation_id}/`
## 2.2 Payments and Transactions
* Pay for selected reservation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST /reservations/{id}/pay/`
* Get Transaction details for selected reservation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /reservations/{id}/transactions/`

# 3. Tickets 
Ticket creation will be handled and automatically created by Ticket Set endpoint
## 3.1 Ticket
* List all tickets:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `GET /tickets/all/`
* List all available tickets for specific event: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /tickets/all/event_id={event_id}/ticket_type={ticket_type}/status={status}/`
* List all selected tickets for specific event:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `GET /tickets/all/{id}/selected/`
* Create a new ticket: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`POST /ticket/all`
* Retrieve ticket for specific event: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /tickets/all/event_id={event_id}/ticket_id={ticket_id}/`
* Reserve ticket for specific event: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PATCH /tickets/all/event_id={event_id}/ticket_id={ticket_id}/reserve`
* Advanced tickets filter: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`GET /tickets/all/event_id={event_id}/ticket_type={ticket_type}/status={status}/`

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
