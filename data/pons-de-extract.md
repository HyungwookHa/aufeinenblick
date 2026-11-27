# PONS 독일어 문법표 추출 자료

> 독일어 문법 사이트(시제 지도 등)를 만들거나 내용을 검증할 때 참고하는 자료입니다. 프랑스어 PONS 자료(`pons-tense-notes.json`, `pons-extract.md`)와 같은 방식으로 만들었습니다.
> 짝 파일 `pons-de-tense-notes.json`은 같은 내용을 사이트에서 바로 쓸 수 있는 데이터로 담고 있습니다.

## 0. 개요

- **원자료**: PONS 「Auf einen Blick – DEUTSCH Grammatik」, Renate Weber 지음 (Ernst Klett Sprachen, Stuttgart, 2003 · 2006년 개정 맞춤법 반영, ISBN 978-3-12-560701-9). 독일어로 쓰인 독일어 문법 요약표 (6쪽, 접이식).
- **얻은 방법**: 사용자가 올린 스캔 PDF(6쪽, 텍스트층 없음)를 독일어 OCR로 읽고 페이지 이미지와 대조해 판독.
- **이 파일에 담긴 것**
  1. 동사(시제·법·수동태·분사)에 관한 PONS 내용을 한국어로 요약해 칸별로 정리한 것 → 2장, 2-1장
  2. 주의할 점 → 3장
  3. 문법표 6쪽 전체의 제목 띠와 공식 박스를 독일어 → 한국어로 옮긴 것 (동사 외 문법 포함) → 4장
- **주의**: 원문을 그대로 옮긴 것이 아니라 한국어로 번역·요약한 것. 예문은 표에서 그대로 인용함. 공개 사이트에 쓸 때는 출처 표기를 유지할 것.

## 1. 사이트에서 쓰는 방식

- 각 칸은 아래 `id`로 구분합니다. 독일어 사이트가 아직 없어서 id와 한국어 이름은 이 파일에서 제안한 것입니다 (3장 참고).
- 데이터 구조: `{ id: { src, p, blocks: [ { h, p, items, item_p } ] } }`. 프랑스어 PONS 구조에 블록별 위치 `p`와 항목별 위치 `item_p`를 더했습니다.
- **위치 표기**: 쪽 번호가 없는 접이식 표라서 `3장 · 왼쪽 단`처럼 **실물 문법표의 쪽(1~6)과 세로 단(왼쪽·가운데·오른쪽)**으로 적었습니다. 본문 문장 안에는 위치를 넣지 않았습니다.
- **출처 표기 틀**: `출처: PONS 『Auf einen Blick – Deutsch Grammatik』, {p}` → 예: 출처: PONS 『Auf einen Blick – Deutsch Grammatik』, 3장 · 왼쪽 단
- 상자에 블록 하나를 쓰면 그 블록의 `p`를, 항목 하나만 쓰면 그 항목의 `item_p`를 씁니다. 이 MD에서는 각 블록 아래 `출처:` 줄이 블록의 `p`이고, 한 블록 안에서 위치가 갈리면 항목 끝에 〔 〕로 따로 적었습니다.

| id | 한국어 | 독일어 | 분류 | 위치 |
|---|---|---|---|---|
| `praesens` | 현재 | Präsens | 직설법 · 단순시제 | 2장 · 왼쪽 단 / 3장 · 왼쪽·가운데 단 |
| `praeteritum` | 과거 | Präteritum | 직설법 · 단순시제 · 주로 글말 | 2장 · 왼쪽 단 / 3장 · 왼쪽·가운데 단 |
| `perfekt` | 현재완료 | Perfekt | 직설법 · 복합시제 · 입말에서 과거 대신 | 3장 · 왼쪽 단 / 4장 · 오른쪽 단 |
| `plusquamperfekt` | 과거완료 | Plusquamperfekt | 직설법 · 복합시제 | 3장 · 가운데 단 |
| `futur1` | 미래 | Futur I | 직설법 · 복합시제 | 3장 · 가운데 단 |
| `futur2` | 미래완료 | Futur II | 직설법 · 복합시제 · 드물게 씀 | 3장 · 가운데 단 |
| `konj1` | 접속법 1식 현재 | Konjunktiv I | 접속법 1식 · 단순형 · 주로 글말 (간접화법) | 3장 · 가운데·오른쪽 단 |
| `konj1_perfekt` | 접속법 1식 과거 | Konjunktiv I Perfekt | 접속법 1식 · 복합형 | 3장 · 오른쪽 단 |
| `konj1_futur` | 접속법 1식 미래 | Konjunktiv I Futur | 접속법 1식 · 복합형 | 3장 · 오른쪽 단 |
| `konj2` | 접속법 2식 현재 | Konjunktiv II (würde + 원형 포함) | 접속법 2식 · 단순형 또는 würde형 | 2장 · 오른쪽 단 / 3장 · 가운데·오른쪽 단 |
| `konj2_pqp` | 접속법 2식 과거 | Konjunktiv II Plusquamperfekt | 접속법 2식 · 복합형 | 3장 · 오른쪽 단 |
| `imperativ` | 명령법 | Imperativ | 명령법 | 2장 · 가운데 단 / 3장 · 오른쪽 단 / 4장 · 가운데·오른쪽 단 |
| `partizip2` | 과거분사 | Partizip II | 분사 · 완료시제와 수동태의 재료 | 2장 · 왼쪽·가운데·오른쪽 단 |
| `passiv_vorgang` | 동작수동 | Vorgangspassiv | 수동태 · werden + 과거분사 | 2장 · 오른쪽 단 |
| `passiv_zustand` | 상태수동 | Zustandspassiv | 수동태 · sein + 과거분사 | 2장 · 오른쪽 단 |

## 2. 칸별 PONS 설명 (`pons_by_verb`)

### `praesens` — 현재 (Präsens)
위치: 2장 · 왼쪽 단 / 3장 · 왼쪽·가운데 단

**만들기 (공식 박스)**
- 동사 어간 + 인칭 어미: *ich male, du malst, er malt, wir malen, ihr malt, sie malen* 〔3장 · 왼쪽 단〕
- 기본 활용 (동사 첫머리): *ich wohn-e, du wohn-st, er/sie/es wohn-t, wir wohn-en, ihr wohn-t, sie wohn-en* 〔2장 · 왼쪽 단〕
<sub>출처: 2장 · 왼쪽 단 / 3장 · 왼쪽 단</sub>

**발음 때문에 생기는 특이점**
- 어간이 *-d/-t, -m/-n*으로 끝나면 *e*를 넣음: *arbeiten → du arbeitest, er arbeitet, ihr arbeitet* · *rechnen → du rechnest, er rechnet, ihr rechnet*
- 어간이 *-ß, -s, -ss, -z, -tz*로 끝나면 *du*형 어미의 *-s*가 빠짐: *grüßen → du grüßt*
- *-eln* 동사는 *ich*형에서 *-e*가 빠짐: *lächeln → ich lächle*
<sub>출처: 3장 · 왼쪽 단</sub>

**어간 모음이 바뀌는 불규칙동사 (du·er형)**
- *a → ä*: *fallen → du fällst, er fällt* · *au → äu*: *laufen → du läufst, er läuft* · *e → i*: *helfen → du hilfst, er hilft*
- *e → ie*: *lesen → du liest, er liest* · *o → ö*: *stoßen → du stößt, er stößt*
- '주의!!!' 표시가 붙은 예: *nehmen → du nimmst, er nimmt*
<sub>출처: 3장 · 왼쪽 단</sub>

