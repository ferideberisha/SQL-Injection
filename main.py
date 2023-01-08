#importojmë libraritë që na duhen
import tkinter as tk
from tkinter import END
import json
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from IPython.utils import frame

# krijojmë dritaren kryesore
window = tk.Tk()
window.geometry("800x690")
window.resizable(False, False)
window.title("SQL Injection Scanner")

# krijojmë fushën e hyrjes së URL-së
url_label = tk.Label(master=window, text="URL:")
url_label.pack()
url_input = tk.Entry(window, width=107)
url_input.pack()

# krijojmë fushën e hyrjës së Response
response_label = tk.Label(master=window, text="Response:")
response_label.pack()
response_field = tk.Text(master=window, height=35, width=95)
response_field.pack()

# inicializojmë një sesion HTTP dhe vendosim shfletuesin
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

def get_all_forms(url):
    # Duke pasur një `URL`, ai kthen të gjitha format nga përmbajtja HTML
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    # Ky funksion nxjerr të gjithë informacionin e mundshëm të dobishëm në lidhje me një 'formë' HTML
    details = {}
    # marrim veprimin (action) e formës (url-ja e synuar)
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # marrim metodën e formës (POST, GET, etj)
    method = form.attrs.get("method", "get").lower()
    # marrim të gjitha detajet e input-eve sikur tipi dhe emri
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    # vendosim gjithçka në fjalorin e rezultateve
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def is_vulnerable(response):
    #Një funksion i thjeshtë boolean që përcakton nëse një faqe është SQL Injection e cenueshme nga "përgjigja" e saj
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # nëse gjen ndonjë prej këtyre error-eve rikthen True
        if error in response.content.decode().lower():
            return True
    # asnjë error nuk është detektuar
    return False


def scan_sql_injection(url):
    # test në URL
    for c in "\"'":
        # shtojmë karakterin e thonjëzës të njëfishtë/dyfishtë në URL
        new_url = f"{url}{c}"
        response_field.insert(tk.END, f"\n[!] Trying {new_url}")
        # bëjmë krkesën HTTP
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection është detektuar në vet URL-në
            # nuk ka nevojë të paraprihet për ekstratimin e formave dhe dorëzimin e tyre
            response_field.insert(tk.END, f"\nSQL Injection vulnerability detected, link: {new_url}")
            return
    # test në format HTML
    forms = get_all_forms(url)
    response_field.insert(tk.END, f"\n[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            # rivendosim të dhënat
            data = {}
            # trupi i të dhënave që duam të dorëzojmë
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    # çdo formë hyrëse që është e fshehur ose ka ndonjë vlerë,
                    # thjesht përdorim atë në trupin e formës
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # të gjithë të tjerët përveç 'submit', përdorin disa të dhëna të padëshiruara me karakter të veçantë
                    data[input_tag["name"]] = f"test{c}"
            # bashko URL-në me veprimin (formo URL-në e kërkesës)
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
                if not is_vulnerable(res):
                    response_field.insert(tk.END, f"\nSQL Injection vulnerability detected, link: {url}")
                    response_field.insert (tk.END, "\n[+] Form:")
                    response_field.insert(tk.END, json.dumps(form_details, indent=4))
            break
        else:
            response_field.insert(tk.END, "\nSQL Injection vulnerability not detected")

# krijojmë butonin 'submit'
def submit():
    url = url_input.get()
    scan_sql_injection(url)

submit_button = tk.Button(master=window, text="Submit", command=submit)
submit_button.pack()
submit_button.place(x=170, y=640, width=185)

#krijojmë butonin 'clear'
def clearclicked():
    url_input.delete(0,END)
    response_field.delete('1.0', END)

button1 = tk.Button(master=window, text='Clear',command=clearclicked)
button1.pack()
button1.place(x=415, y=640, width=185)

# ekzekutojmë ciklin kryesor
window.mainloop()
