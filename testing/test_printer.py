from unittest import TestCase
from printer import Printer,PrinterError

class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(2.0,300)
        
    # def setUpClass(cls):
    #     cls.printer_two = Printer(23.9,322)

    def test_print_within_capacity(self):
        # printer = Printer(pages_per_s=2.0,capacity=300)

        self.printer.print(25)
        
    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(309)


