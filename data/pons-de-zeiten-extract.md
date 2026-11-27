# PONS 독일어 시제표 (Zeiten) 추출 자료

> 독일어 시제 사이트를 만들거나 내용을 검증할 때 참고하는 자료입니다. 앞서 만든 Grammatik 표 자료(`pons-de-tense-notes.json`, `pons-de-extract.md`)와 같은 구조·같은 id를 씁니다.
> 짝 파일 `pons-de-zeiten-notes.json`은 같은 내용을 사이트에서 바로 쓸 수 있는 데이터로 담고 있습니다.

## 0. 개요

- **원자료**: PONS 「Auf einen Blick – Zeiten DEUTSCH」. 독일어로 쓰인 독일어 시제 요약표 (접이식, 각 쪽에 쪽 번호 인쇄).
- **얻은 방법**: 사용자가 찍은 사진 5장(인쇄 쪽 1~5)을 독일어 OCR로 읽고, 휘거나 반사된 부분은 확대한 사진과 대조해 판독.
- **받은 범위**: 1~5쪽. 저자·연도·ISBN은 받은 쪽에 없습니다 (3장 참고).
- **이 파일에 담긴 것**
  1. 시제·법·수동태·분사를 칸(id)별로 한국어로 요약하고 예문을 인용한 것 → 2장
  2. 한 칸에 묶이지 않는 내용 (어간 + 어미 모음, 기본형, 조동사·화법조동사 표, 전철, 어순 표) → 2-1장
  3. 주의할 점과 Grammatik 표와의 대조 → 3장, 3-1장
  4. 5쪽 전체의 제목 띠와 공식 박스를 독일어 → 한국어로 옮긴 것 → 4장
- **주의**: 원문을 그대로 옮긴 것이 아니라 한국어로 번역·요약한 것. 예문은 표에서 그대로 인용함. 공개 사이트에 쓸 때는 출처 표기를 유지할 것.

## 1. 사이트에서 쓰는 방식

- 데이터 구조: `{ id: { src, p, blocks: [ { h, p, items, item_p } ] } }`. Grammatik 표 자료와 같습니다.
- **위치 표기**: 이 표는 쪽 번호가 인쇄되어 있어서 `2쪽 · 가운데 단`처럼 **인쇄된 쪽 번호와 세로 단**으로 적었습니다 (사진 순서가 아님). 본문 문장 안에는 위치를 넣지 않았습니다.
- **출처 표기 틀**: `출처: PONS 『Auf einen Blick – Zeiten Deutsch』, {p}` → 예: 출처: PONS 『Auf einen Blick – Zeiten Deutsch』, 5쪽 · 가운데 단
- 상자에 블록 하나를 쓰면 그 블록의 `p`를, 항목 하나만 쓰면 그 항목의 `item_p`를 씁니다. 이 MD에서는 각 블록 아래 `출처:` 줄이 블록의 `p`이고, 한 블록 안에서 위치가 갈리면 항목 끝에 〔 〕로 따로 적었습니다.
- **[ ]**: 사진 반사로 가려진 글자를 문맥으로 채운 것입니다. 사이트에 인용하기 전에 실물로 확인하세요.

| id | 한국어 | 표의 이름 | 분류 | Grammatik 표에도 있음 | 위치 |
|---|---|---|---|---|---|
| `praesens` | 현재 | Präsens | 직설법 · 단순시제 | 예 | 1쪽 · 왼쪽·가운데·오른쪽 단 |
| `praeteritum` | 과거 | Präteritum | 직설법 · 단순시제 · 주로 글말 | 예 | 3쪽 · 왼쪽 단 |
| `perfekt` | 현재완료 | Perfekt | 직설법 · 복합시제 · 일상의 말과 글 | 예 | 2쪽 · 가운데·오른쪽 단 |
| `plusquamperfekt` | 과거완료 | Plusquamperfekt | 직설법 · 복합시제 | 예 | 2쪽 · 오른쪽 단 |
| `futur1` | 미래 | Futur I | 직설법 · 복합시제 | 예 | 4쪽 · 왼쪽 단 |
| `futur2` | 미래완료 | Futur II (Futurperfekt) | 직설법 · 복합시제 · 말할 때는 아주 드묾 | 예 | 4쪽 · 왼쪽·가운데 단 |
| `konj1` | 접속법 1식 현재 | Konjunktiv I – Gegenwart | 접속법 1식 · 단순형 · 간접화법 | 예 | 5쪽 · 가운데 단 |
| `konj1_perfekt` | 접속법 1식 과거 | Konjunktiv I – Vergangenheit | 접속법 1식 · 복합형 | 예 | 5쪽 · 가운데 단 |
| `konj1_futur` | 접속법 1식 미래 | Konjunktiv I – Zukunft | 접속법 1식 · 복합형 | 예 | 5쪽 · 가운데 단 |
| `konj2` | 접속법 2식 현재 | Konjunktiv II – Gegenwart (würde + 원형 포함) | 접속법 2식 · 단순형 또는 würde형 | 예 | 5쪽 · 가운데·오른쪽 단 |
| `konj2_pqp` | 접속법 2식 과거 | Konjunktiv II – Vergangenheit | 접속법 2식 · 복합형 | 예 | 5쪽 · 오른쪽 단 |
| `imperativ` | 명령법 | Imperativ | 명령법 · 현재에만 | 예 | 3쪽 · 가운데·오른쪽 단 / 5쪽 · 왼쪽 단 |
| `partizip2` | 과거분사 | Partizip II (Partizip Perfekt) | 분사 · 3번째 기본형 | 예 | 2쪽 · 왼쪽 단 |
| `passiv_vorgang` | 동작수동 | Vorgangspassiv (werden-Passiv) | 수동태 · werden + 과거분사 | 예 | 4쪽 · 가운데·오른쪽 단 |
| `passiv_zustand` | 상태수동 | Zustandspassiv (sein-Passiv) | 수동태 · sein + 과거분사 | 예 | 4쪽 · 오른쪽 단 |
| `passiv_bekommen` | bekommen 수동 | bekommen-Passiv (Dativ-Passiv) | 수동태 · bekommen + 과거분사 · 입말 | 아니오 (새 id) | 4쪽 · 오른쪽 단 |

## 2. 칸별 PONS 설명 (`pons_zeiten_by_id`)

### `praesens` — 현재 (Präsens)
위치: 1쪽 · 왼쪽·가운데·오른쪽 단

**만들기 (공식 박스)**
- 현재 어간(*Präsensstamm* = 원형에서 어미 *-(e)n*을 뗀 것) + 인칭 어미
- *kommen*: *ich komm-e, du komm-st, er/sie/es komm-t, wir komm-en, ihr komm-t, sie/Sie komm-en*
<sub>출처: 1쪽 · 왼쪽 단</sub>

**발음 때문에 글자를 넣거나 빼는 경우 (*Besonderheiten*)**
- e 넣기(*e-Einschub*): 어간이 *-d, -t*로 끝나거나, *-l, -m, -n, -r*이 아닌 자음 + *-m*·*-n*으로 끝나면 2인칭 단수·복수(*du*형·*ihr*형) 어미 앞에 *-e*를 넣음: *du arbeitest – ihr arbeitet; du redest – ihr redet; du atmest – ihr atmet; du rechnest – ihr rechnet*
- 예외: *du*형·*er/sie/es*형에서 모음이 바뀌는 동사는 e를 넣지 않음: *laden: du lädst, er/sie/es lädt; halten: du hältst, er/sie/es hält; treten: du trittst, er/sie/es tritt*
- s 빠짐(*s-Ausfall*): 어간이 *-(s)s, -ß, -x, -tz, -z*로 끝나면 *du*형 어미는 *-t*: *du reist, du heißt, du mixt, du sitzt, du tanzt*
- e 빠짐, *ich*형: *-eln* 동사는 *-l* 앞에 *e*가 없음: *radeln: ich radle, segeln: ich segle*
- e 빠짐, *wir*형·*sie*형: *-eln, -ern* 동사는 어미의 *-e*가 빠짐: *wandern: wir/sie wandern, segeln: wir/sie segeln*
- e 빠짐 가능, *ich*형: *-ern* 동사는 *-r* 앞의 *e*를 넣어도 됨: *wandern: ich wand(e)re, bedauern: ich bedau(e)re*
- 주의: *tun: ich tu(e), du tust, er/sie/es tut, wir tun, ihr tut, sie/Sie tun*
<sub>출처: 1쪽 · 왼쪽 단</sub>

**어간 모음이 바뀌는 동사 (*Verben mit Vokalwechsel*)**
- 강변화(불규칙) 동사의 일부. 현재 *du*형과 *er/sie/es*형에서 어간 모음이 바뀜
- *a → ä*: *fahren: Wir fahren mit dem Bus. Fährst du mit uns?*
- *au → äu*: *laufen: Ich laufe noch schnell zum Bäcker. Maria läuft zum Supermarkt.*
- *e → i(e)*: *stehlen: Ich stehle nicht. Aber Marie stiehlt Blumen aus fremden Gärten.* · *nehmen: Ich nehme heute den Bus. Nimmst du auch den Bus?* · *treten: Ich trete immer nur den Ball, aber du trittst nicht den Ball, sondern mich!*
- 그 밖에 자주 쓰는 동사: *essen, fallen, geben, halten, helfen, lassen, lesen, schlafen, sehen, sprechen, tragen, waschen*
- 주의: *wissen: ich weiß, du weißt, er/sie/es weiß, wir wissen, ihr wisst, sie wissen*
<sub>출처: 1쪽 · 가운데 단</sub>

**쓰임**
- 일반적인 말과 사실: *Die Sommermonate heißen Juni, Juli und August.* · *Die BRD ist eine parlamentarische Demokratie.* · *Viele Babys wachen schon um 5.00 Uhr auf.*
- 지금의 일: 말하는 때에 일어나거나 (a) 되풀이되는 일 (b). 과거 (c)나 미래 (d)까지 이어질 수 있음: (a) *Was liest du denn da?* (b) *Gemüse kaufe ich stets auf dem Markt ein.* (c) *Es regnet schon seit Stunden.* (d) *Heute fange ich mit meiner neuen Diät an.*
- 앞으로의 일: 흔히 시간 표현과 함께: *Ich schreibe dir morgen eine E-Mail.* · *Der Bundestag beschließt bestimmt wieder, die Steuern zu erhöhen.* · *Am Samstag will ich mir ein Fahrrad kaufen.*
- 지난 일 (역사적 현재, *historisches Präsens*): 지난 일을 생생하게 들려줄 때. 주로 말할 때: *Ich liege endlich am Strand und will mich entspannen. – Da kommt ein Verkäufer und bietet Melonen an.*
- 소설, 전기 같은 이야기하는 글에서도 서술 시제로 자주 씀: *Als es schließlich Nacht wird, schleicht die kleine Hexe in ihr Haus.* · *Rudolf Diesel wird am 18.03.1858 in Paris geboren.* · *Dann endet der zweite Weltkrieg, und m[ein] Großvater beschließt, nicht nach Deutsch[la]nd zurückzukehren.*
<sub>출처: 1쪽 · 오른쪽 단</sub>

