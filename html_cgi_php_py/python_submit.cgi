#!C:\Users\info\AppData\Local\Programs\Python\Python312\python.exe

# Modul cgi
import cgi, cgitb


# Modul cgi with: error handling
cgitb.enable()


# Field check
def check_field(field_name: str) -> str:
    global form
    if form.getvalue(field_name):
        return form.getvalue(field_name)
    else:
        return 'Not set'


# Formular
form = cgi.FieldStorage()


# HTML
print("Content-Type: text/html")
print()

print("<!DOCTYPE html>")
print("<head><meta charset='UTF-8'><title>Python CGI</title></head>")
print("<body>")
print("<h1>Python CGI</h1>")
print("<p>Forename:", check_field('forename'), "</p>")
print("<p>Surname:", check_field('surname'), "</p>")
print("</body>")
print("</html>")