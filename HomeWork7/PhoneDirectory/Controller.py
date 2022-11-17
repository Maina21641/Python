import Record as new
import HtmlFormat as html
import view

value = None

def CallMenu():
    view.InterfaceMenu()

def ItemMenu():
    global value
    value = view.Item()

def ChoiceItem():
    global value
    match value:
        case '1':
            new.NewRecord(view.Record())
        case '2':
            html.GoToHtml()