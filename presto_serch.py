import pandas as pd
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests.auth import HTTPBasicAuth
from sqlalchemy.engine import create_engine
from pyhive import presto
database_username = "omron_user_r@omron.boc"
database_password = "HhNg1x9A"
url = 'presto://omron_user_r@omron.boc@presto-prod.cloud.bz:30443/sbb3_boc/omron'
engine = create_engine( url,connect_args={'protocol': 'https','source':'adhoc','requests_kwargs':{'auth': HTTPBasicAuth(database_username,database_password),  'verify':False}
            }
        )
sql_cmd = ' select * from sbb3_boc.omron.s03_shop_ntr_kpi_tm_d limit 1 '
df_train = pd.read_sql(sql_cmd,con=engine)
print(df_train)
