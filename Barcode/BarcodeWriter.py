import  os
import  sys

import barcode
from barcode.writer import ImageWriter

# Importing inner modules, so that it works as a module and as a program
try:
    from . import LogProvider  as	log_provider
except:
    import LogProvider  as	log_provider

def __create(barcode_type, data, file_path):
    """__create is a private method which creates a 'PNG' image of a barcode with the given data
        on the specified file_path
    
    Arguments:
        barcode_type {str} -- A valid barcode type eg. EAN13
        data {str} -- A valid data based on barcode type
        file_path {str} -- A vavlid path where the image has to be stored
    """

    try:
        barcode_class = barcode.get_barcode_class(barcode_type)
        barcode_object = barcode_class(repr(data), writer = ImageWriter())
        barcode_object.save(filename=file_path)
    except Exception as ex:
        process_data.message = 'Exception in __create - ' + str(ex)
        log_provider.insert_error_log(process_data)
 

def createBarcode(data = None, file_path = None, barcode_type = None, is_folder = False):
    """createBarcode will create a barcode image method which creates a 'PNG' image of a barcode with the given data
        on the specified file_path
    
    Keyword Arguments:
        data {str} -- A valid data based on barcode type
        file_path {str} -- A vavlid path where the image has to be stored
        barcode_type {str} -- A valid barcode type eg. EAN13
        is_folder {bool} -- Specifies whether the given path is a folder, used for manual overriding (default: {False})
    
    Returns:
        ProcessData -- ProcessData used for interprocess communication
    """

    ALL_PROVIDED_BARCODES = barcode.PROVIDED_BARCODES
    process_data.message = 'Error'
    process_data.status = -1
    process_data.data = data, file_path, barcode_type
    can_skip = False
    if(file_path):
        file_name, extension = os.path.splitext(os.path.basename(file_path))
    else:
        process_data.message = 'Exception in Writing - No file_path provided'
        log_provider.insert_error_log(process_data)
        return process_data
    if(not data):
        process_data.message = 'Exception in Writing - No Data provided'
        log_provider.insert_error_log(process_data)
        return process_data
    if(barcode_type):
       ALL_PROVIDED_BARCODES.clear()
       ALL_PROVIDED_BARCODES.append(barcode_type)
    else:
        if(not file_path):
            return process_data
    try:
        if(not is_folder):
            if(barcode_type):
                __create(barcode_type= barcode_type, data= data, file_path= file_path)
            else:
                can_skip = True
                for CURRENT_BARCODE in ALL_PROVIDED_BARCODES:
                    file_path = os.path.join(file_path, CURRENT_BARCODE)
                    __create(barcode_type= barcode_type, data= data, file_path= file_path)
        elif(not extension):
            process_data.message = 'Exception in Writing - No extension is provided for folder'
            log_provider.insert_error_log(process_data)
            return process_data
        else:
            if(barcode_type):
                file_path = os.path.join(file_path, barcode_type)
                __create(barcode_type= barcode_type, data= data, file_path= file_path)
    except Exception as e:
        if(not can_skip):
            process_data.message = 'Exception in Writing ' + str(e)
            log_provider.insert_error_log(process_data)
            print('Writer Exception for image ' + file_path)
            input()
            return process_data

    process_data.status = 1
    process_data.message = 'Success'
    process_data.data = file_path
    return process_data

# The Actual Module Code
try:
    bot_name, extention =   os.path.splitext(os.path.basename(__file__))
    process_data        =   log_provider.generate_process_data(bot_name)
    # Import safety block - createbarcode(), only when run as a script
    if(__name__ == '__main__'):
        createBarcode(file_path = 'D:\\Guru\\TEST_FOLDERS\\Barcode\\sample', barcode_type = 'EAN')
	
except Exception as exception:
	log_provider.insert_log(process_data)
	process_data.message  = '@ BarcodeWriter - ' + format(exception)
	log_provider.insert_error_log(process_data)