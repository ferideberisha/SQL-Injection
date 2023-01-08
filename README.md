# SiguriaNeInternet
Zhvillimi i aplikacionit që mundëson SQL Injection teste të automatizuara në një URL të caktuar

Ky është një aplikacion tkinter GUI që lejon përdoruesin të futë një URL dhe ta skanojë atë për dobësi të mundshme të injektimit SQL.
Hapat e mëposhtëm kryhen:

 - Importojmë bibliotekat e nevojshme (tkinter, kërkesat, BeautifulSoup, urljoin).
 - Krijojmë dritaren kryesore tkinter dhe vendosim vetitë e saj (madhësia, ripërmasat, titulli).
 - Krijojmë një fushë etikete(label) dhe fusha e futjes së tekstit që përdoruesi të shkruajë URL-në.
 - Krijojmë një fushë etikete(label) dhe fushë teksti për përgjigjen që do të shfaqet.
 - Inicializojmë një sesion HTTP dhe vendosim një agjent përdoruesi për modulin e kërkesave.
 - Përcaktojmë funksionin get_all_forms, i cili merr një URL dhe kthen të gjitha format që gjenden në përmbajtjen HTML të faqes.
 - Përcaktojmë funksionin get_form_details, i cili merr një formë dhe kthen një fjalor me informacione të dobishme rreth formularit, duke përfshirë URL-në e veprimit, metodën dhe detajet hyrëse.
 - Përcaktojmë funksionin is_vulnerable, i cili merr një përgjigje dhe nëse faqja është potencialisht e cenueshme ndaj injektimit SQL bazuar në përmbajtjen e përgjigjes.
 - Përcaktojmë funksionin scan_sql_injection, i cili merr një URL dhe kryen një sërë testesh për të kontrolluar për dobësitë e injektimit SQL. Këto teste përfshijnë testimin e vetë URL-së dhe testimin e të gjitha formave të gjetura në faqe.
 - Krijojmë butonin e dërgimit dhe përcaktojmë sjelljen e tij kur klikojmë. Butoni dërgo merr URL-në nga fusha e hyrjes, ekzekuton funksionin scan_sql_injection dhe shfaq rezultatin në fushën e përgjigjes.
 - Drejtojmë ciklin kryesor për dritaren tkinter.
 
 ![Foto1](https://user-images.githubusercontent.com/93921511/211205686-7e1c4c43-7869-47a1-9353-97bbcaa641f9.png)

