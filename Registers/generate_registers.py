database = [
    {
        "register": "Members",
        "headings": [
            "Name and correspondence address",
            "Email address",
            "Date became member",
            "Date ceased to be member"
        ],
        "entries": [
            {
                "surname": "Littler", # Full surname
                "forenames": "Alexander", # All forenames
                "correspondence_address": "8 Sydney Road, Mount Knowles, New South Wales, 2850, Australia", # Nominated correspondence address
                "email": "alittler@example.com", # Email address
                "begin": "2016-10-06", # Date membership began
                "end": "" # Date membership ended
            },
            {
                "surname": "Myers",
                "forenames": "William",
                "correspondence_address": "2539 Essendene Avenue, Abbotsford, British Columbia, V2S 2H7, Canada",
                "email": "wmyers@example.com",
                "begin": "2015-01-16",
                "end": ""
            },
            {
                "surname": "Collier",
                "forenames": "Toby",
                "correspondence_address": "44 Holburn Lane, Heaton, SK11 8YD, England, United Kingdom",
                "email": "tcollier@example.com",
                "begin": "2015-12-03",
                "end": ""
            },
            {
                "surname": "Saucedo",
                "forenames": "Aileen",
                "correspondence_address": "4665 Chestnut Street, Polk City, Florida, 33868, United States of America",
                "email": "asaucedo@example.com",
                "begin": "2014-10-19",
                "end": ""
            },
            {
                "surname": "Reliford",
                "forenames": "Sharon",
                "correspondence_address": "34 SH 1, Regent, Whangarei, 0112, New Zealand",
                "email": "sreliford@example.com",
                "begin": "2015-02-26",
                "end": ""
            },
            {
                "surname": "Alonso",
                "forenames": "Fabiana",
                "correspondence_address": "Instituto Medico La Floresta, Piso 2, Consultorio 214, La Floresta, Caracas, Venezuela",
                "email": "falonso@example.com",
                "begin": "2015-09-15",
                "end": ""
            },
            {
                "surname": "Letourneau",
                "forenames": "Fifi",
                "correspondence_address": "77 Rue St Ferreol, Metz, Lorraine, 57050, France",
                "email": "fletourneau@example.com",
                "begin": "2014-12-17",
                "end": ""
            },
            {
                "surname": "Mehrotra",
                "forenames": "Adharma",
                "correspondence_address": "A/2, Jay Yashwant Chamber, Bhandup Village, Uday Shri Road, Bhandup(e), Mumbai, Maharashtra, 400042, India",
                "email": "amehrotra@example.com",
                "begin": "2016-03-15",
                "end": ""
            }
        ]
    },
    {
        "register": "Directors",
        "headings": [
            "Name(s) and service address",
            "Email address",
            "Residence",
            "Nationality",
            "Business occupation",
            "Date of birth",
            "Date of appointment",
            "Date of termination"
        ],
        "entries": [
            {
                "surname": "Littler", # Full surname
                "forenames": "Alexander", # All forenames
                "former_names": "Alex Littler", # Former names used in business in last 20 years, separated by a comma
                "service_address": "The company's registered office", # Address for service of documents; can be 'The company's registered office'
                "email": "alittler@rzzt.io", # Company (not personal) email address
                "residence": "New South Wales, Australia", # State, country or part of the UK in which ordinarily resident
                "nationality": "Australian", # Nationality; if multiple provide all separated by a comma
                "occupation": "Consultant", # Usual business occupation
                "dob": "1991-08-04", # Date of birth (YYYY-MM-DD)
                "appointed": "2016-10-06", # Date appointed (YYYY-MM-DD)
                "terminated": "" # Date terminated (YYYY-MM-DD)
            },
            {
                "surname": "Saucedo",
                "forenames": "Aileen",
                "former_names": "",
                "service_address": "The company's registered office",
                "email": "asaucedo@rzzt.io",
                "residence": "Florida, USA",
                "nationality": "American",
                "occupation": "Software developer",
                "dob": "1993-03-05",
                "appointed": "2014-10-19",
                "terminated": ""
            },
            {
                "surname": "Mehrotra",
                "forenames": "Adharma",
                "former_names": "",
                "service_address": "The company's registered office",
                "email": "amehrotra@rzzt.io",
                "residence": "Maharashtra, India",
                "nationality": "Indian",
                "occupation": "Journalist",
                "dob": "1989-06-22",
                "appointed": "2016-03-15",
                "terminated": ""
            }
        ]
    },
    {
        "register": "Directors' Residential Addresses",
        "headings": [
            "Name",
            "Residential address"
        ],
        "entries": [
            {
                "surname": "Littler", # Full surname
                "forenames": "Alexander", # All forenames
                "residential_address": "8 Sydney Road, Mount Knowles, New South Wales, 2850, Australia" # Usual residential address
            },
            {
                "surname": "Saucedo",
                "forenames": "Aileen",
                "residential_address": "4665 Chestnut Street, Polk City, Florida, 33868, United States of America"
            },
            {
                "surname": "Mehrotra",
                "forenames": "Adharma",
                "residential_address": "A/2, Jay Yashwant Chamber, Bhandup Village, Uday Shri Road, Bhandup(e), Mumbai, Maharashtra, 400042, India"
            }
        ],
    },
    {
        "register": "Secretaries",
        "headings": [
            "Name",
            "Former names",
            "Service address",
            "Email address",
            "Date of appointment",
            "Date of termination"
        ],
        "entries": [
            {
                "surname": "Reliford", # Full surname
                "forenames": "Sharon", # All forenames
                "former_names": "", # Former names used in business in last 20 years, separated by a comma
                "service_address": "The company's registered office", # Address for service of documents; can be 'The company's registered office'
                "email": "sreliford@rzzt.io", # Company (not personal) email address
                "appointed": "2016-03-15",
                "terminated": ""
            }
        ]
    }
]

