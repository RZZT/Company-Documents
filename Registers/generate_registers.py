import sys

reload(sys)
sys.setdefaultencoding('utf8')

import csv

output = '<tr>'

# Register of Members

with open('register-of-members.csv') as csvfile:
    headings = ['Name and correspondence address','Email address and IRC nickname','Joined','Terminated']
    for heading in headings:
        output += '<th>' + heading + '</th>'
    output += '</tr>'
    for row in csv.DictReader(csvfile):
        output += '<tr><td><strong>' + row['forenames'] + ' ' + row['surname'] + '</strong><br>' + row['address'] + '</td><td>' + row['email'] + '<br>' + row['irc'] + '</td><td nowrap>' + row['joined'] + '</td><td nowrap>' + row['terminated'] + '</td></tr>'
    open('register-of-members.html','w').write(open('template.html','r').read().replace('{register_name}','Members').replace('{register}',output.encode('ascii', 'xmlcharrefreplace')))
    output = '<tr>'

# Register of Directors

with open('register-of-directors.csv') as csvfile:
    headings = ['Name(s) and service address','Email address and IRC nickname','Residence','Nationality','Business occupation','Date of birth','Appointed','Terminated']
    for heading in headings:
        output += '<th>' + heading + '</th>'
    output += '</tr>'
    for row in csv.DictReader(csvfile):
        output += '<tr><td><strong>' + row['forenames'] + ' ' + row['surname'] + '</strong><br>'
        if row['former_names'] is not '':
            output += '<em>' + row['former_names'] + '</em><br>'
        output += row['service_address'] + '</td><td>' + row['email'] + '<br>' + row['irc'] + '</td><td>' + row['residence'] + '</td><td>' + row['nationality'] + '</td><td>' + row['occupation'] + '</td><td nowrap>' + row['dob'] + '</td><td nowrap>' + row['appointed'] + '</td><td nowrap>' + row['terminated'] + '</td></tr>'
    open('register-of-directors.html','w').write(open('template.html','r').read().replace('{register_name}','Directors').replace('{register}',output.encode('ascii', 'xmlcharrefreplace')))
    output = '<tr>'

# Register of Directors' Residential Addresses

with open('register-of-directors-residential-addresses.csv') as csvfile:
    headings = ['Name','Residential address']
    for heading in headings:
        output += '<th>' + heading + '</th>'
    output += '</tr>'
    for row in csv.DictReader(csvfile):
        output += '<tr><td>' + row['forenames'] + ' ' + row['surname'] + '</td><td>' + row['residential_address'] + '</td></tr>'
    open('register-of-directors-residential-addresses.html','w').write(open('template.html','r').read().replace('{register_name}',"Directors' Residential Addresses").replace('{register}',output.encode('ascii', 'xmlcharrefreplace')))
    output = '<tr>'

# Register of Secretaries

with open('register-of-secretaries.csv') as csvfile:
    headings = ['Name(s) and service address','Email address and IRC nickname','Appointed','Terminated']
    for heading in headings:
        output += '<th>' + heading + '</th>'
    output += '</tr>'
    for row in csv.DictReader(csvfile):
        output += '<tr><td><strong>' + row['forenames'] + ' ' + row['surname'] + '</strong><br>'
        if row['former_names'] is not '':
            output += '<em>' + row['former_names'] + '</em><br>'
        output += row['service_address'] + '</td><td>' + row['email'] + '<br>' + row['irc'] + '</td><td nowrap>' + row['appointed'] + '</td><td nowrap>' + row['terminated'] + '</td></tr>'
    open('register-of-secretaries.html','w').write(open('template.html','r').read().replace('{register_name}','Secretaries').replace('{register}',output.encode('ascii', 'xmlcharrefreplace')))
    output = '<tr>'
