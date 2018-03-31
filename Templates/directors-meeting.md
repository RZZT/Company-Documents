# Directors' meeting template

This template is to be used for minuting Directors' meetings. For the most part it is a simple matter of filling in the blanks as appropriate. Please find instructions below.

## Template

```
---
layout: meeting
title: Minutes of Directors' meeting
date:
location:
directors:
secretary:
apologies:
members:
quorum:
chair:
notice:
agenda:
next-meeting:
close-meeting:
---

## Agenda item 1

```

## Instructions

This template is compiled with the rest of the Company's website. Completed minutes should be placed in the `_minutes` director of the Company's website repository.

### Dates and times

This section affects the `date`, `next-meeting` and `close-meeting` fields of the template.

Each field should be entered using the ISO 8601 format of `YYYY-MM-DD HH-MM` (eg, 2017-09-07 12:30), using UTC (GMT) time. The time zone does not need to be specified, as it will automatically assume UTC is used.

The `date` field is the date and time of when the current meeting began. The `next-meeting` field is the date and time of the next meeting. The `close-meeting` field is the date and time that the current meeting was closed.

If the Directors did not set a date and time for the next meeting, the `next-meeting` field can be left blank or deleted entirely.

### Location

The `location` field is the location of the meeting. This may be 'online via IRC' or 'at International House, 776–778 Barking Road, London, United Kingdom'. It is important to include the word 'online', 'in' or 'at' as appropriate, so that the minutes render correctly.

### Attendance

This section affects the `directors`, `secretary`, `apologies` and `members` fields of the template.

Each of these fields takes a list, for example:

```
directors:
- director 1
- director 2
- director 3
```

The `directors` and `secretary` fields are for Directors and Company Secretaries respectively who are present at the meeting, even if they arrive after the start of the meeting. Arrivals and departures from the meeting should be noted thus:

```
---
[Name] joined (or left) the meeting at 05:27.
---
```

Apologies should be recorded where a Director or Secretary has informed the Board that they are unable to attend the meeting. Other persons are not required to give apologies, and should not be recorded.

The `members` field may be used to record members in attendance.

The attendance of other persons should be recorded as appropriate in the minutes generally. This may be before the first agenda item:

```
The Directors noted the presence of [name (role)].

## Agenda item 1
```

### Quorum

The `quorum` field is used to record whether the minimum number of Directors required for a meeting to be valid are in attendance. If quorum has been met, the value should be `satisfied`; otherwise `unsatisfied` should be entered.

### Chair

The `chair` field is used to record the person appointed chair for the meeting.

### Notice

The `notice` field is used to record whether or not adequate notice of the meeting has been given. There are three possible values:

- `given` — when the required period of notice has been given.
- `dispensed` — when the required period of notice has been dispensed with by consent.
- `urgent` — when the required period of notice has been dispensed with due to urgent circumstances.

### Agenda

The `agenda` field takes a list of agenda items. It does not need to include matters dealt with by the frontmatter of the minutes template.
