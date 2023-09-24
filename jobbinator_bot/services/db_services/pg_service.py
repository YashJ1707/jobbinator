import psycopg2
from psycopg2 import sql
from models.job_model import Job
def connectDB():
    conn= psycopg2.connect(
        dbname="jobbinator",
        user="yashjaybhaye",
        password="jobbinator@123",
        host="localhost",
        port="5432"
    )
    return conn


def upsertData(jobs: list[Job]):
    conn=connectDB()
    cur=conn.cursor()
    for job in jobs:
        upsert_query=sql.SQL("""INSERT INTO Jobs (company_name,job_title, date_posted,salary,job_location, job_description, job_url,tags)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (job_url) DO NOTHING;""")
        data=(job.company_name,job.jobTitle,job.datePosted,job.salary,job.location,job.job_description,job.url,job.tags)
        try:
            cur.execute(upsert_query,data)
        except Exception as err:
            print(err)
    conn.commit()
    cur.close()
    conn.close()








     # for job in jobs:
    # create_query=sql.SQL("""CREATE TABLE Jobs (
    #                      id SERIAL PRIMARY KEY ,
    #                      job_title VARCHAR(200) NOT NULL,
    #                      job_location VARCHAR(100) NOT NULL,
    #                      company_name VARCHAR(100) NOT NULL,
    #                      salary VARCHAR(200),
    #                      job_url VARCHAR(200) UNIQUE NOT NULL,
    #                      date_posted VARCHAR(100),
    #                      job_description TEXT
    # )""")