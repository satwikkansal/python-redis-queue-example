from rq import Queue
from rq.job import Job
from worker import conn

q = Queue(connection=conn)


def add_to_queue(task, *args):
    job = q.enqueue(task, *args)
    return job


def get_job_status(job_id):
    job = Job.fetch(job_id, connection=conn)
    status = {
        "queued": job.is_queued,
        "finished": job.is_finished,
        "started": job.is_started,
        "failed": job.is_failed,
    }
    return status
