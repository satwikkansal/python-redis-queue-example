from flask import Flask, jsonify
from rq.job import Job

from interface import add_to_queue, get_job_status
from tasks import execute_background_task

app = Flask(__name__)


@app.route('/getnums/<batch_num>')
def queue_get_task(batch_num):
    job = add_to_queue(execute_background_task, batch_num)
    return job.get_id()


@app.route("/status/<job_id>")
def get_results(job_id):
    return jsonify(get_job_status(job_id))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