**시간 표현으로 때를 밝힘 (*Präzisierung durch Zeitangaben*)**
- 현재는 아주 자주 시간 표현과 함께 씀. 시간 표현이 지금·미래·과거 중 언제인지를 밝힘
- 지금 (*gerade, jetzt, im Moment*): *Ich kann jetzt nicht telefonieren, ich koche gerade.* · *Karl liegt im Moment im Krankenhaus.* · *Sarah nimmt zurzeit an einem Tanzkurs teil.*
- 미래 (*morgen, bald, nächstes Jahr*): *Morgen gehe ich mit Jan ins Kino.* · *Wo findet im Jahr 2022 die Fußball-WM statt?* · *Mario tritt nächstes Jahr eine Stelle in Berlin an.*
- 과거 (*gestern, letzte Woche, vorhin*): *Letzte Woche bist du noch in Australien, und heute stehst du hier in Berlin auf dem Ku'damm. Wahnsinn!* · *Gestern Abend um zehn Uhr will ich schlafen gehen. Da klingelt es an der Tür.*
<sub>출처: 1쪽 · 오른쪽 단</sub>

### `praeteritum` — 과거 (Präteritum)
위치: 3쪽 · 왼쪽 단

**소개**
- 주로 글을 쓸 때 씀. 만들 때는 약변화 동사와 강변화 동사의 구분이 중요
<sub>출처: 3쪽 · 왼쪽 단</sub>

**약변화 동사 (공식 박스)**
- 현재 어간 + *-t-* + 인칭 어미 *-e, -est, -e, -en, -et, -en*: *ich lebte, du lebtest, er/sie/es lebte, wir lebten, ihr lebtet, sie/Sie lebten*
- e 넣기는 현재와 같은 규칙: *ich beendete, du beendetest, er/sie/es beendete, wir beendeten, ihr beendetet, sie/Sie beendeten*
<sub>출처: 3쪽 · 왼쪽 단</sub>

**강변화 동사 (공식 박스)**
- 과거 어간 + 인칭 어미 *–, -st, –, -en, -t, -en*. 과거 어간은 사전이나 동사표에서 2번째 기본형으로 찾음
- *ich*형과 *er/sie/es*형은 어미가 없고, 나머지 어미는 현재와 같음
- *fahren* → 과거 어간 *fuhr*: *ich fuhr, du fuhrst, er/sie/es fuhr, wir fuhren, ihr fuhrt, sie/Sie fuhren*
- *bleiben* → 과거 어간 *blieb*: *ich blieb, du bliebst, er/sie/es blieb, wir blieben, ihr bliebt, sie/Sie blieben*
<sub>출처: 3쪽 · 왼쪽 단</sub>

**혼합 동사 (공식 박스)**
- 과거 어간 + *-t-* + 인칭 어미 *-e, -est, -e, -en, -et, -en*
- *bringen* → 과거 어간 *brach*: *ich brachte, du brachtest, er/sie/es brachte, wir brachten, ihr brachtet, sie/Sie brachten*
- 마찬가지: *brennen → brannte, denken → dachte, kennen → kannte, nennen → nannte, rennen → rannte, senden → sandte*
<sub>출처: 3쪽 · 왼쪽 단</sub>

**쓰임**
- 사실을 적는 글(*Sachtexte*): 회의록, 공식 편지, 신문 기사: *An der Besprechung nahmen fünf Kollegen teil.* · *Vor zwei Wochen beschwe[r]ten wir uns schriftlich.*
- 이야기하는 글: 소설, 동화: *Dann küsste die Prinzessin den Frosch.* · *Im März 2003 war Marcel ein unbekannter Mann. Dies sollte sich bald ändern. Er hatte einen Plan …*
- 격식 있는 자리에서 말할 때: 설문, 면접, 연설: *Wie lange blieben Sie 2005 in Berlin?* · *Erst arbeitete ich im Einkauf, dann versetzte man mich in die Marketingabteilung.* · *Unser Jubilar kam schon mit 5 Jahren in die Schule.*
- 참고 상자: 조동사 *sein*, *haben*과 화법조동사는 말할 때도 현재완료보다 과거를 더 자주 씀: *Ich war gestern beim Arzt.* (드물게: *Ich bin gestern beim Arzt gewesen.*) · *Martin musste/wollte/konnte/sollte/durfte noch einkaufen.* (드물게: *Martin hat noch einkaufen müssen/wollen/können/sollen/dürfen.*)
<sub>출처: 3쪽 · 왼쪽 단</sub>

### `perfekt` — 현재완료 (Perfekt)
위치: 2쪽 · 가운데·오른쪽 단

**소개**
- 과거를 말하는 시제는 셋: 과거, 그리고 합성형인 현재완료와 과거완료
- 현재완료는 일상에서 말하고 쓸 때 가장 많이 쓰는 과거 시제
<sub>출처: 2쪽 · 가운데 단</sub>

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 현재 + 과거분사: *Ich habe Jazzmusik gehört.* · *Er ist spät nach Hause gekommen.*
<sub>출처: 2쪽 · 가운데 단</sub>

***haben*과 쓰는 동사 (대부분)**
- 3격 또는 4격 목적어가 있는 동사: *Karin hat ihrem Mann nichts erzählt.* · *Wir haben gestern ein Wildschwein gesehen.*
- 목적어가 없고 장소나 상태가 바뀌지 않는 동사: *Ihr habt heute lange gearbeitet.* · *Vor einer Minute hat es geblitzt.*
- 재귀동사: *Ich habe mich sehr beeilt.* · *Ich habe mich wahnsinnig gefreut.*
- *anfangen, beginnen, aufhören, abnehmen, zunehmen*: *Vorhin haben die Schmerzen aufgehört, und jetzt haben sie wieder angefangen.*
- 모든 화법조동사: *Das habe ich nicht gewollt.* · *Ich habe etwas erledigen müssen.*
<sub>출처: 2쪽 · 가운데 단</sub>

***sein*과 쓰는 동사 (주로 과정을 나타내는 동사)**
- 3격·4격 목적어가 없는 이동 동사: *Wir sind oft im Meer geschwommen.* · *Er ist weit gefahren.* 마찬가지: *gehen, fliegen, folgen, laufen, reisen …*
- 하지만 *fahren*과 *fliegen*은 4격 목적어가 있으면 *haben*: *Ich habe die Kinder nach Hause gefahren.*
- 3격·4격 목적어가 없는 변화 동사: *Wann bist du aufgewacht?* · *Sie ist genau heute vor einem Jahr gestorben.* 마찬가지: *aufstehen, aufwachen, ankommen, einziehen, wachsen, verblühen, einschlafen, werden …*
- 3격 목적어를 가지는 몇몇 과정 동사: *Was ist Ihnen denn geschehen?* · *Mir ist etwas aufgefallen.* 마찬가지: *passieren, gelingen, begegnen …*
- *sein*과 *bleiben*: *Du bist aber lange im Urlaub gewesen.* · *Wir sind drei Tage in Köln geblieben.*
<sub>출처: 2쪽 · 가운데 단</sub>

**쓰임**
- 일상에서 말할 때, 지난 행동·과정·상태: *Hast du es schon erfahren? Marek ist nach München umgezogen, weil er dort eine Stelle bei Siemens gefunden hat.* 〔2쪽 · 가운데 단〕
- 개인적이거나 반쯤 격식 있는 글 (이메일, 편지, 짧은 알림): *Heute habe ich deinen Brief erhalten.* · *Ihre E-Mail habe ich sofort weitergeleitet.* · *Für Samstag haben wir eine Party geplant, zu der wir Sie gern einladen würden.* · *Ich habe gestern versucht, dich anzurufen, aber du hast dich nicht gemeldet.* 〔2쪽 · 가운데 단〕
- 드물게 일반적인 말에도: *Jeder Mediziner hat studiert.* · *Ein Unfall ist so schnell geschehen.* 〔2쪽 · 오른쪽 단〕
- 문장 맨 앞에 시간 부사를 두면 일을 미래로 옮길 수도 있음: *In einer St[unde] habe ich alle Einkäufe erledigt.* 〔2쪽 · 오른쪽 단〕
<sub>출처: 2쪽 · 가운데·오른쪽 단</sub>

### `plusquamperfekt` — 과거완료 (Plusquamperfekt)
위치: 2쪽 · 오른쪽 단

**소개**
- 과거의 다른 일보다 먼저임(*Vorzeitigkeit*)을 나타냄. 주로 글을 쓸 때 과거와 함께 씀
<sub>출처: 2쪽 · 오른쪽 단</sub>

**만들기 (공식 박스)**
- *haben* 또는 *sein*의 과거 + 과거분사: *Als Max ausgeschlafen hatte, duschte er lange.* · *Nachdem alle Gäste gegangen waren, räumte Sonja die Küche auf.*
- *haben*이냐 *sein*이냐는 현재완료와 같은 규칙
<sub>출처: 2쪽 · 오른쪽 단</sub>

**쓰임**
- 과거의 다른 일보다 더 먼저 일어난 일. 거의 늘 과거 문장(드물게 현재완료 문장)과 함께: *Nachdem die letzten Gäste gegangen waren, räumte ich die Wohnung auf.* · *Wir hatten uns so sehr auf den Ausflug gefreut, aber dann wurde mein Sohn krank. Windpocken!*
- 주문장에도 부문장에도 올 수 있음 (표): 주문장 과거완료 + 부문장 과거 *Sie hatte die Hoffnung auf ein Baby schon aufgegeben, als sie plötzlich schwanger wurde.* · 주문장 과거 + 부문장 과거완료 *Sie wurde plötzlich schwanger, als sie die Hoffnung schon aufgegeben hatte.* · 주문장 과거완료 + 주문장 과거 *Sie hatte die Hoffnung schon aufgegeben. Da bekam sie doch noch ein Baby.*
- 입말에서는 가끔 현재완료 대신 씀: (식당에서) *Wir hatten (statt haben) einen Tisch reserviert.* · *Das alles hatte (statt habe) ich dir ja gestern schon gesagt.* · *Hatten (statt haben) wir einen Te[rm]in vereinbart?* · *Ich war (statt bin) heute schon au[f d]em Markt gewesen.*
<sub>출처: 2쪽 · 오른쪽 단</sub>

### `futur1` — 미래 (Futur I)
위치: 4쪽 · 왼쪽 단

**소개**
- 미래형은 둘: 미래(*Futur I*)와 미래완료(*Futur II*). 둘 다 미래의 일을 나타낼 수 있고, 다른 기능도 있음
<sub>출처: 4쪽 · 왼쪽 단</sub>

**만들기 (공식 박스)**
- *werden*의 현재형 + 본동사 원형: *Morgen wird es regnen.* · *Petras Eltern werden bald eine Weltreise machen.*
<sub>출처: 4쪽 · 왼쪽 단</sub>

