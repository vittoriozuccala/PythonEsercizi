# Video https://www.youtube.com/watch?v=u04Cq0aed_4
# Documentazione: https://docxtpl.readthedocs.io/en/latest/
import pandas as pd
import docx.shared as ds
import docxtpl as dt

todos_df = pd.DataFrame(
    {
        'title': ['Buy Domain', 'Buy Web Hosting', 'Setup Wordpress', 'Payment Option'],
        'description': ['Buy Domain', 'Buy Web Hosting', 'Setup Wordpress', 'Payment Option'],
        'note': ['','','Also mySQL', 'Compare alternatives for payment options']
    }
)

doc = dt.DocxTemplate('template.docx')
logo = dt.InlineImage(doc, 'logo.png', width=ds.Mm(30))

context = {
    'project_name': 'Tutorial Project ',
    'project_deadline': '2027-01-01',
    'person_in_charge': 'Mike',
    'dedicated_budget': '€5000',
    'todos': todos_df.to_dict(orient='records'),
    'logo': logo
}

doc.render(context)
doc.save('output.docx')