"""
Spin through NH public assets (self serve public reports)
http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id=[integer]
"""

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


def hr(asset_id_param):
    r = urllib2.Request('http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id={0}'.format(asset_id_param))
    r.get_method = lambda: 'HEAD'
    res = urllib2.urlopen(r)
    ct = res.info().getheader('content-type', '')
    cl = res.info().getheader('content-length', '')
    cd = res.info().getheader('content-disposition', '')
    m = dict([['id', repr(asset_id_param)], ['type', ct], ['length', cl], ['disp', cd]])
    return m


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

Download Links for two pages
[['asset_' + p, [x.attrib['href'].rsplit('=')[1] for x in etree.parse(base + p, parser).xpath(xdl)]] for p in ['/', '/lobby.aspx']]

"""
"""
some_currently_linked_assets = ['10032', '10192', '10346', '10592', '10865', '12412', '12413', '12496', '12497',
                                '12498', '12499', '12562', '12563', '12594', '12600', '12624', '12643', '12644',
                                '12818', '12819', '13048', '13053', '13055', '13177', '13178', '13179', '13180',
                                '13181', '13182', '13183', '14553', '14581', '14582', '14583', '14652', '24626',
                                '24641', '24643', '24644', '24645', '24646', '24655', '24775', '24880', '24881',
                                '25058', '25729', '25730', '25749', '25751', '25767', '25768', '25769', '25770',
                                '25771', '25772', '25989', '26045', '26202', '26429', '26764', '26767', '27439',
                                '27475', '27476', '27477', '27478', '27479', '27480', '27554', '27638', '27666',
                                '27667', '27689', '27894', '27898', '28299', '28367', '28468', '28629', '28631',
                                '28633', '29939', '29940', '29941', '30031', '30034', '31340', '31345', '31351',
                                '31352', '31355', '31367', '31615', '34375', '36758', '3696', '3697', '3698', '3699',
                                '3700', '3704', '3705', '3708', '3709', '3711', '3712', '3713', '37806', '37807',
                                '37808', '37809', '37810', '37811', '37814', '37815', '37816', '37817', '37818',
                                '37819', '37820', '37821', '37822', '37823', '37824', '37825', '37826', '40004',
                                '40175', '40176', '43608', '43609', '43610', '43611', '43612', '43613', '43614',
                                '43615', '43616', '43617', '43618', '43619', '43621', '43622', '43623', '43624',
                                '43625', '43626', '43627', '43628', '43629', '43630', '43631', '43632', '43633',
                                '43634', '43635', '43636', '43637', '43638', '43639', '43640', '43641', '43642',
                                '43643', '43644', '43645', '43646', '43647', '43648', '43649', '43652', '43653',
                                '43654', '43655', '43656', '43657', '43658', '43659', '43660', '43661', '43662',
                                '43663', '43664', '43665', '43666', '43667', '43668', '43669', '43670', '43671',
                                '43672', '43673', '43674', '43675', '43676', '43677', '43678', '43679', '43680',
                                '43681', '43682', '43683', '43684', '43685', '43686', '43687', '43688', '43689',
                                '43722', '43723', '43724', '43725', '43726', '43727', '43728', '43729', '43730',
                                '43731', '43732', '43733', '43734', '43735', '43736', '43737', '43738', '43739',
                                '43740', '43741', '43742', '43743', '43744', '43745', '43746', '43747', '43748',
                                '43749', '43750', '43751', '43752', '43753', '43754', '43755', '43756', '43757',
                                '43758', '43759', '43760', '43761', '43762', '43763', '43764', '43765', '43766',
                                '43767', '43768', '43769', '43770', '43771', '43772', '43773', '43774', '43775',
                                '43776', '43777', '43778', '43779', '43780', '43781', '43782', '43783', '43784',
                                '43785', '43786', '43787', '43788', '43789', '43790', '43791', '43792', '43793',
                                '43794', '43795', '43796', '43797', '43798', '43799', '43800', '43801', '43802',
                                '43803', '43804', '43805', '43806', '43807', '43808', '43809', '43810', '43811',
                                '43812', '43813', '43814', '43815', '43816', '43817', '43818', '43819', '43821',
                                '43822', '43823', '43824', '43825', '43826', '43827', '43828', '43829', '43830',
                                '43832', '43833', '43834', '43835', '43836', '43837', '43838', '43839', '43840',
                                '43841', '43842', '43843', '43844', '43845', '43846', '43848', '43849', '43850',
                                '43851', '43852', '43853', '43854', '43855', '43856', '43857', '43858', '43859',
                                '43860', '43861', '43862', '43868', '43869', '43870', '43872', '43873', '43874',
                                '43875', '43876', '43877', '43878', '43879', '43880', '43881', '43882', '43885',
                                '43886', '43887', '43888', '43889', '43890', '43891', '43892', '43893', '43894',
                                '43895', '43896', '43898', '43902', '43903', '43904', '43905', '43906', '43907',
                                '43908', '43910', '43911', '43912', '43913', '43914', '43915', '43916', '43917',
                                '43918', '43919', '43920', '43921', '43922', '43923', '43924', '43925', '43926',
                                '43927', '43928', '43953', '43954', '43955', '43956', '43957', '43958', '43959',
                                '43960', '43961', '43962', '43963', '43964', '43965', '43966', '43967', '43968',
                                '43969', '43970', '43971', '43972', '43973', '43974', '43975', '43976', '43977',
                                '43978', '43979', '43980', '43981', '43982', '43983', '43984', '43985', '43986',
                                '43987', '43988', '43989', '43990', '43991', '43992', '43993', '43994', '43995',
                                '44248', '44249', '44250', '44251', '44252', '44253', '44254', '44255', '44256',
                                '44257', '44258', '44259', '44260', '44262', '44263', '44264', '44265', '44267',
                                '44268', '44289', '44413', '44441', '44442', '44443', '44444', '44445', '44446',
                                '44447', '44448', '44449', '44450', '44451', '44452', '44453', '44454', '44455',
                                '44456', '44457', '44458', '44459', '44460', '44462', '44463', '44464', '44465',
                                '44466', '44467', '44468', '44469', '44470', '44471', '44472', '44473', '44474',
                                '44475', '44476', '44477', '44478', '44479', '44480', '44481', '44482', '44483',
                                '44484', '44485', '44486', '44487', '44488', '44489', '44490', '44491', '44492',
                                '44493', '44494', '44495', '44496', '44497', '44498', '44499', '44500', '44501',
                                '44502', '44504', '44505', '44506', '44507', '44508', '44509', '44510', '44511',
                                '44512', '44513', '44514', '44515', '44516', '44517', '44518', '44519', '44520',
                                '44521', '44522', '44523', '44524', '44794', '44795', '44796', '44797', '44798',
                                '44799', '44800', '44801', '44802', '44803', '44804', '44805', '44806', '44807',
                                '44808', '44814', '44815', '44816', '44817', '44818', '44819', '44820', '44821',
                                '44822', '44823', '44824', '44825', '44833', '44834', '44835', '44836', '44837',
                                '44838', '44839', '44840', '44841', '44842', '44843', '44844', '44845', '44846',
                                '44847', '44848', '44849', '44850', '44851', '44852', '44853', '44854', '44855',
                                '44856', '44857', '44858', '44859', '44860', '44861', '44862', '44863', '44864',
                                '44865', '44866', '44867', '44868', '44869', '44870', '44871', '44872', '44873',
                                '44874', '44875', '44876', '44877', '44878', '44879', '44880', '44881', '44882',
                                '44883', '44884', '44885', '44886', '44887', '44888', '44890', '44891', '44892',
                                '44893', '44894', '44896', '44897', '44898', '44899', '44900', '44901', '44902',
                                '44903', '44912', '44913', '45365', '45366', '45367', '45369', '45370', '45371',
                                '45372', '45373', '45374', '45375', '45376', '45377', '45378', '45379', '45380',
                                '45381', '45383', '45385', '45386', '45387', '45388', '45476', '45477', '45478',
                                '46056', '46832', '46833', '46835', '46836', '46950', '47054', '47131', '47132',
                                '47156', '47158', '47168', '47228', '47229', '47230', '47231', '47232', '47233',
                                '47234', '47235', '47236', '47237', '47238', '47239', '47240', '47241', '47242',
                                '47243', '47244', '47245', '47246', '47247', '47248', '47249', '47250', '47251',
                                '47252', '47253', '47256', '47257', '47258', '47259', '47260', '47261', '47262',
                                '47263', '47264', '47265', '47266', '47267', '47268', '47269', '47270', '47271',
                                '47272', '47273', '47274', '47275', '47276', '47277', '47278', '47279', '47280',
                                '47281', '47282', '47283', '47284', '47285', '47286', '47287', '47288', '47289',
                                '47290', '47291', '47292', '47293', '47294', '47295', '47296', '47303', '47304',
                                '47310', '47311', '47313', '47314', '47315', '47317', '47319', '47320', '47321',
                                '47322', '47323', '47331', '47332', '47333', '47347', '47348', '47349', '47351',
                                '47352', '47353', '47354', '47355', '47356', '47357', '47358', '47359', '47360',
                                '47361', '47362', '47363', '47364', '47365', '47366', '47367', '47368', '47369',
                                '47370', '47371', '47416', '49141', '49142', '49157', '49158', '49159', '49160',
                                '49257', '49262', '49263', '49288', '49392', '49393', '49523', '49526', '49527',
                                '49531', '49532', '49537', '49538', '50456', '50457', '50458', '50459', '50460',
                                '50462', '50463', '50464', '50465', '50466', '50467', '50468', '50469', '50476',
                                '50480', '50481', '50482', '50483', '50484', '50485', '50486', '50487', '50488',
                                '50489', '50490', '50491', '50492', '50493', '50494', '50495', '50496', '50497',
                                '50498', '50499', '50500', '50501', '50502', '50503', '50504', '50505', '50506',
                                '50507', '50508', '50509', '50510', '50512', '50513', '50514', '50515', '50516',
                                '50517', '50518', '50519', '50520', '50521', '50522', '50523', '50524', '50525',
                                '50526', '50527', '50528', '50529', '50530', '50531', '50532', '50533', '50534',
                                '50535', '50536', '50537', '50538', '50539', '50540', '50541', '50542', '50543',
                                '50556', '50557', '50558', '50559', '50564', '50566', '50567', '50568', '50569',
                                '50589', '50590', '50605', '50606', '50607', '50609', '50982', '50991', '50992',
                                '51176', '51195', '51206', '51478', '51791', '51797', '51799', '51805', '51806',
                                '51807', '51814', '51930', '51933', '51941', '52010', '52015', '52016', '52017',
                                '52027', '52028', '52029', '52030', '52031', '52032', '52129', '53151', '53153',
                                '53154', '53155', '53156', '53157', '53158', '53160', '53161', '53162', '53188',
                                '53189', '53190', '53192', '53193', '53198', '53199', '53200', '53201', '53203',
                                '53283', '53292', '53297', '53299', '53300', '53302', '53307', '53308', '53309',
                                '53310', '53311', '53398', '8589934590', '8589934591', '8589934593', '8589934594',
                                '8589934683', '8589934792', '8589934793', '8589934794', '8589934795', '8589934796',
                                '8589934797', '8589934804', '8589934805', '8589934806', '8589934807', '8589934812',
                                '8589934813', '8589934814', '8589934815', '8589934816', '8589934817', '8589934818',
                                '8589934822', '8589934825', '8589934826', '8589934827', '8589934829', '8589934834',
                                '8589934835', '8589934836', '8589934837', '8589934948', '8589934961', '8589934964',
                                '8589934965', '8589934966', '8589934967', '8589934971', '8589934972', '8589934973',
                                '8589934974', '8589934980', '8589934981', '8589934982', '8589934983', '8589934984',
                                '8589934985', '8589934986', '8589934992', '8589935079', '8589935080', '8589935081',
                                '8589935197', '8589935198', '8589935199', '8589935203', '8589935204', '8589935205',
                                '8589935206', '8589935207', '8589935223', '8589935224', '8589935225', '8589935228',
                                '8589935233', '8589935234', '8589935235', '8589935236', '8589935237', '8589935238',
                                '8589935239', '8589935673', '8589935674', '8589935782', '8589935783', '8589935799',
                                '8589935800', '8589935803', '8589935804', '8589935805', '8589935806', '8589935810',
                                '8589936347', '8589936354', '8589936355', '8589936356', '8589936364', '8589936372',
                                '8589936377', '8589936392', '8589936393', '8589936394', '8589936395', '8589936396',
                                '8589936397', '8589936398', '8589936399', '8589936400', '8589936401', '8589936402',
                                '8589936403', '8589936404', '8589936405', '8589936406', '8589936410', '8589936619',
                                '8589936642', '8589936643', '8589936644', '8589936699', '8589936718', '8589936823',
                                '8589936824', '8589936826', '8589936827', '8589936828', '8589936829', '8589936830',
                                '8589936831', '8589936832', '8589936833', '8589936834', '8589936835', '8589936836',
                                '8589936841', '8589936842', '8589936843', '8589936844', '8589936845', '8589936851',
                                '8589936852', '8589936853', '8589936854', '8589936974', '8589937065', '8589937078',
                                '8589937079', '8589937080', '8589937083', '8589937084', '8589937085', '8589938050',
                                '8589938189', '8589938195', '8589938196', '8589938200', '8589938201', '8589938202',
                                '8589938203', '8589938204', '8589938205', '8589938206', '8589938207', '8589938208',
                                '8589938212', '8589938213', '8589938214', '8589938215', '8589938220', '8589938221',
                                '8589938222', '8589938223', '8589938230', '8589938250', '8589938251', '8589938252',
                                '8589938400', '8589938401', '8589938408', '8589938409', '8589938426', '8589938429',
                                '8589938430', '8589938431', '8589938434', '8589938435', '8589938437', '8589938438',
                                '8589938608', '8589938609', '8589938610', '8589938611', '8589938669', '8589938737',
                                '8589938760', '8589938761', '8589938762', '8589938764', '8589938766', '8589938784',
                                '8589938785', '8589938799', '8589938816', '8589938818', '8589938827', '8589938828',
                                '8589939116', '8589939117', '8589939124', '8589939298', '8589939299', '8589939300',
                                '8589939365', '8589939366', '8589939367', '8589939398', '8589939399', '8589940145',
                                '8589940334', '8589940353', '8589940445', '8589940446', '8589940454', '8589940457',
                                '8589940458', '8589940459', '8589940467', '8589940785', '8589940875', '8589940876',
                                '8589940882', '8589940883', '8589940923', '8589940947', '8589940957', '8589941029',
                                '8589941065', '8589941271', '8589941272', '8589941273', '8589941274', '8589941380',
                                '8589941384', '8589941388', '8589941418', '8589941420', '8589941421']