output = ""

for data in database:
    output += "<tr>"
    for heading in data["headings"]:
        output += "<th>" + heading + "</th>"
    output += "</tr><tr>"
    if data["register"] is "Members":
        for entry in data["entries"]:
            output += "<td><span class='name'>" + entry["forenames"] + " " + entry["surname"] + "</span><br>"
            output += entry["correspondence_address"] + "</td>"
            output += "<td>" + entry["email"] + "</td>"
            output += "<td>" + entry["begin"] + "</td>"
            if entry["end"] is "":
                output += "<td>-</td></tr>"
            else:
                output += "<td>" + entry["end"] + "</td></tr>"
    if data["register"] is "Directors":
        for entry in data["entries"]:
            output += "<td><span class='name'>" + entry["forenames"] + " " + entry["surname"] + "</span><br>"
            if entry["former_names"] is not "":
                output += "<span class='former-name'>" + entry["former_names"] + "</span><br>"
            output += entry["service_address"] + "</td>"
            output += "<td>" + entry["email"] + "</td>"
            output += "<td>" + entry["residence"] + "</td>"
            output += "<td>" + entry["nationality"] + "</td>"
            output += "<td>" + entry["occupation"] + "</td>"
            output += "<td nowrap>" + entry["dob"] + "</td>"
            output += "<td nowrap>" + entry["appointed"] + "</td>"
            if entry["terminated"] is "":
                output += "<td>-</td>"
            else:
                output += "<td>" + entry["terminated"] + "</td>"
            output += "</tr>"
    if data["register"] is "Directors' Residential Addresses":
        for entry in data["entries"]:
            output += "<td><span class='name'>" + entry["forenames"] + " " + entry["surname"] + "</span></td>"
            output += "<td>" + entry["residential_address"] + "</td></tr>"
    if data["register"] is "Secretaries":
        for entry in data["entries"]:
            output += "<td><span class='name'>" + entry["forenames"] + " " + entry["surname"] + "</span></td>"
            if entry["former_names"] is "":
                output += "<td>-</td>"
            else:
                output += "<td>" + entry["former_names"] + "</td>"
            output += "<td>" + entry["service_address"] + "</td>"
            output += "<td>" + entry["email"] + "</td>"
            output += "<td nowrap>" + entry["appointed"] + "</td>"
            if entry["terminated"] is "":
                output += "<td>-</td>"
            else:
                output += "<td>" + entry["terminated"] + "</td>"
            output += "</tr>"
    open("register-of-%s.html" % data["register"].lower().replace(" ","-").replace("'",""),"w").write(open("template.html","r").read().replace("{register_name}",data["register"]).replace("{register}",output))
    output = ""
