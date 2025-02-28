import streamlit as st

st.markdown('''


distill kit

simple_unified_distill_columns(df, subset=None, strategy='unified', bins_cut_or_len=-1, outliers_cut=0.98, return_bin_instances=False, **kwargs) 📊 Description: This function performs unsupervised discretization (binning) of numerical features in a pandas DataFrame. �sample: distill.simple_unified_distill_columns(df, subset=['age', 'income'], strategy='unified', bins_cut_or_len=5)

simple_similarity_distill(df, subset=None, strategy='information', bins_cut_or_len=-1, outliers_cut=0.98, return_bin_instances=False, **kwargs) 🔍 Description: This function performs supervised discretization (binning) of numerical features based on their similarity to the target variable. �sample: distill.simple_similarity_distill(df, subset=['age', 'income'], strategy='information', bins_cut_or_len=5, target='target_column')

simple_ordinal_distill(df, subset=None, strategy='ordinal', bins_cut_or_len=-1, outliers_cut=0.98, return_bin_instances=False, **kwargs) 🔢 Description: This function performs ordinal encoding of categorical features in a pandas DataFrame. �sample: distill.simple_ordinal_distill(df, subset=['category1', 'category2'], strategy='ordinal')

simple_boolify_distill(df, subset=None, strategy='boolify', bins_cut_or_len=-1, outliers_cut=0.98, return_bin_instances=False, **kwargs) 📈 Description: This function binarizes (converts to 0 and 1) numerical features in a pandas DataFrame based on a specified threshold. �ample: distill.simple_boolify_distill(df, subset=['age', 'income'], strategy='boolify', bins_cut_or_len=30)

merge kit

simple_merge(df1, df2, on=None, how='inner', left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) 🔗 Description: This function merges two pandas DataFrames using various merge strategies. �ample: merge.simple_merge(df1, df2, on='key_column', how='left')

simple_concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True) 🧩 Description: This function concatenates pandas objects (e.g., DataFrames, Series) along a particular axis. �ample: merge.simple_concat([df1, df2], axis=1, ignore_index=True)

simple_cross(df1, df2, **kwargs) ✖️ Description: This function computes the cross-product of two pandas DataFrames. �ample: merge.simple_cross(df1, df2)

simple_join(df1, df2, on=None, how='left', lsuffix='', rsuffix='', sort=False) 🔀 Description: This function performs a join operation on two pandas DataFrames based on the specified column(s). �ample: merge.simple_join(df1, df2, on='key_column', how='inner')


''')