**쓰임**
- 현재의 시제지만 거의 모든 시간을 덮을 수 있음 〔3장 · 왼쪽 단〕
- 지금 있거나 일어나는 일: *Ich gehe in Marbach zur Schule.* 〔3장 · 왼쪽 단〕
- 전에 시작해 지금까지 이어지는 일: *Seit neun Monaten lebe ich schon hier.* 〔3장 · 왼쪽 단〕
- 앞으로 일어날 일: *Morgen mache ich einen Klassenausflug.* 〔3장 · 왼쪽 단〕
- 늘 맞는 일: *Ich heiße Carolin und komme aus Brasilien.* 〔3장 · 왼쪽 단〕
- 미래는 보통 미래 시제보다 '시간 표현 + 현재'로 말함: *Morgen beginnen die Ferien.* · *Nächstes Jahr fahren wir wieder nach Spanien.* 〔3장 · 가운데 단〕
<sub>출처: 3장 · 왼쪽·가운데 단</sub>

### `praeteritum` — 과거 (Präteritum)
위치: 2장 · 왼쪽 단 / 3장 · 왼쪽·가운데 단

**만들기 (공식 박스)**
- 규칙동사: 원형 어간 + *-t-* + 인칭 어미
- 불규칙동사: 과거 어간 + 인칭 어미. 1·3인칭 단수는 어미가 없고, 어간 모음은 거의 늘 바뀜
<sub>출처: 3장 · 왼쪽 단</sub>

**활용 예**
- 규칙 *wohnen*: *ich wohnte, du wohntest, er wohnte, wir wohnten, ihr wohntet, sie wohnten*
- 불규칙 *gehen*: *ich ging, du gingst, er ging, wir gingen, ihr gingt, sie gingen*
- *bringen*: *ich brachte, du brachtest, er brachte, wir brachten, ihr brachtet, sie brachten*
<sub>출처: 3장 · 가운데 단</sub>

**규칙동사와 불규칙동사**
- 규칙동사(약변화)는 어간이 모든 시제에서 같고, 과거에서 모든 인칭에 <em>-te-</em>가 붙음: *ich lernte, du lerntest, er lernte*
- 불규칙동사(강변화)는 과거에서, 일부는 과거분사에서도 어간 모음이 바뀜. 과거의 1·3인칭은 같고 대개 어미가 없음
- 모음이 바뀌는 세 유형: ABC *helfen – half – geholfen* · ABB *leihen – lieh – geliehen* · ABA *fahren – fuhr – gefahren*
- 혼합 동사(*Mischgruppe*): 어간 모음은 바뀌는데 어미는 규칙동사와 같음. *brennen, bringen, denken, kennen, nennen, rennen, senden, wissen*과 화법조동사: *denken – dachte – gedacht* · *kennen – kannte – gekannt* · *wissen – wusste – gewusst*
- 아주 불규칙한 동사: *gehen – ging – gegangen* · *stehen – stand – gestanden* · *tun – tat – getan*
- 원형·과거·과거분사 세 꼴을 늘 함께 외우라고 권함. 이 셋으로 여러 시제와 수동태, 접속법을 만듦
<sub>출처: 2장 · 왼쪽 단</sub>

**쓰임**
- 과거에 끝난 일. 주로 글에서 쓰고, 말에서는 조동사·화법조동사를 빼면 현재완료를 더 씀 〔3장 · 가운데 단〕
- *haben, sein, werden*과 화법조동사는 거의 늘 과거로 씀 〔3장 · 왼쪽 단〕
<sub>출처: 3장 · 왼쪽·가운데 단</sub>

### `perfekt` — 현재완료 (Perfekt)
위치: 3장 · 왼쪽 단 / 4장 · 오른쪽 단

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 현재 + 과거분사: *ich habe gekocht, du hast gekocht, er hat gekocht* · *ich bin gelaufen, du bist gelaufen, er ist gelaufen*
<sub>출처: 3장 · 왼쪽 단</sub>

**haben이냐 sein이냐**
- 대부분 *haben*: 특히 재귀동사, 4격 목적어가 있는 동사, 화법조동사
- 나머지는 *sein*: 장소나 상태가 바뀌는 동사(*gehen, fahren, einschlafen, aufwachen*)와 *sein, werden, bleiben, passieren, geschehen*
<sub>출처: 3장 · 왼쪽 단</sub>

**쓰임**
- 지금과 관련이 있는 지난 일: *Wir sind von Japan nach Deutschland gezogen.* · *Nachdem er gelernt hat, ruht er sich aus.*
- 특히 입말에서 과거를 대신해 자주 씀. *haben, sein, werden*과 화법조동사만은 거의 늘 과거
<sub>출처: 3장 · 왼쪽 단</sub>

**어순**
- 조동사(동사 1)는 2번째 자리, 과거분사(동사 2)는 문장 끝에 와서 문장 가운데를 감쌈 (*Satzklammer*): *Der müde Vater hat ihm nicht zugehört.*
<sub>출처: 4장 · 오른쪽 단</sub>

### `plusquamperfekt` — 과거완료 (Plusquamperfekt)
위치: 3장 · 가운데 단

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 과거 + 과거분사: *ich hatte gekocht, du hattest gekocht, er hatte gekocht* · *ich war gelaufen, du warst gelaufen*
<sub>출처: 3장 · 가운데 단</sub>

**쓰임**
- 과거(*Präteritum*)로 말한 일보다 더 먼저 있었던 일: *Nachdem die Mutter alles aufgeräumt hatte, ging sie müde zu Bett. Sie hatte alle Hausarbeiten alleine gemacht.*
<sub>출처: 3장 · 가운데 단</sub>

### `futur1` — 미래 (Futur I)
위치: 3장 · 가운데 단

**만들기 (공식 박스)**
- *werden*의 현재 + 원형: *ich werde fahren, du wirst fahren, er wird fahren, wir werden fahren, ihr werdet fahren, sie werden fahren*
<sub>출처: 3장 · 가운데 단</sub>

**쓰임**
- 앞으로 일어날 일: *Nächstes Jahr werde ich eine Weltreise machen.*
- 기대하거나 짐작하는 일: *Die kommende Woche wird sicher Klarheit bringen.* · *Er wird wohl kündigen.*
- 하지만 보통은 미래임을 밝히는 시간 표현과 함께 현재를 씀: *Morgen beginnen die Ferien.* · *Nächstes Jahr fahren wir wieder nach Spanien.* · *Er hat kommenden Monat Prüfung.*
<sub>출처: 3장 · 가운데 단</sub>

### `futur2` — 미래완료 (Futur II)
위치: 3장 · 가운데 단

**만들기 (공식 박스)**
- *werden*의 현재 + 과거분사 + *haben* 또는 *sein*: *ich werde gegessen haben, du wirst gegessen haben, er wird gegessen haben* · *ich werde gegangen sein, du wirst gegangen sein*
<sub>출처: 3장 · 가운데 단</sub>

**쓰임**
- 미래의 어느 때에 이미 끝나 있을 일. 드물게 씀
- 예측: *Bald wirst du die Prüfung bestanden haben.*
- 짐작: *Er wird noch zu seiner Freundin gegangen sein.*
<sub>출처: 3장 · 가운데 단</sub>

