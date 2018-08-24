"""
Name        :   SMTP
Usage       :   Customized SMTP module for automation
Reusability :   -
Author      :   AVM-Automation-SGO
Created on  :   08/13/2018
-----------------------------------------------------------------------------
Change Log: Recent Modification in TOP
-----------------------------------------------------------------------------
Date        Mod By  Ver     Modification
-----------------------------------------------------------------------------
08/13/2018  528664  1.00    Initial Code
"""

# Custom Modules
from .. import Globals
try:
    if(not Globals.setting):
        Globals.start()

    setting = Globals.setting
    logger = setting['Logger']
    ipc_object = setting['IPC_Object']
except Exception as ex:
    print("Exception when loading globals")

# Python modules
import os
import xml.etree.ElementTree as ET
import sys
import smtplib
import string
import configparser
from datetime import datetime
try:
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.utils import formatdate
    from email import encoders
    from email.mime.image import MIMEImage
except Exception as ex:
    ipc_object.message = "Error while importing Email Module " + str(ex)
    logger.write_error_log(ipc_object)


class Constants:
    CONFIG_MAIL_HEADER = "Mail_Configuration"
    CONFIG_MAIL_CONFIG_FILE_PATH = "Config_path"
    CONFIG_MAIL_SENDER = "Sender"
    CONFIG_MAIL_RECEIVERS = "Receivers"
    CONFIG_MAIL_SUBECT = "Subject"
    CONFIG_MAIL_BODY = "Mail_body_content"
    CONFIG_MAIL_ATTACHMENTS = "Attachments"
    CONFIG_MAIL_BODY_AS_FILE = "Mail_body_as_file"


class Configuration:

    __smtp_server = None
    __sender = None
    __receivers = None
    __subject = None
    __mail_body = None
    __attachments = None

    def __init__(self, mail_config_path=None):
        self.config_mail(mail_config_path)
        return None

    def config_mail(self, mail_config_file):
        config_parser = configparser.RawConfigParser()
        config_parser.read(mail_config_file)

        server_config_file_path = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_CONFIG_FILE_PATH
            ).strip('"').lower()
        tree = ET.parse(server_config_file_path)
        root = tree.getroot()
        smtp_server = root.find('SmtpServer').text
        self.set_smtp_server(smtp_server)

        sender = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_SENDER
            ).strip('"').lower()
        self.set_sender(sender)

        receivers = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_RECEIVERS
            ).strip('"').lower()
        self.set_receivers(receivers)

        subject = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_SUBECT
            ).strip('"').lower()
        self.set_subject(subject)

        attachments = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_ATTACHMENTS
            ).strip('"').lower().split(',')
        self.set_attachments(attachments)

        body_as_file = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_BODY_AS_FILE
            ).strip('"').lower()
        body = config_parser.get(
            Constants.CONFIG_MAIL_HEADER,
            Constants.CONFIG_MAIL_BODY
            ).strip('"').lower()
        body_as_file = (body_as_file == "true") or (body_as_file == "yes")
        if(body_as_file):
            with open(body, 'r') as body_file:
                lines = body_file.readlines()
            body = "\n".join(lines)
        self.set_mail_body(body)

        return None

    def get_smtp_server(self):
        return self.__smtp_server

    def set_smtp_server(self, smtp_server):
        self.__smtp_server = smtp_server

    def get_sender(self):
        return self.__sender

    def set_sender(self, sender):
        self.__sender = sender

    def get_receivers(self):
        return self.__receivers

    def set_receivers(self, receivers):
        if(isinstance(receivers, list) or (isinstance(receivers, tuple))):
            receivers = ", ".join(receivers)
        self.__receivers = receivers

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_mail_body(self):
        return self.__mail_body

    def set_mail_body(self, mail_body):
        self.__mail_body = mail_body

    def get_attachments(self):
        return self.__attachments

    def set_attachments(self, attachments):
        self.__attachments = attachments


class MailServer:

    __configuration = None

    def set_smtp_configuration(self, configuration):
        self.__configuration = configuration

    def get_smtp_configuration(self):
        return self.__configuration

    def __init__(self):
        return None

    def send_mail(self, configuration=None):

        ipc_object.message = "send_mail started"
        logger.write_info_log(ipc_object)
        """ Checks configuration object in MailServer and replaces with
            user provided Configuraiton"""

        if(not self.__configuration):
            self.__configuration = configuration

        """Checks for user provided configuration,
            If available Proceed to send mail"""
        if(not self.__configuration):
            ipc_object.message = ("SMTP not configured Properly")
            logger.write_error_log(ipc_object)
            sys.exit(0)

        else:
            ipc_object.message = "Configuration Loaded Successfully"
            logger.write_info_log(ipc_object)

            config = self.__configuration
            smtp_server = config.get_smtp_server()
            sender = config.get_sender()
            receivers = config.get_receivers()
            subject = config.get_subject()
            mail_body = config.get_mail_body()
            attachments = config.get_attachments()

            """Configuring Mail basic details
            """

            message_object = MIMEMultipart()
            message_object["From"] = sender
            message_object["Subject"] = subject
            message_object["Date"] = formatdate(localtime=True)
            message_object["To"] = receivers
            message_object.attach(MIMEText(mail_body))
            ipc_object.message = "Mail Configuration Completed"
            logger.write_debug_log(ipc_object)

            """Adding mail attachments
            """

            try:
                for current_file in attachments:

                    with open(current_file.strip(), "r") as fh:
                        data = fh.read()
                    attachment = MIMEBase('application', "octet-stream")
                    attachment.set_payload(data)
                    encoders.encode_base64(attachment)
                    attachment.add_header(
                        'Content-Disposition',
                        'attachment; filename="%s"' % os.path.basename(
                            current_file
                            )
                        )
                    message_object.attach(attachment)

            except IOError:
                ipc_object.message = (
                    "Error opening attachment file %s"
                    % current_file
                )
                logger.write_error_log(ipc_object)

            ipc_object.message = "Mail Attachments Added"
            logger.write_debug_log(ipc_object)
            # Connect to the SMTP server and sending mail
            smtpObj = smtplib.SMTP(smtp_server)
            smtpObj.sendmail(sender, receivers, message_object.as_string())
            ipc_object.message = "Mail Sent Successfully"
            logger.write_debug_log(ipc_object)
