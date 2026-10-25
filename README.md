# Mini JSON ↔ CSV Converter

Converts JSON arrays of objects to CSV and CSV rows to JSON using explicit headers.

## Requirements

- Python 3.10+
- Standard library only; no `pip install` step required.

## Run

```bash
python main.py --help
```

## Example

`python main.py json-to-csv data.json data.csv` or `python main.py csv-to-json data.csv data.json`

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety notes

Use copies of important files. Review output before using it in production. Do not add credentials, private data, or real customer files to Git.

## License

MIT. See [LICENSE](LICENSE).
