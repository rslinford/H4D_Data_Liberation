'''
Independent Expenditures - Primary 2012
http://sos.nh.gov/IndExpPrim12.aspx
'''

from lxml import etree
import os
import urllib2
import time
import datetime


def normalize(a):
    if a:
        return a[0].encode('utf8').strip()
    return ""


parser = etree.HTMLParser()


try:
    right_now = time.time()
    current_timestamp = datetime.datetime.fromtimestamp(right_now).strftime('%Y-%m-%d_%H-%M-%S')
    current_username = os.environ.get("USERNAME")
    run_tag = current_timestamp + "_" + current_username
    target_dir = run_tag
    os.makedirs(target_dir)

except OSError, e:
    if os.path.exists(target_dir):
        with open('testwrite', 'w') as tw:
            text = "testing write permissions"
            tw.write(text)
        os.remove(target_dir)
        print "Local download target (" + target_dir + ")"
    else:
        target_dir = ""
        print "Failed to create download target directory. Will attempt to write data to current directory."

if os.path.exists(target_dir):
    target_dir = target_dir + os.sep
print " "
print "Target download directory (" + target_dir + ")"

url_report_list = 'http://sos.nh.gov/IndExpPrim12.aspx'
url_report_pdf_base_location = 'http://sos.nh.gov'
filename_report_list = 'IndependentExpenditures2012.html'

print " "

xpath_report_query = '''//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl01_WidgetHost_WidgetHost_widget_ListSummary1"]/div[*]/a/@href'''
xpath_report_name = '''//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl01_WidgetHost_WidgetHost_widget_ListSummary1"]/div[*]/a/text()'''
xpath_page_title = '''//*[@id="UxMainContentTitle"]/text()'''
xpath_report_pdf_query = '''//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl02_WidgetHost_WidgetHost_widget_CB"]/iframe/@src'''
tree_report_list = etree.parse(url_report_list, parser)

report_query_list = tree_report_list.xpath(xpath_report_query)
report_name_list = tree_report_list.xpath(xpath_report_name)
page_title = normalize(tree_report_list.xpath(xpath_page_title))

print "Downloading", len(report_query_list), "reports listed at " + url_report_list
for i in range(len(report_query_list)):
    print " "
    report_display_name = report_name_list[i]
    report_query = report_query_list[i]
    url_report_wrapper = url_report_list + report_query
    filename_report_pdf = target_dir + report_display_name + ".pdf"
    print (i + 1), "] report (" + filename_report_pdf + ")"
    tree_report_wrapper = etree.parse(url_report_wrapper, parser)
    print "   loading page " + url_report_wrapper
    report_pdf_query = normalize(tree_report_wrapper.xpath(xpath_report_pdf_query))
    url_report_pdf = url_report_pdf_base_location + report_pdf_query
    print "   remote PDF located (" + url_report_pdf + ")"
    with open(filename_report_pdf, 'wb') as pdf_file:
        socket = urllib2.urlopen(url_report_pdf)
        pdf_report = socket.read()
        socket.close()
        pdf_file.write(pdf_report)
        pdf_file.close()
        print "   downloaded (file:" + filename_report_pdf + ")"
