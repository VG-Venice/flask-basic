from sqlalchemy import create_engine, text

# database: flaskpythontutorial
# username: 7udvach8ptc5j41hg86b
# host: aws.connect.psdb.cloud
# password: pscale_pw_DA5uVQWoiHr6d0xAgsaNksaM9Y3XRFos3YJmOlrA0Vu


engine = create_engine("mysql+pymysql://7udvach8ptc5j41hg86b:pscale_pw_DA5uVQWoiHr6d0xAgsaNksaM9Y3XRFos3YJmOlrA0Vu@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4",
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
