#!/usr/bin/env python

# shape of html

title_tag = "TITLE-STRING"
menu_tag = "MENU-HTML"
content_tag = "CONTENT-HTML"
filename_tag = "FILENAME-DOT-HTML"
dates_tag = "DATES-TABLE"

format = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TITLE-STRING</title>
<link rel="stylesheet" href="main.css">
</head>
<body>
<nav>
MENU-HTML
</nav>
<article><div class="content">
CONTENT-HTML
</div></article>
<footer style="text-align:center;">
</footer>
</body>
</html>"""

validate_link = """ - <a style="color:grey;" href="https://validator.w3.org/nu/?doc=http%3A%2F%2Fwww.cse.chalmers.se%2F~myreen%2Fcade-26%2FFILENAME-DOT-HTML">FILENAME-DOT-HTML</a>"""

dates_table = """<table class="dates">
    <tbody>
      <tr><td>Submission for formal review (pre-symposium review):</td>          <td>March 26, 2018</td></tr>
      <tr><td>Submission of draft papers (post-symposium review):</td>           <td><s>April 26, 2018</s><br/><b>May 11, 2018</b></td></tr>
      <tr><td>Notification (pre-symposium review):</td>                          <td>May 3, 2018</td></tr>
      <tr><td>Notification (post-symposium review):</td>                         <td><s>May 3, 2018</s><br/><b>May 13, 2018</b></td></tr>
      <tr><td>Registration:</td>                                                 <td>June 3, 2018</td></tr>
      <tr><td>TFP Symposium:</td>                                                <td>June 11-13, 2018</td></tr>
      <tr><td>TFPIE Workshop:</td>                                               <td>June 14, 2018</td></tr>
      <tr><td>Student papers feedback:</td>                                      <td>June 21, 2018</td></tr>
      <tr><td>Submission for formal review (post-symposium review):</td>         <td><s>August 14, 2018</s><br/><b>August 24, 2018</b></td></tr>
      <tr><td>Notification of acceptance (post-symposium review):</td>           <td><s>September 20, 2018</s><br/><b>September 30, 2018</b></td></tr>
      <tr><td>Camera-ready submission (both pre- and post-symposium review):</td><td>November 30, 2018</td></tr>
    </tbody>
  </table>"""


# a list, where each item is: filename, title, in_menu, is_local page

pages = [("index","TFP 2018",True,True),
         ("program","Programme",True,True),
         ("cfp","Call for Papers",True,True),
         ("registration","Registration",True,True),
         ("excursion","Social Dinner",True,True),
         ("venue","Local Information",True,True)]

# generate html

def get_menu(filename):
  str = '<ul>\n'
  for (i, (filename,title,in_menu,is_local)) in enumerate(pages):
    if i == 0:
      title_proper = '<strong>' + title + '</strong>'
    else:
      title_proper = title;

    if in_menu:
      if is_local:
        str += '<li><a href="'+filename+'.html">'+title_proper+'</a></li>\n'
      else:
        str += '<li><a href="'+filename+'" target="_blank">'+title_proper+'</a></li>\n'
  str += '</ul>\n'
  return str

validate_html = ""

for (i, (filename,title,in_menu,is_local)) in enumerate(pages):
  if (is_local):
    with open(filename+'.txt', 'r') as content_file:
      content = content_file.read()
    if i == 0:
      title_proper = title
    else:
      title_proper = "TFP 2018: " + title

    html = format.replace(title_tag,title_proper)
    html = html.replace(menu_tag,get_menu(filename))
    html = html.replace(content_tag,content)
    html = html.replace(filename_tag,filename+'.html')
    html = html.replace(dates_tag,dates_table)
    with open(filename+'.html', 'w') as html_file:
      html_file.write(html)
    validate_html += validate_link.replace(filename_tag,filename+'.html') + '\n'

validate_html = """<html><head><link rel="stylesheet" href="style2.css"></head><body><pre><b>Validate:</b>""" + '\n' + validate_html + "</pre></body></html>"

with open('validate.html', 'w') as html_file:
  html_file.write(validate_html)
