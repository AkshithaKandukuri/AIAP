import csv
import math
from typing import Dict, Optional


def csv_stats(path: str, columns: Optional[list] = None, delimiter: str = ',', encoding: str = 'utf-8') -> Dict[str, dict]:
	stats = {}

	with open(path, 'r', encoding=encoding, newline='') as f:
		reader = csv.DictReader(f, delimiter=delimiter)
		header = reader.fieldnames or []

		# Determine which columns to track
		if columns is None:
			target_cols = list(header)
		else:
			target_cols = [c for c in columns if c in header]

		# Initialize accumulators
		for col in target_cols:
			stats[col] = {'count': 0, 'sum': 0.0, 'min': None, 'max': None}

		for row in reader:
			for col in target_cols:
				raw = row.get(col)
				if raw is None:
					continue
				val = raw.strip()
				if val == '' or val.upper() in ('NA', 'N/A'):
					continue
				try:
					num = float(val)
				except (ValueError, TypeError):
					# not numeric, skip
					continue

				st = stats[col]
				st['count'] += 1
				st['sum'] += num
				if st['min'] is None or num < st['min']:
					st['min'] = num
				if st['max'] is None or num > st['max']:
					st['max'] = num

	result = {}
	for col, st in stats.items():
		if st['count'] == 0:
			result[col] = {'mean': None, 'min': None, 'max': None, 'count': 0}
		else:
			mean = st['sum'] / st['count']
			# Avoid -0.0 display
			if mean == 0.0:
				mean = 0.0
			result[col] = {'mean': mean, 'min': st['min'], 'max': st['max'], 'count': st['count']}

	return result


if __name__ == '__main__':
	import tempfile
	import os

	sample = [
		['id', 'name', 'age', 'score'],
		['1', 'Alice', '30', '85.5'],
		['2', 'Bob', '25', '91'],
		['3', 'Charlie', '', '78.25'],
		['4', 'Dana', '27', 'NA'],
		['5', 'Eve', '22', '88']
	]

	tmp = tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', suffix='.csv', encoding='utf-8')
	try:
		writer = csv.writer(tmp)
		writer.writerows(sample)
		tmp_path = tmp.name
	finally:
		tmp.close()

	print(f"Wrote sample CSV to: {tmp_path}")
	stats = csv_stats(tmp_path)
	print("Computed stats:")
	for col, s in stats.items():
		print(f"  {col}: mean={s['mean']}, min={s['min']}, max={s['max']}, count={s['count']}")

	try:
		os.unlink(tmp_path)
	except Exception:
		pass

