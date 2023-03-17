import pandas as pd
import polars as pl
from ydata_profiling import ProfileReport

data_alert_bogor = pl.read_csv('data/raw/aggregate_alerts_Kota Bogor.csv').to_pandas()
data_med_irr_bogor = pl.read_csv('data/raw/aggregate_median_irregularities_Kota Bogor.csv').to_pandas()
data_med_jam_bogor = pl.read_csv('data/raw/aggregate_median_jams_Kota Bogor.csv').to_pandas()

data_alert_bogor_profile = ProfileReport(data_alert_bogor)
data_alert_bogor_profile.to_file('reports/alert_bogor_report.html')

data_med_irr_bogor_profile = ProfileReport(data_med_irr_bogor)
data_med_irr_bogor_profile.to_file('reports/med_irr_bogor_report.html')

data_med_jam_bogor_profile = ProfileReport(data_med_jam_bogor)
data_med_jam_bogor_profile.to_file('reports/med_jam_bogor_report.html')