#!/usr/local/bin/python2
# coding: utf-8
##############################################################################
# Copyright (c) 2013-14: fritz-hh from Github (https://github.com/fritz-hh)
#
# Copyright (c) 2010: Jonathan Brinley from Github (https://github.com/jbrinley/HocrConverter)
# Initial version by Jonathan Brinley, jonathanbrinley@gmail.com
##############################################################################
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from lxml import etree as ElementTree
from PIL import Image
import re
import sys
import argparse


class HocrTransform2():
    """
    A class for converting documents from the hOCR format.
    For details of the hOCR format, see:
    http://docs.google.com/View?docid=dfxcv4vc_67g844kf
    """

    boxPattern = re.compile('bbox((\s+\d+){4})')
    namespacePattern = re.compile('({.*})html')

    def __init__(self):
        pass

    def __str__(self, hocr):
        """
        Return the textual content of the HTML body
        """
        if hocr is None:
            return ''
        xmlns = HocrTransform2.lookup_namespace()
        body = hocr.find(".//%sbody" % xmlns)
        if body:
            return self._get_element_text(body).encode('utf-8')  # XML gives unicode
        else:
            return ''

    def _get_element_text(self, element):
        """
        Return the textual content of the element and its children
        """
        text = ''
        if element.text is not None:
            text = text + element.text
        for child in element.getchildren():
            text = text + self._get_element_text(child)
        if element.tail is not None:
            text = text + element.tail
        return text

    def element_coordinates(self, element):
        """
        Returns a tuple containing the coordinates of the bounding box around
        an element
        """
        out = (0, 0, 0, 0)
        if 'title' in element.attrib:
            matches = HocrTransform2.boxPattern.search(element.attrib['title'])
            if matches:
                coords = matches.group(1).split()
                out = (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
        return out

    @staticmethod
    def px2pt(pxl, dpi):
        """
        Returns the length in pt given length in pxl
        """
        return float(pxl) / dpi * inch

    @staticmethod
    def replace_unsupported_chars(string_thing):
        """
        Given an input string, returns the corresponding string that:
        - is available in the helvetica facetype
        - does not contain any ligature (to allow easy search in the PDF file)
        """
        # The 'u' before the character to replace indicates that it is a unicode character
        string_thing = string_thing.replace(u"ﬂ", "fl")
        string_thing = string_thing.replace(u"ﬁ", "fi")
        return string_thing

    @staticmethod
    def coordinates(box_coordinates, dpi):
        """

        :rtype : list[4]
        """
        x1 = HocrTransform2.px2pt(box_coordinates[0], dpi)
        y1 = HocrTransform2.px2pt(box_coordinates[1], dpi)
        x2 = HocrTransform2.px2pt(box_coordinates[2], dpi)
        y2 = HocrTransform2.px2pt(box_coordinates[3], dpi)
        return x1, y1, x2, y2

    @staticmethod
    def lookup_namespace(hocr):
        # if the hOCR file has a namespace, ElementTree requires its use to find elements
        matches = HocrTransform2.namespacePattern.search(hocr.getroot().tag)
        xmlns = ''
        if matches:
            xmlns = matches.group(1)

        return xmlns

    def to_pdf(self, out_filename, image_filename, show_bounding_boxes, hocr_file, dpi, font_name="Helvetica"):
        """
        Creates a PDF file with an image superimposed on top of the text.
        Text is positioned according to the bounding box of the lines in
        the hOCR file.
        The image need not be identical to the image used to create the hOCR file.
        It can have a lower resolution, different color mode, etc.
        """

        # constructor stuff
        hocr = ElementTree.ElementTree()
        hocr.parse(hocr_file)

        xmlns = self.lookup_namespace(hocr)

        # get dimension in pt (not pixel!!!!) of the OCRed image
        width, height = None, None
        for div in hocr.findall(".//%sdiv[@class='ocr_page']" % (xmlns)):
            coords = self.element_coordinates(div)
            width = HocrTransform2.px2pt(coords[2] - coords[0], dpi)
            height = HocrTransform2.px2pt(coords[3] - coords[1], dpi)
            break  # there shouldn't be more than one, and if there is, we don't want it

        # no width and heigh definition in the ocr_image element of the hocr file
        if width is None:
            print("No page dimension found in the hocr file")
            sys.exit(1)
        # end constructor stuff

        # create the PDF file
        pdf = Canvas(out_filename, pagesize=(width, height), pageCompression=1)  # page size in points (1/72 in.)

        # draw bounding box for each paragraph
        pdf.setStrokeColorRGB(0, 1, 1)  # light blue for bounding box of paragraph
        pdf.setFillColorRGB(0, 1, 1)  # light blue for bounding box of paragraph
        pdf.setLineWidth(0)  # no line for bounding box
        for elem in hocr.findall(".//%sp[@class='%s']" % (xmlns, "ocr_par")):

            elemtxt = self._get_element_text(elem).rstrip()
            if len(elemtxt) == 0:
                continue

            coords = self.element_coordinates(elem)

            x1, y1, x2, y2 = HocrTransform2.coordinates(coords, dpi)

            # draw the bbox border
            if show_bounding_boxes:
                pdf.rect(x1, height - y2, x2 - x1, y2 - y1, fill=1)

        # check if element with class 'ocrx_word' are available
        # otherwise use 'ocr_line' as fallback
        elemclass = "ocr_line"
        if hocr.find(".//%sspan[@class='ocrx_word']" % xmlns) is not None:
            elemclass = "ocrx_word"

        # iterate all text elements
        pdf.setStrokeColorRGB(1, 0, 0)  # light green for bounding box of word/line
        pdf.setLineWidth(0.5)  # bounding box line width
        pdf.setDash(6, 3)  # bounding box is dashed
        pdf.setFillColorRGB(0, 0, 0)  # text in black
        for elem in hocr.findall(".//%sspan[@class='%s']" % (xmlns, elemclass)):
            elemtxt = self._get_element_text(elem).rstrip()
            elemtxt = self.replace_unsupported_chars(elemtxt)
            if len(elemtxt) == 0:
                continue

            coords = self.element_coordinates(elem)
            x1, y1, x2, y2 = HocrTransform2.coordinates(coords, dpi)

            # draw the bbox border
            if show_bounding_boxes:
                pdf.rect(x1, height - y2, x2 - x1, y2 - y1, fill=0)

            text = pdf.beginText()
            fontsize = HocrTransform2.px2pt(coords[3] - coords[1], dpi)
            text.setFont(font_name, fontsize)

            # set cursor to bottom left corner of bbox (adjust for dpi)
            text.setTextOrigin(x1, height - y2)

            # scale the width of the text to fill the width of the bbox
            text.setHorizScale(100 * (x2 - x1) / pdf.stringWidth(elemtxt, font_name, fontsize))

            # write the text to the page
            text.textLine(elemtxt)
            pdf.drawText(text)

        # put the image on the page, scaled to fill the page
        if image_filename is not None:
            im = Image.open(image_filename)
            pdf.drawInlineImage(im, 0, 0, width=width, height=height)

        # finish up the page and save it
        pdf.showPage()
        pdf.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert hocr file to PDF')
    parser.add_argument('-b', '--boundingboxes', action="store_true", default=False, help='Show bounding boxes borders')
    parser.add_argument('-r', '--resolution', type=int, default=300, help='Resolution of the image that was OCRed')
    parser.add_argument('-i', '--image', default=None, help='Path to the image to be placed above the text')
    parser.add_argument('hocrfile', help='Path to the hocr file to be parsed')
    parser.add_argument('outputfile', help='Path to the PDF file to be generated')
    args = parser.parse_args()

    hocr = HocrTransform2()
    hocr.to_pdf(args.outputfile, args.image, args.boundingboxes, args.hocrfile, args.resolution)
