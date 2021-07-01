import shutil
import os
import pandas as pd
import logging
import distutils.core

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.debug('This will get logged to a file')

#jobs_source = 'G:\\ProntoTenders\\TendersMW\\'
jobs_source = 'C:\\Users\\aoakley\\Documents\\'
#destination_root = 'E:\\SiteNumbers\\'
destination_root = 'C:\\Users\\aoakley\\Documents\\'
datatable = 'C:\\Users\\aoakley\\Documents\\cmw_sitenumber_model.csv'

# import datatable into dictionary
# cmw_model = pd.read_csv(datatable, header=None, index_col=0, squeeze=True).to_dict()
cmw_model = {'C100113': '10320-02'}

for jn,sn in cmw_model.items():
    source = os.path.join(jobs_source,jn)
    dest = ''

    # set destination based on job_type
    if 'C' in jn:
        dest = os.path.join(destination_root,sn,'02. Construction')
    elif 'MW' in jn:
        dest = os.path.join(destination_root,sn,'05. Minor Works')

    # if the source exists we have to move 
    if os.path.exists(source):
        if os.path.exists(os.path.join(dest,jn)):
            logging.info(dest + ' exists')
            logging.info('walking directory and directory individually')
            for root, directories, files in os.walk(source, topdown=False):
                logging.info('moving directories')
                for name in directories:
                    logging.info('moving ' + root + name + ', to' + dest)
                    logging.info(shutil.move(os.path.join(root,name), os.path.join(dest,jn)))
        else:
            # check if source file exists and if it doesnt create in destination, else move folder
            shutil.move(source, dest)
    # if source does not exist and destination does not exist, create directory in destination
    elif not os.path.exists(os.path.join(dest,jn)):
        os.makerdir(os.path.join(dest,jn))
