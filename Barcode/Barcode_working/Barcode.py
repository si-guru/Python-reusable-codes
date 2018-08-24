import BarcodeWriter
import BarcodeReader

BarcodeWriter.createBarcode()
BarcodeReader.readBarcode()



# # Create Barcode using barcode and ImageWriter
# import barcode
# from barcode.writer import ImageWriter

# ALL_PROVIDED_BARCODES = barcode.PROVIDED_BARCODES
# for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
#   try:
#     print(CURRENT_BARCODE)
#     file_path = 'D:\\Guru\\TEST_FOLDERS\\Barcode\\' + CURRENT_BARCODE
#     barcode_class = barcode.get_barcode_class(CURRENT_BARCODE)
#     barcode_object = barcode_class(u'9781234567890', writer = ImageWriter())
#     barcode_object.save(filename=file_path)
#   except Exception as e:
#     print('Exception in Creating ' + str(e))

# # Read barcode from image

# from pyzbar.pyzbar import decode
# from PIL import Image

# for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
#   try:
#     file_path = 'D:\\Guru\\TEST_FOLDERS\\Barcode\\' + CURRENT_BARCODE +'.png'
#     decodedOutput = decode(Image.open(file_path))
#     print(decodedOutput)
#     for output in decodedOutput:
#       barcode_data = output.data
#       barcode_type = output.type
#       print('Barcode Data - ' + str(barcode_data))
#       print('Barcode Type - ' + str(barcode_type))
#   except Exception as e:
#     print('Exception in Reading ' + str(e))