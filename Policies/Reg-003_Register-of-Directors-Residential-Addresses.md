# [DRAFT] RZZT Policy Document Reg-003: Register of Directors' Residential Addresses

This policy document sets out the legislative requirements for maintaining the Register of Directors' Residential Addresses, and establishes procedures for meeting those requirements. **This policy should be read together with RZZT Policy Document Reg-002: Register of Directors.**

## Legislative requirements

The _Companies Act 2006_ (UK) c 46 ('CA2006') requires all companies to maintain a Register of Directors' Residential Addresses, unless a private company elects to keep this information on a Government-held public register: CA2006 ss 161A, 165(1). RZZT maintains its own register to protect the personal information of its directors.

The Register of Directors' Residential Addresses _must_ state the usual residential address of each of the company's directors: CA2006 s 165(2). By extension, it must also include sufficient information to identify the the Director to whom an entry relates, such as their full name. A Director's usual residential address _may_ be the same as their service address (in which case 'The Director's service address' is acceptable) but _may not_ be the Company's registered office: CA2006 s 165(3).

The Registrar must be notified withn 14 days if a person becomes or ceases to be a director, or if any existing director's particulars required to be contained in the Register of Directors' Residential Addresses has changed: CA2006 s 167(1). Notice that a person has become a director must contain a statement of their usual residential address, and must confirm that the person has consented to act in that capacity: CA2006 s 167(2). If a director's service address changes but no change is required to their usual residential address, the notice to the Registrar must be accompanied by a statement that no such change is required: CA2006 s 167(3).

The Register of Directors' Residential Addresses is not required to be kept available at any specific location, or to be made available for inspection by members of the Company or the public.

## Maintaining the Register of Directors' Residential Addresses

The Company Secretary shall maintain the Register of Directors' Residential Addresses, including updating the details of Directors as necessary and appropriate.

The Register of Directors shall be kept electronically, in such form as to be accessible at all times by the Company Secretary and Directors with the exception of routine maintenance and unplanned outages.

The Company Secretary shall make and keep a current backup copy or copies of the Register (in addition to any other backup copies) which must be accessible to the Company Secretary at least once every five working days.

The Directors may also choose to make and keep backup copies of their own.

## Contents of the Register of Directors' Residential Addresses

The Register of Directors' Residential Addresses shall include the following information about each Director:

- their full forename(s) and surname, and
- their residential address.

## Updating the Register of Directors' Residential Addresses

The Company Secretary must update the Register of Directors' Residential Addresses to reflect any changes within five working days of being notified that amendments are required.

The Company Secretary must not remove any person from the Register of Directors' Residential Addresses, regardless of whether they have ceased to be a Director.

## Requests to inspect and be given a copy of the Register of Directors' Residential Addresses

No officer of the Company shall disclose the contents of the Register of Directors' Residential Addresses except as required by law or directed by lawful order.

## Technical procedure

A Python script has been created to process company registers and create static HTML pages containing the required information. For the Register of Directors' Residential Addresses, this script processes a CSV file named 'register-of-directors-residential-addresses.csv' and creates a file called 'directors-residential-addresses.html'. As a CSV file, it can be edited with standard spreadsheet and text editing software.

### Columns

The Register of Directors CSV file includes the following columns:

- surname
- forenames,
- residential_address

Each column corresponds with the information required by this policy. The 'residential_address' should be in the standard format used in the relevant country, should always include a postcode, and be surrounded by double inverted commas (") to preserve commas.
