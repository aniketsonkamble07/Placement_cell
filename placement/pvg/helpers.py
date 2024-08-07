# helpers.py
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import xlsxwriter
import io

def studentlist_pdf(template_source, context_dict={}):
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)  # Encode as UTF-8
    if not pdf.err:
        return result.getvalue()
    return None


def studentlist_xls(queryset):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Write headers
    headers = ['CRN Number', 'Name', 'Branch', 'Year', 'Gender', 'Email', 'Mobile Number',
               'CGPA', 'Aggregate Marks', '10th Marks', '12th Marks', 'Diploma Marks',
               'Active Backlog', 'Year Down', 'Remarks']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write data
    row = 1
    for student in queryset:
        worksheet.write(row, 0, student.crn_number)
        worksheet.write(row, 1, student.name)
        worksheet.write(row, 2, student.branch)
        worksheet.write(row, 3, student.year)
        worksheet.write(row, 4, student.gender)
        worksheet.write(row, 5, student.email)
        worksheet.write(row, 6, student.mobile_number)
        worksheet.write(row, 7, student.CGPA)
        worksheet.write(row, 8, student.aggregate_marks)
        worksheet.write(row, 9, student.mark_10th)
        worksheet.write(row, 10, student.mark_12th)
        worksheet.write(row, 11, student.diploma_marks)
        worksheet.write(row, 12, student.active_backlog)
        worksheet.write(row, 13, student.year_down)
        worksheet.write(row, 14, student.remarks)
       
        row += 1

    workbook.close()
    output.seek(0)
    return output.getvalue()