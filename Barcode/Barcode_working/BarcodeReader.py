# Read barcode from image
import LogProvider  as	log_provider
import os
import sys

from pyzbar.pyzbar import decode
from PIL import Image
import barcode

def readBarcode(file_path = None):
    ALL_PROVIDED_BARCODES = barcode.PROVIDED_BARCODES

    if(file_path):
        try:
            decodedOutput = decode(Image.open(file_path))
            print(decodedOutput)
            for output in decodedOutput:
                barcode_data = output.data
                barcode_type = output.type
                return barcode_data, barcode_type
        except Exception as e:
            # process_data.message = 'Exception in Reading ' + str(e)
            # log_provider.insert_error_log(process_data)
            print('Reader Exception')
    else:
        for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
            print('cnt')
            try:
                file_path = 'D:\\Guru\\TEST_FOLDERS\\Barcode\\' + CURRENT_BARCODE +'.png'
                print(file_path)
                decodedOutput = decode(Image.open(file_path))
                print(not decodedOutput)
                for output in decodedOutput:
                    barcode_data = output.data
                    barcode_type = output.type
                #return barcode_data, barcode_type
            except Exception as e:
                # process_data.message = 'Exception in Reading ' + str(e)
                # log_provider.insert_error_log(process_data)
                print('Reader Exception for image - ' + file_path)


# The Actual Module Code
try:
    bot_name, extention =   os.path.splitext(os.path.basename(__file__))
    process_data        =   log_provider.generate_process_data(bot_name)
    # Import safety block - perform_ftp_operation, only when run as a script
    if(__name__ == '__main__'):
        print('Called as Module')
        readBarcode()
        print('stop')
	
except Exception as exception:
    print ('Some exxception')
    log_provider.insert_log(process_data)
    process_data.message  = '@ BarcodeReader - ' + format(exception)
    print(process_data)
    log_provider.insert_error_log(process_data)