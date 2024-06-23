#%%
import pandas_datareader.data as wb
import datetime as date
import pandas as pd
import numpy as np
startdate='2014-2-1'
enddate='2016-2-1'

tenyear=wb.DataReader("DGS10", "fred",startdate,enddate)
fiveyear=wb.DataReader("DGS5", "fred",startdate,enddate)
oneyear=wb.DataReader("DGS1", "fred",startdate,enddate)
sixmonth=wb.DataReader("DGS6MO", "fred",startdate,enddate)

tenyearmean=tenyear['DGS10'].mean()
tenyearstd=np.std(tenyear['DGS10'])
print("Ten year Mean: ",tenyearmean)
print("Ten Year STD: ",tenyearstd)

mask = (tenyear['DGS10'] > tenyearmean + tenyearstd) | (tenyear['DGS10'] < tenyearmean - tenyearstd)
selection = tenyear[mask]
print(selection)

fiveyearmean=fiveyear['DGS5'].mean()
fiveyearstd=np.std(fiveyear['DGS5'])
print("Five year Mean: ",fiveyearmean)
print("Five Year STD: ",fiveyearstd)

oneyearmean=oneyear['DGS1'].mean()
oneyearstd=np.std(oneyear['DGS1'])
print("One year Mean: ",oneyearmean)
print("One Year STD: ",oneyearstd)
# %%
