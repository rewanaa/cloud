from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@core_bp.route("/index")
@core_bp.route("/index.html")
@login_required
def home():
    return render_template("core/index.html")


@core_bp.route("/about-us")
@core_bp.route("/about-us.html")
@login_required
def about_us():
    return render_template("core/about_us.html")


@core_bp.route("/appointment")
@core_bp.route("/appointment.html")
@login_required
def appointment():
    return render_template("core/appointment.html")


@core_bp.route("/department")
@core_bp.route("/department.html")
@login_required
def department():
    return render_template("core/department.html")


@core_bp.route("/doctor")
@core_bp.route("/doctor.html")
@login_required
def doctor():
    return render_template("core/doctor.html")


@core_bp.route("/medication")
@core_bp.route("/medication.html")
@login_required
def medication():
    return render_template("core/medication.html")


@core_bp.route("/nurse")
@core_bp.route("/nurse.html")
@login_required
def nurse():
    return render_template("core/nurse.html")


@core_bp.route("/patient")
@core_bp.route("/patient.html")
@login_required
def patient():
    return render_template("core/patient.html")


@core_bp.route("/prescribes")
@core_bp.route("/prescribes.html")
@login_required
def prescribes():
    return render_template("core/prescribes.html")


@core_bp.route("/procedure")
@core_bp.route("/procedure.html")
@login_required
def procedure():
    return render_template("core/procedure.html")


@core_bp.route("/room")
@core_bp.route("/room.html")
@login_required
def room():
    return render_template("core/room.html")


@core_bp.route("/undergoes")
@core_bp.route("/undergoes.html")
@login_required
def undergoes():
    return render_template("core/undergoes.html")
