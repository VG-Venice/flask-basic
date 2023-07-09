from sqlalchemy import create_engine, text

# database: flaskpythontutorial
# username: q5ypnu7ke2nuriun8pqc
# host: aws.connect.psdb.cloud
# password: pscale_pw_EhWnGlz6m9bMJhAui67lR2NguO8sWcSKAe57ENyCdrY


engine = create_engine("mysql+pymysql://q5ypnu7ke2nuriun8pqc:pscale_pw_EhWnGlz6m9bMJhAui67lR2NguO8sWcSKAe57ENyCdrY@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4",
                       connect_args={"ssl": {
                         "ssl_ca": "cert.pem"
                       }})


def ListJobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(({
      "id": row.id,
      "title": row.title,
      "location": row.location,
      "salary": row.salary,
      "currency": row.currency,
      "responsbilities": row.responsbilities,
      "requirements": row.requirements,
    }))
  return result_dicts

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      val = id
    )