**쓰임**
- 예측(*Prognose*): *Die Deutschen werden dieses Jahr mehr Geld für ihren Urlaub ausgeben.* · *Am Wochenende werden die Temperaturen sinken.* · *2020 wird es im Land weniger Geburten geben.*
- 약속(*Versprechen*): *Dieser Fehler wird mir nicht noch einmal passieren.* · *Ich werde dich bald in Dresden besuchen.* · *Das werden wir morgen alles besprechen.*
- 의도(*Intention*, 계획): *Bald werde ich viel Geld verdienen.* · *Heute werde ich nichts tun.* · *Dieses Jahr werde ich die Weihnachtsgeschenke rechtzeitig einkaufen.*
- 지금 일에 대한 짐작. 흔히 *wohl*과 함께: *Kai ist heute nicht im Büro. Er wird wohl krank sein.* · *Die Kollegen werden die neuen Pläne der Geschäftsführung (wohl) bereits kennen.*
- 참고 상자: 위협이나 경고를 나타내는 관용 표현: *Du wirst mich noch kennen lernen.* · *Er wird sich noch wundern/umschauen.* · *Du wirst schon sehen, was du [m]it deinem Verhalten anrichtest.* · <em>„Du wirst lachen, …“</em>로 놀라운 이야기를 꺼냄
- 미래와의 관계보다 양태(*modal*) 뜻이 더 중요한 경우가 많음. 정확한 뜻은 문맥으로 앎
<sub>출처: 4쪽 · 왼쪽 단</sub>

**미래 대신 현재 (*Alternative zum Futur I*)**
- 예측, 짐작, 약속 같은 양태 뜻 없이 미래를 말할 때는 보통 현재를 씀. 미래를 가리키는 시간 표현(*morgen, nächste Woche, in 5 Jahren …*)이 미래임을 밝힘: *Im nächsten Jahr wählt Deutschland eine neue Regierung.* · *Morgen fällt unser Deutschkurs leider aus.* · *Nächste Woche bleibt unser Geschäft geschlossen.*
- 시간 표현이 없으면 미래임을 분명히 하려고 미래형을 씀: *Du hast so gute Noten. Du wirst die Prüfung sicher bestehen.*
<sub>출처: 4쪽 · 왼쪽 단</sub>

### `futur2` — 미래완료 (Futur II (Futurperfekt))
위치: 4쪽 · 왼쪽·가운데 단

**만들기 (공식 박스)**
- *werden*의 현재형 + 본동사의 과거분사 + *haben* 또는 *sein*의 원형. *haben*/*sein* 고르기는 현재완료와 같은 규칙
- *Am Ende meines Urlaubs werde ich den Eiffelturm gesehen haben.* · *Nach meinem Besuch in Paris werde ich mit der Metro gefahren sein.*
<sub>출처: 4쪽 · 왼쪽 단</sub>

**쓰임**
- 미래보다 먼저(*Vorzeitigkeit zum Futur I*): 미래의 한 일이 미래의 다른 일보다 앞섬. 미래완료의 일이 미래의 일보다 지금에 더 가까움: *Bis Mai werden wir die Projektplanung abgeschlossen haben. Dann werden wir alle Mitarbeiter informieren.*
- 위 예에서 계획과 알림 둘 다 미래지만, 계획이 알림보다 먼저 일어남
- 지난 일에 대한 짐작. 흔히 *wohl*과 함께: *Er wird (wohl) schon ein Hotel gebucht haben.* (그가 이미 호텔을 예약했으리라 짐작) · *Er wird mit dem alten Fahrzeug (wohl) nicht viel Freude gehabt haben.*
- 과거의 일도 나타낼 수 있어서 *Futurperfekt*라고도 부름
<sub>출처: 4쪽 · 가운데 단</sub>

**미래완료 대신 현재완료 (*Alternative zum Futur II*)**
- 말할 때는 아주 드물게 씀. 번거롭게 들리고 만들기 어려워서 현재완료를 더 씀
- 미래완료: *Bis du nach Hause kommen wirst, werde ich die Koffer gepackt haben. Und übermorgen um diese Zeit werden wir beide bereits in Spanien angekommen sein. Hurra!*
- → 현재완료가 나음: *Bis du nach Hause kommst, habe ich die Koffer gepackt. Und übermorgen um diese Zeit sind wir beide bereits in Spanien angekommen. Hurra!*
- 주의: 이때 부문장에는 미래가 아니라 현재를 씀
<sub>출처: 4쪽 · 가운데 단</sub>

### `konj1` — 접속법 1식 현재 (Konjunktiv I – Gegenwart)
위치: 5쪽 · 가운데 단

**소개**
- 접속법은 가능성의 꼴(*Möglichkeitsform*). 접속법 1식(K I)과 2식(K II)이 있음
- K I은 간접화법의 접속법이라고도 함. 주로 글에서 남이 말하거나 생각하거나 뜻한 것을 전할 때 씀
<sub>출처: 5쪽 · 가운데 단</sub>

**만들기 (공식 박스)**
- 현재: 현재 어간 + *-e/-est/-e/-en/-et/-en*: *Das Fernsehen berichtete, dass man weitere Probleme befürchte.*
<sub>출처: 5쪽 · 가운데 단</sub>

**쓰임**
- 주문장에 *sagen, meinen, erklären, behaupten, versichern* 같은 동사가 오고, 간접화법은 *dass* 부문장: *Der Vater sagte seiner Tochter, dass sie um 20.00 Uhr zu Hause sein solle.*
- *dass* 없이도 씀. 그때 K I 동사는 2번째 자리: *Sie behauptete, es gehe ihr gut.*
- 예/아니오로 답하는 간접의문문은 *ob*로 시작: *Die Reporter fragten, ob der Minister zurücktrete.*
- 주의: K I과 직설법의 꼴이 같을 때가 많음. 그러면 K II를 쓰거나 *würde* + 원형: *Der Kanzler erklärte, dass beide Minister im Amt bleiben → blieben → bleiben würden.*
- 말할 때는 접속법을 아예 쓰지 않을 때가 많음: *Mirko hat gesagt, dass er heute nicht ins Kino geht.*
<sub>출처: 5쪽 · 가운데 단</sub>

**특이점**
- 간접화법의 요구·명령: *sollen*의 K I + 원형. 아주 격식 있게 들려 주로 글에서만: *Der Chef ordnete an, jeder solle heute seinen Schreibtisch aufräumen.*
- 수동태의 K I: 수동태를 만드는 조동사 *sein*, *werden*을 K I으로: *Der Arzt sagte, der Patient werde sofort geröntgt.* · *Der Patient sagte, er sei bereits geröntgt worden.*
<sub>출처: 5쪽 · 가운데 단</sub>

### `konj1_perfekt` — 접속법 1식 과거 (Konjunktiv I – Vergangenheit)
위치: 5쪽 · 가운데 단

**만들기 (공식 박스)**
- 과거: *haben*/*sein*의 K I + 과거분사: *Herr Kohl meinte, er habe das Geld nicht genommen.* · *Mona sagt, dass ihr Vater nach Paris gefahren sei.*
<sub>출처: 5쪽 · 가운데 단</sub>

### `konj1_futur` — 접속법 1식 미래 (Konjunktiv I – Zukunft)
위치: 5쪽 · 가운데 단

**만들기 (공식 박스)**
- 미래: *werden*의 K I + 원형: *Die Polizei versicherte, dass man den Fall genau untersuchen werde.*
<sub>출처: 5쪽 · 가운데 단</sub>

### `konj2` — 접속법 2식 현재 (Konjunktiv II – Gegenwart (würde + 원형 포함))
위치: 5쪽 · 가운데·오른쪽 단

**만들기 (공식 박스)**
- K II는 현재형과 과거형이 중요 〔5쪽 · 가운데 단〕
- 현재: 과거 어간 + *-e, -est, -e, -en, -et, -en*. 인칭 어미는 K I과 같음 〔5쪽 · 가운데 단〕
- 많은 강변화 동사는 어간 모음도 바뀜: *a → ä, o → ö, u → ü*: *ich besaß → ich besäße, ich bot → ich böte, ich fuhr → ich führe, ich gab → ich gäbe, ich kam → ich käme, [i]ch nahm → ich nähme …* · *Ich käme früher an, [we]nn ich den Zug nähme.* 〔5쪽 · 오른쪽 단〕
<sub>출처: 5쪽 · 가운데·오른쪽 단</sub>

**K II 대신 *würde* + 원형 (*Alternative zum Konjunktiv II*)**
- 규칙동사는 K II가 과거와 같은 꼴이라 보통 *werden*의 K II + 원형을 씀: *Wenn ich mehr Zeit hätte, dann kaufte ich die Zeitung.* → *… dann würde ich die Zeitung kaufen.*
- 말할 때는 강변화 동사도 보통 *werden*의 K II + 원형: *Gingest du mit mir zu diesem Konzert?* → *Würdest du mit mir zu diesem Konzert gehen?*
- 화법조동사는 보통 *würde*로 바꾸지 않음: *Ich könnte/wollte/dürfte/möchte/sollte/müsste heute früher nach Hause gehen.* (✗ *Ich würde … gehen können/wollen …*)
<sub>출처: 5쪽 · 오른쪽 단</sub>

**수동태·화법조동사의 K II 현재 (공식 박스)**
- 수동태: *werden*의 K II + 과거분사: *Wenn unsere Stadt mehr Geld hätte, würde hier ein Schwimmbad gebaut.*
- 화법조동사: 화법조동사의 K II + 원형: *Ich könnte besser schlafen, wenn es leise[r w]äre.* · *Solltest du jetzt nicht in der Besprechung s[ein]?*
<sub>출처: 5쪽 · 오른쪽 단</sub>

**쓰임**
- 공손한 부탁: 화법조동사나 *werden*이 K II, 본동사는 원형: *Würden Sie mir helfen?* · *Könnten Sie bitte das Fens[ter] öffnen?*
- 공손한 조언: *sollen*의 K II + 원형: *Du solltest besser eine Tablette nehmen. Und wenn du müde bist, dann solltest du ins Bett gehen.*
- 현실이 아닌 말: 사정이나 조건이 달랐다면 가능할 (또는 불가능할) 일: *Wenn wir einen Garten hätten, würde ich einen Pool bauen.* · *Hätte ich bloß keine Aktien gekauft!*
- 현실이 아닌 비교: 실제 상황을 가상의 상황과 비교. *als ob, wie wenn, als wenn* 또는 *als*(동사가 2번째 자리)로 시작: *Es sieht so aus, als ob/wie wenn/als wenn es bald schneien würde.* · *Deine Fotos sind so gut, als wärst du ein Profi.*
<sub>출처: 5쪽 · 오른쪽 단</sub>

### `konj2_pqp` — 접속법 2식 과거 (Konjunktiv II – Vergangenheit)
위치: 5쪽 · 오른쪽 단

**만들기 (공식 박스)**
- 과거: *haben* 또는 *sein*의 K II + 과거분사: *Er hätte gewonnen, [we]nn er nicht gefallen wäre.* · *Wir wären so gern [nach] Ägypten gereist.*
- 수동태: *sein*의 K II + 과거분사 + *worden*: *Der Wagen wäre nicht gestohlen worden, wenn er abgeschlossen worden wäre.*
- 화법조동사: *haben*의 K II + 원형 + 화법조동사 원형: *Hätte er Lotto gespielt, hätte er dieses Mal mehr als zwei Millionen Euro gewinnen können.*
<sub>출처: 5쪽 · 오른쪽 단</sub>

### `imperativ` — 명령법 (Imperativ)
위치: 3쪽 · 가운데·오른쪽 단 / 5쪽 · 왼쪽 단

