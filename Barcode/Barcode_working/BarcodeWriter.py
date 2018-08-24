# Create Barcode using barcode and ImageWriter
import LogProvider  as	log_provider
import os
import sys

import barcode
from barcode.writer import ImageWriter


def createBarcode(data = None, file_path = None, barcodeType = None):
    ALL_PROVIDED_BARCODES = barcode.PROVIDED_BARCODES
    if(not data):
        data = str('9781234567890')
    if(barcodeType):
       ALL_PROVIDED_BARCODES.clear()
       ALL_PROVIDED_BARCODES.append(barcodeType)

    for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
        try:
            if(not file_path):
                file_path = 'D:\\Guru\\TEST_FOLDERS\\Barcode\\' + CURRENT_BARCODE
            barcode_class = barcode.get_barcode_class(CURRENT_BARCODE)
            barcode_object = barcode_class(u'' + data, writer = ImageWriter())
            barcode_object.save(filename=file_path)
        except Exception as e:
            # process_data.message = 'Exception in Writing ' + str(e)
            # log_provider.insert_error_log(process_data)
            print('WRiter Exception for image ' + file_path)



# The Actual Module Code
try:
    bot_name, extention =   os.path.splitext(os.path.basename(__file__))
    process_data        =   log_provider.generate_process_data(bot_name)
    	# Import safety block - perform_ftp_operation, only when run as a script
    if(__name__ == '__main__'):
        print('Called as Module')
	
except Exception as exception:
	log_provider.insert_log(process_data)
	process_data.message  = '@ BarcodeWriter - ' + format(exception)
	log_provider.insert_error_log(process_data)