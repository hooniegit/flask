# MODULE IMPORT
import sys
sys.path.append("/Users/kimdohoon/git/hanul-site-pipeline/lib/MySQL")
import connector_job as lib

# PARAMETERS
JSON_DIR = "/Users/kimdohoon/git/hanul-site-pipeline/datas/JSON/sensors/404"
TABLE_NAME = 'Sensors'

# UPDATE DATABASE
lib.JSON_to_table(JSON_DIR, TABLE_NAME)