"""
Spin through NH public assets (self serve public reports)
http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id=[integer]
"""

from lxml import etree
import os
from shutil import make_archive
import urllib2
from urlparse import urlparse
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

<a title="Addendum A"                              href="/WorkArea/DownloadAsset.aspx?id=        12,643 "> 12,515 : 12,915  range(12515, 12915)
<a title="Addendum B"                              href="/WorkArea/DownloadAsset.aspx?id=        12,644 ">
<a title="single lobbyists"                        href="/WorkArea/DownloadAsset.aspx?id=        49,392 "> 49,015 : 49,615  range(49015, 49615)
<a title="multi lobbyists"                         href="/WorkArea/DownloadAsset.aspx?id=        49,393 ">
<a title="Statement of Income and Expenses"        href="/WorkArea/DownloadAsset.aspx?id=        52,028 "> 51,915 : 52,415  range(51915, 52415)
<a title="Signature form for associated lobbyists" href="/WorkArea/DownloadAsset.aspx?id=        52,029 ">
<a title="2013"                                    href="/WorkArea/DownloadAsset.aspx?id= 8,589,934,961 "> 8,589,934,515 : 8,589,935,314  range(8589934515, 8589935314)
<a title="Addendum C"                              href="/WorkArea/DownloadAsset.aspx?id= 8,589,934,980 ">
<a title="2014"                                    href="/WorkArea/DownloadAsset.aspx?id= 8,589,935,223 ">

"""

id_ranges = [range(12515, 12915), range(49015, 49615), range(51915, 52415), range(8589934515, 8589935314)]
for id_range in id_ranges:
    id_first = id_range[0]
    id_last = id_range[len(id_range) - 1]
    right_now = time.time()
    current_timestamp = datetime.datetime.fromtimestamp(right_now).strftime('%Y-%m-%d_%H-%M-%S')
    reporting_batch = 'spin_' + repr(id_first) + "-" + repr(id_last)
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
            download_path = 'bogus directory todo do something more intelligent'
            print 'Failed to create download target directory. Will now continue blithely on to explode later.'

    print
    print 'Target download directory \n\t{0}'.format(download_path)
    print
    sys.stdout.flush()

    print 'Downloading ' + reporting_batch
    sys.stdout.flush()

    for asset_id in id_range:
        print
        url_download = "http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id={0}".format(asset_id)
        filename_download = '{0}{1}spin_id({2}).pdf'.format(download_path, os.sep, asset_id)
        print '{0}] downloading to {1}'.format(asset_id, filename_download)
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
