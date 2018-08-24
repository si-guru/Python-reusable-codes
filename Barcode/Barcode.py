import BarcodeWriter
import BarcodeReader

BarcodeWriter.createBarcode(data = "234567", file_path = "D:\\Guru\\TEST_FOLDERS\\Barcode\\sample")
# input('hi')
BarcodeWriter.createBarcode(data= "234567", file_path = "D:\\Guru\\TEST_FOLDERS\\Barcode\\sample",
                            barcode_type='EAN')
# input('hi')
BarcodeWriter.createBarcode(data= "34567822", file_path = "D:\\Guru\\TEST_FOLDERS\\Barcode\\sample.png",
                            barcode_type='EAN')
input('hi')
BarcodeReader.readBarcode(file_path = "D:\\Guru\\TEST_FOLDERS\\Barcode\\sample.png")
BarcodeReader.readBarcode(file_path = "D:\\Guru\\TEST_FOLDERS\\Barcode\\sample")