"""
Lobbyists (self service page, blank forms, etc.)
http://sos.nh.gov/lobby.aspx
"""

from lxml import etree
import os
from shutil import make_archive
import urllib2
import time
import datetime


def isinstance_string(x):
    # Type 'str' is sufficient to catch all string types in Python 3
    # but would miss type 'unicode' which can occur in Python 2.7
    if isinstance(x, str):
        return True

    # Type 'basestring' catches both 'str' and 'unicode' in Python 2.7
    # but doesn't exist in Python 3 and throws a NameError.
    try:
        if isinstance(x, basestring):
            return True
    except NameError:
        pass

    return False


def normalize(a):
    if not a:
        return ''

    if isinstance_string(a):
        return a.encode('utf8').strip()

    return a[0].encode('utf8').strip()


parser = etree.HTMLParser()

right_now = time.time()
current_timestamp = datetime.datetime.fromtimestamp(right_now).strftime('%Y-%m-%d_%H-%M-%S')
current_username = os.environ.get('USERNAME')
reporting_batch = 'home-lobbyists'
run_tag = reporting_batch + '_crawled-' + current_timestamp + '_by-' + current_username
archive_name = run_tag
target_dir = '..{0}downloads{1}{2}'.format(os.sep, os.sep, run_tag)

try:
    os.makedirs(target_dir)
except OSError, e:
    if os.path.exists(target_dir):
        with open('testwrite', 'w') as tw:
            text = 'testing write permissions'
            tw.write(text)
        os.remove(target_dir)
        print 'Local download target {' + target_dir + '}'
    else:
        target_dir = ''
        print 'Failed to create download target directory. Will attempt to write data to current directory.'

print
print 'Target download directory {{0}}'.format(target_dir)

url_nh_base = 'http://sos.nh.gov'
url_report_list = '{0}/lobby.aspx'.format(url_nh_base)
# filename_report_list = 'IndependentExpenditures2012.html'

print

"""
Example URLs to Assets
  http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id=52028
  http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id=12643

Example Anchor Tag
<a title="Statement of Income and Expenses"
  href="/WorkArea/DownloadAsset.aspx?id=52028">Statement of Income and Expenses</a>

XPath Selector for Download Assets
(All matching target='_self' are excluded. It's the sites HTML.)

  //body//a[contains(@href,'DownloadAsset') and not(contains(@target, '_self'))]

Home -> Lobbyists - All PDF Assets

<a title="2014"                                    href="/WorkArea/DownloadAsset.aspx?id= 8589935223 ">
<a title="2013"                                    href="/WorkArea/DownloadAsset.aspx?id= 8589934961 ">
<a title="single lobbyists"                        href="/WorkArea/DownloadAsset.aspx?id=      49392 ">
<a title="multi lobbyists"                         href="/WorkArea/DownloadAsset.aspx?id=      49393 ">
<a title="Statement of Income and Expenses"        href="/WorkArea/DownloadAsset.aspx?id=      52028 ">
<a title="Addendum A"                              href="/WorkArea/DownloadAsset.aspx?id=      12643 ">
<a title="Addendum B"                              href="/WorkArea/DownloadAsset.aspx?id=      12644 ">
<a title="Addendum C"                              href="/WorkArea/DownloadAsset.aspx?id= 8589934980 ">
<a title="Signature form for associated lobbyists" href="/WorkArea/DownloadAsset.aspx?id=      52029 ">
"""

xpath_asset_links = "//body//a[contains(@href,'DownloadAsset') and not(contains(@target, '_self'))]"
# xpath_report_query = '//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl01_WidgetHost_WidgetHost_widget_ListSummary1"]/div[*]/a/@href'
# xpath_report_name = '//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl01_WidgetHost_WidgetHost_widget_ListSummary1"]/div[*]/a/text()'
xpath_page_title = '//*[@id="UxMainContentTitle"]/text()'
#xpath_report_pdf_query = '//*[@id="ctl00_cphMain_dzTopSection_columnDisplay_ctl00_controlcolumn_ctl02_WidgetHost_WidgetHost_widget_CB"]/iframe/@src'
tree_report_list = etree.parse(url_report_list, parser)

report_query_list = tree_report_list.xpath(xpath_report_query)
report_name_list = tree_report_list.xpath(xpath_report_name)
page_title = normalize(tree_report_list.xpath(xpath_page_title))

print 'Downloading', len(report_query_list), 'reports listed at {' + url_report_list + '}'
for i in range(len(report_query_list)):
    print
    report_display_name = report_name_list[i]
    report_query = report_query_list[i]
    url_report_wrapper = url_report_list + report_query
    filename_report_pdf = target_dir + os.sep + report_display_name + '.pdf'
    print repr(i + 1) + '] report {' + filename_report_pdf + '}'
    tree_report_wrapper = etree.parse(url_report_wrapper, parser)
    print '   loading page {' + url_report_wrapper + '}'
    report_pdf_query = normalize(tree_report_wrapper.xpath(xpath_report_pdf_query))
    url_report_pdf = url_nh_base + report_pdf_query
    print '   remote PDF located {' + url_report_pdf + '}'
    with open(filename_report_pdf, 'wb') as pdf_file:
        socket = urllib2.urlopen(url_report_pdf)
        pdf_report = socket.read()
        socket.close()
        pdf_file.write(pdf_report)
        pdf_file.close()
        print '   stored locally {' + filename_report_pdf + '}'

print
print 'Creating ZIP archive'
zip_archive_name = make_archive(archive_name, 'zip', '.', target_dir)

print '   {' + zip_archive_name + '}'
print
print 'TODO: upload archive'
print
print 'Done'