### `konj1` — 접속법 1식 현재 (Konjunktiv I)
위치: 3장 · 가운데·오른쪽 단

**만들기 (공식 박스)**
- 원형 어간 + 접속법 어미. 모든 꼴에 <em>-e-</em>가 있음: *ich höre, du hörest, er höre, wir hören, ihr höret, sie hören*
- 예외 *sein*: *ich sei, du sei(e)st, er sei, wir seien, ihr seiet, sie seien*
- 직설법과 꼴이 같으면 접속법 2식이나 *würde(n)* + 원형을 씀
<sub>출처: 3장 · 가운데 단</sub>

**쓰임**
- 주로 글에서 씀. 간접화법과 간접의문문: *Der Angeklagte behauptete, er sei unschuldig.* · *Der Richter fragte, ob das auch stimme.*
<sub>출처: 3장 · 오른쪽 단</sub>

### `konj1_perfekt` — 접속법 1식 과거 (Konjunktiv I Perfekt)
위치: 3장 · 오른쪽 단

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 접속법 1식 + 과거분사
<sub>출처: 3장 · 오른쪽 단</sub>

**쓰임**
- 이미 지나간 일을 전할 때: *Der Angeklagte sagte, er habe nichts gestohlen.*
<sub>출처: 3장 · 오른쪽 단</sub>

### `konj1_futur` — 접속법 1식 미래 (Konjunktiv I Futur)
위치: 3장 · 오른쪽 단

**만들기 (공식 박스)**
- *werden*의 접속법 1식 + 원형: *du werdest spielen, er werde spielen*
- 1인칭 단수와 복수 인칭은 대개 <em>würde(n)</em>으로 만듦: *ich würde spielen, wir würden spielen*
<sub>출처: 3장 · 오른쪽 단</sub>

**쓰임**
- 앞으로 일어날 일을 전할 때: *Der Anwalt versicherte, er werde die Unschuld des Angeklagten beweisen.*
<sub>출처: 3장 · 오른쪽 단</sub>

### `konj2` — 접속법 2식 현재 (Konjunktiv II (würde + 원형 포함))
위치: 2장 · 오른쪽 단 / 3장 · 가운데·오른쪽 단

**만들기 (공식 박스)**
- 규칙동사: 직설법 과거와 꼴이 같아서 대신 *würde(n)* + 원형을 씀
- 불규칙동사: 직설법 과거의 어간 + 접속법 1식 어미. *a, o, u*는 대개 *ä, ö, ü*로: *kam – käme, zog – zöge, wusch – wüsche*
- *sein, haben, werden, bleiben, lassen, wissen, kommen, gehen*과 모든 화법조동사는 보통 이 접속법 2식 꼴을 씀
- 다른 동사는 보통 *würde(n)*(*werden*의 접속법 2식) + 원형: *Ich würde am liebsten drei Tage wegfahren.* · *Und dich würde ich gerne mitnehmen.*
<sub>출처: 3장 · 오른쪽 단</sub>

**쓰임**
- 현실이 아닌 일. 바람: *Ich wüsste zu gerne, was in dem Koffer ist.* · 조건: *Wenn er da wäre, würde ich ihm alles erzählen.* · 비교: *Du tust so, als wäre ich noch ein Kind.* 〔3장 · 오른쪽 단〕
- 부탁이나 조언을 아주 공손하게: *Könnten Sie etwas leiser sprechen?* (부탁) · *Du solltest nicht so viel mit ihr schimpfen.* (조언) 〔3장 · 오른쪽 단〕
- 간접화법에서 접속법 1식이 직설법과 같을 때 대신 씀: *Er sagte, sie müssten besser aufpassen.* 〔3장 · 오른쪽 단〕
- 법(Modus) 소개의 예: *Wenn Guillerme doch käme.* (가능성이나 바람) 〔3장 · 가운데 단〕
<sub>출처: 3장 · 가운데·오른쪽 단</sub>

**möchte**
- *möchte*는 원래 *mögen*의 접속법 2식이지만 현재형처럼 씀. 뜻이 다름: *mögen* = 즐겨 하다, *möchten* = 무엇을 원하다(공손하게). 과거로는 *wollen*을 씀
<sub>출처: 2장 · 오른쪽 단</sub>

### `konj2_pqp` — 접속법 2식 과거 (Konjunktiv II Plusquamperfekt)
위치: 3장 · 오른쪽 단

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 접속법 2식 + 과거분사
<sub>출처: 3장 · 오른쪽 단</sub>

**쓰임**
- 과거에 있을 수 있었지만 이루어지지 않은 일: *Wenn du besser aufgepasst hättest, wäre das sicher nicht passiert.*
<sub>출처: 3장 · 오른쪽 단</sub>

### `imperativ` — 명령법 (Imperativ)
위치: 2장 · 가운데 단 / 3장 · 오른쪽 단 / 4장 · 가운데·오른쪽 단

**세 가지 꼴**
- 2인칭 단수: *Komm mal rüber!* · 2인칭 복수: *Fragt bitte erst eure Eltern!* · 존칭(*Sie*): *Rufen Sie mich später an!*
<sub>출처: 3장 · 오른쪽 단</sub>

**만들기 (공식 박스)**
- 2인칭 단수: 현재 *du*형에서 *-st*와 *du*를 뺌 〔3장 · 오른쪽 단〕
- 2인칭 복수: 현재 *ihr*형에서 *ihr*를 뺌 〔3장 · 오른쪽 단〕
- 존칭: 3인칭 복수 꼴. *Sie*는 동사 뒤 〔3장 · 오른쪽 단〕
- 분리동사는 전철이 떨어져 뒤로: *anfangen → fang an!* · 비분리동사는 그대로: *erzählen → erzähl!* 〔2장 · 가운데 단〕
<sub>출처: 2장 · 가운데 단 / 3장 · 오른쪽 단</sub>

**쓰임**
- 부탁·요구·명령·조언. *bitte*나 *mal*을 넣으면 조금 더 부드러움 〔3장 · 오른쪽 단〕
- 원형, 화법조동사, 접속법 2식으로도 명령을 대신할 수 있고, 흔히 훨씬 공손함: *Könntest du mich bitte mit dem Auto abholen?* · *Das Rauchen bitte einstellen!* 〔3장 · 오른쪽 단〕
- 명령문은 동사가 첫 자리: *Hör doch endlich damit auf!* · *Geben Sie mir die Hand! Bitte, sprechen Sie jetzt!* 〔4장 · 가운데·오른쪽 단〕
<sub>출처: 3장 · 오른쪽 단 / 4장 · 가운데·오른쪽 단</sub>

### `partizip2` — 과거분사 (Partizip II)
위치: 2장 · 왼쪽·가운데·오른쪽 단

**만들기 (표)**
- 규칙동사: *ge-* + 어간 + *-t* (*-d, -t, -n, -m* 뒤에서는 *-et*): *fragen – gefragt* · *arbeiten – gearbeitet* · *zeichnen – gezeichnet* 〔2장 · 오른쪽 단〕
- *-ieren* 동사: 어간 + *-t*, *ge-* 없음: *studieren – studiert* · *passieren – passiert* · *sortieren – sortiert* 〔2장 · 오른쪽 단〕
- 불규칙동사: *ge-* + 어간 + *-en*, 모음과 자음이 바뀔 수 있음: *geben – gegeben* · *nehmen – genommen* · *schreiben – geschrieben* 〔2장 · 오른쪽 단〕
- 혼합형: *ge-* + 어간 + *-t*, 어간 모음이 바뀜: *denken – gedacht* · *kennen – gekannt* · *wissen – gewusst* 〔2장 · 오른쪽 단〕
- 규칙동사의 과거분사는 늘 *-(e)t*, 불규칙동사는 *-(e)n*으로 끝남 〔2장 · 왼쪽 단〕
<sub>출처: 2장 · 왼쪽·오른쪽 단</sub>

