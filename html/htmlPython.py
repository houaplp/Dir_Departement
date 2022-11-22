telephone={'guitare - chant':'Jean-Louis Aubert',
    'guitare':'Louis Bertignac',
    'basse':'Corinne Marienneau',
    'batterie':'Richard Kolinka'}
"""
<table border=1>
<tr backgroundcolor=green>
<td>Le plus grand groupe français</td>
</tr>
</table>
<table>
"""
for item in telephone.keys():
    print ("<tr><td>%s</td><td>%s</td></tr>" %(item,telephone[item]))
"</table>"
