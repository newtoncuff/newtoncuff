# Update the SQLAlchemy database URI for MSSQL
# database_config.py


db_username = "sa"
db_password = "password"
db_server = "192.168.1.108"
db_port = "1433"
db_name = "testdb"
db_driver = "ODBC+Driver+17+for+SQL+Server"

# Construct the full SQLAlchemy database URI
database_connection_uri = (
    f"mssql+pyodbc://{db_username}:{db_password}@{db_server}:{db_port}/{db_name}?driver={db_driver}"
)