**소개**
- 명령, 부탁, 제안에 씀
<sub>출처: 5쪽 · 왼쪽 단</sub>

**만들기 (공식 박스)**
- 단수: 현재 어간. *du*로 부르는 한 사람(가족, 친구, 아이)에게: *Komm! Fahr! Lass! Lauf! Schlaf! Wasch!*
- 단수 특이점: 현재에서 e를 넣는 동사와 *-eln, -ern, -igen* 동사는 어간에 *-e*를 붙임: *Arbeite! Atme! Samm(e)le! Bedau(e)re! Reinige!*
- 단수 특이점: 현재에서 모음이 *e → i*로 바뀌는 동사는 *du*형에서 *-st*를 뺀 꼴: *Gib! Nimm! Befiehl!*
- 주의: *sein*의 단수 명령은 *Sei!*
- 복수: 현재 *ihr*형에서 대명사를 뺌. *du*로 부르는 둘 이상(가족, 친구)에게: *Kommt! Fahrt! Esst! Nehmt! Redet!*
- 존칭: 현재 복수 *sie*형 + *Sie*. *Sie*로 부르는 한 사람이나 여러 사람(모르는 사람, 윗사람)에게: *Kommen Sie! Fahren Sie! Essen Sie! Reden Sie!*
- *wir* 명령: 현재 *wir*형 + *wir*. 말하는 사람을 포함한 무리에게 제안: *Gehen wir! Fahren wir! Essen wir! Reden wir!*
<sub>출처: 5쪽 · 왼쪽 단</sub>

**쓰임**
- 명령·요구: 엄하거나 무례하게 들릴 수 있음. 주로 빨리 행동해야 할 때: *Lass das! Das tut mir weh.* · *Passen Sie auf! Da kommt ein Auto.*
- 부탁: 흔히 *bitte*를 더해 더 친절하게. *doch bitte*는 말을 더 강하게 함: *Bring mir (doch) bitte etwas Wasser!* · *Ich habe das Protokoll vergessen. Holen Sie es (doch) bitte aus meinem Büro!*
- 제안: *mal*이나 *doch mal*과 함께 쓰면 상대가 받아들이거나 거절할 수 있는 가벼운 제안: *Ruft mich (doch) mal an!* · *Telefonieren wir (doch) mal!*
- 좋은 바람: *Genießt den Urlaub! Bleib (bitte) gesund!*
<sub>출처: 5쪽 · 왼쪽 단</sub>

***lassen* 제안과 원형 명령 (참고 상자)**
- 말하는 사람도 포함하는 제안은 *lassen*으로도 나타냄. 공식: *lass/lasst/lassen Sie* + *uns* + 원형: *Lass(t) uns gehen/fahren/essen/reden!* · *Lassen Sie uns gehen/fahren/essen/reden!*
- 일반적인 요구(주로 표지판)에는 원형을 씀: *Baustelle nicht betreten! Bitte nicht stören! Nicht öffnen! Einfahrt freihalten!*
<sub>출처: 5쪽 · 왼쪽 단</sub>

**어순 (동사 자리 표)**
- 명령법은 현재에만 있음. 동사가 1번째 자리: *Seien Sie vorsichtig! Esst mehr Obst!*
- 분리동사는 본동사가 1번째, 전철은 끝: *Kommen Sie doch bitte herein!* · *Schreibt diesen Satz nicht auf!*
- 화법조동사로는 명령법을 만들지 않음. 본동사 1번째, 원형은 끝: *Lass ihn zu uns kommen!*
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

### `partizip2` — 과거분사 (Partizip II (Partizip Perfekt))
위치: 2쪽 · 왼쪽 단

**쓰임**
- 3번째 기본형. *Partizip Perfekt*라고도 함. 현재완료, 과거완료, 미래완료, 수동태, K I 과거, K II 과거를 만들 때 필요
<sub>출처: 2쪽 · 왼쪽 단</sub>

**만들기 (공식 박스)**
- 강변화 동사: *ge-* + 완료 어간(*Perfektstamm*) + *-en*: *sehen: gesehen* · *kommen: gekommen*
- 약변화 동사와 혼합 동사: *ge-* + 완료 어간 + *-(e)t*: *kaufen: gekauft* · *bringen: gebracht*
- 혼합 동사는 강변화처럼 어간 모음이 바뀌지만, 과거에서는 약변화 어미를 붙이고 과거분사도 약변화처럼 만듦
<sub>출처: 2쪽 · 왼쪽 단</sub>

**특이점**
- 분리 전철 동사: <em>ge-</em>가 전철과 어간 사이에 들어감: *angereist, eingeladen, ferngesehen, zugehört …*
- 비분리 전철 동사: <em>ge-</em>가 없음: *besucht, entschieden, verkauft, zerrissen …*
- *-ieren* 동사도 <em>ge-</em>가 없음: *diskutiert, probiert, qualifiziert, studiert …*
<sub>출처: 2쪽 · 왼쪽 단</sub>

### `passiv_vorgang` — 동작수동 (Vorgangspassiv (werden-Passiv))
위치: 4쪽 · 가운데·오른쪽 단

**능동과 수동**
- 능동문에서는 행동하는 사람이나 사물이 주어: *Eine Pizzeria liefert uns das Essen.* · *Papa hat heute die Blumen gegossen.* 〔4쪽 · 가운데 단〕
- 수동문은 행위나 과정을 강조. 누가 했는지는 중요하지 않거나, 모르거나, 밝히고 싶지 않음: *Das Essen wird uns geliefert.* · *Die Blumen sind heute gegossen worden.* 〔4쪽 · 가운데 단〕
- 행위자는 *von* + 3격으로 밝힐 수 있음: *Das Essen wird uns von einer Pizzeria geliefert.* · *Die Blumen sind heute von Papa gegossen worden.* 〔4쪽 · 가운데 단〕
- 모든 타동사(4격 목적어가 있는 동사)로 수동문을 만듦. 능동문의 4격 목적어가 수동문의 주어: *Herr Strom repariert bald den Computer.* → *Der Computer wird bald (von Herrn Strom) repariert.* 〔4쪽 · 가운데 단〕
- 일부 자동사로도 수동문을 만듦. 그때 *es*가 주어로 1번째 자리: *Es wird hier nicht geduscht.* · *Es wird sonntags nicht gearbeitet.* · *Es wird heute noch allen Kunden geantwortet!* 〔4쪽 · 가운데 단〕
- 장소·시간 표현이나 3격 목적어가 1번째 자리에 오면 *es*가 없음. 주어 없는 수동문: *Hier wird nicht geduscht.* · *Sonntags wird nicht gearbeitet.* · *Allen Kunden wird heute noch geantwortet!* 〔4쪽 · 오른쪽 단〕
- 수동은 두 가지: 동작수동(*werden*-수동)과 상태수동(*sein*-수동) 〔4쪽 · 오른쪽 단〕
<sub>출처: 4쪽 · 가운데·오른쪽 단</sub>

**만들기 (공식 박스)**
- *werden* + 과거분사. 모든 시제와 법에 씀: *Die Torte wird gegessen. Die Torte wurde gegessen. Die Torte wäre gegessen worden. Die Torte wird gegessen worden sein.*
- 화법조동사와 함께: 화법조동사 + 과거분사 + *werden*의 원형: *Der Täter muss bestraft werden.*
- 합성 시제에서는 화법조동사가 원형. 순서는 조동사 + 과거분사 + *werden* + 화법조동사 원형: *Der Täter hat bestraft werden müssen.* · *Der Täter wird bestraft werden müssen.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

**쓰임**
- 신문 기사, 관청 말, 사실을 적는 글에서 자주: *Bei der Demonstration wurde eine Person verhaftet.* · *Es wurde festgestellt, dass das Projekt nicht realisiert werden kann.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

**수동 대신 (*Alternative zum Passiv*)**
- *man*을 주어로 한 능동문: *Hier wird ein neuer Kindergarten gebaut.* → *Man baut hier einen neuen Kindergarten.*
- *müssen* 수동문은 가끔 *gehören* + 과거분사나 *sein* + *zu* 원형으로 바꿈: *Diese Tat muss bestraft werden.* → *Diese Tat gehört bestraft.* → *Diese Tat ist zu bestrafen.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

### `passiv_zustand` — 상태수동 (Zustandspassiv (sein-Passiv))
위치: 4쪽 · 오른쪽 단

**만들기 (공식 박스)**
- *sein* + 과거분사: *Deine Jeans sind jetzt gewaschen.* · *Die Koffer waren schon gepackt.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

**쓰임**
- 주로 현재나 과거로 씀. 과정이 아니라 행위의 결과를 강조: *Der Antrag ist abgewiesen.* · *Die Tür war immer abgeschlossen.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

### `passiv_bekommen` — bekommen 수동 (bekommen-Passiv (Dativ-Passiv))
위치: 4쪽 · 오른쪽 단

**만들기 (공식 박스)**
- 말할 때 4격과 3격 목적어를 함께 갖는 일부 동사(*schenken, bringen* 등)로 씀. 능동문의 3격 목적어가 주어가 되고, 4격 목적어는 그대로 4격
- *bekommen* + 과거분사, 행위자는 *von* + 3격: 능동 *Ich bringe meinem Vater die Zeitung. Kai schenkte mir einen Ring.* → 수동 *Mein Vater bekommt von mir die Zeitung gebracht. Ich bekam von Kai einen Ring geschenkt.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

***kriegen* (참고 상자)**
- 입말에서는 *bekommen* 대신 *kriegen*도 자주 씀: *Ich habe einen Teddy geschenkt gekriegt.* · *Tanja kriegt das gestohlene Fahrrad von der Versicherung ersetzt.*
<sub>출처: 4쪽 · 오른쪽 단</sub>

## 2-1. 한 칸에 묶이지 않는 내용 (`pons_zeiten_extra`)

`stem_view`는 표의 공식 박스를 어간별로 다시 묶은 것입니다. 프랑스어 사이트의 「어간 + 어미」 규칙 상자와 같은 틀로 쓸 수 있고, 내용은 모두 표에 있는 것만 넣었습니다.

### `stem_view` — 어간 + 어미로 본 활용 (공식 박스 모음)
위치: 1쪽 · 왼쪽 단 / 2쪽 · 왼쪽·가운데·오른쪽 단 / 3쪽 · 왼쪽 단 / 4쪽 · 왼쪽·오른쪽 단 / 5쪽 · 왼쪽·가운데·오른쪽 단

**현재 어간 (*Präsensstamm* = 원형 − *-(e)n*)**
- + 현재 인칭 어미 *-e, -st, -t, -en, -t, -en* → 현재: *ich komm-e, du komm-st …* 〔1쪽 · 왼쪽 단〕
- + *-t-* + 인칭 어미 *-e, -est, -e, -en, -et, -en* → 과거 (약변화): *ich lebte, du lebtest …* 〔3쪽 · 왼쪽 단〕
- + *-e/-est/-e/-en/-et/-en* → 접속법 1식 현재: *man befürchte* 〔5쪽 · 가운데 단〕
- 그대로 → 명령법 단수: *Komm! Fahr! Lass!* 〔5쪽 · 왼쪽 단〕
<sub>출처: 1쪽 · 왼쪽 단 / 3쪽 · 왼쪽 단 / 5쪽 · 왼쪽·가운데 단</sub>

