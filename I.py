Порушується:
class PrinterScanner:
    def print_document(self, document):
        print(f"Printing {document}")

    def scan_document(self, document):
        print(f"Scanning {document}")

    def fax_document(self, document):
        print(f"Faxing {document}")

# Клас PrinterScanner реалізує всі методи для принтера, сканера і факсу


Приклад застосування в Python:

class Printer:
    def print(self, document):
        pass


class Scanner:
    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print(f"Printing {document}")

    def scan(self, document):
        print(f"Scanning {document}")
