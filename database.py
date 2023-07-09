from sqlalchemy import create_engine, text

# database: flaskpythontutorial
# username: 16ndd2le9m6la94nbq16
# host: aws.connect.psdb.cloud
# password: pscale_pw_hoDcnk7nR5eH62lYiVKLQ0I3AKCyalWSYCRmAkTN9P1

engine = create_engine("mysql+pymysql://16ndd2le9m6la94nbq16:pscale_pw_hoDcnk7nR5eH62lYiVKLQ0I3AKCyalWSYCRmAkTN9P1@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4",
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

'''def ListJobs1(id):
  id = jobs['id']
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), val=jobs['id'])
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
  return result_dicts'''

'''def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      val = id
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])'''

def loadthe_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id ={id}")
    )
    rows = []
    for row in result.all():
      rows.append(({
      "id": row.id,
      "title": row.title,
      "location": row.location,
      "salary": row.salary,
      "currency": row.currency,
      "responsbilities": row.responsbilities,
      "requirements": row.requirements,
    }))
    if len(rows) == 0:
      return None
    else:
      return row