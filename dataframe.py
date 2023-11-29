import sqlite3
import pandas as pd

class GetDataframe:

    def frame_to_data(self, database_data, columns):
        df = pd.DataFrame(database_data, columns=columns)
        print(df)
        return df

if __name__ == "__main__":
    connection = sqlite3.connect(r"encrypted_student_finder.db")
    cur = connection.cursor()

    # Fetch data from the database
    database_data = cur.execute("select * from facebook_message order by id").fetchall()

    # Create a DataFrame from the fetched data
    columns = ["id", "facebook_id", "message"]

    # Call frame_to_data with the fetched data and columns
    GetDataframe().frame_to_data(database_data, columns)


