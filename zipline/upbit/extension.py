import sys
from pathlib import Path
sys.path.append(Path('~', '.zipline_process').expanduser().as_posix())
from zipline.data.bundles import register
from upbit_kr_coin import upbit_to_bundle
import pandas as pd

upbit_start_session = pd.Timestamp('2020-12-31', tz='utc')
upbit_end_session = pd.Timestamp('2022-03-18', tz='utc')

register('upbit',
         upbit_to_bundle(),
         calendar_name='24/7',
         start_session=upbit_start_session,
         end_session=upbit_end_session,
         minutes_per_day=1440,
         )