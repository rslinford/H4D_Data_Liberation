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
from reportlab.lib.colors import Color
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

    def __str__(self, hocr_tree):
        """
        Return the textual content of the HTML body
        """
        if hocr_tree is None:
            return ''
        xmlns = HocrTransform2.lookup_namespace()
        body = hocr_tree.find(".//%sbody" % xmlns)
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

    @staticmethod
    def element_coordinates(element):
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
    def convert_px_coordinates_to_pt(box_coordinates, dpi):
        """
        :rtype : list[4]
        """
        x1 = HocrTransform2.px2pt(box_coordinates[0], dpi)
        y1 = HocrTransform2.px2pt(box_coordinates[1], dpi)
        x2 = HocrTransform2.px2pt(box_coordinates[2], dpi)
        y2 = HocrTransform2.px2pt(box_coordinates[3], dpi)
        return x1, y1, x2, y2

    @staticmethod
    def lookup_namespace(hocr_tree):
        # ElementTree requires the namespace, if it has one, to find elements
        matches = HocrTransform2.namespacePattern.search(hocr_tree.getroot().tag)
        xmlns = ''
        if matches:
            xmlns = matches.group(1)

        return xmlns

    @staticmethod
    def calculate_pt_dimensions(dpi, hocr_tree, xmlns):
        height, width = None, None
        for div in hocr_tree.findall(".//%sdiv[@class='ocr_page']" % (xmlns)):
            coordinates = HocrTransform2.element_coordinates(div)
            width = HocrTransform2.px2pt(coordinates[2] - coordinates[0], dpi)
            height = HocrTransform2.px2pt(coordinates[3] - coordinates[1], dpi)
            break  # there shouldn't be more than one, and if there is, we don't want it

        return height, width

    @staticmethod
    def draw_box(canvas, page_height, x1, y1, x2, y2, stroke_color, fill_color, line_width=1, is_filled=0):

        canvas.setStrokeColor(stroke_color)  # light blue for bounding box of paragraph
        canvas.setFillColor(fill_color)  # light blue for bounding box of paragraph
        canvas.setLineWidth(line_width)  # no line for bounding box
        canvas.rect(x1, page_height - y2, x2 - x1, y2 - y1, fill=is_filled)

    def to_pdf(self, out_filename, image_filename, show_bounding_boxes, hocr_file, dpi, font_name="Helvetica"):
        """
        Creates a PDF file with an image superimposed on top of the text.
        Text is positioned according to the bounding box of the lines in
        the hOCR file.
        The image need not be identical to the image used to create the hOCR file.
        It can have a lower resolution, different color mode, etc.
        """

        hocr_tree = ElementTree.ElementTree()
        hocr_tree.parse(hocr_file)
        xmlns = self.lookup_namespace(hocr_tree)

        pt_page_height, pt_page_width = self.calculate_pt_dimensions(dpi, hocr_tree, xmlns)

        # no width and height definition in the ocr_image element of the hocr file
        if pt_page_width is None:
            print("No page dimension found in the hocr file")
            sys.exit(1)

        # Create the PDF file. Page size in points (1/72 in.)
        pdf = Canvas(out_filename, pagesize=(pt_page_width, pt_page_height), pageCompression=1)

        # draw bounding box for each paragraph
        green = Color(0, 1, 0)
        blue = Color(0, 1, 1)
        if show_bounding_boxes:
            for elem in hocr_tree.findall(".//%sp[@class='%s']" % (xmlns, "ocr_par")):
                element_text = self._get_element_text(elem).rstrip()
                if len(element_text) == 0:
                    continue
                x1, y1, x2, y2 = self.convert_px_coordinates_to_pt(self.element_coordinates(elem), dpi)
                self.draw_box(pdf, pt_page_height, x1, y1, x2, y2, green, blue, is_filled=1, line_width=4)
                green = Color(green.rgb()[0] + 0.1, 1, 0)

        # check if element with class 'ocrx_word' are available
        # otherwise use 'ocr_line' as fallback
        element_class = "ocr_line"
        if hocr_tree.find(".//%sspan[@class='ocrx_word']" % xmlns) is not None:
            element_class = "ocrx_word"

        # iterate all text elements
        red = Color(1, 0, 0)
        pdf.setDash(6, 3)  # bounding box is dashed
        black = Color(0, 0, 0)
        for elem in hocr_tree.findall(".//%sspan[@class='%s']" % (xmlns, element_class)):
            element_text = self._get_element_text(elem).rstrip()
            element_text = self.replace_unsupported_chars(element_text)
            if len(element_text) == 0:
                continue

            coordinates = self.element_coordinates(elem)
            x1, y1, x2, y2 = HocrTransform2.convert_px_coordinates_to_pt(coordinates, dpi)

            # draw the bbox border
            if show_bounding_boxes:
                self.draw_box(pdf, pt_page_height, x1, y1, x2, y2, red, black, line_width=0.5)

            text = pdf.beginText()
            fontsize = self.px2pt(coordinates[3] - coordinates[1], dpi)
            text.setFont(font_name, fontsize)

            # set cursor to bottom left corner of bbox (adjust for dpi)
            text.setTextOrigin(x1, pt_page_height - y2)

            # scale the width of the text to fill the width of the bbox
            text.setHorizScale(100 * (x2 - x1) / pdf.stringWidth(element_text, font_name, fontsize))

            # write the text to the page
            text.textLine(element_text)
            pdf.setStrokeColor(black)
            pdf.drawText(text)

        # put the image on the page, scaled to fill the page
        if image_filename is not None:
            im = Image.open(image_filename)
            pdf.drawInlineImage(im, 0, 0, width=pt_page_width, height=pt_page_height)

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
