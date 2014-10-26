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
import sys


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


right_now = time.time()
current_timestamp = datetime.datetime.fromtimestamp(right_now).strftime('%Y-%m-%d_%H-%M-%S')
reporting_batch = 'blanks'
run_tag = reporting_batch + '_' + current_timestamp
download_root_path = '..{0}downloads'.format(os.sep)
download_path = '{0}{1}{2}'.format(download_root_path, os.sep, run_tag)

try:
    os.makedirs(download_path)
except OSError, e:
    if os.path.exists(download_path):
        with open('testwrite', 'w') as tw:
            text = 'testing write permissions'
            tw.write(text)
        os.remove(download_path)
        print 'Local download target {{}}'.format(download_path)
    else:
        download_path = ''
        print 'Failed to create download target directory. Will attempt to write data to current directory.'

print
print 'Target download directory \n\t{0}'.format(download_path)
print
sys.stdout.flush()

url_nh_base = 'http://sos.nh.gov'
url_lobbyist_home_page = '{0}/lobby.aspx'.format(url_nh_base)

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

xpath_download_links = "//body//a[contains(@href,'DownloadAsset') and not(contains(@target, '_self'))]"
xpath_page_title = "//*[@id='UxMainContentTitle']/text()"

parser = etree.HTMLParser()
tree_lobbyist_home_page = etree.parse(url_lobbyist_home_page, parser)

download_links = tree_lobbyist_home_page.xpath(xpath_download_links)
page_title = normalize(tree_lobbyist_home_page.xpath(xpath_page_title))
print 'Downloading ' + repr(len(download_links)) + ' assets listed on page\n\t' + url_lobbyist_home_page
sys.stdout.flush()

i = 0
for a in download_links:
    i += 1
    print
    asset_path_and_id = normalize(a.attrib['href'])
    asset_id = asset_path_and_id.split('aspx?id=')[1]
    asset_name = normalize(a.attrib['title'])
    url_download = url_nh_base + asset_path_and_id
    filename_download = '{0}{1}{2} id({3}).pdf'.format(download_path, os.sep, asset_name, asset_id)
    print '{0}] downloading to {1}'.format(i, filename_download)
    print '   from {0}'.format(url_download)
    sys.stdout.flush()
    with open(filename_download, 'wb') as file_download:
        socket = urllib2.urlopen(url_download)
        content = socket.read()
        socket.close()
        file_download.write(content)
        file_download.close()

print
print 'Creating ZIP archive'
sys.stdout.flush()

os.chdir(download_root_path)
zip_archive_name = make_archive(run_tag, 'zip', '.', run_tag)
print '   {' + zip_archive_name + '}'
print "ZIP size", os.stat(zip_archive_name).st_size / 1024, "kB"
print

print 'Deleting unzipped files'
sys.stdout.flush()
byte_size_total = 0
for f in os.listdir(run_tag):
    fp = "{0}{1}{2}".format(run_tag, os.sep, f)
    byte_size = os.stat(fp).st_size
    byte_size_total += byte_size
    print "  ", byte_size, 'bytes: ', f
    os.remove(fp)
os.rmdir(run_tag)
print "Total removed", byte_size_total / 1024, "kB"

print 'Done'
sys.stdout.flush()