**과거 어간 (*Präteritumstamm* = 과거 *ich*형)**
- + 인칭 어미 *–, -st, –, -en, -t, -en* → 과거 (강변화): *ich fuhr, du fuhrst …* 〔3쪽 · 왼쪽 단〕
- + *-t-* + 인칭 어미 *-e, -est, -e, -en, -et, -en* → 과거 (혼합 동사): *ich brachte, du brachtest …* 〔3쪽 · 왼쪽 단〕
- + *-e, -est, -e, -en, -et, -en* → 접속법 2식 현재 (많은 강변화 동사는 *a, o, u → ä, ö, ü*): *ich käme, ich nähme* 〔5쪽 · 가운데·오른쪽 단〕
- 규칙동사의 접속법 2식은 과거와 꼴이 같아서 보통 *würde* + 원형으로 대신함 〔5쪽 · 오른쪽 단〕
<sub>출처: 3쪽 · 왼쪽 단 / 5쪽 · 가운데·오른쪽 단</sub>

**완료 어간 (*Perfektstamm* = 과거분사 속 어간)**
- *ge-* + 완료 어간 + *-en* → 과거분사 (강변화): *gesehen, gekommen*
- *ge-* + 완료 어간 + *-(e)t* → 과거분사 (약변화·혼합 동사): *gekauft, gebracht*
<sub>출처: 2쪽 · 왼쪽 단</sub>

**표가 직접 밝힌 어미의 관계**
- 강변화 과거 어미: *ich*형과 *er/sie/es*형은 어미가 없고, 나머지는 현재 어미와 같음 〔3쪽 · 왼쪽 단〕
- 접속법 2식의 인칭 어미는 접속법 1식과 같음 (*Die Personenendungen sind also dieselben wie im K I.*) 〔5쪽 · 가운데 단〕
<sub>출처: 3쪽 · 왼쪽 단 / 5쪽 · 가운데 단</sub>

**조동사 + 과거분사 또는 원형 (합성형)**
- 현재완료 = *haben/sein* 현재 + 과거분사 · 과거완료 = *haben/sein* 과거 + 과거분사 〔2쪽 · 가운데·오른쪽 단〕
- 미래 = *werden* 현재형 + 원형 · 미래완료 = *werden* 현재형 + 과거분사 + *haben/sein* 원형 〔4쪽 · 왼쪽 단〕
- K I 과거 = *haben/sein* K I + 과거분사 · K I 미래 = *werden* K I + 원형 〔5쪽 · 가운데 단〕
- K II 과거 = *haben/sein* K II + 과거분사 · *würde*형 = *werden* K II + 원형 〔5쪽 · 오른쪽 단〕
- 동작수동 = *werden* + 과거분사 · 상태수동 = *sein* + 과거분사 · *bekommen* 수동 = *bekommen* + 과거분사 〔4쪽 · 오른쪽 단〕
<sub>출처: 2쪽 · 가운데·오른쪽 단 / 4쪽 · 왼쪽·오른쪽 단 / 5쪽 · 가운데·오른쪽 단</sub>

### `stammformen` — 세 기본형, 어간, 어간 모음
위치: 2쪽 · 왼쪽 단

**세 기본형 (*Stammformen*)**
- 동사마다 기본형이 셋 있고, 이것으로 동사가 어떻게 활용하는지 알 수 있음: 1번째 원형(사전 표제어), 2번째 과거 *ich*형, 3번째 과거분사
- 기본형마다 어간이 있음: 원형에는 현재형을 만드는 현재 어간(*Präsensstamm*), 과거 *ich*형에는 과거형을 만드는 과거 어간(*Präteritumstamm*), 과거분사에는 완료 어간(*Perfektstamm*)
- 어간마다 모음(또는 이중모음)이 하나 있고, 이를 어간 모음(*Stammvokal*)이라 부름
<sub>출처: 2쪽 · 왼쪽 단</sub>

**약변화와 강변화**
- 약변화(= 규칙) 동사는 세 기본형에서 어간과 어간 모음이 그대로: *atmen, spielen, wohnen* / *ich atmete, ich spielte, ich wohnte* / *geatmet, gespielt, gewohnt*
- 강변화(= 불규칙) 동사는 어간 모음이, 때로는 어간 전체가 바뀜: *bleiben, finden, gehen* / *ich blieb, ich fand, ich ging* / *geblieben, gefunden, gegangen*
- 강변화 동사의 과거 *ich*형은 어미가 없어서 과거 어간과 같음
<sub>출처: 2쪽 · 왼쪽 단</sub>

**외우는 법 (참고 상자)**
- 동사마다 세 기본형과 함께 현재 *du*형도 외울 것. 일부 강변화 동사는 현재 *du*형·*er/sie/es*형에서 모음이 바뀌기 때문: *sagen, du sagst, ich sagte, gesagt* · *kommen, du kommst, ich kam, gekommen* · *treffen, du triffst, ich traf, getroffen*
<sub>출처: 2쪽 · 왼쪽 단</sub>

### `tense_overview` — 시제 한눈에 (지금 · 과거 · 미래)
위치: 1쪽 · 왼쪽·오른쪽 단 / 2쪽 · 가운데 단 / 4쪽 · 왼쪽·가운데 단

**지금 · 과거 · 미래의 시제**
- 지금(*Tempus der Gegenwart*): 시제는 하나, 현재(*Präsens*) 〔1쪽 · 왼쪽 단〕
- 과거(*Tempus der Vergangenheit*): 셋. 과거(*Präteritum*), 그리고 합성형인 현재완료(*Perfekt*)와 과거완료(*Plusquamperfekt*) 〔2쪽 · 가운데 단〕
- 미래(*Tempus der Zukunft*): 둘. 미래(*Futur I*)와 미래완료(*Futur II*). 둘 다 미래를 나타낼 수 있고 다른 기능도 있음 〔4쪽 · 왼쪽 단〕
- 현재는 시간 표현과 함께 과거·미래도 나타내고, 미래는 짐작·약속처럼 양태 뜻이 중요할 때가 많고, 미래완료는 지난 일의 짐작에도 씀 〔1쪽 · 오른쪽 단 / 4쪽 · 왼쪽·가운데 단〕
<sub>출처: 1쪽 · 왼쪽·오른쪽 단 / 2쪽 · 가운데 단 / 4쪽 · 왼쪽·가운데 단</sub>

### `modus_overview` — 법 한눈에 (직설법 · 접속법 · 명령법)
위치: 5쪽 · 왼쪽·가운데 단

**세 가지 법**
- 법(*Modus*)은 말이 현실인지 가상인지, 바람인지, 자기 생각인지 남의 생각인지를 나타냄 〔5쪽 · 왼쪽 단〕
- 직설법(*Indikativ*, 현실의 꼴), 접속법(*Konjunktiv*, 가능성의 꼴), 명령법(*Imperativ*, 명령의 꼴) 〔5쪽 · 왼쪽 단〕
- 접속법은 1식(K I)과 2식(K II). K I은 간접화법, K II는 현실이 아닌 일과 공손한 말 〔5쪽 · 가운데 단〕
<sub>출처: 5쪽 · 왼쪽·가운데 단</sub>

### `hilfsverben` — 조동사 sein · haben · werden 활용표
위치: 1쪽 · 왼쪽 단 / 3쪽 · 왼쪽 단 / 5쪽 · 가운데·오른쪽 단

**현재 (일부는 다른 어간으로 만듦)**
- *sein*: *bin, bist, ist, sind, seid, sind* · *haben*: *habe, hast, hat, haben, habt, haben* · *werden*: *werde, wirst, wird, werden, werdet, werden*
- 참고 상자: *seid*(*sein*)와 전치사·접속사 *seit*를 헷갈리지 말 것: *Seit dieser Nachricht seid ihr so aufgeregt.*
<sub>출처: 1쪽 · 왼쪽 단</sub>

**과거**
- *sein*: *war, warst, war, waren, wart, waren* · *haben*: *hatte, hattest, hatte, hatten, hattet, hatten* · *werden*: *wurde, wurdest, wurde, wurden, wurdet, wurden*
<sub>출처: 3쪽 · 왼쪽 단</sub>

**접속법 1식**
- *sein*: *sei, sei(e)st, sei, seien, seiet, seien* · *haben*: *habe, habest, habe, haben, habet, haben* · *werden*: *werde, werdest, werde, werden, werdet, werden*
<sub>출처: 5쪽 · 가운데 단</sub>

**접속법 2식**
- *sein*: *wäre, wär(e)st, wäre, wären, wär(e)t, wären* · *haben*: *hätte, hättest, hätte, hätten, hättet, hätten* · *werden*: *würde, würdest, würde, würden, würdet, würden*
<sub>출처: 5쪽 · 오른쪽 단</sub>

### `modalverben` — 화법조동사
위치: 1쪽 · 가운데 단 / 2쪽 · 가운데 단 / 3쪽 · 왼쪽·가운데·오른쪽 단 / 4쪽 · 오른쪽 단 / 5쪽 · 오른쪽 단

**현재**
- 화법조동사는 강변화 동사에 속함. 단수에서 모음이 바뀌고(*sollen*은 빼고), *ich*형과 *er/sie/es*형은 어미가 없음
- *können*: *kann, kannst, kann, können, könnt, können* · *müssen*: *muss, musst, muss, müssen, müsst, müssen* · *dürfen*: *darf, darfst, darf, dürfen, dürft, dürfen*
- *wollen*: *will, willst, will, wollen, wollt, wollen* · *sollen*: *soll, sollst, soll, sollen, sollt, sollen* · *mögen*: *mag, magst, mag, mögen, mögt, mögen*
<sub>출처: 1쪽 · 가운데 단</sub>

**다른 쪽에 나오는 화법조동사 규칙**
- 현재완료는 모두 *haben*: *Das habe ich nicht gewollt.* · *Ich habe etwas erledigen müssen.* 〔2쪽 · 가운데 단〕
- 말할 때도 현재완료보다 과거를 더 자주 씀: *Martin musste/wollte/konnte/sollte/durfte noch einkaufen.* 〔3쪽 · 왼쪽 단〕
- 다른 동사의 원형과 함께 합성 시제가 되면 이중 원형: *Ich habe/hatte dich nicht sehen können.* 〔3쪽 · 가운데·오른쪽 단〕
- 수동태와 함께: *Der Täter muss bestraft werden.* · *Der Täter hat bestraft werden müssen.* 〔4쪽 · 오른쪽 단〕
- K II는 *würde*로 바꾸지 않음: *Ich könnte/wollte/dürfte/möchte/sollte/müsste heute früher nach Hause gehen.* 〔5쪽 · 오른쪽 단〕
<sub>출처: 2쪽 · 가운데 단 / 3쪽 · 왼쪽·가운데·오른쪽 단 / 4쪽 · 오른쪽 단 / 5쪽 · 오른쪽 단</sub>

### `praefixe` — 전철이 있는 동사 (분리 · 비분리 · 뜻에 따라)
위치: 1쪽 · 가운데·오른쪽 단 / 2쪽 · 왼쪽 단 / 3쪽 · 가운데·오른쪽 단