**전철이 있는 동사 (공식 박스)**
- 비분리 전철: *ge-* 없음: *verstanden, empfunden, missachtet, widersprochen*
- 분리 전철: 전철이 *-ge-* 앞: *abgeräumt, aufgegessen, eingekauft, mitgemacht*
<sub>출처: 2장 · 가운데 단</sub>

**쓰임**
- 현재완료와 수동태를 만들 때 씀 〔2장 · 오른쪽 단〕
- 형용사로도 쓰고, 그때는 형용사처럼 변화함: *Die Polizei sucht nach dem gestohlenen Auto.* 〔2장 · 오른쪽 단〕
- 조동사의 과거분사: *gehabt, gewesen, (ge)worden* 〔2장 · 가운데 단〕
- 주의: 수동태에서 *werden*의 과거분사는 *worden* (*geworden* 아님) 〔2장 · 오른쪽 단〕
<sub>출처: 2장 · 가운데·오른쪽 단</sub>

### `passiv_vorgang` — 동작수동 (Vorgangspassiv)
위치: 2장 · 오른쪽 단

**수동태란**
- 사람이나 사물에게 무엇이 행해지는지를 말함. 행위자를 밝히려면 *von* + 3격: *Das Stück wird von einem jungen Pianisten gespielt.*
- 사물이나 기관은 흔히 *durch* + 4격: *Das Klavier wurde durch Spenden finanziert.*
- 동작수동과 상태수동으로 나뉨
<sub>출처: 2장 · 오른쪽 단</sub>

**만들기 (공식 박스)**
- *werden* + 과거분사. 행위 자체가 중심: *Das Kind wird geimpft.*
- 모든 시제에 쓰고, 상태수동보다 훨씬 자주 씀: 현재 *ich werde geimpft* · 과거 *ich wurde geimpft* · 현재완료 *ich bin geimpft worden*
- 주의: 이때 *werden*의 과거분사는 *worden* (*geworden* 아님)
<sub>출처: 2장 · 오른쪽 단</sub>

### `passiv_zustand` — 상태수동 (Zustandspassiv)
위치: 2장 · 오른쪽 단

**만들기 (공식 박스)**
- *sein* + 과거분사. 행위의 결과가 중심: *Das Kind ist bereits geimpft.*
- 보통 현재와 과거에만 씀: 현재 *ich bin geimpft* · 과거 *ich war geimpft*
<sub>출처: 2장 · 오른쪽 단</sub>

## 2-1. 한 칸에 묶이지 않는 동사 내용 (`pons_extra`)

여러 칸에 걸치거나 칸 밖에 있는 주제입니다. `stem_view`는 표의 공식 박스를 어간별로 다시 묶은 것으로, 프랑스어 사이트의 「어간 + 어미」 규칙 상자와 같은 용도로 쓸 수 있습니다 (내용은 모두 표에 있는 것만).

### `tense_overview` — 시제 한눈에 (Tempus)
위치: 3장 · 왼쪽 단

**여섯 시제**
- 시제(*Tempus*)는 일이 언제 일어나는지, 곧 지금·과거·미래를 보여 줌. 독일어에는 시제가 여섯 개
- 표의 순서 (위 = 과거, 가운데 = 지금, 아래 = 미래): *er hatte gelesen* 과거완료 · *er las* 과거 · *er hat gelesen* 현재완료 · *er liest* 현재 · *er wird gelesen haben* 미래완료 · *er wird lesen* 미래
<sub>출처: 3장 · 왼쪽 단</sub>

### `modus_overview` — 법 한눈에 (Modus)
위치: 3장 · 가운데 단

**세 가지 법**
- 직설법(*Indikativ*, 현실의 꼴), 접속법(*Konjunktiv*, 가능성의 꼴), 명령법(*Imperativ*, 명령의 꼴). 법은 말하는 사람이 자기 말을 어떻게 보는지를 나타냄
- *Guillerme kommt gerade.* 사실 · *Wenn Guillerme doch käme.* 가능성이나 바람 · *Komm jetzt, Guillerme!* 요구나 명령
<sub>출처: 3장 · 가운데 단</sub>

### `stem_view` — 어간 + 어미로 본 동사 (공식 박스 모음)
위치: 2장 · 오른쪽 단 / 3장 · 왼쪽·가운데·오른쪽 단

**원형 어간에서**
- 현재: 동사 어간 + 인칭 어미 〔3장 · 왼쪽 단〕
- 과거 (규칙동사): 원형 어간 + *-t-* + 인칭 어미 〔3장 · 왼쪽 단〕
- 접속법 1식: 원형 어간 + 접속법 어미 (모든 꼴에 *-e-*) 〔3장 · 가운데 단〕
- 명령법: 현재 *du*형에서 *-st*와 *du*를 뺌 · 현재 *ihr*형에서 *ihr*를 뺌 〔3장 · 오른쪽 단〕
<sub>출처: 3장 · 왼쪽·가운데·오른쪽 단</sub>

**과거 어간에서**
- 과거 (불규칙동사): 과거 어간 + 인칭 어미 (1·3인칭 단수는 어미 없음) 〔3장 · 왼쪽 단〕
- 접속법 2식 (불규칙동사): 직설법 과거의 어간 + 접속법 1식 어미, *a, o, u → ä, ö, ü*: *kam – käme* 〔3장 · 오른쪽 단〕
- 규칙동사의 접속법 2식은 직설법 과거와 같아서 *würde(n)* + 원형으로 대신함 〔3장 · 오른쪽 단〕
<sub>출처: 3장 · 왼쪽·오른쪽 단</sub>

**조동사 + 과거분사 또는 원형**
- 현재완료 = *haben/sein* 현재 + 과거분사 · 과거완료 = *haben/sein* 과거 + 과거분사 〔3장 · 왼쪽·가운데 단〕
- 미래 = *werden* 현재 + 원형 · 미래완료 = *werden* 현재 + 과거분사 + *haben/sein* 〔3장 · 가운데 단〕
- 접속법 1식 과거 = *haben/sein* 접속법 1식 + 과거분사 · 접속법 1식 미래 = *werden* 접속법 1식 + 원형 · 접속법 2식 과거 = *haben/sein* 접속법 2식 + 과거분사 〔3장 · 오른쪽 단〕
- 동작수동 = *werden* + 과거분사 · 상태수동 = *sein* + 과거분사 〔2장 · 오른쪽 단〕
<sub>출처: 2장 · 오른쪽 단 / 3장 · 왼쪽·가운데·오른쪽 단</sub>

### `verb_basics` — 동사의 기본: 어간 + 인칭 어미
위치: 2장 · 왼쪽 단

