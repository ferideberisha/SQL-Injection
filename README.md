# SiguriaNeInternet
Zhvillimi i aplikacionit që mundëson SQL Injection teste të automatizuara në një URL të caktuar

Ky është një aplikacion tkinter GUI që lejon përdoruesin të futë një URL dhe ta skanojë atë për dobësi të mundshme të injektimit SQL.
Hapat e mëposhtëm kryhen:

 - Importojmë bibliotekat e nevojshme (tkinter, kërkesat, BeautifulSoup, urljoin).
 - Krijojmë dritaren kryesore tkinter dhe vendosim vetitë e saj (madhësia, ripërmasat, titulli).
 - Krijojmë një fushë etikete(label) dhe fusha e futjes së tekstit që përdoruesi të shkruajë URL-në.
 - Krijojmë një fushë etikete(label) dhe fushë teksti për përgjigjen që do të shfaqet.
 - Inicializojmë një sesion HTTP dhe vendosim një agjent përdoruesi për modulin e kërkesave.
