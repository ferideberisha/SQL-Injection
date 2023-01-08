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
 - Ekzekutojmë ciklin kryesor për dritaren tkinter.
 
 Ekzekutimi i aplikacionit dhe përgjigja e tij në raste të ndyshme: 
 
 ![Foto1](https://user-images.githubusercontent.com/93921511/211205686-7e1c4c43-7869-47a1-9353-97bbcaa641f9.png)

![Foto2](https://user-images.githubusercontent.com/93921511/211205743-12d02947-112e-4989-af8d-887e8a2ceb43.png)

![Foto3](https://user-images.githubusercontent.com/93921511/211205750-a4cf670f-6245-4ac2-99f8-e79bd64dcddb.png)

Linqet e testuara: http://128.198.49.198:8102/mutillidae/index.php?page=user-info.php, http://testphp.vulnweb.com/artists.php?artist=1, https://www.facebook.com/