**어간 + 인칭 어미**
- 동사는 늘 어간(*Verbstamm*)과 인칭 어미(*Personalendung*)로 이루어짐. 어간(*leb-en*)은 뜻을, 어미(*leb-en*)는 누가 하는지를 보여 줌
- 여러 인칭이 같은 어미를 가지므로 대명사나 명사가 따로 필요함: *ich wohn-e, du wohn-st, er/sie/es wohn-t, wir wohn-en, ihr wohn-t, sie wohn-en*
- 규칙동사와 불규칙동사로 나누며, 각각 약변화 동사·강변화 동사라고도 부름
- 규칙동사 *lernen*: 현재 *ich lerne* · 과거 *ich lernte* · 현재완료 *ich habe gelernt*
<sub>출처: 2장 · 왼쪽 단</sub>

### `hilfsverben` — 조동사 haben · sein · werden
위치: 2장 · 가운데 단

**활용표**
- *haben, sein, werden*은 불규칙동사
- 현재: *habe, hast, hat, haben, habt, haben* · *bin, bist, ist, sind, seid, sind* · *werde, wirst, wird, werden, werdet, werden*
- 과거: *hatte, hattest, hatte, hatten, hattet, hatten* · *war, warst, war, waren, wart, waren* · *wurde, wurdest, wurde, wurden, wurdet, wurden*
- 과거분사: *gehabt, gewesen, (ge)worden*
<sub>출처: 2장 · 가운데 단</sub>

**쓰임**
- 복합시제(현재완료, 과거완료, 미래)와 수동태를 만듦
- 본동사로도 씀: *Das ist meine Großmutter. Sie hat morgen Geburtstag. Sie wird 70 Jahre.*
<sub>출처: 2장 · 가운데 단</sub>

### `modalverben` — 화법조동사
위치: 2장 · 오른쪽 단

**활용표**
- *sollen*을 빼면 모두 불규칙동사
- 원형 · 현재 · 과거 · 과거분사: *können – kann – konnte – gekonnt* · *mögen – mag – mochte – gemocht* · *wollen – will – wollte – gewollt* · *dürfen – darf – durfte – gedurft* · *sollen – soll – sollte – gesollt* · *müssen – muss – musste – gemusst*
<sub>출처: 2장 · 오른쪽 단</sub>

**쓰임과 뜻**
- 어떤 마음으로 하는지(기꺼이 하는지 아닌지, 스스로 원해서 하는지 아닌지 등)를 나타냄. 원형과 함께 쓰고 원형은 문장 끝: *Ich darf keinen Kaffee trinken.*
- 원형을 빼기도 함: *Möchtest du einen Kaffee?* (*trinken*)
- 능력 *Ich kann arbeiten.* · 내킴 *Ich mag/möchte arbeiten.* · 의지 *Ich will arbeiten.* · 허락 *Ich darf arbeiten.* · 요구 *Ich soll arbeiten.* · 필요 *Ich muss arbeiten.*
<sub>출처: 2장 · 오른쪽 단</sub>

### `reflexive` — 재귀동사
위치: 2장 · 가운데 단

**재귀동사**
- 재귀대명사와 함께 쓸 수 있거나 써야 하는 동사. 재귀대명사는 대개 4격, 3격일 수도 있음: *Ich freue mich auf den Urlaub.* (4격) · *Ich stelle mir den Strand und das Meer vor.* (3격)
- 어느 격인지는 규칙이 없어 함께 외워야 함: *ich freue mich, du freust dich, er freut sich…* / *ich wünsche mir, du wünschst dir, er wünscht sich…*
- 진짜 재귀동사는 재귀대명사를 빼거나 명사로 바꿀 수 없음: *Ich freue mich.* · 가짜 재귀동사는 바꿀 수 있음: *Ich wasche mich.* / *Ich wasche meine Hände.*
<sub>출처: 2장 · 가운데 단</sub>

### `praefixe` — 전철이 있는 동사 (분리·비분리)
위치: 2장 · 가운데 단

**분리 전철**
- 전철로 뜻이 바뀜: *fahren, losfahren, mitfahren, zurückfahren*
- 대부분의 전철은 강세가 있고, 원형과 과거분사가 아니면 동사와 떨어짐: *anfangen → ich fange an, ich fing an, fang an!*
- 주요 분리 전철: *ab-, an-, auf-, aus-, bei-, ein-, her-, hin-, mit-, nach-, vor-, weg-, zu-*
<sub>출처: 2장 · 가운데 단</sub>

**비분리 전철**
- 늘 동사에 붙어 있고 <em>miss-</em>를 빼면 강세가 없음: *erzählen → ich erzähle, ich erzählte, erzähl!*
- 비분리 전철: *be-, emp-, ent-, er-, ge-, miss-, ver-, wider-, zer-*
<sub>출처: 2장 · 가운데 단</sub>

### `verbposition` — 문장 속 동사 자리와 문장 괄호
위치: 4장 · 가운데·오른쪽 단

**동사의 세 자리**
- 문장 종류가 동사 자리를 정함. 평서문·의문사 의문문은 동사 1이 2번째 자리, 명령문·판정 의문문은 동사 1이 첫 자리, 동사 2는 문장 끝
- *Sie kann ihn nicht hören.* · *Warum hast du mir nicht zugehört?* · *Könntest du mich erst mal anhören?*
<sub>출처: 4장 · 오른쪽 단</sub>

**문장 괄호 (Satzklammer)**
- 동사 1과 동사 2가 문장 가운데를 '감쌈'. 동사 1은 늘 인칭 변화한 동사이고 1번째나 2번째 자리
- 동사 2는 늘 문장 끝: 분리 전철, 현재완료·수동태의 과거분사, 화법조동사와 쓰인 원형 등
<sub>출처: 4장 · 오른쪽 단</sub>

**부문장**
- 부문장에서는 동사의 모든 부분이 문장 끝에 오고, 여러 부분이면 인칭 변화한 동사가 맨 끝: *Ich bin froh, dass du mich nicht geweckt hast.* 〔4장 · 가운데·오른쪽 단〕
- 분리동사도 떨어지지 않음: *…weil ich ihn Vokabeln abhöre.* 〔4장 · 오른쪽 단〕
<sub>출처: 4장 · 가운데·오른쪽 단</sub>

## 3. 주의할 점 (`notes`)

- **칸 id는 제안**: 독일어 사이트가 아직 없어서 verb_ids(praesens, praeteritum …)는 이 파일에서 정한 것. 사이트를 만들 때 이름을 바꾸면 이 파일의 키도 같이 바꿀 것
- **시제 표의 순서**: 3장 맨 위 표는 과거완료 → 과거 → 현재완료 → 현재 → 미래완료 → 미래 순으로, 미래완료가 현재와 미래 사이에 놓여 있음 (시간 축: 위가 과거, 아래가 미래). 시제 지도를 만들 때 참고
- **책에 없는 것**: 현재분사(Partizip I), 원형 완료형(gelesen haben), 접속법 2식 미래(würde + 과거분사 + haben/sein), 화법조동사의 완료형(hat … machen müssen), 수동태의 미래·과거완료형은 이 표에 나오지 않음
- **용어**: 표는 Konjunktiv I Perfekt / Konjunktiv I Futur / Konjunktiv II Plusquamperfekt라는 이름을 씀. 한국 교재에서는 흔히 접속법 1식 과거 / 1식 미래 / 2식 과거라고 부르므로 이 파일의 ko 이름도 그렇게 맞춤
- **약변화·강변화**: 표는 regelmäßig/unregelmäßig(규칙/불규칙)를 주로 쓰고 schwach/stark(약/강)를 별칭으로 소개함
- **스캔**: 텍스트층이 없어 OCR(tesseract, 독일어)로 읽고 페이지 이미지와 대조함. 2006년 개정 철자 기준(daß가 아니라 dass, muss)

