import argparse,csv,json
from pathlib import Path

def convert_json_to_csv(source,destination):
    src,dst=Path(source).resolve(),Path(destination).resolve()
    if src==dst: raise ValueError("Input and output paths must be different")
    if dst.exists(): raise FileExistsError(dst)
    data=json.loads(src.read_text(encoding="utf-8-sig"))
    if not isinstance(data,list) or any(not isinstance(x,dict) for x in data): raise ValueError("JSON must be an array of objects")
    fields=[]
    for obj in data:
        for key in obj:
            if key not in fields: fields.append(key)
    with dst.open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction="raise"); writer.writeheader(); writer.writerows(data)
    return len(data)

def convert_csv_to_json(source,destination):
    src,dst=Path(source).resolve(),Path(destination).resolve()
    if src==dst: raise ValueError("Input and output paths must be different")
    if dst.exists(): raise FileExistsError(dst)
    with src.open("r",encoding="utf-8-sig",newline="") as f: data=list(csv.DictReader(f))
    dst.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return len(data)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("direction",choices=["json-to-csv","csv-to-json"]); ap.add_argument("input"); ap.add_argument("output"); a=ap.parse_args()
    n=convert_json_to_csv(a.input,a.output) if a.direction=="json-to-csv" else convert_csv_to_json(a.input,a.output)
    print(f"Converted {n} records")
if __name__=="__main__": main()
