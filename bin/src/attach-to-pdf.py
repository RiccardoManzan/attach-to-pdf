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
    parser.add_argument('-a', '--attachments', required=True,  nargs='*', help='files to attach to the src file')
    parser.add_argument('-o', '--output', required=True, help='pdf output file')
    parser.add_argument('--rel', required=True, help=argparse.SUPPRESS)
    
    args = parser.parse_args()

    src = args.src
    print('loading file ' + os.path.basename(src) + ' ...')
    
    if src[0] == "~":
        src = os.path.expanduser(src)
    elif src[0] != '/':
        if src[:2] == './':
            src = src[2:]
        src = args.rel + "/" + src
    print("src: " + src)
    
    doc: typing.Optional[Document] = None
    with open(os.path.abspath(src), "rb") as fh:
        doc = PDF.loads(fh)

    attachments = args.attachments
    print(attachments)
    for att in attachments:
        print(att)
        print('attaching file ' + os.path.basename(att) + ' ...')

        if att[0] == "~":
            att = os.path.expanduser(att)
        elif att[0] != '/':
            if att[:2] == './':
                att = att[2:]
            att = args.rel + "/" + att

        with open(os.path.abspath(att), 'rb') as attReader:
            attBytes = attReader.read()
        doc = doc.add_embedded_file(os.path.basename(att) , attBytes)

    print('dumping result into file ' + os.path.basename(args.output) + ' ...')

    output = args.output
    if output[0] == "~":
        output = os.path.expanduser(output)
    elif output[0] != '/':
        if output[:2] == './':
            output = output[2:]
        output = args.rel + "/" + output

    with open(os.path.abspath(output), "wb") as fh:
        PDF.dumps(fh, doc)








