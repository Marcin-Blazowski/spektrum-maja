# Spektrum

Gra Spektrum by Maja — dla dwóch osób i jednego urządzenia, w przeglądarce.

Jedna osoba widzi ukryty cel na tarczy i podaje jedno hasło; druga ustawia
wskazówkę tam, gdzie jej zdaniem to hasło pasuje. Punkty: 4 za sam środek,
3 obok, 2 na skraju celu, 0 poza nim. Role zmieniają się co rundę, wynik jest
wspólny. 70 kart z przeciwieństwami, tasowanych bez powtórek.

## Jak grać

Otwórz `index.html` w przeglądarce (dwuklik albo `microsoft-edge index.html`).
Działa offline; jedyne, co strona pobiera z sieci, to fonty Google.

## Jak budować

```bash
python3 build.py
```

- `src/spektrum.html` — **źródło, tu się robi zmiany.** To treść strony bez
  `<!doctype>`, `<head>` i `<body>`, bo w takiej postaci publikuje się ją jako
  artefakt na claude.ai, który dokleja własny szkielet i reset CSS.
- `index.html` — **plik generowany, nie edytuj go ręcznie.** `build.py` dokleja
  równoważny szkielet, dzięki czemu ta sama gra działa z dysku i z GitHub Pages.

Po każdej zmianie w `src/spektrum.html` uruchom `build.py`, zanim sprawdzisz
`index.html` w przeglądarce.

## Publikacja na claude.ai

Link do gry: <https://claude.ai/artifact/9ztSqqi5TfyB8AS7Pj2mE7>

Publikuje się przez narzędzie Artifact w Claude Code — nie ma na to polecenia
w terminalu. Wystarczy poprosić: „opublikuj grę". Claude wysyła wtedy
`src/spektrum.html` (nigdy `index.html` — on ma już własny `<!doctype>`
i szkielet, a claude.ai dokleiłby drugi).

**W nowej rozmowie trzeba podać powyższy URL**, żeby Claude zaktualizował ten
artefakt w miejscu. Bez URL-a powstanie drugi, osobny artefakt z innym linkiem,
a stary zostanie z nieaktualną wersją.

Artefakt jest prywatny. Żeby ktoś inny mógł go otworzyć, trzeba go udostępnić
z menu Share na stronie artefaktu — Claude nie może tego zmienić.

Kolejność przy zmianach: edycja `src/spektrum.html` → `python3 build.py`
(dla wersji lokalnej i GitHub Pages) → publikacja artefaktu.

## Hosting

`index.html` jest samowystarczalny, więc wystarczy włączyć GitHub Pages dla
gałęzi `main` (katalog główny) — koszt zero. Wtedy gra działa z linku na każdym
telefonie, bez logowania.