## 4. 문법표 6쪽 전체 번역 (제목 띠와 공식 박스)

실물 문법표와 같은 순서입니다: 쪽(1~6) → 단(왼쪽·가운데·오른쪽) → 위에서 아래. 각 줄은 `[칸 종류] 독일어 원문 → 한국어` 형식입니다.

- **[큰 단원]** 큰 파란 띠 · **[작은 단원]** 파란 글씨 제목 · **[소제목]** 연한 파란 띠 · **[공식 박스]** 파란 테두리 상자 · **[굵은 제목]** 본문 속 굵은 글씨 · **[표 라벨]** 표 머리 줄 · **[표지]** 1장 표지
- 프랑스어 PONS 표와 달리, 이 표는 큰 파란 띠 아래에 파란 글씨 제목이 오고 그 아래에 연한 띠가 옵니다 (예: Verb → Verb – Tempus → Präsens).

### 표 안에 자주 나오는 독일어

| 독일어 | 한국어 |
|---|---|
| Substantiv / Nomen | 명사 |
| Genus | 성 (Maskulinum 남성 · Femininum 여성 · Neutrum 중성) |
| Numerus | 수 (Singular 단수 · Plural 복수) |
| Kasus | 격 |
| Nominativ · Genitiv · Dativ · Akkusativ | 1격 · 2격 · 3격 · 4격 |
| Deklination / deklinieren | 격변화 / 격변화하다 |
| Artikel (bestimmt / unbestimmt) | 관사 (정관사 / 부정관사) |
| Begleiter | 명사 앞에서 명사를 꾸미는 말 (관사 자리에 오는 대명사) |
| Stellvertreter | 명사를 대신하는 말 (대명사로 쓰임) |
| Verbstamm · Stammvokal | 동사 어간 · 어간 모음 |
| Personalendung | 인칭 어미 |
| Infinitiv | 원형 (부정형) |
| Partizip II | 과거분사 |
| regelmäßig / unregelmäßig (schwach / stark) | 규칙 / 불규칙 (약변화 / 강변화) |
| Hilfsverb · Modalverb · Vollverb | 조동사 · 화법조동사 · 본동사 |
| Präfix (trennbar / untrennbar) | 전철 (분리 / 비분리) |
| Tempus · Modus | 시제 · 법 |
| Indikativ · Konjunktiv · Imperativ | 직설법 · 접속법 · 명령법 |
| Passiv (Vorgangs- / Zustandspassiv) | 수동태 (동작수동 / 상태수동) |
| Hauptsatz · Nebensatz · Satzglied | 주문장 · 부문장 · 문장 성분 |
| Satzklammer | 문장 괄호 (동사 1과 동사 2가 문장을 감싸는 틀) |
| Aussagesatz · W-Frage · Ja/Nein-Frage · Aufforderungssatz | 평서문 · 의문사 의문문 · 판정 의문문 · 명령문 |
| Komparation (Positiv · Komparativ · Superlativ) | 비교 변화 (원급 · 비교급 · 최상급) |
| starke · schwache · gemischte Deklination | 강변화 · 약변화 · 혼합변화 (형용사) |
| Umlaut | 변모음 (ä, ö, ü) |
| Achtung! · z.B. · usw. / u.a. · vgl. | 주의! · 예를 들어 · 등 · 참고 |

### 1장 · 표지 · 명사 (Substantiv)

#### 왼쪽 단

- **[표지]** Auf einen Blick · Grammatik · DEUTSCH → 한눈에 보는 문법 · 독일어
  - 설명: 1장 위쪽 절반은 표지. 붉은 원 안: Topaktuell – entspricht den geltenden Rechtschreibregeln (최신판 – 현행 맞춤법 규칙에 맞음)
- **[큰 단원]** Substantiv / Nomen → 명사
  - 설명: 구체명사·추상명사·고유명사. 늘 대문자로 시작하고 성·수·격을 가짐
- **[작은 단원]** Genus des Substantivs → 명사의 성
  - 설명: 사람 말고는 성을 정하기 어려움. das Mädchen처럼 자연의 성과 문법의 성이 다를 수 있음
- **[표 라벨]** männliche Person / weibliche Person → 남자 / 여자
- **[소제목]** Genusbestimmung mithilfe von Suffixen → 접미사로 성 알아보기
  - 설명: 여성: -heit, -keit, -ung, -schaft, -tät, -tion, -ei, -ur, -in, -frau · 중성: -chen, -lein, -nis, -ment, -um, -tum, 명사가 된 동사·형용사
- **[작은 단원]** Numerus des Substantivs → 명사의 수
  - 설명: 단수로만 쓰는 명사(추상명사, 물질명사, 집합명사 등)와 복수로만 쓰는 명사(die Eltern, die Ferien 등)

#### 가운데 단

- **[소제목]** Typen der Pluralbildung → 복수형 만드는 유형
  - 설명: Typ 1 -e · Typ 2 -(e)n · Typ 3 어미 없음 · Typ 4 -er · Typ 5 -s (자주 변모음)
- **[작은 단원]** Kasus des Substantivs → 명사의 격
  - 설명: 네 격과 묻는 말: Wer?/Was? (1격) · Wen?/Was? (4격) · Wem? (3격) · Wessen? (2격)

#### 오른쪽 단

- **[소제목]** Typen der Deklination im Singular → 단수 격변화 유형
  - 설명: Typ 1 (대부분의 남성·중성, 2격 -s/-es) · Typ 2 = n-변화 (사람·동물 남성명사) · Typ 2.1 (der Name, das Herz) · Typ 3 (여성, 어미 없음)
- **[소제목]** Typen der Deklination im Plural → 복수 격변화 유형
  - 설명: 3격 복수는 늘 -n. Typ 5만 모든 격에 -s

### 2장 · 동사의 기본 · 재귀동사 · 전철 · 조동사 · 화법조동사 · 수동태 · 과거분사 (Verb)

#### 왼쪽 단

- **[큰 단원]** Verb → 동사
  - 설명: 어간 + 인칭 어미
- **[작은 단원]** Regelmäßige Verben → 규칙동사
  - 설명: 과거 -te-, 과거분사 -(e)t
- **[작은 단원]** Unregelmäßige Verben → 불규칙동사
  - 설명: ABC · ABB · ABA 모음 유형, 혼합 동사, 아주 불규칙한 동사

#### 가운데 단

- **[작은 단원]** Reflexive Verben → 재귀동사
- **[작은 단원]** Verben mit Präfixen → 전철이 있는 동사
- **[소제목]** Trennbare Präfixe → 분리 전철
- **[소제목]** Untrennbare Präfixe → 비분리 전철
- **[공식 박스]** Bildung des Partizips II bei Verben mit untrennbarem / trennbarem Präfix → 전철 동사의 과거분사 만들기
  - 설명: 비분리: ge- 없음 · 분리: 전철 + ge-
- **[작은 단원]** Hilfsverben → 조동사
  - 설명: haben · sein · werden 활용표

#### 오른쪽 단

