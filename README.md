# Auf einen Blick

**독일어 학습 지도 (시제 · 화법)**

독일어의 시제와 화법(법)을 한 장의 표로 정리한 사이트입니다. 프랑스어 학습 지도([lestempslespronomslesrelatifs](https://hyungwookha.github.io/lestempslespronomslesrelatifs))의 독일어판입니다.

**접속 주소:** https://hyungwookha.github.io/aufeinenblick

## 이 사이트는

- **정보 전달용 참고 자료입니다.** 연습 문제나 점수 기능은 없습니다.
- **한 장의 표:** 가로 = 시간 (과거완료 · 과거 · 현재완료 · 현재 · 미래1 · 미래2), 세로 = 화법 (직설법 · 접속법 Ⅰ · 접속법 Ⅱ · 명령법) × 능동 / 수동·동작 / 수동·상태.
- **예시 동사 두 개:** 표 위 버튼으로 *fragen* (약변화 · 타동사 · *haben* 지배)과 *bleiben* (강변화 · 자동사 · *sein* 지배)을 오갑니다. *bleiben*은 수동이 없어서 수동 줄이 「수동 없음」으로 바뀝니다.
- **칸을 누르면** 표 아래에 그 칸의 PONS 설명(만드는 법, 쓰임, 예문)이 열립니다. 맨 아래 「칸 밖의 규칙」에는 여러 칸에 걸치는 내용(기본형, 어간, 조동사, 어순 등)이 접혀 있습니다.
- **휴대폰에서 읽기 좋게** 만들었습니다. 화면 폭 390px 기준으로 확인했고, 다크 모드를 지원합니다.

## 표 안의 표시

| 표시 | 뜻 |
|---|---|
| 파란 굵은 상자 + 「원인」「결과」 | 직설법에서 능동 완료형(원인) → 짝 시제의 상태수동(결과). 과거완료 → 과거, 현재완료 → 현재, 미래2 → 미래1 |
| 빨간 점선 상자 | 시제 일치: 같은 시제의 능동 = 동작수동 (과거 · 현재 · 미래1) |
| 노란 「완료」 상자 | 접속법은 과거 쪽이 완료형 하나뿐 |
| 점선 동그라미 | 접속법 Ⅱ 미래2. *würde*의 자리 (정리 예정) |
| 「거의 안 씀²」 | PONS 표에서 「거의 쓰지 않음」 각주가 붙은 형태 |

## 출처

| 내용 | 출처 |
|---|---|
| 능동 · 수동(동작) 형태, 각주 | PONS 『Auf einen Blick – Deutsch Zeiten』 (2016) |
| 초록 설명 상자 | 위 표와 PONS 『Auf einen Blick – Deutsch Grammatik』 (Renate Weber, 2003/2006)을 한국어로 요약. 블록마다 표의 위치(쪽 · 단)를 적음 |
| 수동·상태 줄, 명령법 줄, 원인 → 결과 · 시제 일치 표시 | 이 사이트가 덧붙인 것 |

Zeiten 자료의 `[ ]`는 사진 반사로 가려진 글자를 문맥으로 채운 것입니다. 실물로 확인되면 `[ ]`를 지웁니다.

## 화면 기능

- **다크 모드:** 오른쪽 위 버튼. localStorage `aufeinenblick-theme`에 저장됩니다.
- **항목별 바로가기:** 칸을 누르면 주소 끝이 그 칸으로 바뀝니다 (`#perfekt`, `#passiv_vorgang`, `#k2-gegenwart-vorgang`, `#bleiben/k1-vergangenheit`). 그 주소로 들어오면 그 설명이 바로 열리고, 「링크 복사」 버튼으로 복사할 수 있습니다.
- **서버·빌드 없음:** `index.html` 하나가 혼자 동작합니다. 글꼴(Gowun Batang, IBM Plex Sans KR, Newsreader)만 Google Fonts에서 불러옵니다.

## 고칠 때 볼 곳

`index.html` 맨 위 `:root` CSS 변수가 색상입니다 (다크 모드 포함).

| 이름 | 내용 |
|---|---|
| `VERBS` | 동사별 칸 내용 (`fragen`, `bleiben` → `IND`, `K1`, `K2`, `IMP`) |
| `RARE` | 「거의 안 씀」 표시를 다는 칸 |
| `CAUSE`, `SAME` | 파란 상자(원인 → 결과), 빨간 점선 상자(시제 일치)를 그릴 칸 |
| `cellInfo()` | 칸마다 열 PONS 항목 id와 주소 이름 |
| `RULES` | 「칸 밖의 규칙」에 넣을 항목 |
| `PONS` | PONS 설명 데이터. `/*DATA-START*/ … /*DATA-END*/` 사이는 손으로 고치지 않습니다 |

### PONS 자료 (`data/`)

| 파일 | 내용 |
|---|---|
| `pons-de-zeiten-notes.json`, `pons-de-zeiten-extract.md` | PONS 『Auf einen Blick – Zeiten』 정리 |
| `pons-de-tense-notes.json`, `pons-de-extract.md` | PONS 『Auf einen Blick – Grammatik』 정리 |

JSON을 고친 뒤에는 저장소 맨 위 폴더에서 `python3 tools/build-data.py`를 실행하면 `index.html`의 `PONS` 데이터가 다시 만들어집니다.
