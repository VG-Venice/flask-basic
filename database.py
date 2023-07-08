from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://fu1bao7d4a2mo5hmmmmr:pscale_pw_kTszmmr4jB64c1G6t2b44WDQ1To64FDXpJdylbsoKLu@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4"

engine = create_engine(db_connection_string,
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