- **[작은 단원]** Modalverben → 화법조동사
- **[소제목]** Bedeutung der Modalverben → 화법조동사의 뜻
  - 설명: 능력 · 내킴 · 의지 · 허락 · 요구 · 필요
- **[작은 단원]** Passiv → 수동태
- **[공식 박스]** werden + Partizip II → werden + 과거분사 (동작수동)
- **[공식 박스]** Achtung! Das Partizip II von werden ist im Passiv worden (nicht: geworden). → 주의! 수동태에서 werden의 과거분사는 worden
- **[공식 박스]** sein + Partizip II → sein + 과거분사 (상태수동)
- **[작은 단원]** Partizip II → 과거분사
- **[표 라벨]** regelmäßige Verben: ge- + Verbstamm + -t (-et nach -d, -t und -n, -m) → 규칙동사: ge- + 어간 + -t (-d, -t, -n, -m 뒤에서는 -et)
- **[표 라벨]** Verben auf -ieren: Verbstamm + -t (ohne ge-) → -ieren 동사: 어간 + -t (ge- 없음)
- **[표 라벨]** unregelmäßige Verben: ge- + Verbstamm + -en → 불규칙동사: ge- + 어간 + -en (모음·자음이 바뀔 수 있음)
- **[표 라벨]** Mischformen: ge- + Verbstamm + -t und Änderung des Stammvokals → 혼합형: ge- + 어간 + -t, 어간 모음이 바뀜

### 3장 · 동사의 시제와 법 (Verb – Tempus · Verb – Modus)

#### 왼쪽 단

- **[작은 단원]** Verb – Tempus → 동사 – 시제
  - 설명: 여섯 시제의 표
- **[소제목]** Präsens → 현재
- **[공식 박스]** Verbstamm + Personalendung → 동사 어간 + 인칭 어미
- **[굵은 제목]** Lautliche Besonderheiten → 발음 때문에 생기는 특이점
- **[굵은 제목]** Stammvokalwechsel → 어간 모음 바뀜
  - 설명: 일부 불규칙동사의 2·3인칭 단수
- **[소제목]** Perfekt → 현재완료
- **[공식 박스]** Präsens von haben oder sein + Partizip II → haben 또는 sein의 현재 + 과거분사
- **[굵은 제목]** haben oder sein? → haben이냐 sein이냐
- **[소제목]** Präteritum → 과거
- **[공식 박스]** regelmäßiges Verb: Infinitivstamm + -t- + Personalendung → 규칙동사: 원형 어간 + -t- + 인칭 어미
- **[공식 박스]** unregelmäßiges Verb: Präteritumstamm + Personalendung → 불규칙동사: 과거 어간 + 인칭 어미
  - 설명: 1·3인칭 단수는 어미 없음, 어간 모음은 거의 늘 바뀜

#### 가운데 단

- **[소제목]** Plusquamperfekt → 과거완료
- **[공식 박스]** Präteritum von haben oder sein + Partizip II → haben 또는 sein의 과거 + 과거분사
- **[소제목]** Futur I → 미래
- **[공식 박스]** Präsens von werden + Infinitiv → werden의 현재 + 원형
- **[소제목]** Futur II → 미래완료
- **[공식 박스]** Präsens von werden + Partizip II + haben oder sein → werden의 현재 + 과거분사 + haben 또는 sein
- **[작은 단원]** Verb – Modus → 동사 – 법
  - 설명: 직설법 · 접속법 · 명령법
- **[소제목]** Konjunktiv I → 접속법 1식
- **[공식 박스]** Infinitivstamm + Konjunktivendungen → 원형 어간 + 접속법 어미
  - 설명: 모든 꼴에 -e-. 예외 sein
- **[공식 박스]** Bei Formen, die sich nicht vom Indikativ unterscheiden, benutzt man den Konjunktiv II bzw. würde(n) + Infinitiv. → 직설법과 꼴이 같으면 접속법 2식이나 würde(n) + 원형을 씀

#### 오른쪽 단

- **[공식 박스]** Konjunktiv I von haben oder sein + Partizip II → haben 또는 sein의 접속법 1식 + 과거분사 (접속법 1식 과거)
- **[공식 박스]** Konjunktiv I von werden + Infinitiv → werden의 접속법 1식 + 원형 (접속법 1식 미래)
- **[소제목]** Konjunktiv II → 접속법 2식
- **[공식 박스]** regelmäßige Verben: = Indikativform des Präteritums → stattdessen: würde(n) + Infinitiv → 규칙동사: 직설법 과거와 같은 꼴 → 대신 würde(n) + 원형
- **[공식 박스]** unregelmäßige Verben: Verbstamm des Präteritums Indikativ + Endungen des Konjunktivs I → 불규칙동사: 직설법 과거의 어간 + 접속법 1식 어미
  - 설명: a, o, u → ä, ö, ü
- **[공식 박스]** Konjunktiv II von haben oder sein + Partizip II → haben 또는 sein의 접속법 2식 + 과거분사 (접속법 2식 과거)
- **[소제목]** Imperativ → 명령법
- **[공식 박스]** 2. Person Singular: wie 2. Person Präsens ohne -st und ohne du; 2. Person Plural: wie 2. Person Plural ohne ihr; Höfliche Anredeform: wie 3. Person Plural. Sie steht nach dem Verb. → 2인칭 단수: 현재 du형에서 -st와 du를 뺌 · 2인칭 복수: ihr형에서 ihr를 뺌 · 존칭: 3인칭 복수 꼴, Sie는 동사 뒤

### 4장 · 전치사 · 접속사 · 문장의 종류와 어순 (Präposition · Konjunktion · Satz)

#### 왼쪽 단

- **[큰 단원]** Präposition → 전치사
  - 설명: 뒤에 오는 말의 격을 정함
- **[소제목]** Präpositionen mit Akkusativ → 4격 전치사
  - 설명: bis, durch, für, gegen, ohne, um, entlang (뒤에 옴)
- **[소제목]** Präpositionen mit Dativ → 3격 전치사
  - 설명: ab, aus, außer, bei, gegenüber, mit, nach, seit, von, zu
- **[소제목]** Wechselpräpositionen mit Akkusativ oder Dativ → 3·4격 전치사
  - 설명: an, auf, hinter, in, neben, über, unter, vor, zwischen
- **[공식 박스]** Wechselpräpositionen haben eine lokale Bedeutung: wo? → Dativ, wohin? → Akkusativ → 3·4격 전치사는 장소의 뜻: wo?(어디에) → 3격, wohin?(어디로) → 4격
- **[표 라벨]** Kurzformen → 전치사 + 관사 줄임꼴
  - 설명: am, ans, aufs, beim, im, ins, vom, zum, zur
- **[소제목]** Präpositionen mit Genitiv → 2격 전치사
  - 설명: außerhalb, innerhalb, statt, trotz, während, wegen. 일상어에서는 흔히 3격으로
- **[큰 단원]** Konjunktion → 접속사
- **[소제목]** Konjunktionen, die Wörter und Wortgruppen verbinden → 단어와 어구를 잇는 접속사
  - 설명: und, sowie, sowohl … als auch, weder … noch 등

#### 가운데 단

- **[소제목]** Konjunktionen, die Hauptsätze verbinden → 주문장끼리 잇는 접속사
  - 설명: aber, denn, oder, und, sondern, doch. 어순 그대로
