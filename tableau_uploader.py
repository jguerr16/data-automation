# tableau_uploader.py
from tableauhyperapi import HyperProcess, Connection, TableDefinition, SqlType, Inserter

def upload_to_tableau_cloud(processed_csv):
    with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
        with Connection(endpoint=hyper.endpoint, database="output.hyper") as connection:
            table_definition = TableDefinition(table_name="Extract", columns=[
                ("City", SqlType.text()),
                ("Other_Columns", SqlType.text()),  # Adjust based on your CSV columns
            ])
            connection.catalog.create_table(table_definition)
            
            # Insert rows from the processed CSV
            df = pd.read_csv(processed_csv)
            with Inserter(connection, table_definition) as inserter:
                inserter.add_rows(df.itertuples(index=False, name=None))
                inserter.execute()
