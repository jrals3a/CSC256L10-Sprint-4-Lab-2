# app/routes/ui.py
from typing import Any

from flask import Blueprint, current_app, redirect, render_template, request, url_for

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def home() -> Any:
    """Home page — redirect to add task form."""
    return redirect(url_for("ui.task_submit"))

@ui_bp.route("/tasks/new", methods=["GET", "POST"])
def task_submit() -> Any:
    """Display add task form (GET) and handle submission (POST).

    Validation layers:
    - HTML5 'required' attribute — front-end (bypassed by disabling JS)
    - Server-side check here — back-end (cannot be bypassed)
    - TaskService.add_task() ValueError — business layer
    """
    error = None

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title:
            error = "Title is required."
        else:
            try:
                current_app.task_service.add_task(title, description)  # type: ignore[attr-defined]
                return redirect(url_for("ui.show_tasks"))
            except Exception as e:
                error = f"Error creating task: {str(e)}"

    return render_template("add_task.html", error=error)

@ui_bp.route("/tasks")
def show_tasks() -> Any:
    """Display all tasks in a list view."""
    tasks = current_app.task_service.get_all_tasks()  # type: ignore[attr-defined]
    return render_template("task_list.html", tasks=tasks)

@ui_bp.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id: int) -> Any:
    """Mark a task as complete and redirect to task list."""
    try:
        current_app.task_service.complete_task(task_id)  # type: ignore[attr-defined]
    except Exception:
        pass
    return redirect(url_for("ui.show_tasks"))

@ui_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id: int) -> Any:
    """Delete a task and redirect to task list."""
    try:
        current_app.task_service.delete_task(task_id)  # type: ignore[attr-defined]
    except Exception:
        pass
    return redirect(url_for("ui.show_tasks"))
