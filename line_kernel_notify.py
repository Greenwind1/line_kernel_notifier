# -*- coding: utf-8 -*-

from kaggle import KaggleApi
import requests
import os
from functions import pickle_read, pickle_write

""" ENVIRONMENT SETTING """
COMP_NAME = 'freesound-audio-tagging-2019'  # competition name
KERNEL_LIST = './kernel_list/' + COMP_NAME + '.pkl'  # save directory

os.makedirs('./kernel_list', exist_ok=True)


def kernel_notifier(message='', image_name=None):
    """

    Send messages about new posted kernels.

    ---

    message: text
    image_name: image_file name (path)

    """

    url = "https://notify-api.line.me/api/notify"
    token = 'hogehoge'  # change line api token to yours.
    headers = {"Authorization": "Bearer " + token}

    payload = {"message": message}
    if image_name:
        try:
            files = {"imageFile": open(image_name, "rb")}
            requests.post(url, headers=headers, params=payload, files=files)
        except:
            requests.post(url, headers=headers, params=payload)
    else:
        requests.post(url, headers=headers, params=payload)


""" CREATE AND AUTHENTICATE KAGGLE API CLASS OBJECT """
api = KaggleApi()
api.authenticate()

klist = api.kernels_list(competition=COMP_NAME, page_size=999)
klist_old_ref = pickle_read(KERNEL_LIST)

klist_ref = [k.ref for k in klist]

if len(set(klist_ref) - set(klist_old_ref)) > 0:
    for t in set(klist_ref) - set(klist_old_ref):
        kernel_notifier(
            'A New kernel has posted !\n\n' +
            'https://www.kaggle.com/' + t
        )
    pickle_write(list(set(klist_old_ref) | set(klist_ref)), KERNEL_LIST)
