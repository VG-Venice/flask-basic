from sqlalchemy import create_engine, text
import os

# database: flaskpythontutorial
# username: g6tiedivq7sgy6ccijl9
# host: aws.connect.psdb.cloud
# password: pscale_pw_rpQV331JU7SeronXWalfhnhVXcfkd56Ma7FRlS4t4QR



db_connection_string = os.environ['DB_CONNECTION_STRING']

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
