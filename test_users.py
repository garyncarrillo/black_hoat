#!/usr/bin/env python3

from fastapi.testclient import TestClient
from .users import app

service = TestClient(app)

def test_create():
    response = service.post(
        '/users/1',
        json = {
            "first_name": "Garyn",
            "last_name": "Carrillo",
            "email": "garyn.c@hotmail.com",
            "street": "calle 70 # 60",
            "phone": "55555555"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "Garyn",
        "last_name": "Carrillo",
        "email": "garyn.c@hotmail.com",
        "street": "calle 70 # 60",
        "phone": "55555555"
    }

def test_create_id_already_exist():
    response = service.post(
        '/users/1',
        json = {
            "first_name": "Garyn",
            "last_name": "Carrillo",
            "email": "garyn.c@hotmail.com",
            "street": "calle 70 # 60",
            "phone": "55555555"
        }
    )
    assert response.status_code == 400
    assert response.json() == { "detail": "User Already Exists" }


def test_show():
    response = service.get('/users/1')
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "Garyn",
        "last_name": "Carrillo",
        "email": "garyn.c@hotmail.com",
        "street": "calle 70 # 60",
        "phone": "55555555"
    }

def test_show_id_already_exist():
    response = service.get('/users/2')
    assert response.status_code == 404
    assert response.json() == { "detail": "User not found" }

def test_update_id_not_exist():
    response = service.put(
        '/users/4',
        json = {
            "first_name": "Garyn",
            "last_name": "Carrillo",
            "email": "garyn.c@hotmail.com",
            "street": "calle 70 # 60"
        }
    )
    assert response.status_code == 404
    assert response.json() == { "detail": "User not found" }


def test_update():
    response = service.put(
        '/users/1',
        json = {
            "first_name": "Jairo",
            "last_name": "Hernandez",
            "email": "jairo.h@hotmail.com",
            "street": "calle 50 # 30",
            "phone": "7777777"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "Jairo",
        "last_name": "Hernandez",
        "email": "jairo.h@hotmail.com",
        "street": "calle 50 # 30",
        "phone": "7777777"
    }

def test_update_incomplete():
    response = service.put(
        '/users/1',
        json = {
            "first_name": "Garyn",
            "last_name": "Carrillo",
            "email": "garyn.c@hotmail.com",
            "street": "calle 70 # 60"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "Garyn",
        "last_name": "Carrillo",
        "email": "garyn.c@hotmail.com",
        "street": "calle 70 # 60",
        "phone": "7777777"
    }

def test_delete_id_not_exist():
    response = service.delete('/users/2')
    assert response.status_code == 404
    assert response.json() == { "detail": "User not found" }

def test_delete():
    response = service.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == { "Message": "User Deleted Succesfully" }
