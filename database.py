from sqlalchemy import create_engine, text
import os

# database: flaskpythontutorial
# username: idbfwk66pa71jfimypw8
# host: aws.connect.psdb.cloud
# password: pscale_pw_kgzOhNWcshHlyDkcvkrmgIYJXu3ql68a1pQpDLsePTY





engine = create_engine("mysql+pymysql://idbfwk66pa71jfimypw8:pscale_pw_kgzOhNWcshHlyDkcvkrmgIYJXu3ql68a1pQpDLsePTY@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4",
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
