import Record as new
import HtmlFormat as html
import CsvFormat as csv
import View

value = None

def CallMenu():
    View.InterfaceMenu()

def ItemMenu():
    global value
    value = View.Item()

def ChoiceItem():
    global value
    match value:
        case '1':
            new.NewRecord(View.Record())
        case '2':
            html.GoToHtml()
        case '3':
            csv.GoToCsv()