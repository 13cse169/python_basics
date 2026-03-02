"""
This file is intentionally self-contained: it creates small in-memory
datasets (using StringIO / dicts) so you can run it without external files.

Each example function returns a small result (DataFrame or summary) and
prints a short informative message. The module guards against pandas
not being installed and prints a helpful hint.

Run this module directly to execute all examples:

	python pandas_examples.py

"""
from __future__ import annotations

import sys
import io
from typing import Optional


def import_pandas():
	try:
		import pandas as pd

		return pd
	except Exception:  # pragma: no cover - runtime environment
		print("pandas is not installed. Install it with: pip install pandas")
		return None


def create_dataframe_example(pd):
	"""Create a DataFrame from a dict and return it."""
	data = {
		"name": ["Alice", "Bob", "Charlie", "Diana"],
		"age": [25, 30, 35, 40],
		"score": [85.5, 92.0, 88.0, 79.5],
	}
	df = pd.DataFrame(data)
	print("create_dataframe_example:\n", df, sep="")
	return df


def read_csv_example(pd):
	"""Read CSV from an in-memory string and return the DataFrame."""
	csv = io.StringIO("""
		name,city,visits
		Alice,London,3
		Bob,Paris,1
		Charlie,London,2
		Diana,Berlin,5
	""")
	df = pd.read_csv(csv)
	print("read_csv_example:\n", df, sep="")
	return df


def selection_and_filter_example(pd, df: Optional[object] = None):
	"""Show selection, boolean filtering, and column operations."""
	if df is None:
		df = create_dataframe_example(pd)
	# select columns
	names = df["name"]
	# boolean filter
	older = df[df["age"] >= 30]
	# create new column
	df2 = df.copy()
	df2["age_plus_score"] = df2["age"] + df2["score"]
	print("selection_and_filter_example: names ->", names.tolist())
	print("selection_and_filter_example: older (age>=30)\n", older, sep="")
	print("selection_and_filter_example: with new column\n", df2, sep="")
	return df2


def groupby_aggregation_example(pd):
	"""Group by a column and aggregate."""
	csv = io.StringIO("""
city,category,amount
London,A,10
Paris,B,20
London,B,5
Berlin,A,8
Paris,A,7
""")
	df = pd.read_csv(csv)
	grouped = df.groupby("city").agg(total_amount=("amount", "sum"), count=("amount", "size"))
	print("groupby_aggregation_example:\n", grouped, sep="")
	return grouped


def merge_example(pd):
	"""Demonstrate merging (joins)."""
	left = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
	right = pd.DataFrame({"id": [2, 3, 4], "score": [88, 92, 75]})
	merged = left.merge(right, on="id", how="left")
	print("merge_example:\n", merged, sep="")
	return merged


def time_series_example(pd):
	"""Create a simple time series and resample it."""
	rng = pd.date_range("2023-01-01", periods=6, freq="D")
	ts = pd.Series([1, 3, 2, 5, 4, 6], index=rng, name="value")
	resampled = ts.resample("2D").sum()
	print("time_series_example: original:\n", ts, sep="")
	print("time_series_example: resampled (2D sum)\n", resampled, sep="")
	return resampled


def missing_data_example(pd):
	"""Show handling missing values."""
	df = pd.DataFrame({"A": [1, None, 3], "B": [None, 2, 3]})
	filled = df.fillna(df.mean(numeric_only=True))
	dropped = df.dropna()
	print("missing_data_example: original\n", df, sep="")
	print("missing_data_example: filled\n", filled, sep="")
	print("missing_data_example: dropped (rows with any NA)\n", dropped, sep="")
	return filled, dropped


def main():
	pd = import_pandas()
	if pd is None:
		return 1

	print("--- pandas examples starting ---")
	df1 = create_dataframe_example(pd)
	print("\n---\n")
	df2 = read_csv_example(pd)
	print("\n---\n")
	_ = selection_and_filter_example(pd, df1)
	print("\n---\n")
	_ = groupby_aggregation_example(pd)
	print("\n---\n")
	_ = merge_example(pd)
	print("\n---\n")
	_ = time_series_example(pd)
	print("\n---\n")
	_ = missing_data_example(pd)
	print("--- pandas examples finished ---")
	return 0


if __name__ == "__main__":
	sys.exit(main())