**비분리 전철 (공식 박스)**
- 현재뿐 아니라 모든 시제에서 본동사와 붙어 있음. 말할 때 전철이 아니라 본동사에 강세: *be-, emp-, ent-, er-, ge-, miss-, ver-, zer-*
- *Lara besucht ihre alte Schule.* · *Ich erzähle dir alles, denn ich vertraue dir vollkommen.*
<sub>출처: 1쪽 · 가운데 단</sub>

**분리 전철 (공식 박스)**
- 현재와 과거에서 조동사나 화법조동사가 따로 없으면 떨어짐. 말할 때 전철에 강세, 전철은 문장 끝: *ab-, an-, auf-, aus-, bei-, ein-, fest-, fort-, her-, hin-, los-, mit-, vor-, weg-, zu-, zurück-, zusammen- …*
- *Anne kauft Lebensmittel nur im Bioladen ein.* / *Anne muss heute Brot einkaufen.* · *Ich komme auf Ihr Angebot zurück.* / *Ich mag gerne auf Ihr Angebot zurückkommen.*
<sub>출처: 1쪽 · 가운데 단</sub>

**뜻에 따라 분리·비분리 (공식 박스)**
- *durch-, hinter-, über-, um-, unter-, voll-, wider-, wieder-*
- *umfahren*(분리, 들이받아 넘어뜨리다): *Achtung, fahr das Stopp-Schild nicht um!* · *umfahren*(비분리, 돌아서 가다): *Bitte umfahren Sie das Stadtzentrum.*
<sub>출처: 1쪽 · 오른쪽 단</sub>

**다른 쪽에 나오는 전철 규칙**
- 과거분사: 분리 전철은 <em>ge-</em>가 전철과 어간 사이 (*angereist*), 비분리 전철은 *ge-* 없음 (*besucht*) 〔2쪽 · 왼쪽 단〕
- 어순: 주문장에서 본동사 2번째, 전철 끝 (*Wir stehen immer früh auf.*), 부문장에서는 붙어서 끝 (*…, wenn die Hausbesitzer einkaufen.*) 〔3쪽 · 가운데·오른쪽 단〕
<sub>출처: 2쪽 · 왼쪽 단 / 3쪽 · 가운데·오른쪽 단</sub>

### `satzstellung` — 문장 속 동사 자리 (표와 현재완료·과거완료의 특이점)
위치: 2쪽 · 오른쪽 단 / 3쪽 · 가운데·오른쪽 단

**기본 규칙**
- 술어(*Prädikat*)는 동사 하나, 여러 부분으로 된 동사, 또는 여러 동사로 이루어짐. 주문장과 부문장에서 동사 자리는 둘: 2번째 자리와/또는 마지막 자리. 의문사 없는 의문문과 명령법에서는 동사가 1번째 자리
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

**동사 하나 (*Prädikat mit einfachem Verb*)**
- 주문장·의문사 의문문: 현재·과거는 동사가 2번째 (*Goethe kommt/kam aus Frankfurt.* · *Woher kommt/kam Goethe?*). 현재완료·과거완료·미래는 조동사가 2번째, 과거분사·원형은 끝 (*Goethe hat/hatte au[ch] in Weimar gelebt.* · *Goethe wird keine Bücher mehr schreiben.* · *Wann ist Goethe nach Italien gereist?*)
- 부문장: 동사가 끝 (*Man spricht von Mobbing, wenn Gruppen eine Person attackieren, die von ihrer Norm abweicht.*). 합성 시제는 조동사가 끝, 과거분사·원형은 조동사 앞 (*Mobbing wurde ein wichtiges Thema, weil immer mehr Betroffene davon berichtet haben/hatten.* · *Mediziner warnen, dass immer mehr Menschen durch Mobbing erkranken werden.*)
- 의문사 없는 의문문: 동사가 1번째 (*Verleiht man den Nobelpreis jährlich?*). 합성 시제는 조동사가 1번째, 과거분사·원형은 끝 (*Hat/Hatte Mme. Curie den Nobelpreis bekommen?* · *Werden auch Pädagogen den Preis bekommen?*)
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

**분리동사 (*Prädikat mit trennbarem Verb*)**
- 주문장·의문사 의문문: 본동사 2번째, 전철 끝 (*Wir stehen/standen immer früh auf.* · *Warum stehen/standen wir immer früh auf?*). 합성 시제: *Wir sind/waren gestern früh aufgestanden.* · *Morgen werden wir nicht früh aufstehen.* · *Warum sind wir nicht später aufgestanden?*
- 부문장: 동사가 붙어서 끝 (*Einbrecher kommen oft samstags, wenn die Hausbesitzer einkaufen.*). 합성 시제: *Versicherungen zahlen bei Diebstahl nur, wenn der Besitzer die Haustür abgeschlossen hat/hatte.* · *Ich weiß, dass mein Agent bald anrufen wird.*
- 의문사 없는 의문문: 본동사 1번째, 전철 끝 (*Nehmen/Nahmen Sie auch an dem Seminar teil?*). 합성 시제: *Sind/Waren die Teilnehmer schon angereist?* · *Werden Sie sich auch nächstes Jahr anmelden?*
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

**여러 동사 (*Prädikat mit mehreren Verben*: 화법조동사 + 원형 또는 본동사 + 원형)**
- 주문장·의문사 의문문: 화법조동사나 본동사가 2번째, 원형은 끝 (*Hier müssen/mussten wir leise reden.* · *Unsere Kinder gehen/gingen nicht gern spazieren.*). 합성 시제는 조동사가 2번째, 끝에 이중 원형 또는 원형 + 과거분사 (*Ich habe/hatte dich nicht sehen können.* · *Karin wird leider zum Arzt gehen müssen.* · *Kurt ist gestern spazieren gegangen.*)
- 부문장: 원형이 화법조동사·본동사 앞, 맨 끝 (*Ich kann dich nicht abholen, weil ich das Auto in die Werkstatt bringen muss/musste.* · *Ich weiß nicht, ob ich das Auto noch einmal reparieren lasse.*). 합성 시제는 조동사가 이중 원형 앞 (*Er kam nach Deutschland, weil er hier hat/hatte arbeiten wollen.* · *Er ist in seine Heimat zur[ückg]ekehrt, als er dort bessere Zeiten hat/hatte [ko]mmen sehen.* · *Ich weiß nicht, ob er seine [To]chter zum Konzert wird gehen lassen.*)
- 의문사 없는 의문문: 1번째, 원형은 끝 (*Darf/Durfte ich dir diese Frage stellen?* · *Hörst du den Wind rauschen?*). 합성 시제는 조동사 1번째, 이중 원형은 끝 (*Hast/Hattest du jetzt schon deinen Sommerurlaub buchen müssen?* · *Hast/Hattest du mich kommen hören?* · *Wird er uns zuschauen lassen?*)
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

**이중 원형 (*Anmerkung*)**
- 화법조동사 말고 이중 원형을 만드는 동사는 다음뿐
- *lassen*: *Wir lassen die Kinder spielen.* → *Wir haben die Kinder spielen lassen.*
- *brauchen*: 원형과 함께면 부정문에서만: *Du brauchst nicht (zu) kommen.* → *Du hast nicht (zu) kommen brauchen.*
- *sehen, hören, fühlen, spüren*: 4격 목적어 + 원형과 함께 쓰고, 합성 시제에서는 원형으로: *Ich sehe ein Unglück kommen.* → *Ich habe ein Unglück kommen sehen.*
<sub>출처: 3쪽 · 가운데·오른쪽 단</sub>

**현재완료·과거완료의 특이점**
- 술어에 본동사가 둘이거나 본동사와 화법조동사가 있으면 조동사만 인칭 변화하고, 본동사와 화법조동사는 원형
- 주문장: 조동사 2번째, 나머지 동사는 끝: *Leider habe/hatte ich gestern nicht kommen können.* · *Ich habe/hatte gestern spazieren gehen wollen, doch dann kam das Gewitter.*
- 부문장: 모든 동사가 끝에 모이고, 인칭 변화한 조동사는 원형들 앞: *Obwohl er seine Eltern hat/hatte besuchen wollen, musste er wegen einer Grippe zu Hause bleiben.* · *Da der Hausbesitzer ihn nicht hatte kommen hören, gelangte der Einbrecher ungestört ins Haus.*
<sub>출처: 2쪽 · 오른쪽 단</sub>

## 3. 주의할 점 (`notes`)

- **쪽 번호**: 이 표는 각 쪽 아래 초록 네모에 쪽 번호(1~5)가 인쇄되어 있어서 '1쪽 · 왼쪽 단'으로 적음. 쪽 번호가 없던 Grammatik 표('1장')와 다름. 3쪽의 「Stellung der Verben im Satz」 표는 가운데·오른쪽 단을 가로질러서 '3쪽 · 가운데·오른쪽 단'으로 적음
- **받은 쪽**: 사진 5장 = 1~5쪽. 이 시리즈는 보통 6쪽이라 마지막 쪽이 더 있을 수 있음. 저자·연도·ISBN은 받은 쪽에 없음 (예문에 2020년, 2022년이 나와서 그 무렵 판으로 보임)
- **반사로 가린 글자**: 사진에 빛이 반사되어 안 보이는 글자는 문맥으로 [ ] 안에 채움. 끝까지 읽지 못한 2쪽 오른쪽 단의 <em>Morgen h[…] die Renovierung endlich geschafft.</em>는 넣지 않았음. [ ]가 있는 예문을 사이트에 쓸 때는 실물로 한 번 확인할 것
- **칸 id**: Grammatik 표 자료(pons-de-tense-notes.json)와 같은 id를 씀. 이 표에만 있는 *bekommen* 수동은 새 id `passiv_bekommen`
- **어간 모델**: 이 표는 '현재 어간 · 과거 어간 · 완료 어간'과 '어미 묶음'을 공식 박스로 직접 보여 줌. 같은 접속법 어미가 현재 어간에 붙으면 K I, 과거 어간에 붙으면 K II. 프랑스어 사이트의 「어간 + 어미」 규칙 상자와 같은 틀로 쓸 수 있음 (`stem_view`)
- **✗ 표시**: 5쪽 오른쪽 단의 (Nicht: …)를 ✗로 옮김

## 3-1. Grammatik 표와 대조 (`crosscheck_grammatik_sheet`)