"""

sr = 8589934000
er = 8589937500
ssize = 1000
id_ranges = [range(x, x + ssize) for x in list(range(sr, er, ssize))]
for id_range in id_ranges:
    id_first = id_range[0]
    id_last = id_range[len(id_range) - 1]
    right_now = time.time()
    current_timestamp = datetime.datetime.fromtimestamp(right_now).strftime('%Y-%m-%d_%H-%M-%S')
    reporting_batch = 'spin_' + repr(id_first) + "-" + repr(id_last)
    download_root_path = '..{0}downloads'.format(os.sep)
    run_tag = reporting_batch + '_' + current_timestamp

    # Check for existing dir. Resume spin if found.
    for n in os.listdir(download_root_path):
        m = n.rsplit('_', 2)
        if len(m) == 3 and m[0] == run_tag.rsplit('_', 2)[0]:
            print 'Resuming existing spin range', n, 'instead of making new', run_tag
            run_tag = n

    download_path = '{0}{1}{2}'.format(download_root_path, os.sep, run_tag)
    try:
        os.makedirs(download_path)
    except OSError, e:
        if os.path.exists(download_path):
            with open('testwrite', 'w') as tw:
                text = 'testing write permissions'
                tw.write(text)
            os.remove('testwrite')
        else:
            download_path = 'bogus directory todo do something more intelligent'
            print 'Failed to create download target directory. Will now continue blithely on to explode later.'

    print
    print 'Target download directory \n\t{0}\n\texisting files {1}'.format(download_path, len(os.listdir(download_path)))
    print
    sys.stdout.flush()

    print 'Downloading ' + reporting_batch
    sys.stdout.flush()
    for asset_id in id_range:
        print
        url_download = "http://sos.nh.gov/WorkArea/DownloadAsset.aspx?id={0}".format(asset_id)
        hres = hr(asset_id)
        if hres['disp'] == '' and int(hres['length']) < 3000:
            print "HEAD Check] skipping small({0} bytes) HTML file id({1})".format(hres['length'], asset_id)
            continue

        socket = urllib2.urlopen(url_download)
        resp_st = socket.headers.subtype  # 'pdf' or 'jpeg' or 'msword'
        resp_ct = socket.headers.dict['content-type']  # 'application/pdf' or 'text/html; charset=utf-8'
        if resp_ct == 'text/html; charset=utf-8':
            resp_cl = socket.headers.dict['content-length']  # '2704'
            if int(resp_cl) < 4096:
                print "Skipping small({0} bytes) HTML file id({1})".format(resp_cl, asset_id)
                socket.close()
                continue
            their_file_name = 'some.html'
        else:  # 'application/msword','application/pdf','application/msword'
            resp_cd = socket.headers.dict[
                'content-disposition']  # 'attachment; filename="Cornerstone Action PAC (amend).pdf"'
            resp_te = socket.headers.dict['transfer-encoding']  # 'chunked'
            their_file_name = resp_cd.rsplit("\"")[1]

        if set(os.listdir(download_path)).issuperset(set(['spin_id({0})_{1}'.format(asset_id, their_file_name)])):
            print "Resume mode. File already exits."
            socket.close()
            continue

        filename_download = '{0}{1}spin_id({2})_{3}'.format(download_path, os.sep, asset_id, their_file_name)
        print '{0}] downloading to {1}'.format(asset_id, filename_download)
        print '   from {0}'.format(url_download)
        sys.stdout.flush()
        with open(filename_download, 'wb') as file_download:
            content = socket.read()
            socket.close()
            file_download.write(content)

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