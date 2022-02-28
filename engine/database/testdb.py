from db_connect import Database_Controller
import db_info
dbc = Database_Controller(db_info.login,
db_info.pw,
db_info.host,
db_info.port,
db_info.db,
'/home/michael/dev/search-engine/engine/indexer/html_files')

dbc.connect_database()
dbc.set_cursor()
dbc.set_title('Google')
dbc.insert_data()