| 주제 | Zeiten 표 (이 자료) | Grammatik 표 | 판단 |
|---|---|---|---|
| 어간 이름 | *Präsensstamm* · *Präteritumstamm* · *Perfektstamm* (2쪽 왼쪽 단) | *Verbstamm* · *Infinitivstamm* · *Präteritumstamm* (3장) | 같은 것을 다르게 부름. Zeiten의 현재 어간 = Grammatik의 원형 어간. 사이트에서는 '현재 어간'으로 통일 |
| 접속법 1식·2식 만들기 | K I = 현재 어간 + *-e/-est/-e/-en/-et/-en*, K II = 과거 어간 + 같은 어미 (5쪽) | K I = 원형 어간 + 접속법 어미, K II = 과거 어간 + K I 어미 (3장) | 일치. Zeiten은 어미를 하나하나 적고 'K I과 같다'고 직접 밝힘 |
| e 넣기 (*e-Einschub*) | *du*형·*ihr*형만 말함: *du arbeitest – ihr arbeitet* (1쪽 왼쪽 단) | *du arbeitest, er arbeitet, ihr arbeitet* (3장 왼쪽 단) | *er/sie/es*형에도 e가 들어감(*er arbeitet*). Grammatik 쪽이 빠짐없음 |
| 명령법 단수 | 현재 어간 (*Fahr! Lauf! Schlaf!*). *e → i* 동사만 *du*형 − *-st* (*Gib! Nimm!*) (5쪽 왼쪽 단) | 모든 동사를 '현재 *du*형에서 *-st*와 *du*를 뺌'으로 설명 (3장 오른쪽 단) | Grammatik 규칙을 *a → ä* 동사에 그대로 쓰면 ✗<em>Fähr!</em>가 나옴. Zeiten 쪽이 정확 |
| 비분리·분리 전철 목록 | 비분리 *be-, emp-, ent-, er-, ge-, miss-, ver-, zer-*. <em>wider-</em>는 '뜻에 따라' 무리. 분리에 <em>fest-, fort-, los-, zurück-, zusammen-</em>이 있고 <em>nach-</em>는 없음 (1쪽) | 비분리에 *wider-* 포함. 분리 목록에 *nach-* 있음 (2장 가운데 단) | <em>wider-</em>의 분류가 다름. 사이트에 목록을 쓸 때는 어느 표를 따랐는지 밝힐 것 |
| 혼합 동사 | *bringen, brennen, denken, kennen, nennen, rennen, senden* (3쪽 왼쪽 단) | 같은 목록 + *wissen*과 화법조동사 (2장 왼쪽 단) | 일치. Grammatik이 더 넓게 묶음 |
| 과거와 현재완료의 쓰임 | 과거는 주로 글, 격식 있는 말. 현재완료는 일상의 말과 개인적인 글. *sein, haben*과 화법조동사는 말에서도 과거 | 과거는 주로 글, 말은 현재완료. 조동사·화법조동사는 거의 늘 과거 | 일치. Zeiten이 '격식 있는 말'과 '개인적인 글'을 더함 |
| 미래완료 | 미래보다 먼저, 지난 일의 짐작. 말할 때는 아주 드물고 현재완료로 바꿈 (4쪽) | 드물게 씀. 예측과 짐작 (3장 가운데 단) | 어긋나지 않음. Zeiten이 자세함 |
| 접속법 1식 미래 | *werden*의 K I + 원형. K I이 직설법과 같으면 K II나 *würde* (일반 규칙) | 1인칭 단수와 복수는 대개 *würde(n)* (3장 오른쪽 단) | 같은 원리. Grammatik이 어느 인칭에서 바뀌는지 직접 적음 |
| 동작수동·상태수동 | 동작수동은 모든 시제와 법, 상태수동은 주로 현재·과거 (4쪽) | 동작수동은 모든 시제, 상태수동은 주로 현재·과거 (2장 오른쪽 단) | 일치 |
| 접속법 이름 | K I der Gegenwart / Vergangenheit / Zukunft, K II der Gegenwart / Vergangenheit | Konjunktiv I / I Perfekt / I Futur, Konjunktiv II / II Plusquamperfekt | 이름만 다름. 두 파일의 id를 같게 맞춤 (konj1, konj1_perfekt, konj1_futur, konj2, konj2_pqp) |
| 한쪽에만 있는 것 | Zeiten에만: *bekommen* 수동, *wir* 명령, *lassen* 제안, 원형 명령, 이중 원형, 역사적 현재, 시간 표현, 미래의 관용 표현, 수동 대신 쓰는 말, K I·K II의 수동, K II의 화법조동사 | Grammatik에만: 여섯 시제를 시간 축에 늘어놓은 표, *Satzklammer*라는 이름, *möchte* 설명 | 칸을 채울 때 두 파일을 함께 볼 것 |

## 4. 표 5쪽 전체 번역 (제목 띠와 공식 박스)

실물 표와 같은 순서입니다: 쪽(1~5) → 단(왼쪽·가운데·오른쪽) → 위에서 아래. 각 줄은 `[칸 종류] 독일어 원문 → 한국어` 형식입니다.

- **[큰 단원]** 남색 띠 · **[작은 단원]** 파란 띠 · **[소제목]** 연한 파란 띠 · **[굵은 제목]** 본문 속 굵은 글씨 · **[공식 박스]** 테두리 상자 · **[참고 상자]** 연한 파란 바탕 상자 · **[표 라벨]** 표 머리 줄 · **[표지]** 1쪽 표지

### 표 안에 자주 나오는 독일어

| 독일어 | 한국어 |
|---|---|
| Tempus (Pl. Tempora) · Zeitform | 시제 |
| Gegenwart · Vergangenheit · Zukunft | 지금(현재) · 과거 · 미래 |
| Stammform (1./2./3.) | 기본형 (1번째 원형 · 2번째 과거 ich형 · 3번째 과거분사) |
| Präsensstamm · Präteritumstamm · Perfektstamm | 현재 어간 · 과거 어간 · 완료 어간 |
| Stammvokal · Vokalwechsel | 어간 모음 · 모음 바뀜 |
| Personalendung | 인칭 어미 |
| schwache / starke Verben · Mischverben | 약변화(규칙) / 강변화(불규칙) 동사 · 혼합 동사 |
| Hilfsverb · Modalverb · Vollverb · Grundverb | 조동사 · 화법조동사 · 본동사 · (전철이 붙기 전의) 기본 동사 |
| Präfix (Vorsilbe) · trennbar / untrennbar | 전철 · 분리 / 비분리 |
| e-Einschub · s-Ausfall · e-Ausfall | e 넣기 · s 빠짐 · e 빠짐 |
| Partizip II · Partizip Perfekt | 과거분사 |
| Infinitiv · doppelter Infinitiv | 원형 · 이중 원형 |
| Prädikat (Satzaussage) | 술어 |
| Hauptsatz · Nebensatz · W-Frage · Fragesatz ohne W-Fragewort | 주문장 · 부문장 · 의문사 의문문 · 의문사 없는 의문문 |
| Position 1 / 2. Position / letzte Position | 1번째 / 2번째 / 마지막 자리 |
| Vorzeitigkeit | 먼저임 (다른 일보다 앞섬) |
| Prognose · Versprechen · Intention · Vermutung | 예측 · 약속 · 의도 · 짐작 |
| Modus · Indikativ · Konjunktiv · Imperativ | 법 · 직설법 · 접속법 · 명령법 |
| K I · K II | 접속법 1식 · 접속법 2식 |
| indirekte Rede | 간접화법 |
| Aktiv · Passiv · Vorgangspassiv · Zustandspassiv | 능동 · 수동 · 동작수동 · 상태수동 |
| Akkusativobjekt · Dativobjekt | 4격 목적어 · 3격 목적어 |
| transitiv / intransitiv | 타동사 / 자동사 |
| Bildung · Gebrauch · Besonderheiten · Alternative | 만들기 · 쓰임 · 특이점 · 대신 쓰는 말 |
| Achtung! · Ebenso · Aber · Seltener · Nicht | 주의! · 마찬가지 · 하지만 · 드물게 · 틀림(✗) |
| duzen / siezen | du로 부르다 / Sie로 부르다 |

### 1쪽 · 표지 · 지금의 시제: 현재 (Tempus der Gegenwart)

#### 왼쪽 단

- **[표지]** AUF EINEN BLICK · Zeiten · DEUTSCH → 한눈에 보는 시제 · 독일어
  - 설명: 1쪽 위쪽은 표지 (PONS, € 5,–)
- **[큰 단원]** Tempus der Gegenwart → 지금의 시제
  - 설명: 지금을 말하는 시제는 현재 하나
- **[작은 단원]** Präsens → 현재
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Präsensstamm (= Infinitiv ohne die Endung -(e)n) + Personalendung → 현재 어간 (= 원형에서 -(e)n을 뗀 것) + 인칭 어미
  - 설명: 예: kommen
- **[표 라벨]** Präsensstamm · Personalendung · Singular · Plural → 현재 어간 · 인칭 어미 · 단수 · 복수
- **[굵은 제목]** Besonderheiten → 특이점
  - 설명: e-Einschub, s-Ausfall, e-Ausfall
- **[굵은 제목]** Achtung! → 주의!
  - 설명: tun: ich tu(e)
- **[소제목]** Hilfsverben → 조동사
  - 설명: 현재는 일부 다른 어간으로 만듦. sein · haben · werden 표
- **[참고 상자]** Achtung! Verwechseln Sie seid nicht mit der Präposition bzw. Konjunktion seit. → 주의! seid를 전치사·접속사 seit와 헷갈리지 말 것

#### 가운데 단

- **[소제목]** Verben mit Vokalwechsel → 모음이 바뀌는 동사
  - 설명: a → ä, au → äu, e → i(e)
- **[굵은 제목]** Achtung! → 주의!
  - 설명: wissen: ich weiß
- **[소제목]** Modalverben → 화법조동사
  - 설명: können · müssen · dürfen · wollen · sollen · mögen 표
- **[소제목]** Verben mit Präfix → 전철이 있는 동사
- **[공식 박스]** be-, emp-, ent-, er-, ge-, miss-, ver-, zer- → 비분리 전철
  - 설명: 모든 시제에서 붙어 있음. 본동사에 강세
- **[공식 박스]** ab-, an-, auf-, aus-, bei-, ein-, fest-, fort-, her-, hin-, los-, mit-, vor-, weg-, zu-, zurück-, zusammen- … → 분리 전철
  - 설명: 현재·과거에서 떨어짐. 전철에 강세, 문장 끝

#### 오른쪽 단

- **[표지]** www.pons.de/zeiten-aeb – Hier finden Sie ein kleines Zeiten-Training. → 여기서 짧은 시제 연습을 할 수 있음
  - 설명: QR 코드
- **[공식 박스]** durch-, hinter-, über-, um-, unter-, voll-, wider-, wieder- → 뜻에 따라 분리·비분리
  - 설명: umfahren 두 가지
- **[소제목]** Gebrauch → 쓰임
  - 설명: Allgemeingültiges und Fakten · Gegenwärtiges · Zukünftiges · Vergangenes (historisches Präsens)
- **[굵은 제목]** Präzisierung durch Zeitangaben → 시간 표현으로 때를 밝힘
  - 설명: Gegenwart · Zukunft · Vergangenheit

### 2쪽 · 기본형과 과거분사 · 과거의 시제: 현재완료, 과거완료 (Stammformen · Tempus der Vergangenheit)

#### 왼쪽 단

- **[큰 단원]** Stammformen, Verbstamm, Stammvokal und Partizip II → 기본형, 동사 어간, 어간 모음과 과거분사
  - 설명: 세 기본형과 세 어간
- **[참고 상자]** Merken Sie sich bei jedem Verb die drei Stammformen. → 동사마다 세 기본형을 외울 것
  - 설명: 현재 du형도 함께
- **[작은 단원]** Die 3. Stammform: Das Partizip II → 3번째 기본형: 과거분사
- **[소제목]** Bildung → 만들기
- **[공식 박스]** bei starken Verben: ge- + Perfektstamm + -en / bei schwachen Verben und Mischverben: ge- + Perfektstamm + -(e)t → 강변화: ge- + 완료 어간 + -en / 약변화·혼합: ge- + 완료 어간 + -(e)t
- **[굵은 제목]** Besonderheiten: → 특이점
  - 설명: 분리 전철, 비분리 전철, -ieren

