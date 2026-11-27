"""data/*.json 에서 사이트에 필요한 부분만 골라 index.html 안의 DATA 블록을 다시 씁니다.
   실행: python3 tools/build-data.py  (저장소 맨 위 폴더에서)"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
z = json.loads((root / "data/pons-de-zeiten-notes.json").read_text())
g = json.loads((root / "data/pons-de-tense-notes.json").read_text())
data = {
  "Z": {"cite": z["citation"]["short_template"], "ids": z["ids"],
        "by": z["pons_zeiten_by_id"], "extra": z["pons_zeiten_extra"]},
  "G": {"cite": g["citation"]["short_template"], "ids": g["verb_ids"],
        "by": g["pons_by_verb"], "extra": g["pons_extra"]},
}
js = "const PONS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";"
html = (root / "index.html").read_text()
new, n = re.subn(r"/\*DATA-START\*/.*?/\*DATA-END\*/", lambda m: "/*DATA-START*/" + js + "/*DATA-END*/", html, flags=re.S)
assert n == 1, "DATA 표시를 찾지 못했습니다"
(root / "index.html").write_text(new)
print("ok", len(js), "bytes")
