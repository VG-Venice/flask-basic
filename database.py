from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://4z5xony1qnse9hpmnt5n:pscale_pw_Iuo2iVOi2Y41JtZtDMtHgxB2F2r4X1VqgZXUyEF504U@aws.connect.psdb.cloud/flaskpythontutorial?charset=utf8mb4"

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())