#### 가운데 단

- **[큰 단원]** Tempus der Vergangenheit → 과거의 시제
  - 설명: 과거, 현재완료, 과거완료
- **[작은 단원]** Perfekt → 현재완료
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Präsens von haben oder sein + Partizip II → haben 또는 sein의 현재 + 과거분사
- **[소제목]** Perfekt mit haben → haben과 쓰는 현재완료
- **[소제목]** Perfekt mit sein → sein과 쓰는 현재완료
- **[소제목]** Gebrauch → 쓰임

#### 오른쪽 단

- **[작은 단원]** Plusquamperfekt → 과거완료
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Präteritum von haben oder sein + Partizip II → haben 또는 sein의 과거 + 과거분사
- **[소제목]** Plusquamperfekt mit haben oder sein → haben이냐 sein이냐
  - 설명: 현재완료와 같은 규칙
- **[소제목]** Gebrauch → 쓰임
- **[표 라벨]** Plusquamperfekt / Präteritum · im Hauptsatz / im Nebensatz → 과거완료 / 과거 · 주문장 / 부문장
  - 설명: 세 가지 짝
- **[소제목]** Besonderheiten bei Perfekt und Plusquamperfekt → 현재완료·과거완료의 특이점
  - 설명: 동사가 여럿일 때 어순. → siehe auch Seite 3 (3쪽도 볼 것)

### 3쪽 · 과거 · 문장 속 동사 자리 (Präteritum · Stellung der Verben im Satz)

#### 왼쪽 단

- **[작은 단원]** Präteritum → 과거
- **[소제목]** Bildung bei schwachen Verben → 약변화 동사의 만들기
- **[공식 박스]** Präsensstamm + -t- + Personalendungen -e, -est, -e, -en, -et, -en → 현재 어간 + -t- + 인칭 어미
- **[굵은 제목]** e-Einschub → e 넣기
  - 설명: 현재와 같은 규칙 (→ Seite 1)
- **[소제목]** Bildung bei starken Verben → 강변화 동사의 만들기
- **[공식 박스]** Präteritumstamm + Personalendungen –, -st, –, -en, -t, -en → 과거 어간 + 인칭 어미
  - 설명: ich형과 er/sie/es형은 어미 없음
- **[소제목]** Bildung bei Mischverben → 혼합 동사의 만들기
- **[공식 박스]** Präteritumstamm + -t- + Personalendungen -e, -est, -e, -en, -et, -en → 과거 어간 + -t- + 인칭 어미
- **[소제목]** Präteritumformen der Hilfsverben → 조동사의 과거형
  - 설명: sein · haben · werden 표
- **[소제목]** Gebrauch → 쓰임
  - 설명: Sachtexte · Erzählende Texte · Beim Sprechen in förmlichen Situationen
- **[참고 상자]** Die Hilfsverben sein und haben und die Modalverben werden auch beim Sprechen häufiger im Präteritum als im Perfekt benutzt. → sein, haben과 화법조동사는 말할 때도 현재완료보다 과거를 더 자주 씀

#### 가운데 단

- **[큰 단원]** Stellung der Verben im Satz → 문장 속 동사 자리
  - 설명: 가운데·오른쪽 단을 가로지르는 표
- **[작은 단원]** Prädikat mit einfachem Verb → 동사 하나로 된 술어
- **[표 라벨]** Präsens, Präteritum \| Perfekt, Plusquamperfekt, Futur I → 현재·과거 | 현재완료·과거완료·미래
  - 설명: 표의 두 열
- **[표 라벨]** Hauptsatz und W-Fragen · Nebensatz · Fragesatz ohne W-Fragewort · Imperativ → 주문장과 의문사 의문문 · 부문장 · 의문사 없는 의문문 · 명령법
  - 설명: 표의 네 줄
- **[작은 단원]** Prädikat mit trennbarem Verb → 분리동사로 된 술어
- **[작은 단원]** Prädikat mit mehreren Verben → 여러 동사로 된 술어
  - 설명: 화법조동사 + 원형 또는 본동사 + 원형
- **[굵은 제목]** \* Anmerkung → * 덧붙임
  - 설명: 이중 원형을 만드는 동사: lassen, brauchen, sehen, hören, fühlen, spüren

### 4쪽 · 미래의 시제 · 수동태 (Tempus der Zukunft · Passiv)

#### 왼쪽 단

- **[큰 단원]** Tempus der Zukunft → 미래의 시제
  - 설명: Futur I과 Futur II
- **[작은 단원]** Futur I → 미래
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Präsensform von werden + Infinitiv des Vollverbs → werden의 현재형 + 본동사 원형
- **[소제목]** Gebrauch → 쓰임
  - 설명: Prognose · Versprechen · Intention · Vermutung
- **[참고 상자]** Es gibt einige Redensarten im Futur I, die eine Drohung oder Warnung ausdrücken → 위협이나 경고를 나타내는 미래의 관용 표현
- **[소제목]** Alternative zum Futur I → 미래 대신 쓰는 말
  - 설명: 시간 표현 + 현재
- **[작은 단원]** Futur II → 미래완료
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Präsensform von werden + Partizip Perfekt des Vollverbs + Infinitiv von haben oder sein → werden의 현재형 + 본동사의 과거분사 + haben 또는 sein의 원형

#### 가운데 단

- **[소제목]** Gebrauch → 쓰임
  - 설명: Vorzeitigkeit zum Futur I · Vermutung über die Vergangenheit
- **[소제목]** Alternative zum Futur II → 미래완료 대신 쓰는 말
  - 설명: 현재완료
- **[굵은 제목]** Futur II: / → Besser im Perfekt: → 미래완료: / → 현재완료가 나음:
- **[큰 단원]** Passiv → 수동태

#### 오른쪽 단

- **[소제목]** Bildung des Vorgangspassivs → 동작수동 만들기
- **[공식 박스]** werden + Partizip II → werden + 과거분사
- **[공식 박스]** Modalverb + Partizip II + werden im Infinitiv → 화법조동사 + 과거분사 + werden 원형
- **[소제목]** Bildung des Zustandspassivs → 상태수동 만들기
- **[공식 박스]** sein + Partizip II → sein + 과거분사
- **[소제목]** bekommen-Passiv oder Dativ-Passiv → bekommen 수동 (3격 수동)
- **[공식 박스]** bekommen + Partizip II + Dativ mit von → bekommen + 과거분사 + von + 3격
- **[참고 상자]** In der Umgangssprache wird statt des Verbs bekommen auch häufig das Verb kriegen benutzt → 입말에서는 bekommen 대신 kriegen도 자주 씀
- **[소제목]** Gebrauch → 쓰임
- **[소제목]** Alternative zum Passiv → 수동 대신 쓰는 말
  - 설명: man · gehören + 과거분사 · sein + zu 원형

### 5쪽 · 법: 명령법, 접속법 1식·2식 (Modus)

#### 왼쪽 단

- **[큰 단원]** Modus → 법
  - 설명: Indikativ · Konjunktiv · Imperativ
- **[작은 단원]** Imperativ → 명령법
- **[소제목]** Bildung → 만들기
- **[굵은 제목]** Imperativ Singular: → 명령법 단수
- **[공식 박스]** Präsensstamm (→ siehe Seite 2) → 현재 어간 (→ 2쪽 참고)
- **[굵은 제목]** Besonderheiten: → 특이점
  - 설명: e 넣기, e → i, Sei!
- **[굵은 제목]** Imperativ Plural: → 명령법 복수
- **[공식 박스]** ihr-Form im Präsens ohne Pronomen → 현재 ihr형에서 대명사를 뺌
- **[굵은 제목]** Höflicher Imperativ: → 존칭 명령
- **[공식 박스]** sie-Form im Plural im Präsens + Sie → 현재 복수 sie형 + Sie
- **[굵은 제목]** Wir-Imperativ: → wir 명령
- **[공식 박스]** wir-Form im Präsens + wir → 현재 wir형 + wir
- **[소제목]** Gebrauch → 쓰임
  - 설명: Befehle · Bitten · Vorschlag · Gute Wünsche
- **[참고 상자]** lass/lasst/lassen Sie + uns + Infinitiv → lassen으로 하는 제안
  - 설명: Besonderheit: 표지판의 원형 명령

#### 가운데 단

- **[작은 단원]** Konjunktiv → 접속법
  - 설명: Möglichkeitsform. K I과 K II
- **[작은 단원]** Konjunktiv I → 접속법 1식
  - 설명: 간접화법의 접속법
- **[소제목]** Bildung → 만들기
- **[공식 박스]** Gegenwart: Präsensstamm + -e/-est/-e/-en/-et/-en → 현재: 현재 어간 + 접속법 어미
- **[공식 박스]** Vergangenheit: haben/sein im K I + Partizip II → 과거: haben/sein의 K I + 과거분사
- **[공식 박스]** Zukunft: werden im K I + Infinitiv → 미래: werden의 K I + 원형
- **[굵은 제목]** Die Formen der Hilfsverben im Konjunktiv I → 조동사의 접속법 1식
  - 설명: sein · haben · werden 표
- **[굵은 제목]** Besonderheiten → 특이점
  - 설명: Passiv im Konjunktiv I · Aufforderung mit sollen
- **[소제목]** Gebrauch → 쓰임
- **[작은 단원]** Konjunktiv II → 접속법 2식
- **[소제목]** Bildung → 만들기
- **[굵은 제목]** K II der Gegenwart → K II 현재
- **[공식 박스]** Präteritumstamm + -e, -est, -e, -en, -et, -en → 과거 어간 + 접속법 어미
  - 설명: 인칭 어미는 K I과 같음

#### 오른쪽 단

- **[굵은 제목]** K II der Vergangen[heit] → K II 과거
- **[공식 박스]** haben oder sein im [K II] + Partizip Perfekt → haben 또는 sein의 K II + 과거분사
- **[굵은 제목]** Die Formen der Hilfsverben im Konjunktiv II → 조동사의 접속법 2식
  - 설명: sein · haben · werden 표
- **[굵은 제목]** Alternative zum Konjunktiv II → K II 대신 쓰는 말
  - 설명: würde + 원형
- **[굵은 제목]** Passiv im Konjunktiv II → 접속법 2식의 수동
- **[공식 박스]** Gegenwart: werden im K II + Partizip II → 현재: werden의 K II + 과거분사
- **[공식 박스]** Vergangenheit: sein im K II + Partizip II + worden → 과거: sein의 K II + 과거분사 + worden
- **[굵은 제목]** Konjunktiv II mit Modalverben → 화법조동사의 접속법 2식
- **[공식 박스]** Gegenwart: Modalverb im K II + Infinitiv → 현재: 화법조동사의 K II + 원형
- **[공식 박스]** Vergangenheit: haben im K II + Infinitiv + Modalverb im Infinitiv → 과거: haben의 K II + 원형 + 화법조동사 원형
- **[소제목]** Gebrauch → 쓰임
  - 설명: Höfliche Bitte · Höfliche Ratschläge · Irreale Aussagen · Irrealer Vergleich
