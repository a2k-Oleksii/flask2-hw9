from app import app
from models.models import Plant
from flask import render_template, request, redirect


@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")


@app.route("/save-plant", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(name, location)
    plant.save()
    return redirect("/")


@app.route("/info-plant/<int:id>")
def info_plant(id):
    plant_employees = Plant.get_by_id(id)
    return render_template("info_plant.html", plant=plant_employees[0], employees=plant_employees[1])


@app.route("/delete-plant/<int:id>")
def delete(id):
    Plant.delete(id)
    return redirect("/")