- **[소제목]** Konjunktionen, die Haupt- und Nebensätze verbinden → 주문장과 부문장을 잇는 접속사
  - 설명: als, bevor, dass, weil, wenn 등. 부문장의 동사는 늘 문장 끝
- **[소제목]** Adverbien als Konjunktionen → 접속사처럼 쓰는 부사
  - 설명: darum, außerdem, trotzdem 등. 동사가 부사 바로 뒤
- **[큰 단원]** Satzarten und Positionen im Satz → 문장의 종류와 문장 속 자리
- **[작은 단원]** Satzarten → 문장의 종류
  - 설명: 주문장과 부문장
- **[소제목]** Hauptsatzarten → 주문장의 종류
  - 설명: 평서문 · 의문문(의문사 의문문, 판정 의문문) · 명령문
- **[소제목]** Nebensatzarten → 부문장의 종류
  - 설명: 접속사 부문장 · 관계문 · 의문사 부문장(간접의문) · zu + 원형

#### 오른쪽 단

- **[작은 단원]** Positionen des Verbs im Satz → 문장 속 동사 자리
  - 설명: 세 자리: 동사 1 · 가운데 · 동사 2
- **[소제목]** A. Aussagesatz, W-Frage → A. 평서문, 의문사 의문문
  - 설명: 동사 1이 2번째 자리
- **[소제목]** B. Aufforderungssatz, Ja/Nein-Frage → B. 명령문, 판정 의문문
  - 설명: 동사 1이 첫 자리
- **[공식 박스]** Satzklammer → 문장 괄호
  - 설명: 동사 1과 동사 2가 가운데 성분을 감쌈. 동사 2: 분리 전철, 과거분사, 화법조동사와 쓰인 원형
- **[소제목]** C. Nebensatz → C. 부문장
- **[공식 박스]** Im Nebensatz stehen alle Verbteile am Satzende. Bei mehrteiligen Verben bildet immer das konjugierte Verb den Schluss. → 부문장에서는 동사의 모든 부분이 끝에. 여러 부분이면 인칭 변화한 동사가 맨 끝
- **[작은 단원]** Negation im Satz → 문장의 부정
  - 설명: nicht는 대개 문장 끝. 예외: 2부분 동사, sein + 부사/명사/형용사, 방법 부사, 전치사 목적어 앞
- **[작은 단원]** Stellung der Nebensätze → 부문장의 자리
  - 설명: 보통 주문장 뒤. 앞에 오면 주문장 동사가 첫 자리. 끼어들기도 함

### 5장 · 관사 · 대명사 (Artikel · Pronomen)

#### 왼쪽 단

- **[큰 단원]** Artikel → 관사
- **[소제목]** Deklination des bestimmten Artikels → 정관사 격변화
  - 설명: der, die, das …
- **[소제목]** Deklination des unbestimmten Artikels → 부정관사 격변화
  - 설명: ein, eine … (복수 없음. kein은 복수 있음)
- **[큰 단원]** Pronomen → 대명사
  - 설명: 명사 앞 Begleiter와 명사 대신 Stellvertreter
- **[작은 단원]** Personalpronomen → 인칭대명사
  - 설명: 존칭 Sie는 3인칭 복수, 늘 대문자
- **[소제목]** Deklination der Personalpronomen → 인칭대명사 격변화
- **[작은 단원]** Reflexivpronomen → 재귀대명사
  - 설명: 진짜·가짜 재귀대명사. 3격과 4격만
- **[소제목]** Deklination der Reflexivpronomen → 재귀대명사 격변화
  - 설명: 3인칭은 sich

#### 가운데 단

- **[작은 단원]** Possessivpronomen → 소유대명사
- **[소제목]** Possessiva als Begleiter und Pronomen → 명사 앞과 명사 대신의 소유사
- **[소제목]** Deklination des Possessivpronomens → 소유대명사 격변화
  - 설명: 명사 앞에서는 kein처럼
- **[작은 단원]** Demonstrativpronomen → 지시대명사
- **[소제목]** Deklination von dieser und jener → dieser와 jener 격변화
  - 설명: 정관사처럼

#### 오른쪽 단

- **[소제목]** Deklination von der, die, das → 지시대명사 der, die, das 격변화
  - 설명: 명사 대신일 때 2격과 3격 복수가 다름 (dessen, deren, denen)
- **[작은 단원]** Relativpronomen → 관계대명사
  - 설명: 성·수는 선행사, 격은 관계문의 동사가 정함
- **[소제목]** Deklination der Relativpronomen → 관계대명사 격변화
  - 설명: der/welcher …. 보통 der, die, das
- **[작은 단원]** Interrogativpronomen → 의문대명사
- **[소제목]** Deklination von wer und was → wer와 was 격변화
- **[소제목]** Deklination von welcher → welcher 격변화
  - 설명: was für ein?은 성질을 물음

### 6장 · 형용사 · 부사 (Adjektiv · Adverb)

#### 왼쪽 단

- **[큰 단원]** Adjektiv → 형용사
  - 설명: 명사 뒤(서술적, 어미 없음) · 명사 앞(부가적, 어미 있음)
- **[작은 단원]** Deklination des Adjektivs → 형용사 격변화
  - 설명: 강변화 · 약변화 · 혼합변화
- **[소제목]** ohne Artikel – starke Deklination → 관사 없이 – 강변화
- **[공식 박스]** Der letzte Buchstabe entspricht immer dem letzten Buchstaben des jeweiligen bestimmten Artikels → 형용사 끝 글자는 늘 그 정관사의 끝 글자와 같음
  - 설명: der feine Zucker – feiner Zucker
- **[소제목]** mit bestimmtem Artikel – schwache Deklination → 정관사와 함께 – 약변화
- **[소제목]** mit unbestimmtem Artikel – gemischte Deklination → 부정관사와 함께 – 혼합변화

#### 가운데 단

- **[소제목]** Besonderheiten bei der Deklination → 격변화의 특이점
  - 설명: -el, -en, -er 형용사의 e 탈락, hoch → hohe, 변하지 않는 형용사 (rosa, lila, 수사, Berliner)
- **[작은 단원]** Komparation des Adjektivs → 형용사의 비교 변화
  - 설명: 원급 · 비교급 · 최상급, so … wie / -er als
- **[소제목]** Deklination des Komparativs → 비교급·최상급의 격변화
- **[소제목]** Besonderheiten bei den Komparationsformen → 비교 변화의 특이점
  - 설명: 최상급 -esten, e 탈락, 변모음
- **[소제목]** Unregelmäßige Komparationsformen → 불규칙 비교 변화
  - 설명: gut – besser – am besten 등

#### 오른쪽 단

- **[큰 단원]** Adverb → 부사
  - 설명: 격변화도 비교 변화도 하지 않음. 장소 · 방향 · 시간 · 양태 · 접속 · 대명부사
- **[표 라벨]** Positiv · Komparativ · Superlativ → 원급 · 비교급 · 최상급
  - 설명: 비교 변화를 하는 예외 부사: bald – eher – am ehesten, gern – lieber – am liebsten, oft – häufiger – am häufigsten, sehr – mehr – am meisten
- **[표 라벨]** Adverb · Präposition · Pronominaladverb → 부사 · 전치사 · 대명부사
  - 설명: da/hier/wo + 전치사: daran, damit, hiermit, wobei. 모음이 이어지면 -r-를 넣음. 사람에게는 전치사 + 의문사 (Über wen …?)
