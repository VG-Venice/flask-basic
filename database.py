from flask import jsonify
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://x9em91lw3prh5g69dt64:pscale_pw_Mo6OhAdAdEsYJuEA4VM0teT5EMmW0itovCdDgoLR3mx@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4"

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
