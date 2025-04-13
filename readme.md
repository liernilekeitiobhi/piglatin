# 🐷 WEB APLIKAZIO BATEN SORRERA – Pig Latin Itzultzailea

Programa hau *Pig Latin* hizkuntzara esaldiak itzultzen dituen web aplikazio bat da. Aplikazioa Python-eko **Flask** web framework-arekin sortua dago eta ondorengo egitura du:

```
/templates
    index.html
/static
    /css
        style.css
    /js
        main.js
    /img
        pig.jpg
utils.py
app.py
```

---

## 💻 1. EDITORE BAT AUKERATU

Kodea editatzeko, **Visual Studio Code** oso aukera ona da. Honako estekatik deskarga daiteke:  
👉 [Visual Studio Code deskargatu](https://code.visualstudio.com/download)

Editorearen ezker aldean karpeten egitura ikusiko dugu, eta bertan fitxategiak eta karpetak sor ditzakegu. Fitxategiaren amaierako `.py`, `.html`, `.css`... bezalako luzapenei esker, VSC-k zein hizkuntza erabiliko dugun automatikoki antzematen du.

---

## 🧪 2. FLASK ERABILTZEKO PRESTATU

Flask erabili ahal izateko, lehenik eta behin instalatu behar dugu. Horretarako, VSC-ren terminala ireki:

> **Terminal → New Terminal**

Terminalean honako komandoa idatzi:

```
pip install flask
```

**💡 Oharra**: *pip* da Python-en paketak (libreriak edo moduluak) instalatzeko tresna nagusia.

Honekin, Flask zure sisteman instalatuta egongo da eta bere funtzioak erabilgarri izango dira.

---

## 🧠 3. KODEAREN AZALPEN OROKORRA

Fitxategi bakoitzak zer funtzio duen azaltzen da. Kodearen barruan komentario gehiago daude, xehetasun gehiagorekin.

### Ulertu beharreko kontzeptuak:

1. HTTP eskaera motak: **GET** eta **POST**
2. JavaScript-eko `fetch()` metodoa
3. Nola idatzi HTML-eko `<div>` batean JS bidez

---

### `app.py`

Programa nagusia da. Bi URL kudeatzen ditu:

1. `/` (root): `index.html` kargatzen du.
2. `/translation`: POST eskaera bat jasotzen du, esaldia Pig Latin hizkuntzara itzultzen du, eta itzulpena frontend-era bidaltzen du JSON formatuan.

---

### `index.html`

Erabiltzaileak ikusiko duen orrialde nagusia da. Bertan daude:

- Esaldi bat sartzeko formularioa  
- Itzulpena eskatzeko botoia  
- Itzulpena agertzeko HTML elementu bat  

Fitxategi hau honako hauekin konektatuta dago:

- `style.css` (estiloa)
- `main.js` (logika)

---

### `style.css`

HTML orrialdeari estilo bisual erakargarri bat ematen dio. Koloreak, tamainak eta antolaketa hemen definitzen dira.

---

### `main.js`

Erabiltzaileak botoia sakatzean gertatzen dena kudeatzen du:

- Formularioaren edukia jasotzen du  
- `/translation` URL-era POST bidez bidaltzen du  
- Jasotako itzulpena HTML-an erakusten du  

---

### `utils.py`

Pig Latin-era itzultzeko logika hemen kokatzen da. `app.py`-tik funtzio hau inportatzen da, kodea antolatuago egoteko.

---

## 🚀 4. APLIKAZIOA LOKALEAN EXEKUTATU

Zerbitzari lokal batean abiarazteko, terminalean honako komandoa idatzi:

```
flask --app app run
```

Honekin aplikazioa martxan egongo da helbide honetan:  
👉 `http://127.0.0.1:5000`

---

## ☁️ 5. APLIKAZIOA ZERBITZARI EXTERNO BATEAN ARGITARATU

Aplikazioa **Render.com** bezalako doako zerbitzari batera igo daiteke.

### Pausoak:

1. Git biltegia hasieratu:

```
git init
```

2. Fitxategi guztiak gehitu:

```
git add .
```

3. Egindako aldaketak gorde:

```
git commit -m "Lehen bertsioa"
```

4. GitHub-erako urruneko biltegia gehitu:

```
git remote add origin <zure-repositorioaren-URL-a>
```

5. Aldaketak GitHub-era bidali:

```
git push -u origin main
```
**💡 Oharra**: Hau lehen aldiz soilik egin behar da. Ondoren `add .` eta `commit -m "egindako aldaketen azalpena"` egin ondoren nahikoa da `git push`


6. Render.com-en kontua sortu eta GitHub-era konektatu. Proiektua hautatu, eta zure Flask aplikazioa automatikoki exekutatuko da.


