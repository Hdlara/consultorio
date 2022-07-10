# Clinic

The project consists of a system that creates and stores queries/exams

clone the project: git clone https://github.com/Hdlara/consultorio.git

## Setting

This app is using
<table>
	<tr>
		<td>Django</td>
		<td>Python</td>
    <td>djangorestframework</td>
	</tr>
	<tr>
		<td>4.0.1</td>
		<td>3.8.12</td>
    <td>3.13.1</td>
	</tr>
</table>

Import as collections in postman

<img width="381" alt="superuser" src="https://user-images.githubusercontent.com/58369362/178130156-d7594d61-5731-4975-96b6-a5f4fb41d56f.png">

name file Consultorio.postman_collection.json

<img width="381" alt="superuser" src="https://user-images.githubusercontent.com/58369362/178130185-4ab50a6e-fc15-4b17-a155-7e366c45aa52.png">


### Docker

See installation instructions at: https://docs.docker.com/get-docker/

### Docker Compose

Install docker compose , see installation instructions at: https://docs.docker.com/compose/install/

## Build and run the container

First let's start:
```
docker-compose up
```

## Run migrate

After the container started we will run the commands:

```
python manage.py makemigrations
python manage.py migrate
```

<img width="381" alt="superuser" src="https://user-images.githubusercontent.com/58369362/178130058-ebf393af-efe2-4e84-a456-c28fa75d6508.png">



