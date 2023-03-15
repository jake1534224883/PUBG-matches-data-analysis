from pyhive import presto
from sqlalchemy.engine import create_engine
from requests.auth import HTTPBasicAuth
import pandas as pd
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from openpyxl.workbook import Workbook
from datetime import datetime
import os


database_username = "omron_user_r@omron.boc"
database_password = "HhNg1x9A"
url = 'presto://omron_user_r@omron.boc@presto-prod.cloud.bz:30443/sbb3_boc/omron'
engine = create_engine(url, connect_args={'protocol': 'https', 'source': 'adhoc', 'requests_kwargs': {
                       'auth': HTTPBasicAuth(database_username, database_password),  'verify': False}})


table_names = [
    "sbb3_boc.omron.s02_product_conten_top_industry_tm_d",
    "sbb3_boc.omron.s02_product_spu_kpi_tm_d",
    "sbb3_boc.omron.s03_shop_content_goods_alys_tm_d",
    "sbb3_boc.omron.s03_shop_content_video_all_tm_d",
    "sbb3_boc.omron.s03_shop_home_operation_tm_d",
    "sbb3_boc.omron.s03_shop_ntr_kpi_tm_d",
    "sbb3_boc.omron.s03_shop_tr_kpi_tm_d",
    "sbb3_boc.omron.s03_shop_trade_overview_tm_d",
    "sbb3_boc.omron.s04_src_traffic_board_tm_d",
    "sbb3_boc.omron.s04_src_traffic_kpi_tm_d",
    "sbb3_boc.omron.s04_src_trafficm_broadcast_room_tm_d",
    "sbb3_boc.omron.s07_market_broadcast_live_room_tm_d",
    "sbb3_boc.omron.s10_trans_brand_tm_d",
    "sbb3_boc.omron.s10_trans_category_tm_d",
    "sbb3_boc.omron.s10_trans_voice_experience_star_tm_d",
    "sbb3_boc.omron.s10_trans_voice_service_data_tm_d",
            ]

dataframes = []
queries = [f"SELECT distinct date_value, date_value,'{table_name}' AS table_name FROM {table_name}" for table_name in table_names]
query = " UNION ALL ".join(queries)
df = pd.read_sql(query, engine)
today = datetime.today().strftime('%Y-%m-%d')
file_name = f'{today}.xlsx'

# 确定下载文件夹路径

download_folder = f'/Users/arthur/Downloads'

# 文件路径
file_path = os.path.join(download_folder, file_name)

# 删除旧文件
if os.path.exists(file_path):
    os.remove(file_path)

# 保存新文件conda
df.to_excel(file_path, index=False)
