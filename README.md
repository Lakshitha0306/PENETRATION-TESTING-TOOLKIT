# 🔒 Web Application Vulnerability Scanner

COMPANY : CODTECH IT SOLUTIONS

NAME : LAKSHITHA R

INTERN ID : CITSOD467

DOMAIN : CYBER SECURITY AND ETHICAL HACKING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

## 📌 Internship Task 1 — Web Vulnerability Scanner  
*Domain:* Cyber Security  
*Task:* Detect common web application vulnerabilities using Python  
*Created by:* Lakshitha R  
*Submitted for:* CodTech IT Internship – Task 1  

---

## 📁 About the Project

This is a simple Python-based tool that scans websites for two of the most common web vulnerabilities:

- ✅ *SQL Injection*
- ✅ *Cross-Site Scripting (XSS)*

The tool uses the requests and BeautifulSoup libraries to:
- Detect and extract all HTML forms
- Auto-fill the forms with test payloads
- Submit them
- Analyze the response to check for signs of vulnerabilities

---

## 🧠 Key Features

- 🔍 Finds and tests all input forms in the given URL
- 📥 Submits test payloads to simulate real-world attacks
- 🚨 Alerts if SQLi or XSS vulnerabilities are detected
- ⚙ Works on HTTP GET and POST methods

---

## 🔧 Technologies Used

| Tool/Library     | Purpose                     |
|------------------|-----------------------------|
| Python 3.x       | Programming language         |
| requests       | Sending HTTP requests        |
| BeautifulSoup4 | Parsing and extracting HTML  |

---

## ▶ How to Run the Program

### 1. ✅ Install Required Libraries
Make sure you have Python 3 installed, then run:
```bash
pip install requests beautifulsoup4

2. 📁 Save the Python Script

Save the script as scanner.py.

3. 🚀 Run the Script

python scanner.py

4. 🌐 Enter Target URL

Example:

http://testphp.vulnweb.com

> ⚠ Test only on legal targets!
Use websites like http://testphp.vulnweb.com or http://demo.testfire.net which are intentionally made for testing.




---

📌 Sample Payloads Used

Vulnerability	Payload

SQL Injection	' OR '1'='1
XSS	<script>alert('XSS')</script>



---

🧾 Output Example

🔍 Scanning for SQL Injection...
[+] SQL Injection vulnerability found!

🔍 Scanning for XSS...
[-] No XSS vulnerability found.


---

📚 What I Learned

How input forms work in web apps

Basic ethical hacking and security testing

Automating vulnerability scans with Python

Hands-on with SQLi and XSS


OUTPUT:

