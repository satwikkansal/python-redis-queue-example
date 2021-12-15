from flask import Flask, jsonify
from rq.job import Job

from interface import add_to_queue, get_job_status
from tasks import execute_background_task

app = Flask(__name__)


help_string = """
Welcome!

This site has two GET resources;

1. `/getnums/<int>` to queue a background task, the integer can be anything, doesn't matter. It returns a job ID.
2. `/status/<job_id>` You can use the job id returned in the above resource to check the status of the job.

Every job takes 30 seconds to get executed (hardcoded sleep timer of 30s).
"""


@app.route('/')
def home():
    return help_string


@app.route('/getnums/<batch_num>')
def queue_get_task(batch_num):
    # execute_background_task is the task function you want to queue, batch_num is the argument
    job = add_to_queue(execute_background_task, batch_num)
    return job.get_id()


@app.route("/status/<job_id>")
def get_results(job_id):
    # To check the status of current job
    return jsonify(get_job_status(job_id))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
