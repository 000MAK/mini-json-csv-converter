import json,tempfile,unittest
from pathlib import Path
from main import convert_json_to_csv,convert_csv_to_json
class ConverterTests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            j=Path(d)/"a.json"; c=Path(d)/"a.csv"; out=Path(d)/"b.json"
            j.write_text('[{"name":"Ada","score":3},{"name":"Lin","score":4}]')
            self.assertEqual(convert_json_to_csv(j,c),2); self.assertEqual(convert_csv_to_json(c,out),2)
            self.assertEqual(json.loads(out.read_text())[0]["name"],"Ada")
    def test_existing_destination_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            j=Path(d)/"a.json"; dst=Path(d)/"out.csv"; j.write_text("[]"); dst.write_text("keep")
            with self.assertRaises(FileExistsError): convert_json_to_csv(j,dst)
            self.assertEqual(dst.read_text(),"keep")
    def test_non_array_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            j=Path(d)/"a.json"; j.write_text('{"a":1}')
            with self.assertRaises(ValueError): convert_json_to_csv(j,Path(d)/"x.csv")
if __name__=="__main__": unittest.main()
