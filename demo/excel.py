import xlwt
from datetime import datetime


def set_style(font_name, font_height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = font_name  # 'Times New Roman'
    font.height = font_height
    font.bold = bold
    font.colour_index = 4

    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders
    return style


def write_to_excel_xlwt():
    '''Write content to a new excel'''
    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet("SheetName_test")
    new_sheet.write(0, 0, "hello")
    # write cell with style
    new_sheet.write(0, 1, "world", set_style("Times New Roman", 220, True))

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    new_sheet.write(1, 0, 1234.56, style0)
    new_sheet.write(1, 1, datetime.now(), style1)

    # write cell with formula
    new_sheet.write(2, 0, 5)
    new_sheet.write(2, 1, 8)
    new_sheet.write(3, 0, xlwt.Formula("A3+B3"))

    new_workbook.save(r"NewCreateWorkbook.xls")  # if change to xlsx,then open failed


if __name__ == "__main__":
    write_to_excel_xlwt()
