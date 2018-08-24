Introduction
------------
This is a custom barcode module, used to read barcode from images and create barcode image.

Scenario
--------

This module can be used when we need to read barcode from an image or when we want to create a barcode image.

Prerequisite
------------
Windows 7.0 and above
Python 3.4 and above

Required python modules
------------------------
pyZbar
PIL
barcode

Required custom modules
-----------------------

DataObject
LogProvider
CustomLogger

Input
-----
BarcodeReader - used to read barcode from image.
Usage
BarcodeReader.readBarcode(fileName= '/path/to/barcode/image')

BarcodeWriter - creates barcode images from the given input.
Usage:
BarcodeWriter.createBarcode(file_path = '/path/to/stroe/barcode/image', barcode_type='EAN')
BarcodeWriter.createBarcode(data='12334', file_path = '/path/to/stroe/barcode/image', barcode_type='EAN')
data - must be valid to specified barcode_type
barcode_type is optional

Expected Output
-------------
BarcodeReader.readBarcode - returns 'ProcessData' object, the data attribute has the barcode value and type
BarcodeWriter.createBarcode - creates barcode image in the specified location

Error Handling
----------------
Errors will be logged in the error log files along with timestamp and log file path is provided in CustomLogger/Logger.ini file.


Command Prompt Execution
-----------------------
Run as Module:

1. Copy module to script path
2. Modify Values in Barcode.py
3. Run 'Barcode.py' for testing
4. Run 'BarcodeReader.readBarcode()' for reading barcode from image.
5. Run 'BarcodeWriter.createBarcode()' for creating barcode image.

Import as Module:

1. Copy Module to script path
2. Import module
3. Use functions available in module



