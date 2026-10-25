# Mini JSON ↔ CSV Converter

A small Python command-line utility for converting JSON arrays of objects to CSV and CSV records to JSON.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Convert a JSON array of objects to CSV.
- Convert CSV rows to a JSON array of objects.
- Build CSV headers from keys encountered in the JSON objects.
- Read UTF-8 text with an optional UTF-8 BOM.
- Preserve non-ASCII text when writing JSON.
- Reject identical input/output paths and refuse to overwrite an existing output file.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Show all command options:

```bash
python main.py --help
```

Convert JSON to CSV:

```bash
python main.py json-to-csv data.json data.csv
```

Convert CSV to JSON:

```bash
python main.py csv-to-json data.csv data.json
```

Use a new output filename. The tool intentionally stops if the destination already exists.

## Accepted input shapes

For JSON-to-CSV, the input must be a JSON array of objects, for example:

```json
[
  {"name": "Ada", "score": 98},
  {"name": "Grace", "score": 95}
]
```

For CSV-to-JSON, the first row is treated as the CSV header.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Scope and limitations

This utility performs format conversion; it does not infer types, repair malformed source data, or guarantee that every downstream application interprets values identically. For JSON objects with different keys, columns are built from the keys encountered; review the result before using it in a business workflow.

## Related Quantix projects

- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Quantix 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)
- [All public repositories](https://github.com/000MAK?tab=repositories)

## Safety

Use synthetic examples in public demonstrations. Do not commit credentials, private data, or customer files.

## License

MIT. See [LICENSE](LICENSE).
