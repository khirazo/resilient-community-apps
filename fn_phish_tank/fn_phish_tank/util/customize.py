# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_phish_tank"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_phish_tank package"""
    reload_params = {"package": u"fn_phish_tank",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"phish_tank_check_url"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_phish_tank"], 
                    "functions": [u"fn_phish_tank_submit_url"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_phishtank_submit_url"], 
                    "actions": [u"Example: PhishTank: Submit URL"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     phish_tank_check_url
    #   Message Destinations:
    #     fn_phish_tank
    #   Functions:
    #     fn_phish_tank_submit_url
    #   Workflows:
    #     example_phishtank_submit_url
    #   Rules:
    #     Example: PhishTank: Submit URL


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogIjMxMGVkMmZiLWRkYzEt
NDk3OS1iNjJlLTRjNjQzNWZjOWJjNSIsICJkZXNjcmlwdGlvbiI6ICJTZWFyY2hlcyB0aGUgUGhp
c2hUYW5rIGRhdGFiYXNlIChodHRwczovL3d3dy5waGlzaHRhbmsuY29tLykgdG8gZGV0ZXJtaW5l
IGlmIGEgVVJMIGlzIGEgcGhpc2hpbmcgVVJMIG9yIG5vdC4gVGhlIGluZm9ybWF0aW9uIHJldHVy
bmVkIGZyb20gUGhpc2hUYW5rIGlzIHVzZWQgdG8gdXBkYXRlIHRoZSBBcnRpZmFjdHMgZGVzY3Jp
cHRpb24gYW5kIGFkZCBhIG5vdGUgdG8gdGhlIGluY2lkZW50LiIsICJvYmplY3RfdHlwZSI6ICJh
cnRpZmFjdCIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfcGhpc2h0YW5rX3N1Ym1pdF91cmwiLCAi
d29ya2Zsb3dfaWQiOiAzNiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20i
LCAiY29udGVudCI6IHsieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVU
Ri04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4v
MjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9C
UE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9E
RC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQv
MjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20v
YnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1s
bnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJn
ZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1c
ImV4YW1wbGVfcGhpc2h0YW5rX3N1Ym1pdF91cmxcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFt
ZT1cIkV4YW1wbGU6IFBoaXNoVGFuazogU3VibWl0IFVSTFwiPjxkb2N1bWVudGF0aW9uPlNlYXJj
aGVzIHRoZSBQaGlzaFRhbmsgZGF0YWJhc2UgKGh0dHBzOi8vd3d3LnBoaXNodGFuay5jb20vKSB0
byBkZXRlcm1pbmUgaWYgYSBVUkwgaXMgYSBwaGlzaGluZyBVUkwgb3Igbm90LiBUaGUgaW5mb3Jt
YXRpb24gcmV0dXJuZWQgZnJvbSBQaGlzaFRhbmsgaXMgdXNlZCB0byB1cGRhdGUgdGhlIEFydGlm
YWN0cyBkZXNjcmlwdGlvbiBhbmQgYWRkIGEgbm90ZSB0byB0aGUgaW5jaWRlbnQuPC9kb2N1bWVu
dGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNl
cXVlbmNlRmxvd18xbWluN28zPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlk
PVwiU2VydmljZVRhc2tfMTV0ZTR3alwiIG5hbWU9XCJQaGlzaCBUYW5rIFN1Ym1pdCBVUkxcIiBy
ZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6
ZnVuY3Rpb24gdXVpZD1cIjViOWU2NzE3LThjOWQtNGZkMy1iZWYzLTQ2ZmFlMDg5ZjFiMVwiPntc
ImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiZGVmIGFwcGVuZF9hcnRp
ZmFjdF9kZXNjcmlwdGlvbih0aGVfYXJ0aWZhY3QsIHRoZV90ZXh0KTpcXG4gIFxcXCJcXFwiXFxc
IkFwcGVuZHMgdGhlX3RleHQgdG8gdGhlX2FydGlmYWN0LmRlc2NyaXB0aW9uIHNhZmVseVxcbiAg
aGFuZGxpbmcgdW5pY29kZVxcXCJcXFwiXFxcIlxcbiAgXFxuICBuZXdfZGVzY3JpcHRpb24gPSB1
XFxcIlxcXCJcXG4gIFxcbiAgaWYgdGhlX2FydGlmYWN0LmRlc2NyaXB0aW9uIGlzIE5vbmU6XFxu
ICAgIGN1cnJlbnRfZGVzY3JpcHRpb24gPSBOb25lXFxuICBlbHNlOlxcbiAgICBjdXJyZW50X2Rl
c2NyaXB0aW9uID0gdGhlX2FydGlmYWN0LmRlc2NyaXB0aW9uLmdldChcXFwiY29udGVudFxcXCIs
IE5vbmUpXFxuXFxuICBpZiBjdXJyZW50X2Rlc2NyaXB0aW9uIGlzIG5vdCBOb25lOlxcbiAgICBu
ZXdfZGVzY3JpcHRpb24gPSB1XFxcInswfSZsdDticiZndDstLS0mbHQ7YnImZ3Q7ezF9XFxcIi5m
b3JtYXQodW5pY29kZShjdXJyZW50X2Rlc2NyaXB0aW9uKSwgdW5pY29kZSh0aGVfdGV4dCkpXFxu
XFxuICBlbHNlOlxcbiAgICBuZXdfZGVzY3JpcHRpb24gPSB1XFxcInswfVxcXCIuZm9ybWF0KHVu
aWNvZGUodGhlX3RleHQpKVxcblxcbiAgdGhlX2FydGlmYWN0LmRlc2NyaXB0aW9uID0gaGVscGVy
LmNyZWF0ZVJpY2hUZXh0KG5ld19kZXNjcmlwdGlvbilcXG5cXG5cXG5pZiByZXN1bHRzLnN1Y2Nl
c3M6XFxuICBcXG4gICMgR2V0IHRoZSBQaGlzaFRhbmsgUmVzdWx0c1xcbiAgcGhpc2hfdGFua19y
ZXN1bHRzID0gcmVzdWx0cy5jb250ZW50LmdldChcXFwicmVzdWx0c1xcXCIsIHt9KVxcbiAgdXJs
ID0gcGhpc2hfdGFua19yZXN1bHRzLmdldChcXFwidXJsXFxcIiwgdVxcXCJcXFwiKVxcbiAgaW5f
ZGF0YWJhc2UgPSBwaGlzaF90YW5rX3Jlc3VsdHMuZ2V0KFxcXCJpbl9kYXRhYmFzZVxcXCIsIEZh
bHNlKVxcbiAgaXNfdmVyaWZpZWQgPSBwaGlzaF90YW5rX3Jlc3VsdHMuZ2V0KFxcXCJ2ZXJpZmll
ZFxcXCIsIEZhbHNlKVxcbiAgaXNfdmFsaWQgPSBwaGlzaF90YW5rX3Jlc3VsdHMuZ2V0KFxcXCJ2
YWxpZFxcXCIsIEZhbHNlKVxcbiAgXFxuICAjIERlZmluZSB0aGUgY29tbWVudCBhbmQgbXNnIHRv
IGJlIGFwcGVuZGVkIHRvIHRoZSBBcnRpZmFjdCdzIERlc2NyaXB0aW9uXFxuICBjb21tZW50ID0g
dVxcXCJcXFwiXFxuICBtc2cgPSB1XFxcIlxcXCJcXFwiJmx0O2ImZ3Q7UGhpc2hUYW5rIExvb2t1
cCZsdDsvYiZndDsgaGFzIGNvbXBsZXRlXFxuICAgICAgICAgICAgJmx0O2JyJmd0OyZsdDtiJmd0
O1VSTDombHQ7L2ImZ3Q7IHswfSZsdDsvYiZndDtcXG4gICAgICAgICAgICAmbHQ7YnImZ3Q7Jmx0
O2ImZ3Q7Rm91bmQgaW4gRGF0YWJhc2U6Jmx0Oy9iJmd0OyB7MX1cXFwiXFxcIlxcXCIuZm9ybWF0
KHVybCwgdW5pY29kZShpbl9kYXRhYmFzZSkpXFxuXFxuICBpZiBub3QgaW5fZGF0YWJhc2U6XFxu
ICAgIGNvbW1lbnQgPSB1XFxcIk5vdGhpbmcga25vd24gYWJvdXQgdGhpcyB1cmxcXFwiXFxuICBc
XG4gIGVsc2U6XFxuICAgIHBoaXNoX2lkID0gcGhpc2hfdGFua19yZXN1bHRzLmdldChcXFwicGhp
c2hfaWRcXFwiKVxcbiAgICBwaGlzaF9kZXRhaWxfcGFnZV91cmwgPSBwaGlzaF90YW5rX3Jlc3Vs
dHMuZ2V0KFxcXCJwaGlzaF9kZXRhaWxfcGFnZVxcXCIpXFxuICAgIFxcbiAgICBtc2cgPSB1XFxc
IlxcXCJcXFwiezB9XFxuICAgICAgICAgICZsdDticiZndDsmbHQ7YiZndDtQaGlzaCBJRDombHQ7
L2ImZ3Q7IHsxfVxcbiAgICAgICAgICAmbHQ7YnImZ3Q7Jmx0O2ImZ3Q7VmFsaWQgUGhpc2g6Jmx0
Oy9iJmd0OyB7Mn1cXG4gICAgICAgICAgJmx0O2JyJmd0OyZsdDtiJmd0O1ZlcmlmaWVkOiZsdDsv
YiZndDsgezN9XFxuICAgICAgICAgICZsdDticiZndDsmbHQ7YiZndDtMaW5rIHRvIFBoaXNoVGFu
azogJmx0O2EgaHJlZj17NH0mZ3Q7ezR9Jmx0Oy9hJmd0OyZsdDsvYiZndDtcXFwiXFxcIlxcXCIu
Zm9ybWF0KG1zZywgcGhpc2hfaWQsIHVcXFwiWWVzXFxcIiBpZiBpc192YWxpZCBlbHNlIHVcXFwi
Tm9cXFwiLCB1XFxcIlllc1xcXCIgaWYgaXNfdmVyaWZpZWQgZWxzZSBcXFwiTm9cXFwiLCBwaGlz
aF9kZXRhaWxfcGFnZV91cmwpXFxuICAgIFxcbiAgICBpZiBpc192ZXJpZmllZCBhbmQgaXNfdmFs
aWQ6XFxuICAgICAgY29tbWVudCA9IHVcXFwiVmVyaWZpZWQ6IElzIGEgcGhpc2hpbmcgc2l0ZVxc
XCJcXG4gIFxcbiAgICBlbGlmIGlzX3ZlcmlmaWVkIGFuZCBub3QgaXNfdmFsaWQ6XFxuICAgICAg
Y29tbWVudCA9IHVcXFwiVGhpcyBzaXRlIGlzIG5vdCBhIHBoaXNoaW5nIHNpdGVcXFwiXFxuICAg
ICAgXFxuICAgIGVsaWYgbm90IGlzX3ZlcmlmaWVkOlxcbiAgICAgIGNvbW1lbnQgPSB1XFxcIlRo
aXMgdXJsIGhhcyBub3QgYmVlbiB2ZXJpZmllZFxcXCJcXG4gIFxcbiAgbXNnID0gdVxcXCJcXFwi
XFxcInswfSZsdDticiZndDsmbHQ7YnImZ3Q7Jmx0O2ImZ3Q7Q29tbWVudDombHQ7L2ImZ3Q7IHsx
fVxcXCJcXFwiXFxcIi5mb3JtYXQobXNnLCBjb21tZW50KVxcbiAgXFxuICBhcHBlbmRfYXJ0aWZh
Y3RfZGVzY3JpcHRpb24oYXJ0aWZhY3QsIG1zZylcXG4gIGluY2lkZW50LmFkZE5vdGUoaGVscGVy
LmNyZWF0ZVJpY2hUZXh0KG1zZykpXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMgR2V0
IHRoZSB1cmwgZnJvbSB0aGUgQXJ0aWZhY3QncyBWYWx1ZVxcbmlucHV0cy5waGlzaF90YW5rX2No
ZWNrX3VybCA9IGFydGlmYWN0LnZhbHVlXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNp
b25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzFtaW43bzM8L2luY29taW5nPjxvdXRn
b2luZz5TZXF1ZW5jZUZsb3dfMHd0ejk4aTwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48c2VxdWVu
Y2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFtaW43bzNcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50
XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18xNXRlNHdqXCIvPjxlbmRFdmVudCBp
ZD1cIkVuZEV2ZW50XzA2eGo1ZGxcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB3dHo5OGk8L2lu
Y29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wd3R6OThp
XCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMTV0ZTR3alwiIHRhcmdldFJlZj1cIkVuZEV2ZW50
XzA2eGo1ZGxcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3Jh
bV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQ
TU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1
NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjIzNFwiIHk9XCI4OVwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjIyOVwiIHk9XCIx
MjRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzE1dGU0d2pcIiBpZD1cIlNlcnZpY2VUYXNr
XzE1dGU0d2pfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4
PVwiNDAzXCIgeT1cIjY3XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJw
bW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzFtaW43bzNcIiBpZD1cIlNlcXVlbmNlRmxvd18xbWlu
N28zX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIyNzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjEwN1wiLz48b21nZGk6d2F5cG9pbnQgeD1cIjQwM1wiIHhzaTp0eXBlPVwib21nZGM6
UG9pbnRcIiB5PVwiMTA3XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjI5MS41XCIgeT1cIjg1LjVcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwi
RW5kRXZlbnRfMDZ4ajVkbFwiIGlkPVwiRW5kRXZlbnRfMDZ4ajVkbF9kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjYxMFwiIHk9XCI4OVwiLz48YnBtbmRp
OkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCI5MFwiIHg9XCI1
ODNcIiB5PVwiMTI4XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJw
bW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wd3R6OThpXCIgaWQ9XCJT
ZXF1ZW5jZUZsb3dfMHd0ejk4aV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNTAzXCIgeHNpOnR5
cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMDdcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI2MTBcIiB4
c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjEwN1wiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCI5MFwiIHg9XCI1MTEuNVwiIHk9XCI4NS41
XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxh
bmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAi
ZXhhbXBsZV9waGlzaHRhbmtfc3VibWl0X3VybCIsICJ2ZXJzaW9uIjogMn0sICJsYXN0X21vZGlm
aWVkX3RpbWUiOiAxNTYyMDUzMjM0OTY1LCAiY3JlYXRvcl9pZCI6ICJpbnRlZ3JhdGlvbnNAZXhh
bXBsZS5jb20iLCAiYWN0aW9ucyI6IFtdLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9w
aGlzaHRhbmtfc3VibWl0X3VybCIsICJuYW1lIjogIkV4YW1wbGU6IFBoaXNoVGFuazogU3VibWl0
IFVSTCJ9XSwgImFjdGlvbnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIkV4YW1w
bGU6IFBoaXNoVGFuazogU3VibWl0IFVSTCIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwg
IndvcmtmbG93cyI6IFsiZXhhbXBsZV9waGlzaHRhbmtfc3VibWl0X3VybCJdLCAib2JqZWN0X3R5
cGUiOiAiYXJ0aWZhY3QiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImU4NDVl
NTE1LTAzZmQtNDZkYy04MTUwLTY4NTFkMTlmNDY4YSIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJFeGFtcGxlOiBQaGlzaFRhbms6IFN1Ym1pdCBVUkwiLCAiY29uZGl0aW9ucyI6
IFt7InR5cGUiOiBudWxsLCAiZXZhbHVhdGlvbl9pZCI6IG51bGwsICJmaWVsZF9uYW1lIjogImFy
dGlmYWN0LnR5cGUiLCAibWV0aG9kIjogImVxdWFscyIsICJ2YWx1ZSI6ICJVUkwifV0sICJpZCI6
IDQ5LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXX1dLCAibGF5b3V0cyI6IFtdLCAiZXhwb3J0
X2Zvcm1hdF92ZXJzaW9uIjogMiwgImlkIjogMzYsICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNl
cyI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVsbCwgImxvY2FsZSI6IG51bGws
ICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgInZlcnNpb24iOiAiMzEuMC40MjU0Iiwg
ImJ1aWxkX251bWJlciI6IDQyNTQsICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3
b3Jrc3BhY2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRp
c3BsYXlfbmFtZSI6ICJQaGlzaCBUYW5rIFN1Ym1pdCBVUkwiLCAiZGVzY3JpcHRpb24iOiB7ImNv
bnRlbnQiOiAiU2VhcmNoZXMgdGhlIFBoaXNoVGFuayBkYXRhYmFzZSAoaHR0cHM6Ly93d3cucGhp
c2h0YW5rLmNvbS8pIHRvIGRldGVybWluZSBpZiBhIFVSTCBpcyBhIHBoaXNoaW5nIFVSTCBvciBu
b3QuIFRoZSBpbmZvcm1hdGlvbiByZXR1cm5lZCBmcm9tIFBoaXNoVGFuayBpcyB1c2VkIHRvIHVw
ZGF0ZSB0aGUgQXJ0aWZhY3RzIGRlc2NyaXB0aW9uIGFuZCBhZGQgYSBub3RlIHRvIHRoZSBpbmNp
ZGVudC4iLCAiZm9ybWF0IjogInRleHQifSwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJP
cmNoZXN0cmF0aW9uIEVuZ2luZSIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAzOCwgIm5hbWUiOiAi
aW50ZWdyYXRpb25zQGV4YW1wbGUuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51
bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNl
LCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiZTNjOWU0NDYtOTM1Yy00ZDdk
LTliYzAtOTlhZGQ2OTMyMDk5IiwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJleHBvcnRfa2V5Ijog
ImZuX3BoaXNoX3Rhbmtfc3VibWl0X3VybCIsICJ1dWlkIjogIjViOWU2NzE3LThjOWQtNGZkMy1i
ZWYzLTQ2ZmFlMDg5ZjFiMSIsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAi
QWRtaW4gVXNlciIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiA3MSwgIm5hbWUiOiAiYWRtaW5AZXhh
bXBsZS5jb20ifSwgInZlcnNpb24iOiAyLCAid29ya2Zsb3dzIjogW3siZGVzY3JpcHRpb24iOiBu
dWxsLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAiYWN0aW9ucyI6IFtdLCAibmFtZSI6ICJF
eGFtcGxlOiBQaGlzaFRhbms6IFN1Ym1pdCBVUkwiLCAid29ya2Zsb3dfaWQiOiAzNiwgInByb2dy
YW1tYXRpY19uYW1lIjogImV4YW1wbGVfcGhpc2h0YW5rX3N1Ym1pdF91cmwiLCAidXVpZCI6IG51
bGx9XSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NjIwNTM5NTcwNjgsICJkZXN0aW5hdGlvbl9o
YW5kbGUiOiAiZm5fcGhpc2hfdGFuayIsICJpZCI6IDY4LCAibmFtZSI6ICJmbl9waGlzaF90YW5r
X3N1Ym1pdF91cmwifV0sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxs
LCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1NjIwNTM5Njg2MTcsICJkZXNj
cmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tl
eSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQiOiAwLCAibmFtZSI6
ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRlX2RhdGUiOiAxNTYy
MDUzOTY4NjE3LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAi
LCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAi
aGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rl
c3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiZDljYjU5NjItZTU0Mi00NzIzLThiZjItOGZkNzUxOWZl
Mzk4IiwgImV4cG9ydF9rZXkiOiAiZm5fcGhpc2hfdGFuayIsICJuYW1lIjogImZuX3BoaXNoX3Rh
bmsiLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9waGlz
aF90YW5rIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImludGVncmF0aW9uc0BleGFt
cGxlLmNvbSJdfV0sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwg
ImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAwLCAib3BlcmF0aW9uX3Bl
cm1zIjoge30sICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJw
cmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDM4LCAicmVhZF9vbmx5Ijog
dHJ1ZSwgInV1aWQiOiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgImNo
b3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgInRvb2x0aXAiOiAiV2hldGhl
ciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRo
aXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWlu
aW5nIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJuYW1lIjogImluY190cmFpbmluZyIs
ICJkZXByZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwg
InZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgInRleHQiOiAicGhpc2hfdGFua19jaGVja191cmwiLCAiYmxhbmtfb3B0
aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDI0
NSwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJlM2M5ZTQ0Ni05MzVjLTRkN2QtOWJjMC05
OWFkZDY5MzIwOTkiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9v
bHRpcCI6ICJVUkwgdG8gbG9va3VwIGluIFBoaXNoVGFuaydzIERhdGFiYXNlIiwgImludGVybmFs
IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICJfX2Z1bmN0aW9uL3BoaXNoX3RhbmtfY2hlY2tfdXJsIiwgImhpZGVfbm90aWZpY2F0aW9u
IjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICJodHRwOi8vd3d3LmV4YW1wbGUuY29tIiwgIm5hbWUi
OiAicGhpc2hfdGFua19jaGVja191cmwiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjog
W119XSwgIm92ZXJyaWRlcyI6IFtdLCAiZXhwb3J0X2RhdGUiOiAxNTYyMDUzOTY2NzQ1fQ==
"""
    )