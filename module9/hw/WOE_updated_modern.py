# Author:
# Sundar Krishnan

# Updated by: Tyler Whitlock 7/12/2024
# Updated the WOE function to include epsilon to avoid division by zero
# Updated the WOE to avoid using df.append 

# https://github.com/Sundar0989/WOE-and-IV/blob/master/WOE_IV.ipynb

# import packages
import pandas as pd
import numpy as np
from pandas import Series
from scipy.stats import spearmanr
import re
import traceback

max_bin = 20
force_bin = 3
epsilon = 1e-10  # small constant to avoid division by zero

# define a binning function
def mono_bin(Y, X, n=max_bin):
    df1 = pd.DataFrame({"X": X, "Y": Y})
    justmiss = df1[['X', 'Y']][df1.X.isnull()]
    notmiss = df1[['X', 'Y']][df1.X.notnull()]
    r = 0
    while np.abs(r) < 1 and n > 1:
        try:
            d1 = pd.DataFrame({"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.qcut(notmiss.X, n, duplicates='drop')})
            d2 = d1.groupby('Bucket', as_index=True, observed=True)
            r, p = spearmanr(d2.mean().X, d2.mean().Y)
            n = n - 1
        except Exception as e:
            n = n - 1

    if len(d2) == 1 or n == 1:
        n = force_bin
        bins = np.quantile(notmiss.X, np.linspace(0, 1, n))
        if len(np.unique(bins)) == 2:
            bins = np.insert(bins, 0, 1)
            bins[1] = bins[1] - (bins[1] / 2)
        d1 = pd.DataFrame(
            {"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.cut(notmiss.X, np.unique(bins), include_lowest=True)})
        d2 = d1.groupby('Bucket', as_index=True, observed=True)

    d3 = pd.DataFrame({}, index=[])
    d3["MIN_VALUE"] = d2.min().X
    d3["MAX_VALUE"] = d2.max().X
    d3["COUNT"] = d2.count().Y
    d3["EVENT"] = d2.sum().Y
    d3["NONEVENT"] = d2.count().Y - d2.sum().Y
    d3 = d3.reset_index(drop=True)

    if len(justmiss.index) > 0:
        d4 = pd.DataFrame({'MIN_VALUE': [np.nan], 'MAX_VALUE': [np.nan], 'COUNT': justmiss.count().Y, 'EVENT': justmiss.sum().Y,
                           'NONEVENT': justmiss.count().Y - justmiss.sum().Y})
        d3 = pd.concat([d3, d4], ignore_index=True)

    d3["EVENT_RATE"] = d3.EVENT / d3.COUNT
    d3["NON_EVENT_RATE"] = d3.NONEVENT / d3.COUNT
    d3["DIST_EVENT"] = d3.EVENT / (d3["EVENT"].sum() + epsilon)
    d3["DIST_NON_EVENT"] = d3.NONEVENT / (d3["NONEVENT"].sum() + epsilon)
    d3["WOE"] = np.log((d3.DIST_EVENT + epsilon) / (d3.DIST_NON_EVENT + epsilon))
    d3["IV"] = (d3.DIST_EVENT - d3.DIST_NON_EVENT) * np.log((d3.DIST_EVENT + epsilon) / (d3.DIST_NON_EVENT + epsilon))
    d3["VAR_NAME"] = "VAR"
    d3 = d3[['VAR_NAME', 'MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE',
             'DIST_EVENT', 'DIST_NON_EVENT', 'WOE', 'IV']]
    d3 = d3.replace([np.inf, -np.inf], 0)
    d3.IV = d3.IV.sum()

    return d3

def char_bin(Y, X):
    df1 = pd.DataFrame({"X": X, "Y": Y})
    justmiss = df1[['X', 'Y']][df1.X.isnull()]
    notmiss = df1[['X', 'Y']][df1.X.notnull()]
    df2 = notmiss.groupby('X', as_index=True, observed=True)

    d3 = pd.DataFrame({}, index=[])
    d3["COUNT"] = df2.count().Y
    d3["MIN_VALUE"] = df2.sum().Y.index
    d3["MAX_VALUE"] = d3["MIN_VALUE"]
    d3["EVENT"] = df2.sum().Y
    d3["NONEVENT"] = df2.count().Y - df2.sum().Y

    if len(justmiss.index) > 0:
        d4 = pd.DataFrame({'MIN_VALUE': [np.nan], 'MAX_VALUE': [np.nan], 'COUNT': justmiss.count().Y, 'EVENT': justmiss.sum().Y,
                           'NONEVENT': justmiss.count().Y - justmiss.sum().Y})
        d3 = pd.concat([d3, d4], ignore_index=True)

    d3["EVENT_RATE"] = d3.EVENT / d3.COUNT
    d3["NON_EVENT_RATE"] = d3.NONEVENT / d3.COUNT
    d3["DIST_EVENT"] = d3.EVENT / (d3["EVENT"].sum() + epsilon)
    d3["DIST_NON_EVENT"] = d3.NONEVENT / (d3["NONEVENT"].sum() + epsilon)
    d3["WOE"] = np.log((d3.DIST_EVENT + epsilon) / (d3.DIST_NON_EVENT + epsilon))
    d3["IV"] = (d3.DIST_EVENT - d3.DIST_NON_EVENT) * np.log((d3.DIST_EVENT + epsilon) / (d3.DIST_NON_EVENT + epsilon))
    d3["VAR_NAME"] = "VAR"
    d3 = d3[['VAR_NAME', 'MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE',
             'DIST_EVENT', 'DIST_NON_EVENT', 'WOE', 'IV']]
    d3 = d3.replace([np.inf, -np.inf], 0)
    d3.IV = d3.IV.sum()
    d3 = d3.reset_index(drop=True)

    return d3

def data_vars(df1, target):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
    final = (re.findall(r"[\w']+", vars_name))[-1]

    x = df1.dtypes.index
    count = -1

    for i in x:
        if i.upper() not in (final.upper()):
            if np.issubdtype(df1[i], np.number) and len(Series.unique(df1[i])) > 2:
                conv = mono_bin(target, df1[i])
                conv["VAR_NAME"] = i
                count = count + 1
            else:
                conv = char_bin(target, df1[i])
                conv["VAR_NAME"] = i
                count = count + 1

            if count == 0:
                iv_df = conv
            else:
                iv_df = pd.concat([iv_df, conv], ignore_index=True)

    iv = pd.DataFrame({'IV': iv_df.groupby('VAR_NAME').IV.max()})
    iv = iv.reset_index()
    return iv_df, iv

