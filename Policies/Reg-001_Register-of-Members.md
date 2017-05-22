# [DRAFT] RZZT Policy Document Reg-001: Register of Members

This policy document sets out the legislative requirements for maintaining the Register of Members, and establishes procedures for meeting those requirements.

## Legislative requirements

The _Companies Act 2006_ (UK) c 46 ('CA2006') requires all companies to maintain a Register of Members, unless a private company elects to keep this information on a Government-held public register: CA2006 ss 112A, 113. RZZT maintains its own register to protect the personal information of its members.

The Register of Members _must_ contain (a) the names and address of the members, (b) the date on which each person was registered as a member, and (c) the date at which any person ceased to be a member: CA2006 s 113.

The Register of Members must be kept available for inspection at the company's registered office: CA2006 s 114. This requirement is satisfied if it is maintained in electronic form and accessible from the registered office. If the membership exceeds 50 members, an index must be kept: s 115. This can be satisfied by keeping the Register in indexed (that is, alphabetically-ordered) form: s 115.

All members have the right to inspect the Register of Members free of charge, and any other person may inspect it on payment of a fee: CA2006 s 116(1). Any person may request a full or partial copy of the Register on payment of a fee: CA2006 s 116(2). Requests must contain (a) the name and address of the person making the request, (b) the purpose for which the information is to be used, and (c) whether the information will be disclosed to any other person, the other person's name and address, and the purpose for which the information is to be used by that person: CA2006 s 116(4).

If a request to inspect or be given a copy of the Register of Members is made, the Company must comply with the request or apply to the court within five working days: CA2006 s 117(1). If an application to the court is made, it must notify the person who made the request: CA2006 s 117(2). If the court is satisfied that the inspection or copy is not sought for a proper purpose it shall direct the company not to comply with the request and may order that the company's costs be paid in whole or part by the person who made the request: CA2006 s 117(3).

Refusal or failure to permit inspection or provide a copy other than in accordance with an order of the court, an offence is committed by the company and every officer of the company who is in default: CA2006 s 118. It is also an offence to knowingly or recklessly make statements that are misleading, false or deceptive in a request, or to disclose or fail to prevent disclosure of the information: CA2006 s 119.

A company must inform a person who requests to inspect or be given a copy of the Register of Members of the most recent date on which alterations were made to the register and whether there are further alterations to be made: s 120(1). Failure to provide this information is an offence committed by the company and every officer of the company who is in default: CA2006 s 120(3).

An entry relating to a former member may be removed only after they have ceased to be a member for at least 10 years: CA2006 s 121.

## Maintaining the Register of Members

The Company Secretary shall maintain the Register of Members, including updating and removing the details of members as necessary and appropriate. The members shall be listed alphabetically by surname, forenames and date of membership from least recent to most recent.

The Register of Members shall be kept electronically, in such form as to be available from the Company's registered office, and accessible at all times by the Company Secretary and Directors with the exception of routine maintenance and unplanned outages.

The Company Secretary shall make and keep a current backup copy or copies of the Register (in addition to any other backup copies) which must be accessible to the Company Secretary at least once every five working days.

The Directors may also choose to make and keep backup copies of their own.

## Contents of the Register of Members

The Register of Members shall include the following information about each member as required by law:

- their full forename(s) and surname,
- their address,
- the date on which they became a member, and
- the date on which they ceased to be a member.

The address must be a physical address, not a PO box or DX address, but need not be the member's usual residential address.

The Register of Members shall also include the following information about each member:

- their email address intended to be used for correspondence between them and the Company, and
- their IRC nickname intended to be used for participation in meetings of the Company.

A member's email address must not be an address provided by the Company to the member by virtue of their being a member or officer of the Company.

## Updating the Register of Members

The Company Secretary must update the Register of Members to reflect any changes within five working days of being notified that amendments are required.

The Company Secretary must not remove any person from the Register of Members unless ten years has passed since the person ceased to be a member of the Company.

## Requests to inspect and be given a copy of the Register of Members

Any person may request, in writing, to inspect or be given a copy of the Register of Members, or part thereof. If the person making such request is a member, no charge shall be imposed. If the person making such request is not a member, a charge may be imposed as determined by the Directors.

All requests must include the following details:

- the name of the person making the request,
- the address of the person making the request,
- the purpose for which the information is to be used, and
- whether the information will be disclosed to any other person, and, if so:
  - the names and addresses of all persons to which the information will be disclosed, and
  - the purpose for which the information is to be used by such persons.

If the information will not be disclosed to any other person, the person making the request must include a statement to that effect.

The Company Secretary shall comply with a request to inspect or be given a copy of the Register of Members within five working days, unless they suspect the request has not been made for a proper purpose and the Directors have instructed them to apply to the court for an order permitting refusal to comply with the request. If an application to the court is made, the Secretary shall notify the person who made the request.

When complying with a request, the Company Secretary shall make all reasonable efforts to ensure that the Register is up-to-date, and shall inform the person making the request of:

- the most recent date on which alterations were made, and
- whether there are outstanding alterations which are yet to be made.

If the Company Secretary believes, or has reasonable grounds to believe, that a person has knowingly or recklessly made statements that are misleading, false or deceptive in a request, or has disclosed or failed to prevent disclosure of the information, they may inform the relevant authorities.

## Technical procedure

A Python script has been created to process company registers and create static HTML pages containing the required information. For the Register of Members, this script processes a CSV file named 'register-of-members.csv' and creates a file called 'register-of-members.html'. As a CSV file, it can be edited with standard spreadsheet and text editing software.

### Columns

The Register of Members CSV file includes the following columns:

- surname
- forenames
- address
- email,
- irc,
- joined, and
- terminated.

Each column corresponds with the information required by this policy. The address format should be the standard format used in the relevant country, but should always include a postcode, and be surrounded by double inverted commas (") to preserve commas. The 'joined' and 'terminated' columns are the dates the person became and ceased to be a member respectively, and should be in ISO 8601 extended format (YYYY-MM-DD).
