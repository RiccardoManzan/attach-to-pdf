#!/usr/bin/python

import os
import sys
import argparse

from borb.pdf import Document
from borb.pdf import PDF
import typing

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src', required=True, help='pdf input file')
    parser.add_argument('-a', '--attachments', required=True, help='files to attach to the src file')
    parser.add_argument('-o', '--output', required=True, help='pdf output file')
    
    args = parser.parse_args()

    print('loading file ' + os.path.basename(args.src) + ' ...')
    if args.src[0] == "~":
        args.src = os.path.expanduser(args.src)
    doc: typing.Optional[Document] = None
    with open(os.path.abspath(args.src), "rb") as fh:
        doc = PDF.loads(fh)

    attachments = args.attachments.split(',')
    print(attachments)
    for att in attachments:
        print('attaching file ' + os.path.basename(att) + ' ...')
        if att[0] == "~":
            att = os.path.expanduser(att)
        with open(os.path.abspath(att), 'rb') as attReader:
            attBytes = attReader.read()
        doc = doc.add_embedded_file(os.path.basename(att) , attBytes)

    print('dumping result into file ' + os.path.basename(args.output) + ' ...')
    if args.output[0] == "~":
            args.output = os.path.expanduser(args.output)
    with open(os.path.abspath(args.output), "wb") as fh:
        PDF.dumps(fh, doc)








