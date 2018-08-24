# Read barcode from image
import os
import sys
import barcode
from PIL import Image
from pyzbar.pyzbar import decode

# Importing inner modules, so that it works as a module and as a program
try:
    from . import LogProvider  as	log_provider
except:
    import LogProvider  as	log_provider

def readBarcode(file_path = None):
    ALL_PROVIDED_BARCODES = barcode.PROVIDED_BARCODES

    process_data.data = file_path
    process_data.message = 'Error'
    process_data.status  = -1

    if(file_path):
        file_name, extention = os.path.splitext(os.path.basename(file_path))
    else:
        process_data.message = 'Exception in Reading - file_path is mandatory'
        log_provider.insert_error_log(process_data)
        return process_data

    if(extention):
        try:
            process_data.data = decode(Image.open(file_path))
            process_data.message = 'Success'
            process_data.status  = 1
            return process_data
        except Exception as e:
            process_data.message = 'Exception in Reading ' + str(e)
            log_provider.insert_error_log(process_data)
            print('Reader Exception for image - ' + file_path + str(e))
            return process_data
    else:
        for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
            try:
                file_path = os.path.join(file_path, CURRENT_BARCODE +'.png')
                process_data.data = decode(Image.open(file_path))
                process_data.message = 'Success'
                process_data.status  = 1
                return process_data
            except Exception as e:
                process_data.message = 'Exception in Reading ' + str(e)
                log_provider.insert_error_log(process_data)
                print('Reader Exception for image - ' + file_path)
                return process_data


# The Actual Module Code
try:
    bot_name, extention =   os.path.splitext(os.path.basename(__file__))
    process_data        =   log_provider.generate_process_data(bot_name)
    # Import safety block - readBarcode(), only when run as a script
    if(__name__ == '__main__'):
        readBarcode()
        if(process_data.status == 1):
            for values in process_data.data:
                print ('DATA - ' + str(bytes.decode(values.data)))
                print ('TYPE - ' + str(values.type))
	
except Exception as exception:
    log_provider.insert_log(process_data)
    process_data.message  = '@ BarcodeReader - ' + format(exception)
    log_provider.insert_error_log(process_data)