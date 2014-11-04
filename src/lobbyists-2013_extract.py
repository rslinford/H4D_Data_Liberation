"""
Target download directory {lobbyists-2013-batch_crawled-2014-10-18_16-56-15_by-rslinford}
Section Menu at {http://sos.nh.gov/Lob012914A.aspx}
"""

import csv
import os
import re
import subprocess


de = (
    {
        'dn': 'Abbott, Gary(Associated General Contractors of NH)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52135',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/84789e08-c4e2-4fea-96be-97b4567f2611.pdf',
        'da': 'Abbott, Gary(Associated General Contractors of NH).pdf'
    },
    {
        'dn': 'Abbott, Will(SPNHF)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=8589936906',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/89d2415c-6e94-4557-ade8-20f7f1f29d79.pdf',
        'da': 'Abbott, Will(SPNHF).pdf'
    },
    {
        'dn': 'Acres, Valerie( NH College and University Council)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52136',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/c3828e00-7985-4d6c-b1e1-d139c402fbcf.pdf',
        'da': 'Acres, Valerie( NH College and University Council).pdf'
    },
    {
        'dn': 'Acres, Valerie(City of Dover)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52137',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/7ceac408-42fb-43a9-b9a9-4d9c28420261.pdf',
        'da': 'Acres, Valerie(City of Dover).pdf'
    },
    {
        'dn': 'Acres, Valerie(Electrical Contractors Business Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52138',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/8f486daa-3692-4d36-93f0-15803866aeb5.pdf',
        'da': 'Acres, Valerie(Electrical Contractors Business Assoc).pdf'
    },
    {
        'dn': 'Acres, Valerie(Fresenius Medical Care)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52139',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/126f064a-4d49-4a06-a912-07d133c0ca54.pdf',
        'da': 'Acres, Valerie(Fresenius Medical Care).pdf'
    },
    {
        'dn': 'Acres, Valerie(Granite State Home Health Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52140',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/ea3b2fe1-deef-4d5d-91c7-2e19bfed9ed1.pdf',
        'da': 'Acres, Valerie(Granite State Home Health Assoc).pdf'
    },
    {
        'dn': 'Acres, Valerie(Hosp Corp of America Ports Reg Hosp Parkland Med Cent)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52141',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/1382f557-93fb-4cb4-9076-0cf926f4c6a9.pdf',
        'da': 'Acres, Valerie(Hosp Corp of America Ports Reg Hosp Parkland Med Cent).pdf'
    },
    {
        'dn': 'Acres, Valerie(LeadingAge Maine New Hampshire)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52142',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/70b119e4-73e3-4b22-90f8-3a86e89b0ad6.pdf',
        'da': 'Acres, Valerie(LeadingAge Maine New Hampshire).pdf'
    },
    {
        'dn': 'Acres, Valerie(Lenscrafters Pearle Vision)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52143',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/64e29260-2d81-4520-860d-a619fb563ee4.pdf',
        'da': 'Acres, Valerie(Lenscrafters Pearle Vision).pdf'
    },
    {
        'dn': 'Acres, Valerie(Northeast Delta Dental)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52144',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/36586779-da9c-4b20-9e7e-16da384eac59.pdf',
        'da': 'Acres, Valerie(Northeast Delta Dental).pdf'
    },
    {
        'dn': 'Acres, Valerie(Schoolcare Health Benefit Plans of the NH)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52145',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/dac189da-e853-446e-b3c1-f4a8dc03a2f0.pdf',
        'da': 'Acres, Valerie(Schoolcare Health Benefit Plans of the NH).pdf'
    },
    {
        'dn': 'Aissa, Evelyn(NH Voices for Health)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=8589936907',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/0c429a83-1980-41fd-a0c5-ff58f2ce6c0c.pdf',
        'da': 'Aissa, Evelyn(NH Voices for Health).pdf'
    },
    {
        'dn': 'Alan, Larry(Nationwide Insurance)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52146',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/b22a8321-57b2-44c2-a571-a9f3e59b12a0.pdf',
        'da': 'Alan, Larry(Nationwide Insurance).pdf'
    },
    {
        'dn': 'Alibrandi, Christine(Northeast Delta Dental)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52147',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/ea2ec9a0-1f70-4174-bdd4-5521062f3f4d.pdf',
        'da': 'Alibrandi, Christine(Northeast Delta Dental).pdf'
    },
    {
        'dn': 'Allegretti, Daniel(Exelon Generation Company)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52148',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/b97d6830-a0d2-492d-a8dc-61c3401a0758.pdf',
        'da': 'Allegretti, Daniel(Exelon Generation Company).pdf'
    },
    {
        'dn': 'Allinson, Bradford(Quantitative Mgmt Assoc LLC)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52149',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/c210898f-0139-44ea-9c80-ae6761d36dcd.pdf',
        'da': 'Allinson, Bradford(Quantitative Mgmt Assoc LLC).pdf'
    },
    {
        'dn': 'Alpert, Arnold(American Friends Serv Comm)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52150',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/396c6b90-51aa-46a9-b967-fedf51d19fcb.pdf',
        'da': 'Alpert, Arnold(American Friends Serv Comm).pdf'
    },
    {
        'dn': 'Antrobus, Andrew(Pfizer Inc)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52151',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/c8529264-2658-4640-8084-7b0fd796ddd3.pdf',
        'da': 'Antrobus, Andrew(Pfizer Inc).pdf'
    },
    {
        'dn': 'Ardinger, William(Fidelity Investments)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52152',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/3080e77e-066c-4c58-8f57-1115236e5c71.pdf',
        'da': 'Ardinger, William(Fidelity Investments).pdf'
    },
    {
        'dn': 'Ardinger, William(Pennichuck Corp)',
        'wp': 'http://sos.nh.gov/Lob012914A.aspx?id=52153',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2461/dbd4c6e6-bffd-4daf-a163-addf99fa32bf.pdf',
        'da': 'Ardinger, William(Pennichuck Corp).pdf'
    },
    {
        'dn': 'Baldini, Donald(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52154',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/514b8889-79c0-488c-b428-ac2636045382.pdf',
        'da': 'Baldini, Donald(Addendum C).pdf'
    },
    {
        'dn': 'Baldini, Donald(Liberty Mutual Insurance)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52155',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/28886546-a629-4eed-af44-22856fd0ca6d.pdf',
        'da': 'Baldini, Donald(Liberty Mutual Insurance).pdf'
    },
    {
        'dn': 'Barry, Curtis(Atlantic Traders)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939187',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/2b7a3918-1d12-4be5-ac2e-61ebc5a33f6d.pdf',
        'da': 'Barry, Curtis(Atlantic Traders).pdf'
    },
    {
        'dn': 'Barry, Curtis(Express Scripts Holding Co)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939188',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/4c137c47-3b3f-42bf-8199-e9d632fc5d4b.pdf',
        'da': 'Barry, Curtis(Express Scripts Holding Co).pdf'
    },
    {
        'dn': 'Barry, Curtis(MERS)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939190',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e50da5c8-8f46-4a10-91b0-a94e1a8ff487.pdf',
        'da': 'Barry, Curtis(MERS).pdf'
    },
    {
        'dn': 'Barry, Curtis(Microsoft Corp)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939184',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/a149c9f3-7b58-4d32-ad08-aad85f222871.pdf',
        'da': 'Barry, Curtis(Microsoft Corp).pdf'
    },
    {
        'dn': 'Barry, Curtis(New England Auto Finance)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939189',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/245a28bd-2d4d-4b8d-9766-21c871b0bea5.pdf',
        'da': 'Barry, Curtis(New England Auto Finance).pdf'
    },
    {
        'dn': 'Barry, Curtis(NH Assoc of Broadcaster)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939191',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e0184f19-3616-41ba-a412-5db8fe2d784b.pdf',
        'da': 'Barry, Curtis(NH Assoc of Broadcaster).pdf'
    },
    {
        'dn': 'Barry, Curtis(NH Optometric Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939192',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/27180f1e-e13b-4559-88e1-0a0fb91f05d5.pdf',
        'da': 'Barry, Curtis(NH Optometric Assoc).pdf'
    },
    {
        'dn': 'Barry, Curtis(NH Transit Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939193',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/0fc858fb-de5e-4aa3-953a-c5c5b1a73b66.pdf',
        'da': 'Barry, Curtis(NH Transit Assoc).pdf'
    },
    {
        'dn': 'Barry, Curtis(Northeastern Retail Lumber Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939194',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/386b5ecc-ea4a-48c2-8a38-e1be55299726.pdf',
        'da': 'Barry, Curtis(Northeastern Retail Lumber Assoc).pdf'
    },
    {
        'dn': 'Barry, Curtis(Propane Gas Assoc of NE)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939185',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/fc3893e8-8a2f-4f65-b0ff-eebe5a9bc884.pdf',
        'da': 'Barry, Curtis(Propane Gas Assoc of NE).pdf'
    },
    {
        'dn': 'Barry, Curtis(Retail Merchants Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589939186',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/ddbaf6b6-b620-474e-94ec-26fb979cf9ce.pdf',
        'da': 'Barry, Curtis(Retail Merchants Assoc of NH).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(American Cancer Society Cancer Action Network)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52156',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9750febe-40a0-4e19-a4a9-00b914ce08ae.pdf',
        'da': 'Beaujouan, Karen(American Cancer Society Cancer Action Network).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(American Society for the Prevention of Cruelty to Animals)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52157',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/7ae93a02-f340-4b44-8319-bd2978a4273d.pdf',
        'da': 'Beaujouan, Karen(American Society for the Prevention of Cruelty to Animals).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Bridgewater Power Co)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52158',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5d924f9b-c983-48f9-8fda-d27635a69ca0.pdf',
        'da': 'Beaujouan, Karen(Bridgewater Power Co).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Coalition of Insurance and Financial Producers)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52159',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/b42274b3-3e00-474f-8cbc-ebcb29ce88d6.pdf',
        'da': 'Beaujouan, Karen(Coalition of Insurance and Financial Producers).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(CVS Caremark)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52160',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/7d98ae7f-6c38-4097-a0c0-799bbb83fd75.pdf',
        'da': 'Beaujouan, Karen(CVS Caremark).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52161',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/10505ca2-6484-4739-b03c-adcb17fabc7e.pdf',
        'da': 'Beaujouan, Karen(DG Whitefield).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52162',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/d17278f6-adb5-44e3-8c73-922d583d61bb.pdf',
        'da': 'Beaujouan, Karen(Elliot Health System).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(General Motors)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52163',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/a9414528-db1c-4da6-adda-875a9db5297a.pdf',
        'da': 'Beaujouan, Karen(General Motors).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Indeck Energy Alexandria)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52164',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/294e2cb5-5b88-418c-9245-e11bb9ac5d95.pdf',
        'da': 'Beaujouan, Karen(Indeck Energy Alexandria).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Independent Oil Marketers Assoc of N E)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52165',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/ef3da0ea-dd69-45c7-9b23-e08f9f9b4e93.pdf',
        'da': 'Beaujouan, Karen(Independent Oil Marketers Assoc of N E).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(ISO New England)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52166',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/a8edc258-f611-453d-9094-943eb41674f6.pdf',
        'da': 'Beaujouan, Karen(ISO New England).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Assoc of School Principals)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52167',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/25e5b5d2-f600-43f8-b9c0-d92e51be45b4.pdf',
        'da': 'Beaujouan, Karen(NH Assoc of School Principals).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Association of Realtors)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52168',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/1043023e-d709-424b-bcb8-be2a85895d0f.pdf',
        'da': 'Beaujouan, Karen(NH Association of Realtors).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Dental Society)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52169',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/afb678c4-af80-49c8-9f65-5bee4f1b222e.pdf',
        'da': 'Beaujouan, Karen(NH Dental Society).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Manufactured and Modular Housing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52170',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e6a5ef8d-17dc-4795-af6a-5475054f2703.pdf',
        'da': 'Beaujouan, Karen(NH Manufactured and Modular Housing Assoc).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Marine Trades Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52171',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/efc36f85-e8a7-46ff-9440-3370c5ce1f36.pdf',
        'da': 'Beaujouan, Karen(NH Marine Trades Assoc).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Psychiatric Society)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52172',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/89e745f0-002d-43c2-a795-fea5d321d64b.pdf',
        'da': 'Beaujouan, Karen(NH Psychiatric Society).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Snowmobile Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52173',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/759d523c-35fd-4382-afe7-4df02ab6c680.pdf',
        'da': 'Beaujouan, Karen(NH Snowmobile Assoc).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(NH Soft Drink Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52174',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/2b4beb22-0949-4992-af0b-a897f32ca4fd.pdf',
        'da': 'Beaujouan, Karen(NH Soft Drink Assoc).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52175',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e54d84af-8ae3-489f-abd2-f82c2653d8b2.pdf',
        'da': 'Beaujouan, Karen(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52176',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/efbc71b4-64f1-4931-ad3f-2279c06efd6b.pdf',
        'da': 'Beaujouan, Karen(Springfield Power).pdf'
    },
    {
        'dn': 'Beaujouan, Karen(XTL)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52177',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/b9cda7af-8867-450d-b0ed-7f1793e133fb.pdf',
        'da': 'Beaujouan, Karen(XTL).pdf'
    },
    {
        'dn': 'Beaulieu, Kristin(Citizens for a Strong NH)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52178',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9448946d-5153-498b-bf47-275fc269ac41.pdf',
        'da': 'Beaulieu, Kristin(Citizens for a Strong NH).pdf'
    },
    {
        'dn': 'Bennett, Daniel(NH Automobile Dealers Insurance Co)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52179',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/8154e600-9a72-4833-bb9f-3f5314bfcacb.pdf',
        'da': 'Bennett, Daniel(NH Automobile Dealers Insurance Co).pdf'
    },
    {
        'dn': 'Berke, Bruce(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52180',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/4ca38935-57fe-41b5-8bb0-f6592f859ffb.pdf',
        'da': 'Berke, Bruce(Addendum C).pdf'
    },
    {
        'dn': 'Berke, Bruce(Alttria Client Serv and affiliates)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52181',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/017bc4ff-dbbd-43bf-a5f3-9cb3853f5307.pdf',
        'da': 'Berke, Bruce(Alttria Client Serv and affiliates).pdf'
    },
    {
        'dn': 'Berke, Bruce(City of Dover)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52182',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/67b34484-2ef3-40a7-b27b-b66bd46e0866.pdf',
        'da': 'Berke, Bruce(City of Dover).pdf'
    },
    {
        'dn': 'Berke, Bruce(DBA International)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52183',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e549628f-71f0-4600-ac61-4ee20876e678.pdf',
        'da': 'Berke, Bruce(DBA International).pdf'
    },
    {
        'dn': 'Berke, Bruce(Elerctical Contractors Business Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52184',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/78608480-1880-45c7-bbaf-b26f0d9965e6.pdf',
        'da': 'Berke, Bruce(Elerctical Contractors Business Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(Equifax)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52185',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/051b7204-9bcb-437a-b3bd-2c7ad48c726d.pdf',
        'da': 'Berke, Bruce(Equifax).pdf'
    },
    {
        'dn': 'Berke, Bruce(Granite Ridge Energy LLC)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52186',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/a6bb77b6-5c3e-4054-b660-07ad07722c7e.pdf',
        'da': 'Berke, Bruce(Granite Ridge Energy LLC).pdf'
    },
    {
        'dn': 'Berke, Bruce(Granite Stata Coalition Against Expansion of Gambling)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52187',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/d5b9d5c2-3dd7-454f-8a2b-b7f686e9e091.pdf',
        'da': 'Berke, Bruce(Granite Stata Coalition Against Expansion of Gambling).pdf'
    },
    {
        'dn': 'Berke, Bruce(Hosp Corp of America Ports Reg Hosp Parkland Med Center)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52188',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/481c0ab3-6701-434d-b4f7-b2be74b2bd9a.pdf',
        'da': 'Berke, Bruce(Hosp Corp of America Ports Reg Hosp Parkland Med Center).pdf'
    },
    {
        'dn': 'Berke, Bruce(Law Warehouses Inc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52189',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/b8f86579-8f3a-4075-b4d4-a56edbf48ebe.pdf',
        'da': 'Berke, Bruce(Law Warehouses Inc).pdf'
    },
    {
        'dn': 'Berke, Bruce(Lenscrafters Pearle Vision)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52190',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5f627561-31bd-4744-a8d1-78ef4d9d1cb9.pdf',
        'da': 'Berke, Bruce(Lenscrafters Pearle Vision).pdf'
    },
    {
        'dn': 'Berke, Bruce(Mgmt Training Corp)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52191',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/3ce7ae13-7ba7-41d0-9b40-adb642a9cc93.pdf',
        'da': 'Berke, Bruce(Mgmt Training Corp).pdf'
    },
    {
        'dn': 'Berke, Bruce(N E Convience Stores Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52192',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/ca5681eb-93b6-48c0-ae14-e44ca7b56738.pdf',
        'da': 'Berke, Bruce(N E Convience Stores Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(National Grid)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52193',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9569a774-fbe8-420c-a6cc-bd4522896352.pdf',
        'da': 'Berke, Bruce(National Grid).pdf'
    },
    {
        'dn': 'Berke, Bruce(NextEra Energy Seabrook Station)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52194',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/23e1d2c4-fa0b-4fae-8a9d-3779b5035719.pdf',
        'da': 'Berke, Bruce(NextEra Energy Seabrook Station).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH Assoc of Chiefs of Police)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52195',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/c3c71d4b-214f-4a43-90d1-cf18adba68c4.pdf',
        'da': 'Berke, Bruce(NH Assoc of Chiefs of Police).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH College and University Council)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52196',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9afcc9d5-24ea-4762-bdca-ab76fc2fd30b.pdf',
        'da': 'Berke, Bruce(NH College and University Council).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH Land Surveyors Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52197',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e8b296e9-af11-4644-b069-cfcb5ac31714.pdf',
        'da': 'Berke, Bruce(NH Land Surveyors Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH Lodging and Restaurant Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52198',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9bf12857-8396-401a-92a0-dfa341550587.pdf',
        'da': 'Berke, Bruce(NH Lodging and Restaurant Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH Sheriffs Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52199',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e372161c-0af9-4ad3-8023-6eeafd13e98e.pdf',
        'da': 'Berke, Bruce(NH Sheriffs Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(NH Society of Certified Public Accountants)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52200',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5122bb8f-ae4d-4953-9c5c-24de9ec4847b.pdf',
        'da': 'Berke, Bruce(NH Society of Certified Public Accountants).pdf'
    },
    {
        'dn': 'Berke, Bruce(Northeast Delta Dental)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52201',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/fb09529a-16b1-46b5-b4d8-ea8109057aa2.pdf',
        'da': 'Berke, Bruce(Northeast Delta Dental).pdf'
    },
    {
        'dn': 'Berke, Bruce(Ntl Federation of Independent Business)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52202',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/a564bc2d-701c-40d7-9908-f0baf126d77c.pdf',
        'da': 'Berke, Bruce(Ntl Federation of Independent Business).pdf'
    },
    {
        'dn': 'Berke, Bruce(Professional Insurance Agents of New Hampshire)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52203',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/76ca2e77-8df9-47f0-a7b7-315f16be41c4.pdf',
        'da': 'Berke, Bruce(Professional Insurance Agents of New Hampshire).pdf'
    },
    {
        'dn': 'Berke, Bruce(Recreation Vehicle Industry Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52204',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/13449576-457f-478d-89ac-47a13221d6bd.pdf',
        'da': 'Berke, Bruce(Recreation Vehicle Industry Assoc).pdf'
    },
    {
        'dn': 'Berke, Bruce(segTEL)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52205',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/3da20bf9-ef78-4c6d-a935-afa7258da506.pdf',
        'da': 'Berke, Bruce(segTEL).pdf'
    },
    {
        'dn': 'Berke, Bruce(SKi New Hampshire Inc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52206',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/7f372acf-550c-4bf4-8f83-df55beb28a08.pdf',
        'da': 'Berke, Bruce(SKi New Hampshire Inc).pdf'
    },
    {
        'dn': 'Berke, Bruce(White Mountain Attractions)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52207',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/077136eb-5ccb-492b-87ee-f284f06c26ad.pdf',
        'da': 'Berke, Bruce(White Mountain Attractions).pdf'
    },
    {
        'dn': 'Berry, Elliott(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=8589936908',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/d575ce7b-51c4-4cf6-b82a-202a146984ce.pdf',
        'da': 'Berry, Elliott(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'Bianco, James(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52208',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/c1b9724d-a175-4bcd-b1b8-6a5a2eb8485d.pdf',
        'da': 'Bianco, James(Addendum C).pdf'
    },
    {
        'dn': 'Bianco, James(American Cancer Society Cancer Action Network)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52209',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/1a8aa40f-eaf9-4d6e-a25d-8d0d413a1fdf.pdf',
        'da': 'Bianco, James(American Cancer Society Cancer Action Network).pdf'
    },
    {
        'dn': 'Bianco, James(American Society for the Prevention of Cruelty to Animals)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52210',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/eedca252-a02d-4bb7-a25c-0de8fd559dc3.pdf',
        'da': 'Bianco, James(American Society for the Prevention of Cruelty to Animals).pdf'
    },
    {
        'dn': 'Bianco, James(Bridgewater Power Co)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52211',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/3ae1c3a5-4afa-4add-9d83-33a8fe25656a.pdf',
        'da': 'Bianco, James(Bridgewater Power Co).pdf'
    },
    {
        'dn': 'Bianco, James(Cisco Systems)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52212',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/e4e768b1-788b-4bee-9e47-1946cdf83ec2.pdf',
        'da': 'Bianco, James(Cisco Systems).pdf'
    },
    {
        'dn': 'Bianco, James(Coalition of Insurance and Financial Producers)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52213',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/f2d0ae95-2637-43c0-9c47-dfea0e64dacb.pdf',
        'da': 'Bianco, James(Coalition of Insurance and Financial Producers).pdf'
    },
    {
        'dn': 'Bianco, James(CVS Caremark)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52214',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/4334ac81-cbac-4155-9913-93e9f0a1f734.pdf',
        'da': 'Bianco, James(CVS Caremark).pdf'
    },
    {
        'dn': 'Bianco, James(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52215',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/73773bcb-e2c5-4ad7-b309-3a26d2eb8742.pdf',
        'da': 'Bianco, James(DG Whitefield).pdf'
    },
    {
        'dn': 'Bianco, James(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52216',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/6b550c93-10db-4e49-8680-4151d98db290.pdf',
        'da': 'Bianco, James(Elliot Health System).pdf'
    },
    {
        'dn': 'Bianco, James(Focus Technology Solutions)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52217',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/cb067eb8-6b11-4913-b61a-e2cba82e4e7c.pdf',
        'da': 'Bianco, James(Focus Technology Solutions).pdf'
    },
    {
        'dn': 'Bianco, James(General Motors)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52218',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/ab151e60-6bde-4265-b202-61d775fbbcfc.pdf',
        'da': 'Bianco, James(General Motors).pdf'
    },
    {
        'dn': 'Bianco, James(Indeck Energy Alexandria)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52219',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5a1209df-1dc0-45d2-9d29-0210332bd04b.pdf',
        'da': 'Bianco, James(Indeck Energy Alexandria).pdf'
    },
    {
        'dn': 'Bianco, James(Independent Oil Marketers Assoc of N E)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52220',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/3ca347ce-0fba-479f-80d6-01b430c5e15e.pdf',
        'da': 'Bianco, James(Independent Oil Marketers Assoc of N E).pdf'
    },
    {
        'dn': 'Bianco, James(ISO New Enlgand)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52221',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/935ea8a0-9183-496c-ac34-f04fda561414.pdf',
        'da': 'Bianco, James(ISO New Enlgand).pdf'
    },
    {
        'dn': 'Bianco, James(NH Assoc of School Principals)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52222',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5d3ac9d1-1054-4856-9581-27f7832f9361.pdf',
        'da': 'Bianco, James(NH Assoc of School Principals).pdf'
    },
    {
        'dn': 'Bianco, James(NH Association of Realtors)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52223',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/eae51454-03d9-4143-b6f7-5fe1bda44f2d.pdf',
        'da': 'Bianco, James(NH Association of Realtors).pdf'
    },
    {
        'dn': 'Bianco, James(NH Dental Society)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52224',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/fb8c68bf-5e55-4281-91d2-83e99857dad6.pdf',
        'da': 'Bianco, James(NH Dental Society).pdf'
    },
    {
        'dn': 'Bianco, James(NH Manufactured and Modular Housing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52225',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/4e301c65-4383-487a-a330-0202bc0c34af.pdf',
        'da': 'Bianco, James(NH Manufactured and Modular Housing Assoc).pdf'
    },
    {
        'dn': 'Bianco, James(NH Marine Trades Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52226',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/dac70859-723e-4a25-8304-dfea629e473a.pdf',
        'da': 'Bianco, James(NH Marine Trades Assoc).pdf'
    },
    {
        'dn': 'Bianco, James(NH Psychiatric Society)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52227',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/0ac6d1f4-9833-4551-963b-b05402a84ad7.pdf',
        'da': 'Bianco, James(NH Psychiatric Society).pdf'
    },
    {
        'dn': 'Bianco, James(NH Snowmobile Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52228',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5b1d4409-1f2d-4a93-ac81-d7a43514a108.pdf',
        'da': 'Bianco, James(NH Snowmobile Assoc).pdf'
    },
    {
        'dn': 'Bianco, James(NH Soft Drink Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52229',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/4046382f-0239-4989-b550-03317a353749.pdf',
        'da': 'Bianco, James(NH Soft Drink Assoc).pdf'
    },
    {
        'dn': 'Bianco, James(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52230',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/3b8bb307-0bcd-453d-8346-eab08b5a4701.pdf',
        'da': 'Bianco, James(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Bianco, James(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52231',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/9ed2590f-ea24-4eb0-a2fe-f7dbe14efff9.pdf',
        'da': 'Bianco, James(Springfield Power).pdf'
    },
    {
        'dn': 'Bianco, James(XTL)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52232',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/267fb166-bbad-4e92-9b23-ce51c5a63562.pdf',
        'da': 'Bianco, James(XTL).pdf'
    },
    {
        'dn': 'Bisbee, George(NH Assoc of Natural Resource Scientists)',
        'wp': 'http://sos.nh.gov/Lob012914BaBi.aspx?id=52233',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2462/5d3f3e7b-ad54-44e3-bf20-1ae38a3e446b.pdf',
        'da': 'Bisbee, George(NH Assoc of Natural Resource Scientists).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(America Votes)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52234',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/397cdf26-3315-4201-8f04-49669bfca1dc.pdf',
        'da': 'Blaisdell, Robert(America Votes).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Bank of America)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52235',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/b44f816c-15fd-4eac-bc93-7361e4ed71e8.pdf',
        'da': 'Blaisdell, Robert(Bank of America).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Cannery Casino Resorts)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52236',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/6c2eb6bb-d27e-42be-8509-959ef86e13e8.pdf',
        'da': 'Blaisdell, Robert(Cannery Casino Resorts).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Centene Corp)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52237',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/707f46c1-bf4f-4711-8606-d88c0e9198da.pdf',
        'da': 'Blaisdell, Robert(Centene Corp).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Comcast)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52238',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/28dd5435-1826-4f9d-9b5a-f5ab1ac62533.pdf',
        'da': 'Blaisdell, Robert(Comcast).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Consumer Safety Technology)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52239',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/60896226-dc0b-4952-be4f-9f482c18ccf4.pdf',
        'da': 'Blaisdell, Robert(Consumer Safety Technology).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(FedEx)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52240',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/a69afb30-7f14-4fe5-9d0c-e118b1f62136.pdf',
        'da': 'Blaisdell, Robert(FedEx).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Heritage Plumbing Heating Inc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52241',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/10ae3cf4-d72f-4568-9cee-ef90ef714435.pdf',
        'da': 'Blaisdell, Robert(Heritage Plumbing Heating Inc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(IBM Corp)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52242',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/8cb5c3e1-bdbb-488f-b68a-242d43babfe1.pdf',
        'da': 'Blaisdell, Robert(IBM Corp).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(IGT)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52243',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/337d1879-32f2-4f51-abee-d69b9fd62852.pdf',
        'da': 'Blaisdell, Robert(IGT).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(International Bottled Water Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52244',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/44798f7f-549b-441b-bceb-42320011fbf9.pdf',
        'da': 'Blaisdell, Robert(International Bottled Water Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Mortgage Bankers and Brokers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52245',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/c1ab1e9b-1b63-4c93-a1de-612023000a94.pdf',
        'da': 'Blaisdell, Robert(Mortgage Bankers and Brokers Assoc of NH).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Athletic Trainers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52246',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/b6521e9f-3d3d-48b4-816e-aad61d4bb48c.pdf',
        'da': 'Blaisdell, Robert(NH Athletic Trainers Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Automobile Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52247',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/ed7867d8-2ff4-4910-aa40-9f5456bd94f2.pdf',
        'da': 'Blaisdell, Robert(NH Automobile Dealers Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Coalition for Prosthetics)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52248',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/f21d36c5-3737-4993-ba51-0f5dbd2b6942.pdf',
        'da': 'Blaisdell, Robert(NH Coalition for Prosthetics).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Driver Education Teachers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52249',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/31f59591-61ae-4676-a732-fd237a665bdd.pdf',
        'da': 'Blaisdell, Robert(NH Driver Education Teachers Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Genetic Counselors)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52250',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/d46e31ae-6da1-46ba-9d44-e1ce41f81937.pdf',
        'da': 'Blaisdell, Robert(NH Genetic Counselors).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Police Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52251',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/611dd913-a29e-4bde-9bdb-d41461d95424.pdf',
        'da': 'Blaisdell, Robert(NH Police Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Psychological Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52252',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/a4754355-92f8-4691-b7e8-b1d10bb1f145.pdf',
        'da': 'Blaisdell, Robert(NH Psychological Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Speech Language and Hearing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52253',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/229e8cfa-fd33-4795-976b-57c514d31e5a.pdf',
        'da': 'Blaisdell, Robert(NH Speech Language and Hearing Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Troopers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52254',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/685458a5-d7e6-497c-b558-8e2f51cf8f70.pdf',
        'da': 'Blaisdell, Robert(NH Troopers Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(NH Wine and Spirits Brokers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52255',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/96d95c6f-5497-40a3-a88f-b330bd3b894f.pdf',
        'da': 'Blaisdell, Robert(NH Wine and Spirits Brokers Assoc).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(North Country Environmental Services)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52256',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/9bd52e28-3d08-4469-b248-7f2b8d07a89b.pdf',
        'da': 'Blaisdell, Robert(North Country Environmental Services).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Optimum Technology)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52257',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/c9311ce1-c66e-4166-a849-f2edbd373102.pdf',
        'da': 'Blaisdell, Robert(Optimum Technology).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Pfizer)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52258',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/c27baef2-f38a-4876-9513-3b2bf1c46831.pdf',
        'da': 'Blaisdell, Robert(Pfizer).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(PhRMA)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52259',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/3ca54ebe-1ed1-4d3e-8977-3be10c687f1f.pdf',
        'da': 'Blaisdell, Robert(PhRMA).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(Pilot Health LLC)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52260',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/0323fe4c-5fd9-41cf-afaa-9c93bfd7bfa4.pdf',
        'da': 'Blaisdell, Robert(Pilot Health LLC).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(PSNH)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52261',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/f4075999-1cd2-4bd4-b0e6-113ec6c719a0.pdf',
        'da': 'Blaisdell, Robert(PSNH).pdf'
    },
    {
        'dn': 'Blaisdell, Robert(RAI Services Company)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52262',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/302d8363-9a8c-41ce-9d3d-88c09de3d370.pdf',
        'da': 'Blaisdell, Robert(RAI Services Company).pdf'
    },
    {
        'dn': 'Bohne, Meg(Consumer Union of US Inc Consumer Reports)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52263',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/fc5645f3-e41b-4a91-b0ad-50b6ed1329e8.pdf',
        'da': 'Bohne, Meg(Consumer Union of US Inc Consumer Reports).pdf'
    },
    {
        'dn': 'Bouley, Jim(3M)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52264',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/dfe512c0-eedc-43bc-b504-cf1e1d766b09.pdf',
        'da': 'Bouley, Jim(3M).pdf'
    },
    {
        'dn': 'Bouley, Jim(Intralot)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52265',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/08b9c75b-718a-4236-b152-9067242ef03f.pdf',
        'da': 'Bouley, Jim(Intralot).pdf'
    },
    {
        'dn': 'Bouley, Jim(NCES)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52266',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/20caec2c-38c1-4d4c-b318-6256304f78be.pdf',
        'da': 'Bouley, Jim(NCES).pdf'
    },
    {
        'dn': 'Bouley, Jim(NHANA)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52267',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/727fd890-b21d-41ef-8aff-17948acec302.pdf',
        'da': 'Bouley, Jim(NHANA).pdf'
    },
    {
        'dn': 'Bouley, Jim(Northeast Equipment Dealers)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52268',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/d6d3b8bf-b7c5-4a74-b847-3b9f041d571b.pdf',
        'da': 'Bouley, Jim(Northeast Equipment Dealers).pdf'
    },
    {
        'dn': 'Bouley, Jim(Xerox)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52269',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/73fd84a0-0a43-4013-8e34-baa00be4c377.pdf',
        'da': 'Bouley, Jim(Xerox).pdf'
    },
    {
        'dn': 'Bouley, Richard(American Physical Therapist)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52270',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/98f8edb9-5843-4638-b08e-d2fa1c31fa45.pdf',
        'da': 'Bouley, Richard(American Physical Therapist).pdf'
    },
    {
        'dn': 'Bouley, Richard(Atlas)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52271',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/fc7f151c-7436-445b-b40d-b606156439b0.pdf',
        'da': 'Bouley, Richard(Atlas).pdf'
    },
    {
        'dn': 'Bouley, Richard(CBS Outdoors)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52272',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/4efd9f89-5c48-4fcd-b173-e6e8667a6474.pdf',
        'da': 'Bouley, Richard(CBS Outdoors).pdf'
    },
    {
        'dn': 'Bouley, Richard(COG Railway)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52273',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/2880c475-2737-4ed2-8a35-5c9bf86f3856.pdf',
        'da': 'Bouley, Richard(COG Railway).pdf'
    },
    {
        'dn': 'Bouley, Richard(Diamond Distributors)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52274',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/68acb369-98af-4540-8786-1660f8ac30b6.pdf',
        'da': 'Bouley, Richard(Diamond Distributors).pdf'
    },
    {
        'dn': 'Bouley, Richard(NH Opticians)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52275',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/5d2cbb54-da02-4eef-9f73-3cbbee868c38.pdf',
        'da': 'Bouley, Richard(NH Opticians).pdf'
    },
    {
        'dn': 'Bouley, Richard(NH Veterinarians)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52276',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/4b4ffbfe-a5b3-44cc-8293-be6229acbd90.pdf',
        'da': 'Bouley, Richard(NH Veterinarians).pdf'
    },
    {
        'dn': 'Bouley, Richard(Senior Nutrition Network)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52277',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/559b4b4f-fdc7-4054-9e23-41c02612cc38.pdf',
        'da': 'Bouley, Richard(Senior Nutrition Network).pdf'
    },
    {
        'dn': 'Bouley, Richard(Teamsters)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52278',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/2ae5deba-75a1-45e9-849f-26af958a2f92.pdf',
        'da': 'Bouley, Richard(Teamsters).pdf'
    },
    {
        'dn': 'Bouley, Richard(UNH AAUP)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52279',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/ce7b8d81-0958-4906-9fbd-f4829f199dcf.pdf',
        'da': 'Bouley, Richard(UNH AAUP).pdf'
    },
    {
        'dn': 'Bourbeau, Joanne(Humaine Society of the United States)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52280',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/a90bb738-b81e-48ea-91bf-af4884796116.pdf',
        'da': 'Bourbeau, Joanne(Humaine Society of the United States).pdf'
    },
    {
        'dn': 'Bourque, Kevin(Addendum C 1)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52281',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/03a02986-f9d3-46cd-bb15-4c9128c31ea0.pdf',
        'da': 'Bourque, Kevin(Addendum C 1).pdf'
    },
    {
        'dn': 'Bourque, Kevin(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52282',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/62ec4e5e-3d75-4ca1-9777-7e678145ffa5.pdf',
        'da': 'Bourque, Kevin(Addendum C).pdf'
    },
    {
        'dn': 'Braley, Philip(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52283',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/9a44ed86-1ef5-4889-b0a0-b0dc6c3f20be.pdf',
        'da': 'Braley, Philip(Addendum C).pdf'
    },
    {
        'dn': 'Braley, Philip(Casella Waste Systems)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52284',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/66f1fa41-b951-4dfc-9943-1228c0604a55.pdf',
        'da': 'Braley, Philip(Casella Waste Systems).pdf'
    },
    {
        'dn': 'Brewer, Elizabeth(Sanofi US)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52285',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/e0f1c9a2-dfcb-48f2-9ff2-9f1db25363b7.pdf',
        'da': 'Brewer, Elizabeth(Sanofi US).pdf'
    },
    {
        'dn': 'Brown, Gail(NH Oral Health Coalition REVISED)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=8589936909',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/20d3367f-a915-487f-aded-a36cc450154b.pdf',
        'da': 'Brown, Gail(NH Oral Health Coalition REVISED).pdf'
    },
    {
        'dn': 'Brown, Gail(NH Oral Health Coalition)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52286',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/fcbaaf0c-da79-46bb-9822-cc8fa4493b8b.pdf',
        'da': 'Brown, Gail(NH Oral Health Coalition).pdf'
    },
    {
        'dn': 'Brown, Marc(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52287',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/c8ce24ae-2f5b-4bd9-9c7e-373586cab631.pdf',
        'da': 'Brown, Marc(Addendum C).pdf'
    },
    {
        'dn': 'Brown, Marc(New England Ratepayers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52288',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/61d84b1a-6876-4144-90dd-c8b9306b3f35.pdf',
        'da': 'Brown, Marc(New England Ratepayers Assoc).pdf'
    },
    {
        'dn': 'Brown, Sheridan(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52289',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/d640b47e-6925-4a75-812e-3a791501d1ec.pdf',
        'da': 'Brown, Sheridan(Addendum C).pdf'
    },
    {
        'dn': 'Brown, Sheridan(Loon Preservation Committee)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52290',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/21de7d0e-9b3f-4418-8f76-7d49e936316a.pdf',
        'da': 'Brown, Sheridan(Loon Preservation Committee).pdf'
    },
    {
        'dn': 'Brown, Sheridan(New Hampshire Audubon)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52291',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/f2601c90-e928-4252-bd86-2cc3e0c45b80.pdf',
        'da': 'Brown, Sheridan(New Hampshire Audubon).pdf'
    },
    {
        'dn': 'Buck, Kendall(Home Builders Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52292',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/2b9a23e0-5db5-41f2-bca1-35d0f1126b25.pdf',
        'da': 'Buck, Kendall(Home Builders Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Buckley, Kevin(Johnson and Johnson)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52294',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/f41258d1-7ac8-4f3f-9944-d398ab44e38f.pdf',
        'da': 'Buckley, Kevin(Johnson and Johnson).pdf'
    },
    {
        'dn': 'Burger, Peter(Hat Trick Logistics)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52293',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/75cc2563-9527-47d4-a1d5-686fcf43e83b.pdf',
        'da': 'Burger, Peter(Hat Trick Logistics).pdf'
    },
    {
        'dn': 'Butler, Judith Ann(Merck Sharp and Dohme Corp)',
        'wp': 'http://sos.nh.gov/Lob012914BlBu.aspx?id=52295',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2463/4b27c1b4-196f-4b55-8cad-89129553a8c5.pdf',
        'da': 'Butler, Judith Ann(Merck Sharp and Dohme Corp).pdf'
    },
    {
        'dn': 'Cascone, Heather(Express Scripts Holding Co)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52296',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/dec43fb5-a27e-44cf-8ef7-0b4f2f6720d5.pdf',
        'da': 'Cascone, Heather(Express Scripts Holding Co).pdf'
    },
    {
        'dn': 'Chaffee, Devon(NH Civil Liberties Union)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52297',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/65cbae79-6de6-4b8f-a2b0-4b1d50149b76.pdf',
        'da': 'Chaffee, Devon(NH Civil Liberties Union).pdf'
    },
    {
        'dn': 'Clark, Kelly(AARP)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52298',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/653cfeb2-cdb8-4f6b-9282-a3e6ef971692.pdf',
        'da': 'Clark, Kelly(AARP).pdf'
    },
    {
        'dn': 'Clayton, Nancy(Yankee Greyhound Racing Inc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52299',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/53351ea3-35db-4ab5-b83c-24e5a595fea0.pdf',
        'da': 'Clayton, Nancy(Yankee Greyhound Racing Inc).pdf'
    },
    {
        'dn': 'Cleary, Joseph(Bayer Healthcare LLC)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52300',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/47ed35a3-4f76-474c-9462-f1c865a75a49.pdf',
        'da': 'Cleary, Joseph(Bayer Healthcare LLC).pdf'
    },
    {
        'dn': 'Clegg, Robert(Biotechnology Industry Organization)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52301',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/09dbe272-f2ff-4892-9c8a-58606dbea295.pdf',
        'da': 'Clegg, Robert(Biotechnology Industry Organization).pdf'
    },
    {
        'dn': 'Clegg, Robert(Cigar Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52302',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/1a05e00f-a915-43b8-8add-639a0c6fda97.pdf',
        'da': 'Clegg, Robert(Cigar Assoc of NH).pdf'
    },
    {
        'dn': 'Clegg, Robert(Granite State Independent Living)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52303',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/6d733a73-1d90-462d-8035-7688d86fd357.pdf',
        'da': 'Clegg, Robert(Granite State Independent Living).pdf'
    },
    {
        'dn': 'Clegg, Robert(Greenmeadow Golf Club)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52304',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/4c98c750-823c-42db-b510-6fafbf313628.pdf',
        'da': 'Clegg, Robert(Greenmeadow Golf Club).pdf'
    },
    {
        'dn': 'Clegg, Robert(Heritage Case Mgmt)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52305',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/a84d950a-eaf6-4d40-9e76-662711acb7cc.pdf',
        'da': 'Clegg, Robert(Heritage Case Mgmt).pdf'
    },
    {
        'dn': 'Clegg, Robert(Injured Workers Pharmacy)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52306',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/812872a1-7799-4105-b651-afadab68ed15.pdf',
        'da': 'Clegg, Robert(Injured Workers Pharmacy).pdf'
    },
    {
        'dn': 'Clegg, Robert(NH Assoc for Justice)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52307',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/441b8377-fb00-456d-aea1-709ed691448c.pdf',
        'da': 'Clegg, Robert(NH Assoc for Justice).pdf'
    },
    {
        'dn': 'Clegg, Robert(NH Building Officials Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52308',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/02c5d712-4dc6-44b7-bbbc-2ea34d049d01.pdf',
        'da': 'Clegg, Robert(NH Building Officials Assoc).pdf'
    },
    {
        'dn': 'Clegg, Robert(NH Camp Directors Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52309',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/5f723b1b-89d4-46f1-9d82-919eca2de71a.pdf',
        'da': 'Clegg, Robert(NH Camp Directors Assoc).pdf'
    },
    {
        'dn': 'Clegg, Robert(Ntl Assoc of Professional Employer Org)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52310',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/59a2f641-09e7-4c64-9c01-563908c83b9f.pdf',
        'da': 'Clegg, Robert(Ntl Assoc of Professional Employer Org).pdf'
    },
    {
        'dn': 'Clegg, Robert(Responsible Industry for a Sound Environment)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52311',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/1825e0ae-4e2d-4321-921e-cd313d62ef28.pdf',
        'da': 'Clegg, Robert(Responsible Industry for a Sound Environment).pdf'
    },
    {
        'dn': 'Cohen, Richard(Disabilities Rights Center)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52312',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/c95efa37-6472-42f7-84e1-f26f8b51a175.pdf',
        'da': 'Cohen, Richard(Disabilities Rights Center).pdf'
    },
    {
        'dn': 'Colantuono, Thomas(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52313',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/c4f08fdd-dc20-4e1a-851a-9caa2b25ab61.pdf',
        'da': 'Colantuono, Thomas(Elliot Health System).pdf'
    },
    {
        'dn': 'Colantuono, Thomas(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52314',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/6ccebea7-5ca7-487c-895e-3aa41de1cdcd.pdf',
        'da': 'Colantuono, Thomas(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Collins, David(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52315',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/752156fc-dfa8-4222-be40-4068b6e3d7cf.pdf',
        'da': 'Collins, David(Addendum C).pdf'
    },
    {
        'dn': 'Collins, David(American Express)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52316',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/5819c43f-bc2e-440b-91fb-65d23eeab852.pdf',
        'da': 'Collins, David(American Express).pdf'
    },
    {
        'dn': 'Collins, David(American Peteroleum Institute)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52317',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/10d0ad31-0184-49b6-9807-d6ce952e47a9.pdf',
        'da': 'Collins, David(American Peteroleum Institute).pdf'
    },
    {
        'dn': 'Collins, David(Anthem Blue Cross Blue Shield Wellpoint)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52318',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/68441e57-e7dd-40b7-b501-4a43e5beaf41.pdf',
        'da': 'Collins, David(Anthem Blue Cross Blue Shield Wellpoint).pdf'
    },
    {
        'dn': 'Collins, David(AstraZeneca Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52319',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/94164d2d-b85f-4a3d-947c-5ada02d668d3.pdf',
        'da': 'Collins, David(AstraZeneca Pharmaceuticals).pdf'
    },
    {
        'dn': 'Collins, David(Bedford Ambulatory Surgical Center)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52320',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/8729f74f-f54c-4dfe-a5d1-29881850a70b.pdf',
        'da': 'Collins, David(Bedford Ambulatory Surgical Center).pdf'
    },
    {
        'dn': 'Collins, David(Blue Mountain Forest Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52321',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/8217b37e-5aa7-4d16-846c-8f9f8749b5f6.pdf',
        'da': 'Collins, David(Blue Mountain Forest Assoc).pdf'
    },
    {
        'dn': 'Collins, David(City of Rochester Wastewater Treatment Plant)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52322',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/16d828f7-348c-44a2-b4a9-020a195ccd11.pdf',
        'da': 'Collins, David(City of Rochester Wastewater Treatment Plant).pdf'
    },
    {
        'dn': 'Collins, David(Comcast Corp)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52323',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/dfdf2dd6-139b-4719-810b-5ed541f4b5c4.pdf',
        'da': 'Collins, David(Comcast Corp).pdf'
    },
    {
        'dn': 'Collins, David(Correction Corp of America)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52324',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/0188ee93-009e-4ea3-be51-ed98f13cf074.pdf',
        'da': 'Collins, David(Correction Corp of America).pdf'
    },
    {
        'dn': 'Collins, David(Dartmouth College)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52325',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/aee866ff-74db-4fe3-b8b8-e6e4de3ce565.pdf',
        'da': 'Collins, David(Dartmouth College).pdf'
    },
    {
        'dn': 'Collins, David(Dartmouth Medical School)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52326',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/1d56cdab-1914-4d2e-99e6-ad8f346331c6.pdf',
        'da': 'Collins, David(Dartmouth Medical School).pdf'
    },
    {
        'dn': 'Collins, David(Explore Informational Serv)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52327',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/b8a9e341-eaee-4cb4-89eb-7197d94b9216.pdf',
        'da': 'Collins, David(Explore Informational Serv).pdf'
    },
    {
        'dn': 'Collins, David(Feld Entertainment)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52328',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/f6bc695b-ae95-4a2e-ab78-c3e3dc8bcf5a.pdf',
        'da': 'Collins, David(Feld Entertainment).pdf'
    },
    {
        'dn': 'Collins, David(Fidelity Investments)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52329',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/788a3483-91c7-4888-8b53-d5f87ca1bfeb.pdf',
        'da': 'Collins, David(Fidelity Investments).pdf'
    },
    {
        'dn': 'Collins, David(Merck Sharp and Dohme)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52330',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/c81eec46-1dbb-44ad-afc2-d69fc2022f83.pdf',
        'da': 'Collins, David(Merck Sharp and Dohme).pdf'
    },
    {
        'dn': 'Collins, David(N E Medical Equipment Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52331',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/cd1b6abe-db87-4a20-b5bb-2693fa84a1ea.pdf',
        'da': 'Collins, David(N E Medical Equipment Dealers Assoc).pdf'
    },
    {
        'dn': 'Collins, David(N H Credit Union League)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52332',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/b1b18fa9-bfc0-4218-8863-d880a6761574.pdf',
        'da': 'Collins, David(N H Credit Union League).pdf'
    },
    {
        'dn': 'Collins, David(N H Independent Schools)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52333',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/387c88e3-1ea1-4090-92b6-44a17438dd44.pdf',
        'da': 'Collins, David(N H Independent Schools).pdf'
    },
    {
        'dn': 'Collins, David(NH Alliance of Boys and Girls Clubs)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52334',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/210704ef-e361-4302-b3bd-f22c8c1c3584.pdf',
        'da': 'Collins, David(NH Alliance of Boys and Girls Clubs).pdf'
    },
    {
        'dn': 'Collins, David(Ntl Shooting Sports Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52335',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/f6fe2297-2846-44b3-92c3-fa9916e2c0c3.pdf',
        'da': 'Collins, David(Ntl Shooting Sports Foundation).pdf'
    },
    {
        'dn': 'Collins, David(Public Service Co of NH)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52336',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/ef5a9dab-a94d-4c64-a248-d3fc64700e07.pdf',
        'da': 'Collins, David(Public Service Co of NH).pdf'
    },
    {
        'dn': 'Collins, David(RAI Services Co)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52337',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/922caf7c-e10c-4af7-b239-7f45e05c67d2.pdf',
        'da': 'Collins, David(RAI Services Co).pdf'
    },
    {
        'dn': 'Collins, David(Rural Hospital Coalition)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52338',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/f8c84c97-1de1-4ee6-bf9e-c7a9b4f9381b.pdf',
        'da': 'Collins, David(Rural Hospital Coalition).pdf'
    },
    {
        'dn': 'Collins, David(TracFone Wireless)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52339',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/6570c94d-6b37-4b17-a119-fd064dd19935.pdf',
        'da': 'Collins, David(TracFone Wireless).pdf'
    },
    {
        'dn': 'Coluntuono, Thomas(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52340',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/e211e431-5059-4cf8-9eaf-a65a6f0a37c9.pdf',
        'da': 'Coluntuono, Thomas(Addendum C).pdf'
    },
    {
        'dn': 'Connolly, Susan(Alliance of Automobile Manufacurers)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=8589939196',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/e108bd69-2014-4b30-9cbb-6298d973b494.pdf',
        'da': 'Connolly, Susan(Alliance of Automobile Manufacurers).pdf'
    },
    {
        'dn': 'Connolly, Susan(Nature Conservancy)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=8589939197',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/33857520-9385-4321-a537-536ebf80110d.pdf',
        'da': 'Connolly, Susan(Nature Conservancy).pdf'
    },
    {
        'dn': 'Cooper, Katherine(NH Association of Criminal Defense Lawyers)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52341',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/cd37b511-2886-48f9-91ba-562188a715d9.pdf',
        'da': 'Cooper, Katherine(NH Association of Criminal Defense Lawyers).pdf'
    },
    {
        'dn': 'Corey Fox(Independent Oil Marketers Assoc of N E)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52342',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/ea0374ea-2db6-4315-9e45-79c3e0f1a058.pdf',
        'da': 'Corey Fox(Independent Oil Marketers Assoc of N E).pdf'
    },
    {
        'dn': 'Corey Fox(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52343',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/e513f3c3-a7b0-49f6-8c03-56cbbe528eec.pdf',
        'da': 'Corey Fox(Springfield Power).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(American Cancer Society Cancer Action Network)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52344',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/7446657a-d28d-4aee-8829-8a2685e630b4.pdf',
        'da': 'Corey Fox, Kathy(American Cancer Society Cancer Action Network).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(Bridgewater Power Co)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52345',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/7134c56f-c1a2-4623-a536-81d9985c4d46.pdf',
        'da': 'Corey Fox, Kathy(Bridgewater Power Co).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(Coalition of Insurance and Financaial Producers)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52346',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/c9193474-fb03-43e1-95c4-05c483f180ea.pdf',
        'da': 'Corey Fox, Kathy(Coalition of Insurance and Financaial Producers).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(CVS Caremark)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52347',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/55bf7482-5056-4f12-b780-2dd3b1586209.pdf',
        'da': 'Corey Fox, Kathy(CVS Caremark).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52348',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/4343e83a-eeaf-4c48-b29a-85cda8ba46bb.pdf',
        'da': 'Corey Fox, Kathy(DG Whitefield).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52349',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/37766a1c-9fb9-48d5-ad02-420d844119a3.pdf',
        'da': 'Corey Fox, Kathy(Elliot Health System).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(General Motors)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52350',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/0e5987d8-c97c-435d-a7f4-aa94d5d18cd0.pdf',
        'da': 'Corey Fox, Kathy(General Motors).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(Indeck Energy Alexandria)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52351',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/98242bd5-68f1-4b5f-9217-c2b52a6bc212.pdf',
        'da': 'Corey Fox, Kathy(Indeck Energy Alexandria).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(ISO New England)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52352',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/4e63f52c-ddb5-4bb9-8cd1-d4800d5fc354.pdf',
        'da': 'Corey Fox, Kathy(ISO New England).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Dental Society)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52353',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/b4bcc1d1-01e6-4c0c-b259-993c07686de2.pdf',
        'da': 'Corey Fox, Kathy(NH Dental Society).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Manufactured and Modular Housing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52354',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/46a2d1a4-43f7-4165-95e1-11063cf77f5f.pdf',
        'da': 'Corey Fox, Kathy(NH Manufactured and Modular Housing Assoc).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Marine Trades Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52355',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/897863c7-0a7a-407a-a4ae-e9e50bcac68b.pdf',
        'da': 'Corey Fox, Kathy(NH Marine Trades Assoc).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Psyciatric Society)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52356',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/497af3b6-26f5-4699-b490-a31733e89170.pdf',
        'da': 'Corey Fox, Kathy(NH Psyciatric Society).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Snowmobile Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52357',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/393c466d-fc0e-4569-8c50-2a2fedf9480a.pdf',
        'da': 'Corey Fox, Kathy(NH Snowmobile Assoc).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(NH Soft Drink Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52358',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/0157406a-f7ef-4e51-a4bb-82922ff4628b.pdf',
        'da': 'Corey Fox, Kathy(NH Soft Drink Assoc).pdf'
    },
    {
        'dn': 'Corey Fox, Kathy(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52359',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/88cc7bf9-c69f-4139-b36a-7358dd84c1e8.pdf',
        'da': 'Corey Fox, Kathy(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Coronis, Kimberly(Breath NH)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=8589939195',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/b76d8020-7439-4b66-a6f9-beff56af54a9.pdf',
        'da': 'Coronis, Kimberly(Breath NH).pdf'
    },
    {
        'dn': 'Corpora, Ron(Eisai Inc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52360',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/3f083983-295c-4902-a22d-d69985142cc7.pdf',
        'da': 'Corpora, Ron(Eisai Inc).pdf'
    },
    {
        'dn': 'Courchesne, Christophe(Conservation Law Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52361',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/7f7d066b-ac69-4f47-87d5-ea15bbda86e6.pdf',
        'da': 'Courchesne, Christophe(Conservation Law Foundation).pdf'
    },
    {
        'dn': 'Crawford, Bruce(Auto and truck Recyclers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52362',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/8ee9adf1-e5e8-4158-9bd7-e414ef91ef2b.pdf',
        'da': 'Crawford, Bruce(Auto and truck Recyclers Assoc of NH).pdf'
    },
    {
        'dn': 'Currier, Thomas(Purdue Pharma LP)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52363',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/a879971f-2332-476c-9b98-55d4eb592efe.pdf',
        'da': 'Currier, Thomas(Purdue Pharma LP).pdf'
    },
    {
        'dn': 'Cuzzi, David(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52364',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/79a9b15a-146b-45c7-b230-76b6436fbc3d.pdf',
        'da': 'Cuzzi, David(Addendum C).pdf'
    },
    {
        'dn': 'Cuzzi, David(AmSurgNortheast Surgical Center of Newington)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52365',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/16e67f93-440f-4414-9b55-dae8c2af3b2e.pdf',
        'da': 'Cuzzi, David(AmSurgNortheast Surgical Center of Newington).pdf'
    },
    {
        'dn': 'Cuzzi, David(BAE Systems Inc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52366',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/ec2f7f6f-e421-4394-a93c-76f358394023.pdf',
        'da': 'Cuzzi, David(BAE Systems Inc).pdf'
    },
    {
        'dn': 'Cuzzi, David(Juliet Marine Systems)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52367',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/ce5dc522-d2d4-4573-82e2-490166c7f05f.pdf',
        'da': 'Cuzzi, David(Juliet Marine Systems).pdf'
    },
    {
        'dn': 'Cuzzi, David(Velcro USA Inc)',
        'wp': 'http://sos.nh.gov/Lob012914C.aspx?id=52368',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2464/91921eb2-2c30-4cfe-a17e-f807be51025d.pdf',
        'da': 'Cuzzi, David(Velcro USA Inc).pdf'
    },
    {
        'dn': 'Dean, Mark(NH Electric Cooperative Inc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52369',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/84adb6e4-abd6-41a3-8533-0955e9477260.pdf',
        'da': 'Dean, Mark(NH Electric Cooperative Inc).pdf'
    },
    {
        'dn': 'DeJoie, John(NH Kids Count)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589936911',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/0860b107-bb9d-4e99-9976-14965a482bca.pdf',
        'da': 'DeJoie, John(NH Kids Count).pdf'
    },
    {
        'dn': 'DelDeo, Stephen(NH Water Works Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589936910',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/0ff3919a-24cc-4ef2-be91-c0f70933f33a.pdf',
        'da': 'DelDeo, Stephen(NH Water Works Assoc).pdf'
    },
    {
        'dn': 'Demers and Blaisdell(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52370',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/24ac03fc-abf4-4cd8-8d1e-e31dcba1c9e2.pdf',
        'da': 'Demers and Blaisdell(Addendum C).pdf'
    },
    {
        'dn': 'Demers Blaisdell Inc(Totals)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52371',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/d38c9b68-e663-4a45-afb1-e7bd77d46327.pdf',
        'da': 'Demers Blaisdell Inc(Totals).pdf'
    },
    {
        'dn': 'Demers, James(America Votes)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52372',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/f3bdb12b-554a-400e-8882-544501bf6bf7.pdf',
        'da': 'Demers, James(America Votes).pdf'
    },
    {
        'dn': 'Demers, James(Bank of America)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52373',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/e9eae9d3-69f5-41e3-81ef-e38739716d4a.pdf',
        'da': 'Demers, James(Bank of America).pdf'
    },
    {
        'dn': 'Demers, James(Cannery Casino Resorts)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52374',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/f0f77df4-3d96-42fa-99a4-402c794a618c.pdf',
        'da': 'Demers, James(Cannery Casino Resorts).pdf'
    },
    {
        'dn': 'Demers, James(Centene Corp)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52375',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/358cbcef-379c-4a1f-8c04-68e29fad197d.pdf',
        'da': 'Demers, James(Centene Corp).pdf'
    },
    {
        'dn': 'Demers, James(Comcast)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52376',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/92e2a21e-ac22-42d5-a163-9f8bd03c5820.pdf',
        'da': 'Demers, James(Comcast).pdf'
    },
    {
        'dn': 'Demers, James(Consumer Safety Technology)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52377',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8ddaacfd-e688-48d0-9449-134d8a0cd180.pdf',
        'da': 'Demers, James(Consumer Safety Technology).pdf'
    },
    {
        'dn': 'Demers, James(FedEx)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52378',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/aa5439b8-ac3c-4bc3-867b-8a9d94990e5f.pdf',
        'da': 'Demers, James(FedEx).pdf'
    },
    {
        'dn': 'Demers, James(Heritage Plumbing Heating Inc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52379',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/0d7c561b-0da1-4be2-94fa-a9a0552545e7.pdf',
        'da': 'Demers, James(Heritage Plumbing Heating Inc).pdf'
    },
    {
        'dn': 'Demers, James(IBM Corp)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52380',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/c246edca-84f4-4ac8-8f4a-434e219f648f.pdf',
        'da': 'Demers, James(IBM Corp).pdf'
    },
    {
        'dn': 'Demers, James(IGT)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52381',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8dfb08bb-ff9d-45ca-be8d-7f029b3d517a.pdf',
        'da': 'Demers, James(IGT).pdf'
    },
    {
        'dn': 'Demers, James(International Bottled Water Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52382',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/7d3a31a9-d807-490c-a280-e2d23d6a77a4.pdf',
        'da': 'Demers, James(International Bottled Water Assoc).pdf'
    },
    {
        'dn': 'Demers, James(Mortgage Bankers and Brokers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52383',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/dcbfd1a7-fb4d-4505-8ff9-ff74d6e247e7.pdf',
        'da': 'Demers, James(Mortgage Bankers and Brokers Assoc of NH).pdf'
    },
    {
        'dn': 'Demers, James(NH Athletic Trainers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52384',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/9a618e1c-2629-45b5-a0d2-39604b395f32.pdf',
        'da': 'Demers, James(NH Athletic Trainers Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Automobile Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52385',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/1196f5a8-ebed-4739-bec8-4a7eef4f2b87.pdf',
        'da': 'Demers, James(NH Automobile Dealers Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Coalition for Prosthetics)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52386',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/69b17c5d-9fb6-45d0-80db-a34f1b94028f.pdf',
        'da': 'Demers, James(NH Coalition for Prosthetics).pdf'
    },
    {
        'dn': 'Demers, James(NH Driver Education Teachers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52387',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/705893bc-2339-4e6e-a80f-038fe1520ac9.pdf',
        'da': 'Demers, James(NH Driver Education Teachers Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Genetic Counselors)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52388',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/349d9a83-a5ae-42b8-b230-8841ddf84566.pdf',
        'da': 'Demers, James(NH Genetic Counselors).pdf'
    },
    {
        'dn': 'Demers, James(NH Police Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52389',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/2e16cdc4-88f4-463c-9c0d-5b92cbe6176c.pdf',
        'da': 'Demers, James(NH Police Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Psychological Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52390',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/5453443a-2a11-4e84-bb40-40d32ac76d3d.pdf',
        'da': 'Demers, James(NH Psychological Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Speech Language and Hearing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52391',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/c96d7bb2-bc05-4054-bc6d-12f9a8d21f1f.pdf',
        'da': 'Demers, James(NH Speech Language and Hearing Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Troopers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52392',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/c7902214-16bd-49d0-b460-9cbba3c8ef44.pdf',
        'da': 'Demers, James(NH Troopers Assoc).pdf'
    },
    {
        'dn': 'Demers, James(NH Wine and Spirits Brokers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52393',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/501f7454-ce05-4830-a77c-7099f9771bc0.pdf',
        'da': 'Demers, James(NH Wine and Spirits Brokers Assoc).pdf'
    },
    {
        'dn': 'Demers, James(North Country Environmental Services)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52394',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/2c039f4d-5878-46c4-80dd-58850bf8243c.pdf',
        'da': 'Demers, James(North Country Environmental Services).pdf'
    },
    {
        'dn': 'Demers, James(Optimum Technology)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52395',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/cb2c099b-2690-4440-9de6-160b48cb75e7.pdf',
        'da': 'Demers, James(Optimum Technology).pdf'
    },
    {
        'dn': 'Demers, James(Pfizer)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52396',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/d8c58322-8494-4ce2-b925-b747e2172637.pdf',
        'da': 'Demers, James(Pfizer).pdf'
    },
    {
        'dn': 'Demers, James(PhRMA)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52397',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/13462f3d-d7d1-4780-a79b-87b21501ec07.pdf',
        'da': 'Demers, James(PhRMA).pdf'
    },
    {
        'dn': 'Demers, James(Pilot Health LLC)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52398',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/275023c8-733e-44b6-be3e-5f8d77040b4b.pdf',
        'da': 'Demers, James(Pilot Health LLC).pdf'
    },
    {
        'dn': 'Demers, James(PSNH)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52399',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/7f0ce80c-df91-40f4-aa02-2f461bdd0add.pdf',
        'da': 'Demers, James(PSNH).pdf'
    },
    {
        'dn': 'Demers, James(RAI Services Company)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52400',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/07edeaff-8cdf-4c3d-9fee-30946e5baf58.pdf',
        'da': 'Demers, James(RAI Services Company).pdf'
    },
    {
        'dn': 'Dennehy and Bouley(Totals)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52401',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/4d8043be-7ca4-49d8-8757-4d2b1fa1a0be.pdf',
        'da': 'Dennehy and Bouley(Totals).pdf'
    },
    {
        'dn': 'Dennehy, Michael(Concord Hospital)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52402',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/d9b03675-d343-41ec-bea3-f7ac452d4a8a.pdf',
        'da': 'Dennehy, Michael(Concord Hospital).pdf'
    },
    {
        'dn': 'Dennehy, Michael(DLA Piper)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52403',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/60f1c084-3626-4a74-9f85-715fcbf98a6c.pdf',
        'da': 'Dennehy, Michael(DLA Piper).pdf'
    },
    {
        'dn': 'Dennehy,Michael(RESA)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52404',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/86e024a9-3c54-4424-aa80-bf93d7a7fde5.pdf',
        'da': 'Dennehy,Michael(RESA).pdf'
    },
    {
        'dn': 'Dietel, Robert(Hom Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52405',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/f1d7ae27-f6ee-42db-a59b-558733902b83.pdf',
        'da': 'Dietel, Robert(Hom Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Dolan, Dan(N E Power Generators Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52406',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/d37a63a2-6fb6-4629-9bce-7f854d39e704.pdf',
        'da': 'Dolan, Dan(N E Power Generators Assoc).pdf'
    },
    {
        'dn': 'Doyle, Chris(Allergan Inc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52407',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/712e3d9a-9e3e-4522-8137-f48b23532ac4.pdf',
        'da': 'Doyle, Chris(Allergan Inc).pdf'
    },
    {
        'dn': 'Dunn, Robert etal(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52408',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/dc8edc18-c13d-4f3e-9aab-2c14d2081dc7.pdf',
        'da': 'Dunn, Robert etal(Addendum C).pdf'
    },
    {
        'dn': 'Dunn, Robert(AAA Northern New England)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52409',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/5935fc1f-052f-4244-8f8d-7145fa160a02.pdf',
        'da': 'Dunn, Robert(AAA Northern New England).pdf'
    },
    {
        'dn': 'Dunn, Robert(Brain Injury Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52410',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/c726ed90-1094-452b-90e0-59b037fcb704.pdf',
        'da': 'Dunn, Robert(Brain Injury Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(Catholic Medical Center)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52411',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/22d279e8-7f4c-44e2-8e64-fcba5a66565c.pdf',
        'da': 'Dunn, Robert(Catholic Medical Center).pdf'
    },
    {
        'dn': 'Dunn, Robert(Fairpoint Communications)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52412',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/adfc8eff-9146-47c0-a1c0-6e0aafdb3354.pdf',
        'da': 'Dunn, Robert(Fairpoint Communications).pdf'
    },
    {
        'dn': 'Dunn, Robert(Greater Nashua Chamber of Commerce)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52413',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/1c9bba47-1a4c-4332-8634-7eaf00e0bb9b.pdf',
        'da': 'Dunn, Robert(Greater Nashua Chamber of Commerce).pdf'
    },
    {
        'dn': 'Dunn, Robert(Gs1 Global Public Policy)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52414',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/df96b3bf-7b8b-4091-8685-81f858203887.pdf',
        'da': 'Dunn, Robert(Gs1 Global Public Policy).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Assoc of Naturopathic Doctors)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52415',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/00aaec5b-36af-4eeb-87de-cb1643521dcf.pdf',
        'da': 'Dunn, Robert(NH Assoc of Naturopathic Doctors).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Assoc of Residential Care Homes)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52416',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/f35a04e5-b359-438d-bbbf-80f61c926c00.pdf',
        'da': 'Dunn, Robert(NH Assoc of Residential Care Homes).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Catholic Charities)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52417',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/72f71503-382e-4a5b-b7a8-35ae4aa910d1.pdf',
        'da': 'Dunn, Robert(NH Catholic Charities).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Electric Cooperative)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52418',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/b4268315-bc67-433e-be70-6f272c8ae57d.pdf',
        'da': 'Dunn, Robert(NH Electric Cooperative).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Health Care Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52419',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/609d09e7-1082-482c-9eff-83ea1ccc82f9.pdf',
        'da': 'Dunn, Robert(NH Health Care Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Library Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52420',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/9ba9b0c0-c153-4093-964c-9e250f139af8.pdf',
        'da': 'Dunn, Robert(NH Library Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Nurse Practitioners Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52421',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/26e47a45-7316-437b-ac2f-12eb5332361e.pdf',
        'da': 'Dunn, Robert(NH Nurse Practitioners Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Nurses Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52422',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8a6387d6-fc69-4c2f-a3df-4c3e7781fb57.pdf',
        'da': 'Dunn, Robert(NH Nurses Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Public Risk Mgmt Primex3)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52423',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8e1d81ad-4f6a-4124-9554-583e445501ba.pdf',
        'da': 'Dunn, Robert(NH Public Risk Mgmt Primex3).pdf'
    },
    {
        'dn': 'Dunn, Robert(NH Telephone Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52424',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/ec011a28-6240-4991-839a-54eea235aec6.pdf',
        'da': 'Dunn, Robert(NH Telephone Assoc).pdf'
    },
    {
        'dn': 'Dunn, Robert(Roman Catholic Bishop of Manchester)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52425',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/72fef245-9dbd-42d7-a576-0b0529e77dc1.pdf',
        'da': 'Dunn, Robert(Roman Catholic Bishop of Manchester).pdf'
    },
    {
        'dn': 'Dunn, Robert(US Cellular)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=52426',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/9b4bda14-bcb7-457e-b1c7-d726345a7e42.pdf',
        'da': 'Dunn, Robert(US Cellular).pdf'
    },
    {
        'dn': 'Dupont, Edward(Alliance of Automobile Manufacturers)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939198',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/37f9c21f-f7bb-491e-82eb-7a4a10c43fcd.pdf',
        'da': 'Dupont, Edward(Alliance of Automobile Manufacturers).pdf'
    },
    {
        'dn': 'Dupont, Edward(C J Trailways)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939199',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/66b20e19-800c-4938-b340-0535cc03462f.pdf',
        'da': 'Dupont, Edward(C J Trailways).pdf'
    },
    {
        'dn': 'Dupont, Edward(Deloitte Consulting)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939205',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/e4198a71-354a-42b4-98c0-17bd00fa15bc.pdf',
        'da': 'Dupont, Edward(Deloitte Consulting).pdf'
    },
    {
        'dn': 'Dupont, Edward(Eastern Propane)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939206',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/daa5c943-55d0-4297-850e-455eddad43e4.pdf',
        'da': 'Dupont, Edward(Eastern Propane).pdf'
    },
    {
        'dn': 'Dupont, Edward(Gordon Darby)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939200',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/494e0f21-263d-4bec-816d-9dfc9b94ea36.pdf',
        'da': 'Dupont, Edward(Gordon Darby).pdf'
    },
    {
        'dn': 'Dupont, Edward(Harvard Pilgrim Health Care)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939201',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/c7f250b2-7d5a-4e35-8cb9-26a91cfb093c.pdf',
        'da': 'Dupont, Edward(Harvard Pilgrim Health Care).pdf'
    },
    {
        'dn': 'Dupont, Edward(HP Enterprise Services)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939207',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/646d7f17-a9e7-437c-860e-1a3492bfb081.pdf',
        'da': 'Dupont, Edward(HP Enterprise Services).pdf'
    },
    {
        'dn': 'Dupont, Edward(MHM Services)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939202',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8c14518e-124b-42f8-a6ff-5da48c2c8c7b.pdf',
        'da': 'Dupont, Edward(MHM Services).pdf'
    },
    {
        'dn': 'Dupont, Edward(Microsoft Corp)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939203',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/d0ec3a0d-189e-4405-a46f-2d722c93482b.pdf',
        'da': 'Dupont, Edward(Microsoft Corp).pdf'
    },
    {
        'dn': 'Dupont, Edward(NH Motor Speedway)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939209',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8db66037-e93b-49e5-8f29-3afe757ca71c.pdf',
        'da': 'Dupont, Edward(NH Motor Speedway).pdf'
    },
    {
        'dn': 'Dupont, Edward(North American Power and Gas)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939208',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/7e24a865-5462-4ddc-9ecc-0e8e3cab165d.pdf',
        'da': 'Dupont, Edward(North American Power and Gas).pdf'
    },
    {
        'dn': 'Dupont, Edward(Propane Gas Assoc of NE)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939204',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/8b3d5d21-91b2-421a-94c1-d747acd7a670.pdf',
        'da': 'Dupont, Edward(Propane Gas Assoc of NE).pdf'
    },
    {
        'dn': 'Dupont, Edward(Scientific Games)',
        'wp': 'http://sos.nh.gov/Lob012914D.aspx?id=8589939210',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2465/ae249957-e82c-4b4a-8201-60a5c8b43bad.pdf',
        'da': 'Dupont, Edward(Scientific Games).pdf'
    },
    {
        'dn': 'Ehrenberg, Kurt(NH AFL CIO)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52427',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/01458ec2-e3ed-48b2-a1ac-01150049c933.pdf',
        'da': 'Ehrenberg, Kurt(NH AFL CIO).pdf'
    },
    {
        'dn': 'Epler, Gary(Unitil Corp)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52428',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/f7983422-ba8e-44f5-a0c4-e327705deb6e.pdf',
        'da': 'Epler, Gary(Unitil Corp).pdf'
    },
    {
        'dn': 'Fahey, Thomas(NH Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52429',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/de341fdb-f311-4554-95e0-a9ab1f6c4a92.pdf',
        'da': 'Fahey, Thomas(NH Bankers Assoc).pdf'
    },
    {
        'dn': 'Feltes, Daniel(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=8589936913',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/c3a1a956-a207-479c-8706-2a725d2f1fdb.pdf',
        'da': 'Feltes, Daniel(Addendum C).pdf'
    },
    {
        'dn': 'Feltes, Daniel(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=8589936914',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/087b3414-3a51-47e3-ac5e-1a4fdda30d4b.pdf',
        'da': 'Feltes, Daniel(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'Feltes, Daniel(The Way Home)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=8589936912',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/1c4ea7cd-403a-457f-95d9-3a72ca1ae1da.pdf',
        'da': 'Feltes, Daniel(The Way Home).pdf'
    },
    {
        'dn': 'Fisher, Martin(Distilled Spirits Council of the US)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52430',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/7b74e103-1096-454f-9f7a-ca159cc03ba2.pdf',
        'da': 'Fisher, Martin(Distilled Spirits Council of the US).pdf'
    },
    {
        'dn': 'Fogarty, Margaret(American Friends Serv Comm)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52431',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/fbb64101-0add-46a5-bcf0-fc05cc5bd3ac.pdf',
        'da': 'Fogarty, Margaret(American Friends Serv Comm).pdf'
    },
    {
        'dn': 'Foote, Deborah(American Society for the Prevention of Cruelty to Animals)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52432',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/b9385bf3-cca9-4857-958e-2f0256372f9e.pdf',
        'da': 'Foote, Deborah(American Society for the Prevention of Cruelty to Animals).pdf'
    },
    {
        'dn': 'Fortier, Tim(NH Municipal Association)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52433',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/b87f2e99-594c-4a44-b661-ff357934829c.pdf',
        'da': 'Fortier, Tim(NH Municipal Association).pdf'
    },
    {
        'dn': 'Foss, Carol(Audubon Society of NH)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52434',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/8abd7eff-f917-4606-9233-2be1de51905f.pdf',
        'da': 'Foss, Carol(Audubon Society of NH).pdf'
    },
    {
        'dn': 'Fournier, Deborah(NH Fiscal Policy Institute)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52435',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/ec55b9bc-8dc7-4746-bcb3-ee6c0aa4dabd.pdf',
        'da': 'Fournier, Deborah(NH Fiscal Policy Institute).pdf'
    },
    {
        'dn': 'Funk, W John(New Hampshire Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52436',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/fe9a5841-788b-4fde-92ce-7f15a48edb55.pdf',
        'da': 'Funk, W John(New Hampshire Bankers Assoc).pdf'
    },
    {
        'dn': 'Gallagher, Callahan Gartrell(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52437',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/9f96259b-085b-4b33-8b7f-78deb2a0e0dd.pdf',
        'da': 'Gallagher, Callahan Gartrell(Addendum C).pdf'
    },
    {
        'dn': 'Gallo, Geoffrey(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52438',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/79fd5ad3-4fe9-486b-a11b-d53611895360.pdf',
        'da': 'Gallo, Geoffrey(Addendum C).pdf'
    },
    {
        'dn': 'Gallo, Geoffrey(AstraZeneca Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52439',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/109926fe-fc76-48b8-989d-fbec862510a8.pdf',
        'da': 'Gallo, Geoffrey(AstraZeneca Pharmaceuticals).pdf'
    },
    {
        'dn': 'Gamache, Donna(Public Serv of NH)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52440',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/61145c87-19b1-40f4-bcda-90808fe5c64b.pdf',
        'da': 'Gamache, Donna(Public Serv of NH).pdf'
    },
    {
        'dn': 'Gehshan, Shelly(Pew Charitable Trust)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52441',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/c625586c-a6c8-417f-8266-138679c5ee99.pdf',
        'da': 'Gehshan, Shelly(Pew Charitable Trust).pdf'
    },
    {
        'dn': 'Geiger, Susan(Comcast)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52442',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/482ae04a-7355-440e-b68d-2cc676e51adf.pdf',
        'da': 'Geiger, Susan(Comcast).pdf'
    },
    {
        'dn': 'Geiger, Susan(EDP Renewable North America)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52443',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/869141f8-0327-4351-82d5-ee1294b1d25b.pdf',
        'da': 'Geiger, Susan(EDP Renewable North America).pdf'
    },
    {
        'dn': 'Geiger, Susan(Hat Trick Logistics)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52444',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/8eeac52f-025e-4c05-9ac8-0f2b8ce54570.pdf',
        'da': 'Geiger, Susan(Hat Trick Logistics).pdf'
    },
    {
        'dn': 'Geiger, Susan(Technology Exclusive Inc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52445',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/a91ff0c9-6b38-4962-8de9-32ff0170bb12.pdf',
        'da': 'Geiger, Susan(Technology Exclusive Inc).pdf'
    },
    {
        'dn': 'Getz, Thomas(Wheelabrator Technologies Inc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52446',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/84f3b32c-39a3-4538-892b-31a36432b0de.pdf',
        'da': 'Getz, Thomas(Wheelabrator Technologies Inc).pdf'
    },
    {
        'dn': 'Goldwasser, Rachel(EDP Renewable North America)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52447',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/5530cf80-0aab-4ba1-acdc-0eb5680d2714.pdf',
        'da': 'Goldwasser, Rachel(EDP Renewable North America).pdf'
    },
    {
        'dn': 'Goldwasser, Rachel(Electricity NH dba ENH Power)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52448',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/ee3e0d2e-11b7-491b-8b11-f8cce648c940.pdf',
        'da': 'Goldwasser, Rachel(Electricity NH dba ENH Power).pdf'
    },
    {
        'dn': 'Goldwasser, Rachel(Riverstone Resources)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52449',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/c1bf7e1f-f262-4488-b9a6-db090787b5a4.pdf',
        'da': 'Goldwasser, Rachel(Riverstone Resources).pdf'
    },
    {
        'dn': 'Goldwasser, Rachel(TransCanada Hydro Northeast Inc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52450',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/c57119d5-3ba0-40df-8883-9bf976c2e85f.pdf',
        'da': 'Goldwasser, Rachel(TransCanada Hydro Northeast Inc).pdf'
    },
    {
        'dn': 'Gould, Bryan(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52451',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/199c8772-db2d-4468-a47a-9340156d3060.pdf',
        'da': 'Gould, Bryan(Addendum C).pdf'
    },
    {
        'dn': 'Gould, Bryan(Casella Waste Systems)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52452',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/c50e9590-d1bb-4fba-9e2f-8b23d45ae1e9.pdf',
        'da': 'Gould, Bryan(Casella Waste Systems).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52453',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/e88ae4b7-2ceb-4ce2-ae44-e6a088b4f34f.pdf',
        'da': 'Grimbilas, Jodi(Addendum C).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(American Cancer Society Cancer Action Network)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52454',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/22ab96f1-bffc-4c45-9995-b10dc373859b.pdf',
        'da': 'Grimbilas, Jodi(American Cancer Society Cancer Action Network).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(American Society for the Prevention of Cruelty to Animals)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52455',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/8e2335fa-7bcc-4528-b2de-0c64183b26ae.pdf',
        'da': 'Grimbilas, Jodi(American Society for the Prevention of Cruelty to Animals).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Bridgewater Power Co)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52456',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/8f92fa0f-dac2-489b-bc3a-eefd9d15ec39.pdf',
        'da': 'Grimbilas, Jodi(Bridgewater Power Co).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Cisco Systems)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52457',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/ab344a83-0443-423d-9448-41d050934054.pdf',
        'da': 'Grimbilas, Jodi(Cisco Systems).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Coalition of Insurance and Financial Producers)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52458',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/bf6ab29a-3717-4ade-9e19-9d1e60c4b2f6.pdf',
        'da': 'Grimbilas, Jodi(Coalition of Insurance and Financial Producers).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(CVS Caremark)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52459',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/2cb7a24c-2077-48f3-a9ba-06b0d40cc1c3.pdf',
        'da': 'Grimbilas, Jodi(CVS Caremark).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52460',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/d3d933ab-2659-40ce-9c67-e14811107759.pdf',
        'da': 'Grimbilas, Jodi(DG Whitefield).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52461',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/5cadb922-4954-4316-8a12-7e8824660828.pdf',
        'da': 'Grimbilas, Jodi(Elliot Health System).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Focus Technology Solutions)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52462',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/593750ca-61e8-4b24-b0bc-0c9d13826b5a.pdf',
        'da': 'Grimbilas, Jodi(Focus Technology Solutions).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(General Motors)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52463',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/f295c4c0-2f74-44a8-a0f3-39fa97d4a370.pdf',
        'da': 'Grimbilas, Jodi(General Motors).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Indeck Energy Alexandria)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52464',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/f1958dd5-e1df-448b-accf-b7da74d0f65e.pdf',
        'da': 'Grimbilas, Jodi(Indeck Energy Alexandria).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Independent Oil Marketers Assoc of N E)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52465',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/6cfed19f-de8e-4989-a036-635e3e396a62.pdf',
        'da': 'Grimbilas, Jodi(Independent Oil Marketers Assoc of N E).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(ISO New England)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52466',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/641f9d47-d43c-4e5e-8bf7-f08423192b77.pdf',
        'da': 'Grimbilas, Jodi(ISO New England).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Lockridge Grindal Nauen)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52467',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/61f51214-0975-4e22-a5c2-8d98b54b07a3.pdf',
        'da': 'Grimbilas, Jodi(Lockridge Grindal Nauen).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Assoc of School Principals)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52468',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/441a3415-0cd6-4fd6-aaf0-437080b4423a.pdf',
        'da': 'Grimbilas, Jodi(NH Assoc of School Principals).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Association of Realtors)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52469',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/42385fc0-96f2-4bd5-a5c5-6d2427c56a04.pdf',
        'da': 'Grimbilas, Jodi(NH Association of Realtors).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Dental Society)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52470',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/e98005e3-75ff-42e2-a9d3-90c90dbc6e4b.pdf',
        'da': 'Grimbilas, Jodi(NH Dental Society).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Manufactured and Modular Housing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52471',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/d76bc17f-c099-420f-a5f3-2988c96686ac.pdf',
        'da': 'Grimbilas, Jodi(NH Manufactured and Modular Housing Assoc).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Marine Trades Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52472',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/4e2ce419-91b7-414a-b57a-b0facdd93fb2.pdf',
        'da': 'Grimbilas, Jodi(NH Marine Trades Assoc).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Psychiatric Society)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52473',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/24fd1ad3-4fff-4a01-8986-97357ca33f4b.pdf',
        'da': 'Grimbilas, Jodi(NH Psychiatric Society).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Snowmobile Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52474',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/187b87c5-59f1-4ab4-9aee-6a65fce74de5.pdf',
        'da': 'Grimbilas, Jodi(NH Snowmobile Assoc).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(NH Soft Drink Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52475',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/49d5f231-bdd8-471b-b1b0-c505896bb38b.pdf',
        'da': 'Grimbilas, Jodi(NH Soft Drink Assoc).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52476',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/8c2499d0-f9e7-440f-b026-c6ca77b29e1f.pdf',
        'da': 'Grimbilas, Jodi(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52477',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/2a18930b-8b50-4463-8a25-56a0e093c674.pdf',
        'da': 'Grimbilas, Jodi(Springfield Power).pdf'
    },
    {
        'dn': 'Grimbilas, Jodi(XTL)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52478',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/eff66522-e305-4ef3-876e-af3aafdbc83a.pdf',
        'da': 'Grimbilas, Jodi(XTL).pdf'
    },
    {
        'dn': 'Grip, Brian(Bank of America Corp)',
        'wp': 'http://sos.nh.gov/Lob012914EG.aspx?id=52479',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2466/81116d85-1f0d-4548-b4bc-d31f3e84a965.pdf',
        'da': 'Grip, Brian(Bank of America Corp).pdf'
    },
    {
        'dn': 'Habbe, Stephen(American Diabetes Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52480',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/a89d32a0-1a2e-40b4-9d6a-1e35244dc715.pdf',
        'da': 'Habbe, Stephen(American Diabetes Assoc).pdf'
    },
    {
        'dn': 'Hale, Debra(Liberty Utilities Energy North Natural Gas)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=8589936915',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/93e305b3-d0f7-4082-9726-2a9ac985eb93.pdf',
        'da': 'Hale, Debra(Liberty Utilities Energy North Natural Gas).pdf'
    },
    {
        'dn': 'Hale, Ryan(NH Automobile Dealers Insurance Co)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52481',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/972f8141-ce37-472e-9c7d-2ec25c6b09cd.pdf',
        'da': 'Hale, Ryan(NH Automobile Dealers Insurance Co).pdf'
    },
    {
        'dn': 'Haley, Pierce(Distilled Spirits Council of the US)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52482',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/2da84f1a-568d-42f2-abef-235cc995b3ea.pdf',
        'da': 'Haley, Pierce(Distilled Spirits Council of the US).pdf'
    },
    {
        'dn': 'Halloran, Jean(Consumer Union of US Inc Consumer Reports)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52483',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/64bdf01b-1e14-43d9-ab6b-db9498a569dc.pdf',
        'da': 'Halloran, Jean(Consumer Union of US Inc Consumer Reports).pdf'
    },
    {
        'dn': 'Hansen, Michael(Consumer Union of US Inc Consumer Reports)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52484',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/a07cb52c-3444-452d-9fdf-1122f2410aae.pdf',
        'da': 'Hansen, Michael(Consumer Union of US Inc Consumer Reports).pdf'
    },
    {
        'dn': 'Harris, Rebecca(Transport NH)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52485',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/f9ad78af-d016-492b-bbb9-524eea89595b.pdf',
        'da': 'Harris, Rebecca(Transport NH).pdf'
    },
    {
        'dn': 'Hass, Erin(PEW)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52486',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/a1375e9c-2495-42d1-9289-83d55c8fab10.pdf',
        'da': 'Hass, Erin(PEW).pdf'
    },
    {
        'dn': 'Hatem, James(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52487',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/11354bcf-e2e0-45c8-b810-2d9487f150e1.pdf',
        'da': 'Hatem, James(Addendum C).pdf'
    },
    {
        'dn': 'Hatem, James(Asurion)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52488',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/f58a4176-6af0-49bd-ad64-cc65c3df6171.pdf',
        'da': 'Hatem, James(Asurion).pdf'
    },
    {
        'dn': 'Hatem, James(NH Water Well Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52489',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/e4f40800-c6f4-4ad3-bcb5-52c1d92b77d5.pdf',
        'da': 'Hatem, James(NH Water Well Assoc).pdf'
    },
    {
        'dn': 'Hatem, James(State Farm Insurance Co)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52490',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/94c0b964-709b-46ae-a841-8a9d52e55ec3.pdf',
        'da': 'Hatem, James(State Farm Insurance Co).pdf'
    },
    {
        'dn': 'Hawkins, Brian(SEA SEIU Local 1984)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52491',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/75607af1-321f-4f8e-ad26-801290fdc25c.pdf',
        'da': 'Hawkins, Brian(SEA SEIU Local 1984).pdf'
    },
    {
        'dn': 'Hennequin, Sandi(N E Power Generators Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52492',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/4e6a9792-361e-4344-aa7b-b57ea152d56b.pdf',
        'da': 'Hennequin, Sandi(N E Power Generators Assoc).pdf'
    },
    {
        'dn': 'Hodgdon, Christopher(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52493',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/18d2bd3f-7f7c-463e-aa33-265fce53e64d.pdf',
        'da': 'Hodgdon, Christopher(Addendum C).pdf'
    },
    {
        'dn': 'Hodgdon, Christopher(Comcast NBCUniviersal)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52494',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/2d251dc7-2450-47ae-aad3-b24997bca1bc.pdf',
        'da': 'Hodgdon, Christopher(Comcast NBCUniviersal).pdf'
    },
    {
        'dn': 'Hohenwarter, John(Ntl Rifle Association of America)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52495',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/01080f09-5ed5-41b8-8ea8-86b942b4c683.pdf',
        'da': 'Hohenwarter, John(Ntl Rifle Association of America).pdf'
    },
    {
        'dn': 'Holahan, Carol(Securas Technologies Inc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52496',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/bfe89868-d08a-4c78-ba18-975b78c44f4f.pdf',
        'da': 'Holahan, Carol(Securas Technologies Inc).pdf'
    },
    {
        'dn': 'Honigberg, Martin(Hertz Corp)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52497',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/73d78b0e-103c-4e28-a54b-a1ee3ce5b25b.pdf',
        'da': 'Honigberg, Martin(Hertz Corp).pdf'
    },
    {
        'dn': 'Honigberg, Martin(NH Medical Society)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52498',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/f5c81527-c769-4e65-9b87-b0f4998a1b95.pdf',
        'da': 'Honigberg, Martin(NH Medical Society).pdf'
    },
    {
        'dn': 'Honigberg, Martin(Northeast Rehabilitation Hospital)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52499',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/ce7ddc16-9b04-4333-b0d7-191c2f8a4b27.pdf',
        'da': 'Honigberg, Martin(Northeast Rehabilitation Hospital).pdf'
    },
    {
        'dn': 'Houde, Matthew(Dartmouth Hitchcock)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52500',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/6ed47624-196c-4b9e-83a7-3abe018a9ed9.pdf',
        'da': 'Houde, Matthew(Dartmouth Hitchcock).pdf'
    },
    {
        'dn': 'Hounsell, William(Granite State Rural Water Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52501',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/9e3a6a92-3363-454b-97b2-98353bae15c6.pdf',
        'da': 'Hounsell, William(Granite State Rural Water Assoc).pdf'
    },
    {
        'dn': 'Hounsell, William(Lower Bartlett Water Precinct)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52502',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/527525b8-b390-4681-9908-589ef687db72.pdf',
        'da': 'Hounsell, William(Lower Bartlett Water Precinct).pdf'
    },
    {
        'dn': 'Hounsell, William(North Conway Water Precinct)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52503',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/a97a9aad-e78b-4e54-b870-d46d1a4a4e76.pdf',
        'da': 'Hounsell, William(North Conway Water Precinct).pdf'
    },
    {
        'dn': 'Howe, Lisa Kaplan(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=8589936916',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/f160ccbb-e933-4f78-8a01-e3e5ff3b37b4.pdf',
        'da': 'Howe, Lisa Kaplan(Addendum C).pdf'
    },
    {
        'dn': 'Howe, Lisa Kaplan(NH Voice for Health)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=8589936917',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/e09d14ba-6fd7-47cb-90b7-e410a2865489.pdf',
        'da': 'Howe, Lisa Kaplan(NH Voice for Health).pdf'
    },
    {
        'dn': 'Irwin, Thomas(Conservation Law Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52504',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/df9a3c3a-2f3c-4b2d-a9cf-c8d23f7a0549.pdf',
        'da': 'Irwin, Thomas(Conservation Law Foundation).pdf'
    },
    {
        'dn': 'Iserman, Katrina(Sunovion Pharmaceuticals Inc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52505',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/7f1aa40c-57e7-41d9-be9c-6aaab23fdae0.pdf',
        'da': 'Iserman, Katrina(Sunovion Pharmaceuticals Inc).pdf'
    },
    {
        'dn': 'Jencks, Kary(NH Citizens Alliance)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52506',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/b342ea7e-8b9e-4ea5-af82-6376f8814ba1.pdf',
        'da': 'Jencks, Kary(NH Citizens Alliance).pdf'
    },
    {
        'dn': 'Johnson, Nancy(American Lung Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52507',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/7de468b4-628e-45bb-bbcb-16f0dd42353c.pdf',
        'da': 'Johnson, Nancy(American Lung Assoc of NH).pdf'
    },
    {
        'dn': 'Johnson, Nancy(Grey 2K USA)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52508',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/800078e3-54eb-44be-9de5-72121bdcb924.pdf',
        'da': 'Johnson, Nancy(Grey 2K USA).pdf'
    },
    {
        'dn': 'Johnson, Nancy(Hampton Chamber of Commerce)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52509',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/f96f31aa-92d8-47b8-9414-5d7dc1685ff4.pdf',
        'da': 'Johnson, Nancy(Hampton Chamber of Commerce).pdf'
    },
    {
        'dn': 'Johnson, Nancy(Humane Society of the US)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52510',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/eff4f087-df75-4dac-ba28-dbd280fc9261.pdf',
        'da': 'Johnson, Nancy(Humane Society of the US).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NH Assoc of Assessing Officers)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52511',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/31a1b767-cd78-4f95-a622-81097b86e3ea.pdf',
        'da': 'Johnson, Nancy(NH Assoc of Assessing Officers).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NH Assoc of Regional Planning Comm)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52512',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/01284b0a-410d-4206-997c-d74b97e492fd.pdf',
        'da': 'Johnson, Nancy(NH Assoc of Regional Planning Comm).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NH City and Town Clerks Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52513',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/5bdc4b79-b73f-456e-958a-1f327ca8cb4c.pdf',
        'da': 'Johnson, Nancy(NH City and Town Clerks Assoc).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NH Planners Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52514',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/0e8cbfd1-bb0c-49d7-a280-a460e30bbcb9.pdf',
        'da': 'Johnson, Nancy(NH Planners Assoc).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NH Podiatric Medical Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52515',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/faa6b5cc-9210-4a1c-9b80-c8af10aba7ab.pdf',
        'da': 'Johnson, Nancy(NH Podiatric Medical Assoc).pdf'
    },
    {
        'dn': 'Johnson, Nancy(NHCAT)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52516',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/6a165ae1-5829-4743-a9a3-76b76f2accf8.pdf',
        'da': 'Johnson, Nancy(NHCAT).pdf'
    },
    {
        'dn': 'Johnson, Nancy(Portsmouth Chamber of Commerce)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52517',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/e153e02d-a8dd-42ef-afe4-e8f84e5d2290.pdf',
        'da': 'Johnson, Nancy(Portsmouth Chamber of Commerce).pdf'
    },
    {
        'dn': 'Johnson, Nancy(Somersworth Chamber of Commerce)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52518',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/d87536b0-74fe-4873-8b11-f90ef41aff58.pdf',
        'da': 'Johnson, Nancy(Somersworth Chamber of Commerce).pdf'
    },
    {
        'dn': 'Johnston, Cordell(NH Municipal Association)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52519',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/384898d9-9ffa-4b34-860a-457c7ee80512.pdf',
        'da': 'Johnston, Cordell(NH Municipal Association).pdf'
    },
    {
        'dn': 'Joyce, Mark(NH School Administrators Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52520',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/1f85a3c8-5c7b-4c90-a663-a23c5015e883.pdf',
        'da': 'Joyce, Mark(NH School Administrators Assoc).pdf'
    },
    {
        'dn': 'Kelly, Karen(NH Citizens Alliance)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52521',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/755b579f-3ce7-4ef6-9a90-c1b097c51907.pdf',
        'da': 'Kelly, Karen(NH Citizens Alliance).pdf'
    },
    {
        'dn': 'Kokoszyna, James(Allergan Inc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52522',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/556cc23b-ee7d-4466-9669-a8f6e9a22452.pdf',
        'da': 'Kokoszyna, James(Allergan Inc).pdf'
    },
    {
        'dn': 'Kolb, Ellen G.(Cornerstone Action)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52523',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/c21fd291-e121-4930-b708-29d588c5d657.pdf',
        'da': 'Kolb, Ellen G.(Cornerstone Action).pdf'
    },
    {
        'dn': 'Koutroubas, Alex(ACEC)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52524',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/459d49ad-e432-4d94-b0cf-6b0386a28a7a.pdf',
        'da': 'Koutroubas, Alex(ACEC).pdf'
    },
    {
        'dn': 'Koutroubas, Alex(CADSV)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52525',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/25137dda-b4da-4d5f-8cf2-a5f00016cc34.pdf',
        'da': 'Koutroubas, Alex(CADSV).pdf'
    },
    {
        'dn': 'Koutroubas, Alex(CSNI)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52526',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/35b5d9aa-82df-4737-b359-229856a82176.pdf',
        'da': 'Koutroubas, Alex(CSNI).pdf'
    },
    {
        'dn': 'Koutroubas, Alex(HID Global)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52527',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/877789aa-e26b-4c40-bb79-e100bffa0361.pdf',
        'da': 'Koutroubas, Alex(HID Global).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Aggregate Manufacturers of NH)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52528',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/6de8604a-a351-487f-ba8c-5c522d9c0d4e.pdf',
        'da': 'Kroll, Heidi(Aggregate Manufacturers of NH).pdf'
    },
    {
        'dn': 'Kroll, Heidi(America Health Insurance Plans)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52529',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/5aeb34fb-acec-4cd0-8ec1-33a40d32f45d.pdf',
        'da': 'Kroll, Heidi(America Health Insurance Plans).pdf'
    },
    {
        'dn': 'Kroll, Heidi(BJ Alan Company Phantom Fireworks)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52530',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/743d93ec-a981-47dc-890a-692c91633b2c.pdf',
        'da': 'Kroll, Heidi(BJ Alan Company Phantom Fireworks).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Granite State Hydropower Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52531',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/17576d08-c43b-4e9e-b29f-b4b67fcb73d3.pdf',
        'da': 'Kroll, Heidi(Granite State Hydropower Assoc).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Home Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52532',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/d58fb9da-818d-4800-85c8-dfb55d47d4ea.pdf',
        'da': 'Kroll, Heidi(Home Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Life Coping)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52533',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/df69023f-07ce-4a9c-9f16-9a332409acba.pdf',
        'da': 'Kroll, Heidi(Life Coping).pdf'
    },
    {
        'dn': 'Kroll, Heidi(National Academy of Elder Law Attorneys)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52534',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/3aa58d35-af66-46ed-9575-f45c08221fef.pdf',
        'da': 'Kroll, Heidi(National Academy of Elder Law Attorneys).pdf'
    },
    {
        'dn': 'Kroll, Heidi(New Hampshire Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52535',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/2efbeeee-399d-4ebc-a0a5-e3f251300341.pdf',
        'da': 'Kroll, Heidi(New Hampshire Bankers Assoc).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Northeast Rehabilitation Health Network)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52536',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/2bd49574-a7d0-4757-a367-27eba170e0df.pdf',
        'da': 'Kroll, Heidi(Northeast Rehabilitation Health Network).pdf'
    },
    {
        'dn': 'Kroll, Heidi(Progressive Insurance)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52537',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/c5eb4e3b-3ca1-432c-974a-54a7206d333b.pdf',
        'da': 'Kroll, Heidi(Progressive Insurance).pdf'
    },
    {
        'dn': 'Kuenning, Keith(Child and Family Serv)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52538',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/3655d79f-adb2-4350-b309-2c6e23754de4.pdf',
        'da': 'Kuenning, Keith(Child and Family Serv).pdf'
    },
    {
        'dn': 'Kuenning, Tess(Bi State Primary Care Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914HK.aspx?id=52539',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2467/7c5f0f22-ebc0-46fd-8c3e-3a422f9f408b.pdf',
        'da': 'Kuenning, Tess(Bi State Primary Care Assoc).pdf'
    },
    {
        'dn': 'Laboe, John(NH Chapter of the Ntl Academy of Elder Law Atty)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52540',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/68c1c092-e654-4d40-8e70-2140c41d35d6.pdf',
        'da': 'Laboe, John(NH Chapter of the Ntl Academy of Elder Law Atty).pdf'
    },
    {
        'dn': 'Lacey, Diana(SEA SEIU Local 1984)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52541',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/c07c56b5-07a8-4d7f-98ae-162d7875068b.pdf',
        'da': 'Lacey, Diana(SEA SEIU Local 1984).pdf'
    },
    {
        'dn': 'Lafontaine, Michael(NH Community Loan Fund)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52542',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/d3d54a06-a6b1-49b8-be14-0308d01adf48.pdf',
        'da': 'Lafontaine, Michael(NH Community Loan Fund).pdf'
    },
    {
        'dn': 'Lambert, Mark(Unitil Corp)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52543',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/8a4ecc66-3b21-40ad-a6ac-acb7f7d67b8d.pdf',
        'da': 'Lambert, Mark(Unitil Corp).pdf'
    },
    {
        'dn': 'Lamoreaux, Andrea(NH Lakes Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=8589936918',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/8193909c-58d8-455b-af53-6275647a6a87.pdf',
        'da': 'Lamoreaux, Andrea(NH Lakes Assoc).pdf'
    },
    {
        'dn': 'Lang, David(Professional Fire Fighters of NH)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52544',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/034dfa4f-0c21-4cf5-a0dc-5129f47185f2.pdf',
        'da': 'Lang, David(Professional Fire Fighters of NH).pdf'
    },
    {
        'dn': 'Leberman, Peter(Northeast Delta Dental)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52545',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/8c18fdc0-0ab5-431a-8a29-191dc32a9ca0.pdf',
        'da': 'Leberman, Peter(Northeast Delta Dental).pdf'
    },
    {
        'dn': 'Legislative Solutions(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52546',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/392f39e0-a5a9-42bd-b853-09726987b767.pdf',
        'da': 'Legislative Solutions(Addendum C).pdf'
    },
    {
        'dn': 'Lehmann, Suzan(ADP TotalSource)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52547',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/257d2571-2001-4836-9e81-280887c5e9ee.pdf',
        'da': 'Lehmann, Suzan(ADP TotalSource).pdf'
    },
    {
        'dn': 'Lehmann, Suzan(Law Warehouse)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52548',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/a971fa25-3606-4ba1-8a12-26e884fd0637.pdf',
        'da': 'Lehmann, Suzan(Law Warehouse).pdf'
    },
    {
        'dn': 'Lehmann, Suzan(Phoenix Houses of New England)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52549',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/49328a8d-dd12-4904-b5f1-0aa436e4b307.pdf',
        'da': 'Lehmann, Suzan(Phoenix Houses of New England).pdf'
    },
    {
        'dn': 'Linder, Alan(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=8589936919',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/7d0249c7-ec5a-4cf8-a9bd-d96f60a95d3f.pdf',
        'da': 'Linder, Alan(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'Linder, Alan(The Way Home)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=8589936920',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/ba5639bf-32c7-4ff2-b952-4ce8ac501e34.pdf',
        'da': 'Linder, Alan(The Way Home).pdf'
    },
    {
        'dn': 'Lipman, Henry(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52550',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/f9ab2a61-8ac6-4166-bfb6-b6da7616b10e.pdf',
        'da': 'Lipman, Henry(Addendum C).pdf'
    },
    {
        'dn': 'Lipman, Henry(LRG Helathcare)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52551',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/af67f801-34ba-4354-9c22-a93b89430d2c.pdf',
        'da': 'Lipman, Henry(LRG Helathcare).pdf'
    },
    {
        'dn': 'Lucas, Tricia(New Futures Inc)',
        'wp': 'http://sos.nh.gov/Lob012914L.aspx?id=52552',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2468/5806d613-b406-48c9-af77-345fc2b8b7f1.pdf',
        'da': 'Lucas, Tricia(New Futures Inc).pdf'
    },
    {
        'dn': 'MacColl, Campbell(Credit Swisse Securities USA)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52553',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/617e7d59-7224-4863-879a-378a1bedfdf9.pdf',
        'da': 'MacColl, Campbell(Credit Swisse Securities USA).pdf'
    },
    {
        'dn': 'Mackenzie, Mark(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52554',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/3705e749-62d3-43a4-9b91-ca0222b53492.pdf',
        'da': 'Mackenzie, Mark(Addendum C).pdf'
    },
    {
        'dn': 'Mackenzie, Mark(NH AFLl CIO)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52555',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/ecc24391-1c02-46a9-99ac-d68f18722af6.pdf',
        'da': 'Mackenzie, Mark(NH AFLl CIO).pdf'
    },
    {
        'dn': 'Madrazo, Paul',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52556',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/604025e4-8b2f-4cfe-8d60-6a1b54ace387.pdf',
        'da': 'Madrazo, Paul.pdf'
    },
    {
        'dn': 'Maiola, Joel(Cate Street Capital)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52557',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/14fd6f35-f208-4a3a-a5fd-fd283ec18ede.pdf',
        'da': 'Maiola, Joel(Cate Street Capital).pdf'
    },
    {
        'dn': 'Maiola, Joel(Exel Inc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52558',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/055cff0e-c963-421c-8ee2-33f0c6529864.pdf',
        'da': 'Maiola, Joel(Exel Inc).pdf'
    },
    {
        'dn': 'Maiola, Joel(Gamma Medica Inc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52559',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/de3c9c2c-1168-48fc-a28a-106195142742.pdf',
        'da': 'Maiola, Joel(Gamma Medica Inc).pdf'
    },
    {
        'dn': 'Maiola, Joel(Merchants Automotive Group)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52560',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/4cde15a5-3be0-4670-a398-591c2a8b1b5e.pdf',
        'da': 'Maiola, Joel(Merchants Automotive Group).pdf'
    },
    {
        'dn': 'Maiola, Joel(SMG Mgmt Co Verizon Wireless Arena)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52561',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/bd91ed3f-a1b2-481f-856f-1bae159b1875.pdf',
        'da': 'Maiola, Joel(SMG Mgmt Co Verizon Wireless Arena).pdf'
    },
    {
        'dn': 'Maiola, Joel(Well Sense Health Plan)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52562',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/44cf6bf7-a3b2-43b2-ba07-f4115163b3e3.pdf',
        'da': 'Maiola, Joel(Well Sense Health Plan).pdf'
    },
    {
        'dn': 'Margolin, Elissa(Housing Action NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52563',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/9842eac5-7458-41ee-a637-c671a6f6c3bc.pdf',
        'da': 'Margolin, Elissa(Housing Action NH).pdf'
    },
    {
        'dn': 'Mattson, Sarah(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589936923',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/5e939852-0c6d-47af-ac2a-f7fa1ec53e6f.pdf',
        'da': 'Mattson, Sarah(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'McCabe, Casey(Professional Fire Fighters of NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52564',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/dab74bdf-b5f5-422e-a9fa-e3e70145c18d.pdf',
        'da': 'McCabe, Casey(Professional Fire Fighters of NH).pdf'
    },
    {
        'dn': 'McCarthy, Kayla(Professional Fire Fighters of NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52565',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/ada4b0bf-fd72-4b05-a15a-99e98c9ccaa5.pdf',
        'da': 'McCarthy, Kayla(Professional Fire Fighters of NH).pdf'
    },
    {
        'dn': 'McConnell, Julianne(NH Community Loan Fund)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52566',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/01530e56-79ce-417f-848f-51ff3e83e1dc.pdf',
        'da': 'McConnell, Julianne(NH Community Loan Fund).pdf'
    },
    {
        'dn': 'McDougall, Frank(Dartmouth Hitchcock)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52567',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/cf41d96e-92b9-4f18-bea7-106ef3e438f6.pdf',
        'da': 'McDougall, Frank(Dartmouth Hitchcock).pdf'
    },
    {
        'dn': 'McGiluray, Scott(NEA-NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589936921',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/8332e80f-a0a2-4e65-9b64-18843c18ddb2.pdf',
        'da': 'McGiluray, Scott(NEA-NH).pdf'
    },
    {
        'dn': 'Mclane Government and Public Strategies(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52568',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/4d01c7c4-e8bb-4809-b07c-091685d32dad.pdf',
        'da': 'Mclane Government and Public Strategies(Addendum C).pdf'
    },
    {
        'dn': 'McLynch, Jeffrey(NH Fiscal Policy Institute)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52569',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/99f544f8-fc40-446b-8a34-45dbacd8a068.pdf',
        'da': 'McLynch, Jeffrey(NH Fiscal Policy Institute).pdf'
    },
    {
        'dn': 'McNamara, Peter(NH Automobile Dealers Insurance Co)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52570',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/1bef4a23-5c5e-48d8-9372-dd2340d072f9.pdf',
        'da': 'McNamara, Peter(NH Automobile Dealers Insurance Co).pdf'
    },
    {
        'dn': 'McNutt, Douglas(AARP)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52571',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/142c8b8b-9683-4314-a531-d03e817c1648.pdf',
        'da': 'McNutt, Douglas(AARP).pdf'
    },
    {
        'dn': 'McQuillen, William(Professional Fire Fighters of NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52572',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/ec73f35d-020f-4e6f-8fe7-4edf2794b1b3.pdf',
        'da': 'McQuillen, William(Professional Fire Fighters of NH).pdf'
    },
    {
        'dn': 'McSparren, Robert(Bristol Myers Squibb Co)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52573',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/d6dfd9ca-5d31-4437-be2c-12d0677e4740.pdf',
        'da': 'McSparren, Robert(Bristol Myers Squibb Co).pdf'
    },
    {
        'dn': 'Messer, Amy(Disabilities Rights Center)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52574',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/68ed3955-8d8d-46ed-83e8-1af8208e7bf6.pdf',
        'da': 'Messer, Amy(Disabilities Rights Center).pdf'
    },
    {
        'dn': 'Michener, R Dean(NH School Boards Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52575',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/32efb916-6487-46be-8a64-b00dd6018ff5.pdf',
        'da': 'Michener, R Dean(NH School Boards Assoc).pdf'
    },
    {
        'dn': 'Miller, Betsy(NH Assoc of Counties)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589936922',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/300e590b-cd79-40bf-a6e1-4ed3dcf7a545.pdf',
        'da': 'Miller, Betsy(NH Assoc of Counties).pdf'
    },
    {
        'dn': 'Milner, Glenn(American Assoc of Univ Professors UNH Chp)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52576',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/919fc3d0-e755-4ff8-a02b-cef3496dcfda.pdf',
        'da': 'Milner, Glenn(American Assoc of Univ Professors UNH Chp).pdf'
    },
    {
        'dn': 'Milner, Glenn(State Employees Assoc of NH SEIU Loc 1984)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52577',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/302bcfb5-d602-41ec-b5dc-886df7c6b8f0.pdf',
        'da': 'Milner, Glenn(State Employees Assoc of NH SEIU Loc 1984).pdf'
    },
    {
        'dn': 'Minard, Richard(NH Community Loan Fund)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52578',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/ef44c6db-dc08-453a-ab50-f4798556465d.pdf',
        'da': 'Minard, Richard(NH Community Loan Fund).pdf'
    },
    {
        'dn': 'Minkoff Zern, Jonah(Public Citizens)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52579',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/6d184c9c-e470-4229-b3a1-8c7c443bbe03.pdf',
        'da': 'Minkoff Zern, Jonah(Public Citizens).pdf'
    },
    {
        'dn': 'Moccia, Leann(NH Assoc for Justice)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52580',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/60a46b8e-10a3-425c-ac44-33f1f63a2a63.pdf',
        'da': 'Moccia, Leann(NH Assoc for Justice).pdf'
    },
    {
        'dn': 'Monahan, James(Bi State Primary Care Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939211',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/92573a99-9599-4e5d-8866-3623915d77ad.pdf',
        'da': 'Monahan, James(Bi State Primary Care Assoc).pdf'
    },
    {
        'dn': 'Monahan, James(Community Behavioral Health Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939212',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/0574261f-444d-4867-9090-eda2b637b4f4.pdf',
        'da': 'Monahan, James(Community Behavioral Health Assoc).pdf'
    },
    {
        'dn': 'Monahan, James(Crotched Mountain)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939213',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/144c8b5e-4863-415e-9251-0d1c0ad4df89.pdf',
        'da': 'Monahan, James(Crotched Mountain).pdf'
    },
    {
        'dn': 'Monahan, James(Healthsouth)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939217',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/9328472e-76e8-4a3a-8012-df3443c36934.pdf',
        'da': 'Monahan, James(Healthsouth).pdf'
    },
    {
        'dn': 'Monahan, James(LL S)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939218',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/fe726979-a6d9-4157-b646-9d45fe03a1c8.pdf',
        'da': 'Monahan, James(LL S).pdf'
    },
    {
        'dn': 'Monahan, James(Meggitt NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939219',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/00efac07-2949-480b-b828-341bbfb7b1c0.pdf',
        'da': 'Monahan, James(Meggitt NH).pdf'
    },
    {
        'dn': 'Monahan, James(Nature Conservancy)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939216',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/f0b40288-7bcb-44b5-9806-7881bbfa2b0a.pdf',
        'da': 'Monahan, James(Nature Conservancy).pdf'
    },
    {
        'dn': 'Monahan, James(NE Power Generators Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939214',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/dbbf5a99-2cae-4e9b-8615-3419d19bdc72.pdf',
        'da': 'Monahan, James(NE Power Generators Assoc).pdf'
    },
    {
        'dn': 'Monahan, James(New Futures)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939220',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/747bdd1f-c9d1-446a-ab1a-49d63e11ef86.pdf',
        'da': 'Monahan, James(New Futures).pdf'
    },
    {
        'dn': 'Monahan, James(Nextera Energy Resources)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939221',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/44d6a862-34ca-403f-9f07-d1fb1b1e4f08.pdf',
        'da': 'Monahan, James(Nextera Energy Resources).pdf'
    },
    {
        'dn': 'Monahan, James(NH Chiropractic Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939222',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/dd406705-1d36-4f3e-9c56-e6acd0a028bf.pdf',
        'da': 'Monahan, James(NH Chiropractic Assoc).pdf'
    },
    {
        'dn': 'Monahan, James(NH Provider Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939223',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/f2be44c1-1d65-4540-9403-81280e166a2f.pdf',
        'da': 'Monahan, James(NH Provider Assoc).pdf'
    },
    {
        'dn': 'Monahan, James(Pan American Railways)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939224',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/a090f1e3-f66f-4472-90c5-19508e0e0d40.pdf',
        'da': 'Monahan, James(Pan American Railways).pdf'
    },
    {
        'dn': 'Monahan, James(Retail Merchants Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939215',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/7c40bd2c-5d9e-4cc1-be39-5bab09cbf362.pdf',
        'da': 'Monahan, James(Retail Merchants Assoc of NH).pdf'
    },
    {
        'dn': 'Monahan, James(Schaller Anderson)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939225',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/fe22a903-9302-40ad-b6ea-f5677b8309f8.pdf',
        'da': 'Monahan, James(Schaller Anderson).pdf'
    },
    {
        'dn': 'Monahan, James(Society for the Protection of NH Forests)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939226',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/1a7ef147-13ed-4619-88a0-6acfc2008691.pdf',
        'da': 'Monahan, James(Society for the Protection of NH Forests).pdf'
    },
    {
        'dn': 'Monahan, James(Trust for Public Land)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=8589939227',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/ebe5b54d-6980-4bce-9121-3dd1f447da82.pdf',
        'da': 'Monahan, James(Trust for Public Land).pdf'
    },
    {
        'dn': 'Moore, George(grocery Manufacturers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52581',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/eee3a1ae-334b-4d13-8170-ee1bb56fe6c3.pdf',
        'da': 'Moore, George(grocery Manufacturers Assoc).pdf'
    },
    {
        'dn': 'Moore, Gregory(Americans for Prosperity NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52582',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/224807b5-a017-4505-bb2c-8482b3f04953.pdf',
        'da': 'Moore, Gregory(Americans for Prosperity NH).pdf'
    },
    {
        'dn': 'Morin, Paul(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52583',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/569a26cd-6e41-46ad-b74f-bd5a43715cca.pdf',
        'da': 'Morin, Paul(Addendum C).pdf'
    },
    {
        'dn': 'Morin, Paul(PFGF HVAC Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52584',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/14620523-ccdd-4412-aaff-a7ffae411c3b.pdf',
        'da': 'Morin, Paul(PFGF HVAC Assoc of NH).pdf'
    },
    {
        'dn': 'Mullen, William(Reckitt Benckiser Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52585',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/d9b37796-cb14-4362-87a0-ae276940e911.pdf',
        'da': 'Mullen, William(Reckitt Benckiser Pharmaceuticals).pdf'
    },
    {
        'dn': 'Murray, Joseph(FMR LLC)',
        'wp': 'http://sos.nh.gov/Lob012914M.aspx?id=52586',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2469/1d5b8dfe-5508-4329-a9e9-04d827c7612a.pdf',
        'da': 'Murray, Joseph(FMR LLC).pdf'
    },
    {
        'dn': 'Nash, Robert(NH Assoc of Insurance Agents)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52713',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/b0b0e2f6-a24d-47be-ace9-ed4ba03f7b26.pdf',
        'da': 'Nash, Robert(NH Assoc of Insurance Agents).pdf'
    },
    {
        'dn': 'Newhall-Grahame, Tricia(PFGF HVAC Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52714',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/4947d94f-6fe5-4ef7-bea1-9aaf43b518ed.pdf',
        'da': 'Newhall-Grahame, Tricia(PFGF HVAC Assoc of NH).pdf'
    },
    {
        'dn': 'Newman, Erik(American Resort Development Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52715',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/ce6e8fcc-5d6c-47f0-a9a4-d0975d949349.pdf',
        'da': 'Newman, Erik(American Resort Development Assoc).pdf'
    },
    {
        'dn': 'Newman, Rick(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52716',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/b80baeab-cbbe-4925-9f33-f04730c4fe8b.pdf',
        'da': 'Newman, Rick(Addendum C).pdf'
    },
    {
        'dn': 'Newman, Rick(Altria Client Serv Inc and affiliates)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52717',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/e6853589-8aa0-45ba-9e9b-dfed9e1d99f2.pdf',
        'da': 'Newman, Rick(Altria Client Serv Inc and affiliates).pdf'
    },
    {
        'dn': 'Newman, Rick(Mclane North East)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52718',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/c5ea7800-0b4f-4618-a41e-48802ddc07fa.pdf',
        'da': 'Newman, Rick(Mclane North East).pdf'
    },
    {
        'dn': 'Newman, Rick(MillerCoors)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52719',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/022a9211-4cbc-42e2-a592-273f0b25eb2a.pdf',
        'da': 'Newman, Rick(MillerCoors).pdf'
    },
    {
        'dn': 'Newman, Rick(Moonlight Meadery)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52720',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/caeee412-3925-46bc-a98b-238efbabc63f.pdf',
        'da': 'Newman, Rick(Moonlight Meadery).pdf'
    },
    {
        'dn': 'Newman, Rick(NH Independent Pharmacy Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52721',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/f65ab48f-36dd-4e51-b308-71cb804deee1.pdf',
        'da': 'Newman, Rick(NH Independent Pharmacy Assoc).pdf'
    },
    {
        'dn': 'Newman, Rick(Pokertek)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52722',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/05c108ac-3bbe-4537-bbc9-c4bfd001fa66.pdf',
        'da': 'Newman, Rick(Pokertek).pdf'
    },
    {
        'dn': 'Newman, Rick(River Card Room)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52723',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/18fcc454-f6f2-4680-8c87-3d3c7e50151c.pdf',
        'da': 'Newman, Rick(River Card Room).pdf'
    },
    {
        'dn': 'Newman, Rick(Title Cash of NH)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52724',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/2aaa5946-6f71-4e4b-a2c0-8d5425e35c37.pdf',
        'da': 'Newman, Rick(Title Cash of NH).pdf'
    },
    {
        'dn': 'Nicolopoulos, Christopher(American International Group)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52725',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/ed3e604b-595b-483e-860a-9bd3e5f49d1c.pdf',
        'da': 'Nicolopoulos, Christopher(American International Group).pdf'
    },
    {
        'dn': 'Nicolopoulos, Christopher(CNA Insurance)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52726',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/faf88134-a005-41ee-ad7a-933f47eeeaac.pdf',
        'da': 'Nicolopoulos, Christopher(CNA Insurance).pdf'
    },
    {
        'dn': 'Nicolopoulos, Christopher(Food Democracy Now)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52727',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/3b0105bd-41f5-4e15-a5c3-4e5e3940f2c2.pdf',
        'da': 'Nicolopoulos, Christopher(Food Democracy Now).pdf'
    },
    {
        'dn': 'O\'Brien, Jim(Nature Conservancy)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52728',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/a2f20096-b087-4ae3-adff-ea6ff68b2420.pdf',
        'da': 'O\'Brien, Jim(Nature Conservancy).pdf'
    },
    {
        'dn': 'O\'Brien, Michael(America Votes Addendum A)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=8589936926',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/16dcc23d-6d36-4179-a376-9eb66b59ae46.pdf',
        'da': 'O\'Brien, Michael(America Votes Addendum A).pdf'
    },
    {
        'dn': 'OBrien, Thomas(NH Lakes Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=8589936924',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/46e67cb8-c73a-498f-9aec-ddda865e93c0.pdf',
        'da': 'OBrien, Thomas(NH Lakes Assoc).pdf'
    },
    {
        'dn': 'Olson, Robert(Bridgewater Power Company)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52729',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/58de4616-c22b-4cd8-b6de-6e51049cfd91.pdf',
        'da': 'Olson, Robert(Bridgewater Power Company).pdf'
    },
    {
        'dn': 'Olson, Robert(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52730',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/2b8e481b-5e12-43c1-9a9a-30a619a4b87b.pdf',
        'da': 'Olson, Robert(DG Whitefield).pdf'
    },
    {
        'dn': 'Olson, Robert(GDF Suez Energy Generation NH)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52731',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/e7d23f14-91a3-4eda-a91b-5d8781e185bc.pdf',
        'da': 'Olson, Robert(GDF Suez Energy Generation NH).pdf'
    },
    {
        'dn': 'Olson, Robert(Indock Energy Services)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52732',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/8cd17bf0-8c41-4a78-932c-067c82eb81fa.pdf',
        'da': 'Olson, Robert(Indock Energy Services).pdf'
    },
    {
        'dn': 'Olson, Robert(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52733',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/ebef8448-ca1c-4643-b9a8-5fc6670a3dc1.pdf',
        'da': 'Olson, Robert(Springfield Power).pdf'
    },
    {
        'dn': 'Oorman, Margaret(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52734',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/fa853865-e220-4859-83c1-13c416ee4fd7.pdf',
        'da': 'Oorman, Margaret(Addendum C).pdf'
    },
    {
        'dn': 'Oorman, Margaret(American Chemistry Council)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=52735',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/c4b8b400-1dc2-458f-bb94-ed649274ea1b.pdf',
        'da': 'Oorman, Margaret(American Chemistry Council).pdf'
    },
    {
        'dn': 'Peshek, Adam(Excellence in Education National)',
        'wp': 'http://sos.nh.gov/Lob012914NQ.aspx?id=8589936925',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2477/268fa833-5739-484f-a843-d64bacb39934.pdf',
        'da': 'Peshek, Adam(Excellence in Education National).pdf'
    },
    {
        'dn': 'Paquette, Linda(New Futures Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52736',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/fd795bdf-f388-4003-be26-a825036524c6.pdf',
        'da': 'Paquette, Linda(New Futures Inc).pdf'
    },
    {
        'dn': 'Pardy, Preston(NH Assoc of Special Education Administrators Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52737',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/9a6b3954-e85f-4ef8-bc6a-a06ac818761e.pdf',
        'da': 'Pardy, Preston(NH Assoc of Special Education Administrators Inc).pdf'
    },
    {
        'dn': 'Parsons, Richard(American Express)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52738',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3b68e942-6df0-457f-82d6-df6758ca79e8.pdf',
        'da': 'Parsons, Richard(American Express).pdf'
    },
    {
        'dn': 'Parsons, Richard(Anthem Blue Cross Blue Shield Wellpoint)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52739',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/82624bb7-14eb-48a2-8e59-4b7bba38076c.pdf',
        'da': 'Parsons, Richard(Anthem Blue Cross Blue Shield Wellpoint).pdf'
    },
    {
        'dn': 'Parsons, Richard(AstraZeneca Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52740',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/4e639bd5-e6bd-4845-a577-1f35377df5f4.pdf',
        'da': 'Parsons, Richard(AstraZeneca Pharmaceuticals).pdf'
    },
    {
        'dn': 'Parsons, Richard(Bedford Ambulatory Surgical Center)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52741',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/fe6f7d99-9300-47d4-a7e1-c23bb539a22a.pdf',
        'da': 'Parsons, Richard(Bedford Ambulatory Surgical Center).pdf'
    },
    {
        'dn': 'Parsons, Richard(Blue Mountain Forest Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52742',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/eb0e7ed0-9aac-457d-8ad0-fd6d8decefaf.pdf',
        'da': 'Parsons, Richard(Blue Mountain Forest Assoc).pdf'
    },
    {
        'dn': 'Parsons, Richard(City of Rochester Wastewater Treatment Plant)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52743',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/2c78b436-2564-48ce-9ac9-3b4e7c7fb6b2.pdf',
        'da': 'Parsons, Richard(City of Rochester Wastewater Treatment Plant).pdf'
    },
    {
        'dn': 'Parsons, Richard(Comcast Corp)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52744',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/55d7e00e-41dc-471a-8fec-345ca4ce6095.pdf',
        'da': 'Parsons, Richard(Comcast Corp).pdf'
    },
    {
        'dn': 'Parsons, Richard(Correction Corp of America)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52745',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/fa456750-779b-4019-a178-c923139412de.pdf',
        'da': 'Parsons, Richard(Correction Corp of America).pdf'
    },
    {
        'dn': 'Parsons, Richard(Dartmouth College)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52746',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/186656f9-aaae-43c6-b930-d1a5816b0b0b.pdf',
        'da': 'Parsons, Richard(Dartmouth College).pdf'
    },
    {
        'dn': 'Parsons, Richard(Dartmouth Medical School)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52747',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/7ed8c998-c11a-475a-951b-f434c7c31fd2.pdf',
        'da': 'Parsons, Richard(Dartmouth Medical School).pdf'
    },
    {
        'dn': 'Parsons, Richard(Explore Informational Serv)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52748',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/5d59e1b8-33a0-4bc7-90c6-548bd05c5163.pdf',
        'da': 'Parsons, Richard(Explore Informational Serv).pdf'
    },
    {
        'dn': 'Parsons, Richard(Feld Entertainment)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52749',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3cb9c19f-1e4c-4d31-9b5c-5c767d489a06.pdf',
        'da': 'Parsons, Richard(Feld Entertainment).pdf'
    },
    {
        'dn': 'Parsons, Richard(Merck Sharp and Dohme)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52750',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/80075bed-accf-46a3-8712-da492a2814a2.pdf',
        'da': 'Parsons, Richard(Merck Sharp and Dohme).pdf'
    },
    {
        'dn': 'Parsons, Richard(N E Medical Equipment Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52751',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/4293d2c1-528e-4ad0-8471-aff0da25a403.pdf',
        'da': 'Parsons, Richard(N E Medical Equipment Dealers Assoc).pdf'
    },
    {
        'dn': 'Parsons, Richard(N H Credit Union League)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52752',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/78ad837a-4278-4057-a250-3c03a85d9e06.pdf',
        'da': 'Parsons, Richard(N H Credit Union League).pdf'
    },
    {
        'dn': 'Parsons, Richard(N H Independent Schools)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52753',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/cb666203-96b1-46f2-9bcb-c24d5ffdb7b8.pdf',
        'da': 'Parsons, Richard(N H Independent Schools).pdf'
    },
    {
        'dn': 'Parsons, Richard(NH Alliance of Boys and Girls Clubs)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52754',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/cd10cac7-a038-46bc-ad3a-de29d1f2f5da.pdf',
        'da': 'Parsons, Richard(NH Alliance of Boys and Girls Clubs).pdf'
    },
    {
        'dn': 'Parsons, Richard(Ntl Shooting Sports Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52755',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/195b6122-b665-47b7-8b3e-b95ab12f46d6.pdf',
        'da': 'Parsons, Richard(Ntl Shooting Sports Foundation).pdf'
    },
    {
        'dn': 'Parsons, Richard(Public Service Co of NH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52756',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/a7396211-f30e-413b-bcef-0780a519d89d.pdf',
        'da': 'Parsons, Richard(Public Service Co of NH).pdf'
    },
    {
        'dn': 'Parsons, Richard(RAI Services Co)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52757',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b733894e-008d-49a4-a408-e52014ecd5b9.pdf',
        'da': 'Parsons, Richard(RAI Services Co).pdf'
    },
    {
        'dn': 'Parsons, Richard(Rural Hospital Coalition)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52758',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/dcc1df3e-8c1b-4f20-b139-4bdb1e58d694.pdf',
        'da': 'Parsons, Richard(Rural Hospital Coalition).pdf'
    },
    {
        'dn': 'Paschell, Susan(Bi State Primary Care Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939228',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/cd97d89a-3498-4507-911b-08de36949421.pdf',
        'da': 'Paschell, Susan(Bi State Primary Care Assoc).pdf'
    },
    {
        'dn': 'Paschell, Susan(C J Trailways)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939229',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/e00f053d-00da-4805-abfc-7b53a2e29afe.pdf',
        'da': 'Paschell, Susan(C J Trailways).pdf'
    },
    {
        'dn': 'Paschell, Susan(Community Behavioral Health Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939230',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/4b932fa8-5e60-4823-b40c-151fbe54809d.pdf',
        'da': 'Paschell, Susan(Community Behavioral Health Assoc).pdf'
    },
    {
        'dn': 'Paschell, Susan(Crotched Mountain)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939231',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/90b8ec13-ce94-4949-b61d-a1e982e99100.pdf',
        'da': 'Paschell, Susan(Crotched Mountain).pdf'
    },
    {
        'dn': 'Paschell, Susan(Gordon Darby)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939232',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/439e0744-04f9-41a5-92e5-dac9c8c40432.pdf',
        'da': 'Paschell, Susan(Gordon Darby).pdf'
    },
    {
        'dn': 'Paschell, Susan(Harvard Pilgrim Health Care)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939233',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/9a86ed23-b452-4b4a-91fa-d67f26b3438f.pdf',
        'da': 'Paschell, Susan(Harvard Pilgrim Health Care).pdf'
    },
    {
        'dn': 'Paschell, Susan(MHM Services)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939234',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/874f71c9-548b-4414-8579-0908d4e50d48.pdf',
        'da': 'Paschell, Susan(MHM Services).pdf'
    },
    {
        'dn': 'Paschell, Susan(NE Power Generators Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939235',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/bc87b9f0-64d0-4026-b99b-63b9008f404e.pdf',
        'da': 'Paschell, Susan(NE Power Generators Assoc).pdf'
    },
    {
        'dn': 'Paschell, Susan(NH Dental Hygienists Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=8589939236',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b3a36110-835d-4ccd-995d-2b856a0687cf.pdf',
        'da': 'Paschell, Susan(NH Dental Hygienists Assoc).pdf'
    },
    {
        'dn': 'Patch, Douglas(New Hampshire Fire Chiefs Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52759',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/c7134357-591d-43a7-9460-599e24c3c8c4.pdf',
        'da': 'Patch, Douglas(New Hampshire Fire Chiefs Assoc).pdf'
    },
    {
        'dn': 'Patch, Douglas(Riverstone Resources)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52760',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/2dbea025-39a7-4548-aa4f-c35c35cb4cbc.pdf',
        'da': 'Patch, Douglas(Riverstone Resources).pdf'
    },
    {
        'dn': 'Patch, Douglas(TransCanada Hydro Northeast Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52761',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/86744ecc-cd2b-476a-83c5-7253f6883609.pdf',
        'da': 'Patch, Douglas(TransCanada Hydro Northeast Inc).pdf'
    },
    {
        'dn': 'Patch, Douglas(Wagner Forest Management)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52762',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/d0b98e17-429c-4e44-a8fe-73746c7d1867.pdf',
        'da': 'Patch, Douglas(Wagner Forest Management).pdf'
    },
    {
        'dn': 'Pepin, Amy(New Futures Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52763',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/ddf94532-12b3-4aa1-890d-fb17c5ef4371.pdf',
        'da': 'Pepin, Amy(New Futures Inc).pdf'
    },
    {
        'dn': 'Peress, N Jonathan(Conservation Law Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52764',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/78c5ccc3-59d4-4517-8c56-7e68bec6ac4e.pdf',
        'da': 'Peress, N Jonathan(Conservation Law Foundation).pdf'
    },
    {
        'dn': 'Petro, Melissia(Purdue Pharma LP)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52765',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b108b5dd-1975-4678-809b-975730ba90b6.pdf',
        'da': 'Petro, Melissia(Purdue Pharma LP).pdf'
    },
    {
        'dn': 'Pfundstein, Donald(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52766',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/2a282f37-618a-45e7-a0ad-684ce95db9b8.pdf',
        'da': 'Pfundstein, Donald(Addendum C).pdf'
    },
    {
        'dn': 'Pfundstein, Donald(Americas Helath Insurance Plans)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52767',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/6492a3a3-a740-46ca-9844-18d9fe3c5e38.pdf',
        'da': 'Pfundstein, Donald(Americas Helath Insurance Plans).pdf'
    },
    {
        'dn': 'Pfundstein, Donald(Memic Indemnity Company)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52768',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/fbb7c53e-108a-4beb-b4ef-903e7f65b3ba.pdf',
        'da': 'Pfundstein, Donald(Memic Indemnity Company).pdf'
    },
    {
        'dn': 'Pfundstein, Donald(Northern Pass Transmission)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52769',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b3356878-688a-4972-9502-ccd39ab2443d.pdf',
        'da': 'Pfundstein, Donald(Northern Pass Transmission).pdf'
    },
    {
        'dn': 'Pfundstein, Donald(Progressive Insurance)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52770',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/97e66e05-7ef4-44c8-b73e-90046298341a.pdf',
        'da': 'Pfundstein, Donald(Progressive Insurance).pdf'
    },
    {
        'dn': 'Pierce, Erle(Entertainment Software Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52771',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/dddf3586-6997-49ac-8d2a-22439c916c22.pdf',
        'da': 'Pierce, Erle(Entertainment Software Assoc).pdf'
    },
    {
        'dn': 'Pierce, Erle(Granite Ridge Energy LLC)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52772',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/7d7b97fe-f236-4a30-842a-d34b432356e0.pdf',
        'da': 'Pierce, Erle(Granite Ridge Energy LLC).pdf'
    },
    {
        'dn': 'Pierce, Erle(John Deere)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52773',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/858d3930-6ed9-4095-bcf8-10015d5f1361.pdf',
        'da': 'Pierce, Erle(John Deere).pdf'
    },
    {
        'dn': 'Pierce, Erle(Law Warehouses Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52774',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/c4de4b40-8b2e-4f11-b7cf-9bf4d9087523.pdf',
        'da': 'Pierce, Erle(Law Warehouses Inc).pdf'
    },
    {
        'dn': 'Pierce, Erle(Mgmt Training Corp)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52775',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/be5115fc-e416-4734-8ec2-406b6122dccf.pdf',
        'da': 'Pierce, Erle(Mgmt Training Corp).pdf'
    },
    {
        'dn': 'Pierce, Erle(National Grid)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52776',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/8f82048f-f212-4977-b0a6-8ec2e6c252dc.pdf',
        'da': 'Pierce, Erle(National Grid).pdf'
    },
    {
        'dn': 'Pierce, Erle(NH Citizens for the Arts)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52777',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/1c68725e-d432-46b3-be1f-4f0131f41f94.pdf',
        'da': 'Pierce, Erle(NH Citizens for the Arts).pdf'
    },
    {
        'dn': 'Pierce, Erle(segTEL)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52778',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/99221c1e-eae5-41ef-ae0a-e59163e7e392.pdf',
        'da': 'Pierce, Erle(segTEL).pdf'
    },
    {
        'dn': 'Pierce, Erle(Verizon Comm)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52779',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/981205b0-04d3-4620-8161-53eae39ea303.pdf',
        'da': 'Pierce, Erle(Verizon Comm).pdf'
    },
    {
        'dn': 'Pollack, Ari(Aggregate Manufacturers of NH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52780',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/469926e5-1c35-46f5-a295-46d5b20bd993.pdf',
        'da': 'Pollack, Ari(Aggregate Manufacturers of NH).pdf'
    },
    {
        'dn': 'Pollack, Ari(Demoulas Super Markets Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52781',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/f0fb6741-84a4-4929-9043-a19968ccc56d.pdf',
        'da': 'Pollack, Ari(Demoulas Super Markets Inc).pdf'
    },
    {
        'dn': 'Pollack, Ari(Home Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52782',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/dabe42f6-5859-49f3-902a-b5c6e1bed2b5.pdf',
        'da': 'Pollack, Ari(Home Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Pollack, Ari(Pillsbury Realty Development)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52783',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/94173a7e-6728-48f6-b454-29388e3e8f20.pdf',
        'da': 'Pollack, Ari(Pillsbury Realty Development).pdf'
    },
    {
        'dn': 'Powers, Gina(American Express)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52784',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/0a4eb1cc-4860-40f4-b092-670c77d1af9d.pdf',
        'da': 'Powers, Gina(American Express).pdf'
    },
    {
        'dn': 'Powers, Gina(American Petroleum Institute)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52785',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/cb0f755f-845c-4dc2-acb6-cb635bcedd63.pdf',
        'da': 'Powers, Gina(American Petroleum Institute).pdf'
    },
    {
        'dn': 'Powers, Gina(Anthem Blue Cross Blue Shield Wellpoint)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52786',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/e916535a-3e32-4bf5-a84e-bd3fe519e759.pdf',
        'da': 'Powers, Gina(Anthem Blue Cross Blue Shield Wellpoint).pdf'
    },
    {
        'dn': 'Powers, Gina(AstraZeneca Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52787',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/886fe95c-f84b-4b42-8e56-023ccd9fbe5b.pdf',
        'da': 'Powers, Gina(AstraZeneca Pharmaceuticals).pdf'
    },
    {
        'dn': 'Powers, Gina(Bedford Ambulatory Surgical Center)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52788',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/da182b12-c1e3-4876-b0f9-f13e3e1d589b.pdf',
        'da': 'Powers, Gina(Bedford Ambulatory Surgical Center).pdf'
    },
    {
        'dn': 'Powers, Gina(Blue Mountain Forest Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52789',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/d6b22f10-9e80-41ea-8d7b-1718040c8631.pdf',
        'da': 'Powers, Gina(Blue Mountain Forest Assoc).pdf'
    },
    {
        'dn': 'Powers, Gina(City of Rochester Wastewater Treatment Plant)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52790',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/868093e6-f50d-4c9b-b85d-1e1b867016de.pdf',
        'da': 'Powers, Gina(City of Rochester Wastewater Treatment Plant).pdf'
    },
    {
        'dn': 'Powers, Gina(Comcast Corp)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52791',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/53e73a27-3055-411e-aad9-d61e0db7740a.pdf',
        'da': 'Powers, Gina(Comcast Corp).pdf'
    },
    {
        'dn': 'Powers, Gina(Correction Corp of America)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52792',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/beb0cca0-72b6-4b58-bd14-2f1a1281fa27.pdf',
        'da': 'Powers, Gina(Correction Corp of America).pdf'
    },
    {
        'dn': 'Powers, Gina(Dartmouth College)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52793',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/ea2ef81f-dac2-41f5-8a4a-6fe8be5871a5.pdf',
        'da': 'Powers, Gina(Dartmouth College).pdf'
    },
    {
        'dn': 'Powers, Gina(Dartmouth Medical School)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52794',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/644fa2e0-8ae6-4c57-bfdb-f47fa2634ea9.pdf',
        'da': 'Powers, Gina(Dartmouth Medical School).pdf'
    },
    {
        'dn': 'Powers, Gina(Explore Informational Serv)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52795',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/e61cdfc6-2ebe-481e-8e8e-c5c16b10c4bd.pdf',
        'da': 'Powers, Gina(Explore Informational Serv).pdf'
    },
    {
        'dn': 'Powers, Gina(Feld Entertainment)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52796',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3ad58eec-bd4f-4a15-85f0-6a611377e9d8.pdf',
        'da': 'Powers, Gina(Feld Entertainment).pdf'
    },
    {
        'dn': 'Powers, Gina(Merck Sharp and Dohme)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52797',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/cb7e246b-9cc8-404b-a7cc-a1c09aa974ec.pdf',
        'da': 'Powers, Gina(Merck Sharp and Dohme).pdf'
    },
    {
        'dn': 'Powers, Gina(N E Medical Equipment Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52798',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/d8bef4f9-cadf-4817-ac00-45153c6ff6ba.pdf',
        'da': 'Powers, Gina(N E Medical Equipment Dealers Assoc).pdf'
    },
    {
        'dn': 'Powers, Gina(N H Credit Union League)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52799',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/8f8db220-7f73-45c5-a4f4-f5395da6a48c.pdf',
        'da': 'Powers, Gina(N H Credit Union League).pdf'
    },
    {
        'dn': 'Powers, Gina(N H Independent Schools)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52800',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/734dc0c0-5a95-451c-9fb3-c37a71d72e80.pdf',
        'da': 'Powers, Gina(N H Independent Schools).pdf'
    },
    {
        'dn': 'Powers, Gina(NH Alliance of Boys and Girls Clubs)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52801',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b01f9fbc-bde2-4b32-b652-c2ff2590ac5d.pdf',
        'da': 'Powers, Gina(NH Alliance of Boys and Girls Clubs).pdf'
    },
    {
        'dn': 'Powers, Gina(Ntl Shooting Sports Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52802',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/82002c56-daf9-4af5-8c75-ceaefa59344d.pdf',
        'da': 'Powers, Gina(Ntl Shooting Sports Foundation).pdf'
    },
    {
        'dn': 'Powers, Gina(Public Service Co of NH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52803',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/0021be48-e92e-403b-bc40-78fa5e984236.pdf',
        'da': 'Powers, Gina(Public Service Co of NH).pdf'
    },
    {
        'dn': 'Powers, Gina(RAI Services Co)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52804',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3ca8e09b-3015-4115-8375-08c02a351e39.pdf',
        'da': 'Powers, Gina(RAI Services Co).pdf'
    },
    {
        'dn': 'Powers, Gina(Rural Hospital Coalition)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52805',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/df0ddd3e-a836-4545-b334-8ad0d89b7538.pdf',
        'da': 'Powers, Gina(Rural Hospital Coalition).pdf'
    },
    {
        'dn': 'Powers, Gina(TracFone Wireless)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52806',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/6172e288-9190-44e4-929e-4521682cccd3.pdf',
        'da': 'Powers, Gina(TracFone Wireless).pdf'
    },
    {
        'dn': 'Powers, Gina(WebMD)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52807',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/697c20ad-661a-4733-b82c-d35da8c9f2ca.pdf',
        'da': 'Powers, Gina(WebMD).pdf'
    },
    {
        'dn': 'Prasol, THomas(America Votes)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52808',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/528dfb09-7d5f-49fd-86c3-29263ae2a659.pdf',
        'da': 'Prasol, THomas(America Votes).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Bank of America)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52809',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/144db4e9-28bb-4015-86e1-240f96ad3f04.pdf',
        'da': 'Prasol, Thomas(Bank of America).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Cannery Casino Resorts)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52810',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/67a49b74-cd68-4538-948d-7351ad9ffa7d.pdf',
        'da': 'Prasol, Thomas(Cannery Casino Resorts).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Centene Corp)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52811',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/d0ac0a37-7b14-475a-908d-23be17287798.pdf',
        'da': 'Prasol, Thomas(Centene Corp).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Comcast)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52812',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/511e5e16-eeb3-4ffc-bfb1-b5cc3658bf87.pdf',
        'da': 'Prasol, Thomas(Comcast).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Consumer Safety Technology)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52813',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3cb2fec1-38dc-4528-9809-d168e00b3b9b.pdf',
        'da': 'Prasol, Thomas(Consumer Safety Technology).pdf'
    },
    {
        'dn': 'Prasol, Thomas(FedEx)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52814',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/68f12596-0aa4-478d-97a6-83804be3bc4b.pdf',
        'da': 'Prasol, Thomas(FedEx).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Heritage Plumbing Heating Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52815',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/9cc097ed-9089-4b42-b95f-09bd423f04ad.pdf',
        'da': 'Prasol, Thomas(Heritage Plumbing Heating Inc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(IBM Corp)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52816',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/c771c96a-b6fc-4e1d-8a9b-dc5bf9a76a31.pdf',
        'da': 'Prasol, Thomas(IBM Corp).pdf'
    },
    {
        'dn': 'Prasol, Thomas(IGT)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52817',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/4dccc7e2-6807-4cac-87ac-a3c5768947f9.pdf',
        'da': 'Prasol, Thomas(IGT).pdf'
    },
    {
        'dn': 'Prasol, Thomas(International Bottled Water Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52818',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/788534ea-c05f-4986-a4cb-f27df5835a76.pdf',
        'da': 'Prasol, Thomas(International Bottled Water Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Mortgage Bankers and Brokers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52819',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3920d5f1-978b-49cf-9eab-b25258bab332.pdf',
        'da': 'Prasol, Thomas(Mortgage Bankers and Brokers Assoc of NH).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Athletic Trainers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52820',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/9486a59d-2710-43fe-990a-77bb8a93284d.pdf',
        'da': 'Prasol, Thomas(NH Athletic Trainers Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Automobile Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52821',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/3160f12e-36b4-4491-8dd0-a7bdde743e19.pdf',
        'da': 'Prasol, Thomas(NH Automobile Dealers Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Coalition for Prosthetics)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52822',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/409bbddd-6fa2-47c5-b6b9-67c83ac2b946.pdf',
        'da': 'Prasol, Thomas(NH Coalition for Prosthetics).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Driver Education Teachers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52823',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/f4b82ab6-cc45-4521-a961-3e43a974fd9e.pdf',
        'da': 'Prasol, Thomas(NH Driver Education Teachers Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Genetic Counselors)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52824',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/81905d10-21c1-42c1-a59c-741ba38c099e.pdf',
        'da': 'Prasol, Thomas(NH Genetic Counselors).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Police Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52825',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/eac7c063-2ac3-498c-af46-99603fb6a54e.pdf',
        'da': 'Prasol, Thomas(NH Police Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Psychological Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52826',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/92df0691-4b9f-46c8-8532-09f56b4e5a02.pdf',
        'da': 'Prasol, Thomas(NH Psychological Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Speech Language and Hearing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52827',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/daf3b9e0-d8f4-4210-9f5e-5eb9cdf84ac7.pdf',
        'da': 'Prasol, Thomas(NH Speech Language and Hearing Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Troopers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52828',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/95da6714-7a3b-4a7f-9b67-143944b5974b.pdf',
        'da': 'Prasol, Thomas(NH Troopers Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(NH Wine and Spirits Brokers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52829',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/a52113ca-2672-4249-ae77-1dca246740fd.pdf',
        'da': 'Prasol, Thomas(NH Wine and Spirits Brokers Assoc).pdf'
    },
    {
        'dn': 'Prasol, Thomas(North Country Environmental Services)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52830',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/95a868b6-484c-4605-8cd1-c25494abd261.pdf',
        'da': 'Prasol, Thomas(North Country Environmental Services).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Optimum Technology)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52831',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/a9f58660-d9b4-40c8-9245-8c1dec90332c.pdf',
        'da': 'Prasol, Thomas(Optimum Technology).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Pfizer)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52832',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/901a43c2-2a9a-4263-9de5-98f8912750d0.pdf',
        'da': 'Prasol, Thomas(Pfizer).pdf'
    },
    {
        'dn': 'Prasol, Thomas(PhRMA)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52833',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/c22b3314-76d8-4271-ab0c-cdd8f89a9642.pdf',
        'da': 'Prasol, Thomas(PhRMA).pdf'
    },
    {
        'dn': 'Prasol, Thomas(Pilot Health LLC)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52834',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/b9111cc1-ed85-4dc3-a741-5e40a1688068.pdf',
        'da': 'Prasol, Thomas(Pilot Health LLC).pdf'
    },
    {
        'dn': 'Prasol, Thomas(PSNH)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52835',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/060b88c2-2cb2-4869-a337-2795eb6d57e9.pdf',
        'da': 'Prasol, Thomas(PSNH).pdf'
    },
    {
        'dn': 'Prasol, Thomas(RAI Services Company)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52836',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/7a23e1f7-db5a-46fb-ba87-754e6ef27784.pdf',
        'da': 'Prasol, Thomas(RAI Services Company).pdf'
    },
    {
        'dn': 'Pujolas, Elizabeth(MedImmune)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52837',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/0dd53818-7518-41f6-aed8-a9654f7fd21d.pdf',
        'da': 'Pujolas, Elizabeth(MedImmune).pdf'
    },
    {
        'dn': 'Quinn, Jack(Allergan Inc)',
        'wp': 'http://sos.nh.gov/Lob012914PQ.aspx?id=52838',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2478/d66f5c32-b44d-4174-8946-53f0e9ca30aa.pdf',
        'da': 'Quinn, Jack(Allergan Inc).pdf'
    },
    {
        'dn': 'Reandeau, Noah(Mylan Inc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52839',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/ee485260-c2f2-4a97-81b6-55f3cf7db73c.pdf',
        'da': 'Reandeau, Noah(Mylan Inc).pdf'
    },
    {
        'dn': 'Reed, George(First Church of Christ Scientist)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52840',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/3c55054b-d64d-4d95-8f83-13c5e1f4e1b3.pdf',
        'da': 'Reed, George(First Church of Christ Scientist).pdf'
    },
    {
        'dn': 'Reid, Barbara(NH Municipal Association)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52841',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/d960c45d-c924-47a7-ba3c-11ce617ef72c.pdf',
        'da': 'Reid, Barbara(NH Municipal Association).pdf'
    },
    {
        'dn': 'Roberts, BethAnn(Harvard Pilgrim Health Care)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=8589936927',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/1c251cb1-be4e-4b0b-a5d4-5fb003fa0b33.pdf',
        'da': 'Roberts, BethAnn(Harvard Pilgrim Health Care).pdf'
    },
    {
        'dn': 'Rogers, Paula(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52842',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/b535e24f-b6f1-4ae1-a39d-2fbf463a3a90.pdf',
        'da': 'Rogers, Paula(Addendum C).pdf'
    },
    {
        'dn': 'Rogers, Paula(Anthem Health Plans in NH)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52843',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/bb5c9d3d-b175-4b59-b82b-5f42054a3f77.pdf',
        'da': 'Rogers, Paula(Anthem Health Plans in NH).pdf'
    },
    {
        'dn': 'Rollo, Michael(ACSCAN)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52844',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/7dbb0bd6-09b6-46ec-95a4-4d33b117c067.pdf',
        'da': 'Rollo, Michael(ACSCAN).pdf'
    },
    {
        'dn': 'Rollo, Michael(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52845',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/68874d10-132f-43b6-a105-3c825baee2b3.pdf',
        'da': 'Rollo, Michael(Addendum C).pdf'
    },
    {
        'dn': 'Rosario, Stephen(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52846',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/baa97431-b4ce-4d49-ac36-e963ed59181b.pdf',
        'da': 'Rosario, Stephen(Addendum C).pdf'
    },
    {
        'dn': 'Rosario, Stephen(American Chemistry Council)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52847',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/7ad00659-4f20-4d7d-85f4-902f8dc8ca6f.pdf',
        'da': 'Rosario, Stephen(American Chemistry Council).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(Catholic Medical Center)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52848',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/dd1836cb-085c-4012-a26f-0923d16bcc14.pdf',
        'da': 'Rosenberger, Teresa(Catholic Medical Center).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(Fairpoint Communications)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52849',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/59b3ca55-ae37-4e81-9448-6c0cfe4b59fd.pdf',
        'da': 'Rosenberger, Teresa(Fairpoint Communications).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(Grocery Manufacturers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52850',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/267a7141-560a-42e9-956a-1afdf0a12a7a.pdf',
        'da': 'Rosenberger, Teresa(Grocery Manufacturers Assoc).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(GS1 Global Public Policy)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52851',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/b67944de-999a-4c55-912f-62050bfc4974.pdf',
        'da': 'Rosenberger, Teresa(GS1 Global Public Policy).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(NH Preservation Alliance)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52852',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/7e1f6983-ec24-4f0a-973b-8d5ac1223824.pdf',
        'da': 'Rosenberger, Teresa(NH Preservation Alliance).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(NH Telephone Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52853',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/733b1339-83fa-4d11-9119-261b40030e76.pdf',
        'da': 'Rosenberger, Teresa(NH Telephone Assoc).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(Rockingham Venture Inc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52854',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/91cbef41-1b6f-4a20-98f7-bb333b2c3f7e.pdf',
        'da': 'Rosenberger, Teresa(Rockingham Venture Inc).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(US Cellular)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52855',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/31de4b56-917c-4bc4-827f-638c1c3cd3b3.pdf',
        'da': 'Rosenberger, Teresa(US Cellular).pdf'
    },
    {
        'dn': 'Rosenberger, Teresa(Yankee Greyhound Racing Inc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52856',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/38ab5cf2-a10a-4102-b6db-c8f68734cd47.pdf',
        'da': 'Rosenberger, Teresa(Yankee Greyhound Racing Inc).pdf'
    },
    {
        'dn': 'Rouse, Marty(Human Rights Campaign)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52857',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/a8f0e2a0-46ef-4ba7-89ab-1766a4a69f81.pdf',
        'da': 'Rouse, Marty(Human Rights Campaign).pdf'
    },
    {
        'dn': 'Roussos, George(American Insurance Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52858',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/b9cc5c4c-bd82-44ff-8f40-c7ac0f2b4bbe.pdf',
        'da': 'Roussos, George(American Insurance Assoc).pdf'
    },
    {
        'dn': 'Roussos, George(Cigna)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52859',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/8334dc91-9ade-40e7-93d2-e133168f15d4.pdf',
        'da': 'Roussos, George(Cigna).pdf'
    },
    {
        'dn': 'Roussos, George(NH Assoc of Domestic Insurance Co)',
        'wp': 'http://sos.nh.gov/Lob012914R.aspx?id=52860',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2471/3508861c-154e-4544-9047-3e4fae68a257.pdf',
        'da': 'Roussos, George(NH Assoc of Domestic Insurance Co).pdf'
    },
    {
        'dn': 'Sadowski, Sarah(New Futures Inc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52861',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/b92d8c2e-8590-4e64-9f68-d612e57b7402.pdf',
        'da': 'Sadowski, Sarah(New Futures Inc).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(Granite State Coalition Against Expansion of Gambling)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52862',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f1dd9b2c-d274-459f-91c7-a827ef9b5e91.pdf',
        'da': 'Sargent, Elizabeth(Granite State Coalition Against Expansion of Gambling).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Academy of Audiology)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52863',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/af7ebbb6-e1c1-4e81-b3a2-5b571c89e3e5.pdf',
        'da': 'Sargent, Elizabeth(NH Academy of Audiology).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Assoc of Chiefs of Police)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52864',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f9d3851e-8111-4233-9786-2328ad7cdc69.pdf',
        'da': 'Sargent, Elizabeth(NH Assoc of Chiefs of Police).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Funeral Directors Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52865',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/cb1bc691-1d8b-40b6-9bb7-1d6d01609d8c.pdf',
        'da': 'Sargent, Elizabeth(NH Funeral Directors Assoc).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Pharmacists Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52866',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/6a929588-6b46-48c1-b043-cb25cc9ea211.pdf',
        'da': 'Sargent, Elizabeth(NH Pharmacists Assoc).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Sheriffs Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52867',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/67fadd21-36bc-4aa6-ac81-63e1abf4242a.pdf',
        'da': 'Sargent, Elizabeth(NH Sheriffs Assoc).pdf'
    },
    {
        'dn': 'Sargent, Elizabeth(NH Society of Health System Pharmacists Inc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52868',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/8b7beed9-b169-43d4-97a0-11aca9bc694b.pdf',
        'da': 'Sargent, Elizabeth(NH Society of Health System Pharmacists Inc).pdf'
    },
    {
        'dn': 'Scarponi, Ellen(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52869',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/410e51b5-e883-47d5-9ffd-50e819275916.pdf',
        'da': 'Scarponi, Ellen(Addendum C).pdf'
    },
    {
        'dn': 'Scarponi, Ellen(Fairpoint Communications)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52870',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/a5621667-7149-494f-97b7-d5592c4ea852.pdf',
        'da': 'Scarponi, Ellen(Fairpoint Communications).pdf'
    },
    {
        'dn': 'Schaier, Scott(Beer Distributors of NH)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52871',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/b89be797-9cf6-4e4d-9805-14f2b766d1de.pdf',
        'da': 'Schaier, Scott(Beer Distributors of NH).pdf'
    },
    {
        'dn': 'Schaier, Scott(Granite State Strategies)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52872',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/cefac723-ec5e-47aa-b916-1f096a50f92d.pdf',
        'da': 'Schaier, Scott(Granite State Strategies).pdf'
    },
    {
        'dn': 'Schmidt, Adam(American Cancer Society Cancer Action Network)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52873',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f4e71433-9e36-4302-9246-a86e4bde6047.pdf',
        'da': 'Schmidt, Adam(American Cancer Society Cancer Action Network).pdf'
    },
    {
        'dn': 'Schmidt, Adam(American Society for the Prevention of Cruelty to Animals)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52874',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/9e8cb7ba-8b87-4e9a-812c-ef69ed012b1a.pdf',
        'da': 'Schmidt, Adam(American Society for the Prevention of Cruelty to Animals).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Bridgewater Power Co)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52875',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/ca8187d6-1237-40e4-805f-6059611390e6.pdf',
        'da': 'Schmidt, Adam(Bridgewater Power Co).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Cisco Systems)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52876',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/124f6221-5fb8-4ddf-9871-cf1e68451299.pdf',
        'da': 'Schmidt, Adam(Cisco Systems).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Coalition of Insurance and Financial Producers)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52877',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/e52e6b2e-75f8-4ab7-82bf-0ab9632a196c.pdf',
        'da': 'Schmidt, Adam(Coalition of Insurance and Financial Producers).pdf'
    },
    {
        'dn': 'Schmidt, Adam(CVS Caremark)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52878',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/5ca26af4-82dd-4be1-a6ba-bcb20158698e.pdf',
        'da': 'Schmidt, Adam(CVS Caremark).pdf'
    },
    {
        'dn': 'Schmidt, Adam(DG Whitefield)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52879',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/bad68ad1-7539-4db8-8189-d4ac8f6b57c8.pdf',
        'da': 'Schmidt, Adam(DG Whitefield).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Focus Technology Solutions)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52880',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/5462dd2a-cfe6-4d3e-a559-152da691b9fd.pdf',
        'da': 'Schmidt, Adam(Focus Technology Solutions).pdf'
    },
    {
        'dn': 'Schmidt, Adam(General Motors)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52881',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/fa12cfe0-7dd3-4f59-9b8b-a36b454e89bd.pdf',
        'da': 'Schmidt, Adam(General Motors).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Indeck Energy Alexandria)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52882',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/5df8e1c7-da72-418b-a6c0-8d7cbd7fadd0.pdf',
        'da': 'Schmidt, Adam(Indeck Energy Alexandria).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Independent Oil Marketers Assoc of N E)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52883',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/bd43609c-a5f5-415c-9e9c-c29d4a2c6ef2.pdf',
        'da': 'Schmidt, Adam(Independent Oil Marketers Assoc of N E).pdf'
    },
    {
        'dn': 'Schmidt, Adam(ISO New England)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52884',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/63b3c2f4-cf98-41a0-86ba-662bb551ac8f.pdf',
        'da': 'Schmidt, Adam(ISO New England).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Lockridge Grindal Nauen)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52885',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/8756f241-ae9a-4b68-bf32-91497be497ce.pdf',
        'da': 'Schmidt, Adam(Lockridge Grindal Nauen).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Assoc of Creditors Rights Atty)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52886',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/4775a0df-127b-4f83-80f3-3157cf53b7b3.pdf',
        'da': 'Schmidt, Adam(NH Assoc of Creditors Rights Atty).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Association of Realtors)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52887',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/2baf8b70-afa0-47e4-a474-7962b8af616d.pdf',
        'da': 'Schmidt, Adam(NH Association of Realtors).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Dental Society)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52888',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/94900f56-68cb-4384-bb05-9e4b832fce9c.pdf',
        'da': 'Schmidt, Adam(NH Dental Society).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Manufactured and Modular Housing Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52889',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/9dad79c8-9843-4cf4-9171-82d293cb5d5c.pdf',
        'da': 'Schmidt, Adam(NH Manufactured and Modular Housing Assoc).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Marine Trades Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52890',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/bb254ff3-8192-4f75-9250-2ef0d4dfb506.pdf',
        'da': 'Schmidt, Adam(NH Marine Trades Assoc).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Psychiatric Society)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52891',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/d1acb629-5bbb-4df7-b9e9-4b853c01c5b1.pdf',
        'da': 'Schmidt, Adam(NH Psychiatric Society).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Snowmobile Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52892',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/44f2aca0-1a4d-42ac-8fd6-4527d90ce38f.pdf',
        'da': 'Schmidt, Adam(NH Snowmobile Assoc).pdf'
    },
    {
        'dn': 'Schmidt, Adam(NH Soft Drink Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52893',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/c03f0ca4-eb45-4f98-b6fb-c441d92ff7be.pdf',
        'da': 'Schmidt, Adam(NH Soft Drink Assoc).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Select Mgmt Resources Loan Max)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52894',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f169a0d7-2b5d-4189-9b48-fc2758bc69bd.pdf',
        'da': 'Schmidt, Adam(Select Mgmt Resources Loan Max).pdf'
    },
    {
        'dn': 'Schmidt, Adam(Springfield Power)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52895',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/9eb55f6d-3d9d-400c-818d-ac60488c8363.pdf',
        'da': 'Schmidt, Adam(Springfield Power).pdf'
    },
    {
        'dn': 'Schmidt, Adam(XTL)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52896',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/456a2019-610e-4b6a-9b30-fa721293c5a7.pdf',
        'da': 'Schmidt, Adam(XTL).pdf'
    },
    {
        'dn': 'Schmidt, Jodi(Elliot Health System)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52897',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/d2416973-6214-46b8-a0f4-1fcde1d93dfd.pdf',
        'da': 'Schmidt, Jodi(Elliot Health System).pdf'
    },
    {
        'dn': 'Schuyler, Stephanye(Unitil Corp)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52898',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/7b00d7b9-bcfd-493a-aa06-db8d7cb2a542.pdf',
        'da': 'Schuyler, Stephanye(Unitil Corp).pdf'
    },
    {
        'dn': 'Serra, Alexandra(Wal Mart Stores)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52899',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/e484c13b-a6f7-445d-b543-217e3ca4936c.pdf',
        'da': 'Serra, Alexandra(Wal Mart Stores).pdf'
    },
    {
        'dn': 'Sexton, Amanda Grady(NH Coalition Against Domestic and Sexual Violence)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52926',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/31ea8e26-b537-4d98-a316-d7d6d5a5befb.pdf',
        'da': 'Sexton, Amanda Grady(NH Coalition Against Domestic and Sexual Violence).pdf'
    },
    {
        'dn': 'Shaffer, Charles(Credit Swisse Mgmt)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52900',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/8916ed33-5f4e-41ff-9cc4-a8c8073d226b.pdf',
        'da': 'Shaffer, Charles(Credit Swisse Mgmt).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52901',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/ab6cf376-707c-445b-8711-0725b4ddd077.pdf',
        'da': 'Shapiro, Lisa(Addendum C).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Aggregate Manufacturers of NH)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52902',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/d15b4c41-4308-4aed-b2e5-1bf9b9009b49.pdf',
        'da': 'Shapiro, Lisa(Aggregate Manufacturers of NH).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Caterpillar Inc Multistate Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52903',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/15c24276-48a7-4b82-a317-da90ba5cd5ba.pdf',
        'da': 'Shapiro, Lisa(Caterpillar Inc Multistate Assoc).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Demoulas Super Markets Inc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52904',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/623a56b1-e780-4478-8e93-2a2d8417c641.pdf',
        'da': 'Shapiro, Lisa(Demoulas Super Markets Inc).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Home Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52905',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/82b919b2-82bd-4d8b-9e17-65b7310fdbcd.pdf',
        'da': 'Shapiro, Lisa(Home Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Motion Picture Assoc of America)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52906',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/826c79b9-870e-4003-a212-7f4095712810.pdf',
        'da': 'Shapiro, Lisa(Motion Picture Assoc of America).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(New Hampshire Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52907',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/c314e242-b717-475a-89ad-ca195189b7c0.pdf',
        'da': 'Shapiro, Lisa(New Hampshire Bankers Assoc).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Northeast Rehabilitation Health Network)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52908',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/b5e2f233-4402-45b5-a54f-0af1181d2d21.pdf',
        'da': 'Shapiro, Lisa(Northeast Rehabilitation Health Network).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Northern Pass Transmission)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52909',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/a5a36464-b42e-47ee-8169-de4032612fe3.pdf',
        'da': 'Shapiro, Lisa(Northern Pass Transmission).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Planned Parenthood of Northern N E)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52910',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/be0fbf32-2e4f-4bc5-9a03-945fef9434ba.pdf',
        'da': 'Shapiro, Lisa(Planned Parenthood of Northern N E).pdf'
    },
    {
        'dn': 'Shapiro, Lisa(Public Service Co of NH)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52911',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/df2956ec-08f5-4d79-b8bf-18ce20d0c0b2.pdf',
        'da': 'Shapiro, Lisa(Public Service Co of NH).pdf'
    },
    {
        'dn': 'Sigel, Richard(Gamma Medica Inc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52912',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/e6b0d81a-1305-438f-b1a1-883fce4bef2e.pdf',
        'da': 'Sigel, Richard(Gamma Medica Inc).pdf'
    },
    {
        'dn': 'Sigel, Richard(Merchants Automotive Group)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52913',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/80ec4df7-e8de-4ca0-bad1-1d2d239b699e.pdf',
        'da': 'Sigel, Richard(Merchants Automotive Group).pdf'
    },
    {
        'dn': 'Sigel, Richard(Well Sense Health Plans)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52914',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/1db41b80-4ca1-4084-98eb-1f1f83815b28.pdf',
        'da': 'Sigel, Richard(Well Sense Health Plans).pdf'
    },
    {
        'dn': 'Silva, Judy(NH Municipal Association)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52915',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/72f74dcb-3bd7-4442-aeed-5ad79e82d2d7.pdf',
        'da': 'Silva, Judy(NH Municipal Association).pdf'
    },
    {
        'dn': 'Simon, Matt(Marijuana Policy Project)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52916',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/0217f880-c451-4b0e-a001-b712fee7bf78.pdf',
        'da': 'Simon, Matt(Marijuana Policy Project).pdf'
    },
    {
        'dn': 'Singerland, Molly(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52917',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/6a349e7f-9e76-493c-92e4-c6e3c388d6b9.pdf',
        'da': 'Singerland, Molly(Addendum C).pdf'
    },
    {
        'dn': 'Skibbie, Michael(Disabilities Rights Center)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52918',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/28b317b9-5de1-4cb5-be52-f45a1d369d7b.pdf',
        'da': 'Skibbie, Michael(Disabilities Rights Center).pdf'
    },
    {
        'dn': 'Smith, Gregory(Securus Technologies Inc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52919',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/a3277980-da2f-4052-ab77-3bf60c9ee434.pdf',
        'da': 'Smith, Gregory(Securus Technologies Inc).pdf'
    },
    {
        'dn': 'Smith, Maureen(Granite Ridge Energy LLC)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52920',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/6be5cad7-61a2-4a1d-9a6c-443e0ed20189.pdf',
        'da': 'Smith, Maureen(Granite Ridge Energy LLC).pdf'
    },
    {
        'dn': 'Smogor, Diane(Breathe NH)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=8589939237',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/9f97454a-a772-4e32-b175-63f76de77de9.pdf',
        'da': 'Smogor, Diane(Breathe NH).pdf'
    },
    {
        'dn': 'Spradling, Scott(International Union of Painters and Allied Trades)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52927',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/bfe4d8f1-98c8-4075-bb0f-f7395ac408e8.pdf',
        'da': 'Spradling, Scott(International Union of Painters and Allied Trades).pdf'
    },
    {
        'dn': 'Spradling, Scott(Millenium Gaming)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52921',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/abd62094-114c-48c4-8ad7-435f75e0fa7d.pdf',
        'da': 'Spradling, Scott(Millenium Gaming).pdf'
    },
    {
        'dn': 'Stadtman, Judy(NH AFL CIO)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52922',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/97727853-36d3-428a-a12c-cbae3284f8d3.pdf',
        'da': 'Stadtman, Judy(NH AFL CIO).pdf'
    },
    {
        'dn': 'Stitzel, Julie(Pew Charitable Trust)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52923',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f960cdb9-95c9-4fc5-b9df-33471b1c9884.pdf',
        'da': 'Stitzel, Julie(Pew Charitable Trust).pdf'
    },
    {
        'dn': 'Stoddard, Kristine(Bi State Primary Care Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52924',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/7334db3b-c07b-468a-8ed0-0de89fee4ead.pdf',
        'da': 'Stoddard, Kristine(Bi State Primary Care Assoc).pdf'
    },
    {
        'dn': 'Sullivan, Christopher(Millenium Gaming)',
        'wp': 'http://sos.nh.gov/Lob012914S.aspx?id=52925',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2472/f2ddc55d-79ae-47e1-89d1-89f366eae87b.pdf',
        'da': 'Sullivan, Christopher(Millenium Gaming).pdf'
    },
    {
        'dn': 'Taylor, Erik(Aggregate Manufacturers of NH)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52928',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/533fba32-c6f2-42d0-9767-628236b4fd5c.pdf',
        'da': 'Taylor, Erik(Aggregate Manufacturers of NH).pdf'
    },
    {
        'dn': 'Taylor, Erik(Home Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52929',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/979721d6-c78d-494b-902e-064c0174eda9.pdf',
        'da': 'Taylor, Erik(Home Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Taylor, Erik(Motion Picture Assoc of America)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52930',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/fbe1a71c-0bcc-48a2-a674-d19a50a1bf29.pdf',
        'da': 'Taylor, Erik(Motion Picture Assoc of America).pdf'
    },
    {
        'dn': 'Taylor, Erik(Northeast Rehabilitation Health Network)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52931',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/b2cdf4b4-daa4-4767-bfd0-bab460ad41d8.pdf',
        'da': 'Taylor, Erik(Northeast Rehabilitation Health Network).pdf'
    },
    {
        'dn': 'Taylor, Erik(Northern Pass Transmission)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52932',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/6225c3bd-d51a-4010-9387-affb74848edb.pdf',
        'da': 'Taylor, Erik(Northern Pass Transmission).pdf'
    },
    {
        'dn': 'Thornton, Christiana(NH Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52933',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/70197649-bc16-4d05-9567-45156b68bee7.pdf',
        'da': 'Thornton, Christiana(NH Bankers Assoc).pdf'
    },
    {
        'dn': 'Tobin, John(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=8589936928',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/3bb47609-2b1d-4e41-89a3-d0b7d15a8510.pdf',
        'da': 'Tobin, John(Addendum C).pdf'
    },
    {
        'dn': 'Tobin, John(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=8589936929',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/ba2b63ae-82df-4f83-9ce4-3ebf9d8e44fa.pdf',
        'da': 'Tobin, John(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'Trachy, Stuart(AT T)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52934',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/4de6757c-6322-4b4d-a6c1-bbbb5abd3470.pdf',
        'da': 'Trachy, Stuart(AT T).pdf'
    },
    {
        'dn': 'Trachy, Stuart(City of Franklin NH)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52935',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/825b3015-d603-40b8-b880-642ba8f23219.pdf',
        'da': 'Trachy, Stuart(City of Franklin NH).pdf'
    },
    {
        'dn': 'Trachy, Stuart(Coalition of NH Chain Drug Stores)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52936',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/960f1383-c1f6-42af-a28b-785e26ddbd88.pdf',
        'da': 'Trachy, Stuart(Coalition of NH Chain Drug Stores).pdf'
    },
    {
        'dn': 'Trachy, Stuart(Enterprise Holdings)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52937',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/93232f33-bc15-49d4-976a-44b1394306a7.pdf',
        'da': 'Trachy, Stuart(Enterprise Holdings).pdf'
    },
    {
        'dn': 'Trachy, Stuart(NH Assoc of Marriage and Family Therapy)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52952',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/ea662d8e-db92-47f2-bcbb-dd6062025b9e.pdf',
        'da': 'Trachy, Stuart(NH Assoc of Marriage and Family Therapy).pdf'
    },
    {
        'dn': 'Trachy, Stuart(NH Chapter Ntl Assoc of Social Workers)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52938',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/88d261d8-6293-4c38-be68-99368ceeeba6.pdf',
        'da': 'Trachy, Stuart(NH Chapter Ntl Assoc of Social Workers).pdf'
    },
    {
        'dn': 'Trachy, Stuart(NH Grocers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52939',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/2c1d1616-17c0-4d53-a160-2dddf29b8b25.pdf',
        'da': 'Trachy, Stuart(NH Grocers Assoc).pdf'
    },
    {
        'dn': 'Trachy, Stuart(NH State Chiropractic Society)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52940',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/f51dabce-547f-40f3-9bd7-5ead5a2427f9.pdf',
        'da': 'Trachy, Stuart(NH State Chiropractic Society).pdf'
    },
    {
        'dn': 'Trachy, Stuart(Wine Institute)',
        'wp': 'http://sos.nh.gov/Lob012914T.aspx?id=52941',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2473/84bd5851-ec7f-43d6-9d2f-aa97d9ef1d7c.pdf',
        'da': 'Trachy, Stuart(Wine Institute).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Biotechnology Industry Organization)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52957',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/66b88fd7-acf9-4ebe-8983-d0c91f0e454c.pdf',
        'da': 'Vanderbeek, Debra(Biotechnology Industry Organization).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Cigar Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52958',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/ca1de4da-82ae-4799-8844-553d3061444e.pdf',
        'da': 'Vanderbeek, Debra(Cigar Assoc of NH).pdf'
    },
    {
        'dn': 'vanderbeek, Debra(Granite State Independent Living)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52959',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/b2a7bbed-2b01-4948-af63-956b442b4b4a.pdf',
        'da': 'vanderbeek, Debra(Granite State Independent Living).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Greenmeadow Golf Club)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52960',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/2037645b-28ef-4da7-8166-afa589ca87c7.pdf',
        'da': 'Vanderbeek, Debra(Greenmeadow Golf Club).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Heritage Case Mgmt)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52961',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/c87322b8-b99e-4202-84f7-3e130600b918.pdf',
        'da': 'Vanderbeek, Debra(Heritage Case Mgmt).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Injured Workers Pharmacy)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52962',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/62f0bcaf-27aa-4f70-8691-c9743e4f6401.pdf',
        'da': 'Vanderbeek, Debra(Injured Workers Pharmacy).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(NH Assoc for Justice)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52963',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/f45a1fb6-e845-4e9d-afbd-c63bb2a4d159.pdf',
        'da': 'Vanderbeek, Debra(NH Assoc for Justice).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(NH Building Officials Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52964',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/3e5e02d8-8900-41ba-93ac-d6812a5edf02.pdf',
        'da': 'Vanderbeek, Debra(NH Building Officials Assoc).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(NH Camp Directors Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52965',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/b3f002a6-8dc0-432c-b132-3368d80ee9f1.pdf',
        'da': 'Vanderbeek, Debra(NH Camp Directors Assoc).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Ntl Assoc of Professional Employer Org)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52966',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/c618589e-0a32-4b5c-9d51-25e4f3330e81.pdf',
        'da': 'Vanderbeek, Debra(Ntl Assoc of Professional Employer Org).pdf'
    },
    {
        'dn': 'Vanderbeek, Debra(Responsible Industry for a Sound Environment)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52967',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/649af7ec-5a7f-4c25-ade0-a52005860757.pdf',
        'da': 'Vanderbeek, Debra(Responsible Industry for a Sound Environment).pdf'
    },
    {
        'dn': 'Vattes, Mark(The College Board)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52968',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/fe977cc2-4c83-47e5-b2e6-46d7aa11116a.pdf',
        'da': 'Vattes, Mark(The College Board).pdf'
    },
    {
        'dn': 'Vaughan, Nancy(American Heart Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=8589939238',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/b44761dd-7308-4b62-8e6c-519dbf353661.pdf',
        'da': 'Vaughan, Nancy(American Heart Assoc).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Eli Lilly and Company)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52969',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/366c3669-7d36-414f-8dda-315eb66e4f42.pdf',
        'da': 'Veilleux, Henry(Eli Lilly and Company).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Entertainment Software Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52970',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/75f42701-99af-42e6-9c83-707abc43e27d.pdf',
        'da': 'Veilleux, Henry(Entertainment Software Assoc).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Fresenius Medical Care)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52971',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/a7ca475c-bd40-462b-a363-0d4242f7e35d.pdf',
        'da': 'Veilleux, Henry(Fresenius Medical Care).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Granite State Alliance of YMCA)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52972',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/b5832e2c-cc6f-4d13-ac30-9a8c20064ebf.pdf',
        'da': 'Veilleux, Henry(Granite State Alliance of YMCA).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Granite State Coalition Against Expansion of Gambling)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52973',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/8965b54e-02bc-4d52-9629-5920cdb79e01.pdf',
        'da': 'Veilleux, Henry(Granite State Coalition Against Expansion of Gambling).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Hosp Corp of America Ports Reg Hosp Parkland Med Center)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52974',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/ae3556f2-9e53-42ce-9ccb-2be4cb940387.pdf',
        'da': 'Veilleux, Henry(Hosp Corp of America Ports Reg Hosp Parkland Med Center).pdf'
    },
    {
        'dn': 'Veilleux, Henry(John Deere)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52975',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/4a88dda2-3fdb-4f75-b6af-059e6bbcf5d2.pdf',
        'da': 'Veilleux, Henry(John Deere).pdf'
    },
    {
        'dn': 'Veilleux, Henry(NH Campground Owners Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52976',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/6bf68b63-fbbe-4f04-a064-104bd9511b18.pdf',
        'da': 'Veilleux, Henry(NH Campground Owners Assoc).pdf'
    },
    {
        'dn': 'Veilleux, Henry(NH Comm Action Prog Soouthern NH Serv Corp)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52977',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/2488c325-d3ae-46c0-8fbc-1d4cc487ed79.pdf',
        'da': 'Veilleux, Henry(NH Comm Action Prog Soouthern NH Serv Corp).pdf'
    },
    {
        'dn': 'Veilleux, Henry(NH Lodging and Restaurant Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52978',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/dea3c7ea-7a52-4929-a15d-e3f72bafcfb5.pdf',
        'da': 'Veilleux, Henry(NH Lodging and Restaurant Assoc).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Ntl Federation of Independent Business)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52979',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/a71d35cd-3549-4def-b19c-01c293d33a0b.pdf',
        'da': 'Veilleux, Henry(Ntl Federation of Independent Business).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Pennichuck Corp)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52980',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/6a7624eb-f614-42c5-99ad-918ee76b8ec0.pdf',
        'da': 'Veilleux, Henry(Pennichuck Corp).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Ski New Hampshire Inc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52981',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/687b1ac0-01a3-4150-a0fc-add7321d4226.pdf',
        'da': 'Veilleux, Henry(Ski New Hampshire Inc).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Waste Mgmt of New Hampshire)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52982',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/0137021c-6142-4ae4-a07c-1996168b9232.pdf',
        'da': 'Veilleux, Henry(Waste Mgmt of New Hampshire).pdf'
    },
    {
        'dn': 'Veilleux, Henry(Wheelabrator Technologies)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52983',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/99e02f24-313b-4920-8655-ee8ee7896476.pdf',
        'da': 'Veilleux, Henry(Wheelabrator Technologies).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52984',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/4d00e28b-a89a-4097-ab9a-fa9e1b543bda.pdf',
        'da': 'Veracco, Kathleen(Addendum C).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Equifax)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52985',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/aa549a76-7146-443d-9422-7981050be879.pdf',
        'da': 'Veracco, Kathleen(Equifax).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Law Warehouses Inc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52986',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/27d9270a-54cf-445d-b23a-ead8f27e57cd.pdf',
        'da': 'Veracco, Kathleen(Law Warehouses Inc).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(National Grid)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52987',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/054119d5-963d-4815-bf04-348ab7a945cf.pdf',
        'da': 'Veracco, Kathleen(National Grid).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(NextEra Energy Seabrook Station)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52988',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/62bcb0a1-1808-4273-84dc-aaeb3bf983d0.pdf',
        'da': 'Veracco, Kathleen(NextEra Energy Seabrook Station).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Pennichuck Corp)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52989',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/3ac1b11d-e773-493f-b658-675822f51f46.pdf',
        'da': 'Veracco, Kathleen(Pennichuck Corp).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Recreation Vehicle Indusrty Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52990',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/fe90785c-a9ea-4de2-9ba1-cb58b1fc8456.pdf',
        'da': 'Veracco, Kathleen(Recreation Vehicle Indusrty Assoc).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(segTEL)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52991',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/4fb3b235-ae8a-492a-a0a4-b07b432785aa.pdf',
        'da': 'Veracco, Kathleen(segTEL).pdf'
    },
    {
        'dn': 'Veracco, Kathleen(Verizon Comm)',
        'wp': 'http://sos.nh.gov/Lob012914UZ.aspx?id=52992',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2479/2e2f8ab4-1853-489e-97e1-37db8d682c9e.pdf',
        'da': 'Veracco, Kathleen(Verizon Comm).pdf'
    },
    {
        'dn': 'Wallace, Gina(N E Medical Equipment Dealers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52993',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/5b739f36-b399-420f-ae84-0a437573c66b.pdf',
        'da': 'Wallace, Gina(N E Medical Equipment Dealers Assoc).pdf'
    },
    {
        'dn': 'Wallace, Glenn(American Express)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52994',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/6f1854a9-3942-4ad8-982b-ef4d9e527b60.pdf',
        'da': 'Wallace, Glenn(American Express).pdf'
    },
    {
        'dn': 'Wallace, Glenn(American Petroleum Institute)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52995',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/37ab444c-8a5b-4f3f-880f-4a90e5a72ebd.pdf',
        'da': 'Wallace, Glenn(American Petroleum Institute).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Anthem Blue Cross Blue Shield Wellpoint)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52996',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/44bd10ae-2075-47d5-afae-adc6a2c80b6e.pdf',
        'da': 'Wallace, Glenn(Anthem Blue Cross Blue Shield Wellpoint).pdf'
    },
    {
        'dn': 'Wallace, Glenn(AstraZeneca Pharmaceuticals)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52997',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/425486c1-e4c1-4640-aeac-c53b42153d95.pdf',
        'da': 'Wallace, Glenn(AstraZeneca Pharmaceuticals).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Bedford Ambulatory Surgical Center)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52998',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/d9bd6147-0723-4fc4-ad71-9cef37d046e1.pdf',
        'da': 'Wallace, Glenn(Bedford Ambulatory Surgical Center).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Blue Mountain Forest Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=52999',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/8fa31afc-ea96-4c6e-b256-279e97de2b01.pdf',
        'da': 'Wallace, Glenn(Blue Mountain Forest Assoc).pdf'
    },
    {
        'dn': 'Wallace, Glenn(City of Rochester Wastewater Treatment Plant)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53000',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/0b21e025-6b41-45f7-bc07-1cdafbe71f8e.pdf',
        'da': 'Wallace, Glenn(City of Rochester Wastewater Treatment Plant).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Comcast Corp)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53001',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/95fce317-d0d7-4756-8878-37561d7acb8b.pdf',
        'da': 'Wallace, Glenn(Comcast Corp).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Correction Corp of America)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53002',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/d7599f37-3568-436b-a62a-2b26f42a3216.pdf',
        'da': 'Wallace, Glenn(Correction Corp of America).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Dartmouth College)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53003',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/705a51eb-16ba-42a2-a1e5-63f5687b91ad.pdf',
        'da': 'Wallace, Glenn(Dartmouth College).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Dartmouth Medical School)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53004',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/5b524eca-d8cf-4a8e-8688-7b84fe43cf4b.pdf',
        'da': 'Wallace, Glenn(Dartmouth Medical School).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Explore Informational Serv)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53005',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/8b19d9db-3e86-4e3d-a556-18d94206bf12.pdf',
        'da': 'Wallace, Glenn(Explore Informational Serv).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Feld Entertainment)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53006',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/71bc9ec4-0221-4070-91f1-aa7dc09bc782.pdf',
        'da': 'Wallace, Glenn(Feld Entertainment).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Merck Sharp and Dohme)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53007',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/aa4d408b-9b45-411d-9c8e-01adda43349e.pdf',
        'da': 'Wallace, Glenn(Merck Sharp and Dohme).pdf'
    },
    {
        'dn': 'Wallace, Glenn(N H Credit Union League)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53008',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/392cb6e6-085d-486c-bb2d-15e4289f2575.pdf',
        'da': 'Wallace, Glenn(N H Credit Union League).pdf'
    },
    {
        'dn': 'Wallace, Glenn(N H Independent Schools)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53009',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/96b01d56-9478-44a0-a42d-5a4b0a96c25e.pdf',
        'da': 'Wallace, Glenn(N H Independent Schools).pdf'
    },
    {
        'dn': 'Wallace, Glenn(NH Alliance of Boys and Girls Clubs)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53010',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/6460f61d-f9cd-4bc9-9ae6-d328785425da.pdf',
        'da': 'Wallace, Glenn(NH Alliance of Boys and Girls Clubs).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Ntl Shooting Sports Foundation)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53011',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/9810187c-993e-466a-830b-1abffea57cc3.pdf',
        'da': 'Wallace, Glenn(Ntl Shooting Sports Foundation).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Public Service Co of NH)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53012',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/093e388a-debc-4f89-9568-44bd81ad5166.pdf',
        'da': 'Wallace, Glenn(Public Service Co of NH).pdf'
    },
    {
        'dn': 'Wallace, Glenn(RAI Services Co)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53013',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/adc4667e-20e1-49d3-9388-405aee58c216.pdf',
        'da': 'Wallace, Glenn(RAI Services Co).pdf'
    },
    {
        'dn': 'Wallace, Glenn(Rural Hospital Coalition)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53014',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/a9c132ea-0403-403e-82b2-8df637e78859.pdf',
        'da': 'Wallace, Glenn(Rural Hospital Coalition).pdf'
    },
    {
        'dn': 'Wangerin, Michelle(New Hampshire Legal Assistance)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=8589936931',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/f28bb00b-be30-45dc-9572-5865164bf2ff.pdf',
        'da': 'Wangerin, Michelle(New Hampshire Legal Assistance).pdf'
    },
    {
        'dn': 'Warbelow, Sarah(Human Rights Campaign)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53015',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/2f281f71-6d35-423f-885e-713f8c46ea44.pdf',
        'da': 'Warbelow, Sarah(Human Rights Campaign).pdf'
    },
    {
        'dn': 'Ward, Jay(SEA SEIU Local 1984)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53016',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/df99d1ec-21a6-485a-82ed-6ba7230479d8.pdf',
        'da': 'Ward, Jay(SEA SEIU Local 1984).pdf'
    },
    {
        'dn': 'Wendelboe, Fran(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53017',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/19bd68e6-ac5f-489e-83f3-6d9e77bc9a5d.pdf',
        'da': 'Wendelboe, Fran(Addendum C).pdf'
    },
    {
        'dn': 'Weston, Maura(Assoc of Equipment Manufacturers)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53018',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/2736f5c1-b907-4468-8aa1-fad7b79e7424.pdf',
        'da': 'Weston, Maura(Assoc of Equipment Manufacturers).pdf'
    },
    {
        'dn': 'Weston, Maura(AT T)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53019',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/6b1459bd-8391-4b0b-a437-194d5d4f7fba.pdf',
        'da': 'Weston, Maura(AT T).pdf'
    },
    {
        'dn': 'Weston, Maura(Concord Regional Solid Waste Resource Recovery)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53020',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/34e9a4da-10cf-4067-8b7f-36b892ccbad4.pdf',
        'da': 'Weston, Maura(Concord Regional Solid Waste Resource Recovery).pdf'
    },
    {
        'dn': 'Weston, Maura(Derry Medical)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53021',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/f0e44d79-f8d3-41fd-83b6-6986cd0b471d.pdf',
        'da': 'Weston, Maura(Derry Medical).pdf'
    },
    {
        'dn': 'Weston, Maura(Maximus)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53022',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/7d849c50-a4d7-4615-a495-72b2521d01ae.pdf',
        'da': 'Weston, Maura(Maximus).pdf'
    },
    {
        'dn': 'Weston, Maura(NE Cable Telecommunications Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53023',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/fbf3a4df-7441-4c1e-8d93-0c917e491142.pdf',
        'da': 'Weston, Maura(NE Cable Telecommunications Assoc).pdf'
    },
    {
        'dn': 'Weston, Maura(Ntl Grayhound Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53024',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/2b18dc79-045b-4737-a029-3314e89cf7ae.pdf',
        'da': 'Weston, Maura(Ntl Grayhound Assoc).pdf'
    },
    {
        'dn': 'White, Josiett(America Votes)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=8589936930',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/32fbbb04-2049-449a-b474-6c8d08aeb971.pdf',
        'da': 'White, Josiett(America Votes).pdf'
    },
    {
        'dn': 'Wood, Leslie(PhRMA)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53025',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/22da5c2b-3099-4981-a7ea-252ccb336301.pdf',
        'da': 'Wood, Leslie(PhRMA).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Addendum C)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53026',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/048f7dba-269c-47ab-bdb5-e91a22ba95d9.pdf',
        'da': 'Worsowicz, Paul(Addendum C).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Aggregate Manufacturers of NH)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53027',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/cb77a7e3-784d-4c21-9de1-b14f685f315b.pdf',
        'da': 'Worsowicz, Paul(Aggregate Manufacturers of NH).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(American Resort Development Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53028',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/c2ed6b3e-7da9-48d0-a536-27dfcf8bba7f.pdf',
        'da': 'Worsowicz, Paul(American Resort Development Assoc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(BJ Alan Company Phantom Fireworks)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53029',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/7f160980-d64c-482e-ba77-ee555dddf546.pdf',
        'da': 'Worsowicz, Paul(BJ Alan Company Phantom Fireworks).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Caterpillar Inc Multistate Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53030',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/1d202f9f-2a43-4e5b-b8bf-07db4574c60e.pdf',
        'da': 'Worsowicz, Paul(Caterpillar Inc Multistate Assoc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Concord Coach Lines)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53031',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/caa18dc0-08e0-416f-a09d-3a4687ebf092.pdf',
        'da': 'Worsowicz, Paul(Concord Coach Lines).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Demoulas Super Markets Inc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53032',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/349cc546-07b8-4e15-9e32-fd53c215a2d7.pdf',
        'da': 'Worsowicz, Paul(Demoulas Super Markets Inc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Granite State Hydropower Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53033',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/d0ac6822-e7aa-44e9-b899-e188fcb4feec.pdf',
        'da': 'Worsowicz, Paul(Granite State Hydropower Assoc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Home Builders and Remodelers Assoc of NH)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53034',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/80b257c8-615a-4913-8e23-9eabbc9ad49b.pdf',
        'da': 'Worsowicz, Paul(Home Builders and Remodelers Assoc of NH).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Jensens Inc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53035',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/a0437fc4-70ae-4be5-bc2d-914316f1fc09.pdf',
        'da': 'Worsowicz, Paul(Jensens Inc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Life Coping)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53036',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/b52953cd-2383-4510-96ee-bdf584248727.pdf',
        'da': 'Worsowicz, Paul(Life Coping).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Motion Picture Assoc of America)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53037',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/fabfed60-2794-4e6f-89fe-401ad2362fa5.pdf',
        'da': 'Worsowicz, Paul(Motion Picture Assoc of America).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(New Hampshire Bankers Assoc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53038',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/e88493e6-f376-4641-93ff-0e8444c5019e.pdf',
        'da': 'Worsowicz, Paul(New Hampshire Bankers Assoc).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Northeast Rehabilitation Health Network)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53039',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/c945ae6d-f30d-4f72-8870-207ea78464a0.pdf',
        'da': 'Worsowicz, Paul(Northeast Rehabilitation Health Network).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Northern Pass Transmission)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53040',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/af9b6144-4a51-4231-a877-138cc5420fc6.pdf',
        'da': 'Worsowicz, Paul(Northern Pass Transmission).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Pillsbury Realty Development)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53041',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/aeb6fbe0-2579-4b66-a5a6-bbc82030fbc9.pdf',
        'da': 'Worsowicz, Paul(Pillsbury Realty Development).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(Planned Parenthood of Northern N E)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53042',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/dfd20976-c34b-4d73-86c0-bb7a94675d61.pdf',
        'da': 'Worsowicz, Paul(Planned Parenthood of Northern N E).pdf'
    },
    {
        'dn': 'Worsowicz, Paul(St Lawrence and Atlantic Railroad)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53043',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/d845f667-458c-4b86-ad3e-9b21134b6041.pdf',
        'da': 'Worsowicz, Paul(St Lawrence and Atlantic Railroad).pdf'
    },
    {
        'dn': 'Wu, Janson(Park Square Advocates)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53044',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/2c075d67-ee96-4940-9df1-08fb92f8fa53.pdf',
        'da': 'Wu, Janson(Park Square Advocates).pdf'
    },
    {
        'dn': 'Zeytoonjian, Fred(Apple Inc)',
        'wp': 'http://sos.nh.gov/Lob012914WZ.aspx?id=53045',
        'oa': 'http://sos.nh.gov/assets/0/103/105/1601/1922/2129/2460/2480/792e0f90-4a61-47cd-983e-52bdd2743c53.pdf',
        'da': 'Zeytoonjian, Fred(Apple Inc).pdf'
    }
)

"""
Addendum A - Page 1
X,Y Coordinates of Dollar amounts on the page

IV. Fees Received
a) <span class='ocrx_word' id='word_1_146' title='bbox 2059 1407 2219 1442; x_wconf 87' lang='eng'><strong>15,000.00</strong></span>
b) <span class='ocrx_word' id='word_1_175' title='bbox 2053 1553 2219 1586; x_wconf 79' lang='eng'><strong>45,300.00</strong></span>
c) <span class='ocrx_word' id='word_1_191' title='bbox 2055 1700 2219 1735; x_wconf 90' lang='eng'><strong>60,300.00</strong></span>
d) <span class='ocrx_word' id='word_1_211' title='bbox 2077 1846 2220 1881; x_wconf 89' lang='eng'><strong>5,000.00</strong></span>

V. Expenses
a) <span class='ocrx_word' id='word_1_479' title='bbox 2014 2809 2173 2843; x_wconf 91' lang='eng'><strong>15,000.00</strong></span>
b) <span class='ocrx_word' id='word_1_499' title='bbox 2127 2955 2174 2984; x_wconf 91' lang='eng'><strong>.00</strong></span>
c) <span class='ocrx_word' id='word_1_514' title='bbox 2127 3053 2174 3082; x_wconf 94' lang='eng'><strong>.00</strong></span>
"""

"""
Commands and their Params

pdftoppm -f 1 -l 1 -r 300 -gray SOME.pdf RESULT

    -gray creates gray scaled image with a .pgm extension; without -gray it defaults to color with a .ppm extension

unpaper --dpi 300 --mask-scan-size 100 --no-deskew --no-grayfilter --no-blackfilter --no-mask-center
    --no-border-align SOURCE.pgm TARGET.pgm

unpaper --dpi 300 --mask-scan-size 100 --no-border-align AAA BBB

unpaper -vv --pre-border 100,200,100,100 --deskew-scan-depth 1 --deskew-scan-direction left,top,bottom --deskew-scan-step 0.01 [SOURCE].pgm [TARGET].pgm

tesseract IMAGE OUTPUT -l eng [hocr] [myconfig1]

'pnmtopng', '-compression', '9', 'wor-1.pgm', '>', 'wor-1.png'

"""

# TODO: move to util package
box_pattern = re.compile('bbox((\s+\d+){4})')


def element_coordinates(element):
    out = (0, 0, 0, 0)
    if 'title' in element.attrib:
        matches = box_pattern.search(element.attrib['title'])
        if matches:
            coords = matches.group(1).split()
            out = (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
    return out


"""
Base all paths on project_dir. And project_dir is a fully qualified path.
"""
project_dir = os.path.normpath(os.path.join(os.getcwd(), '..'))

pdf_base_dir = os.path.join(project_dir, 'reports/dist/lobbyists-2013-original')
extract_base_dir = os.path.join(project_dir, 'reports/dist/extract')
csv_output_filename = os.path.join(extract_base_dir, 'lobbyist-2013-extract.csv')

# Give each entry an index number
dei = zip(range(0, len(de)), de)
print 'Number of reports', len(dei)
print 'Local PDFs', len(os.listdir(pdf_base_dir))
with open(csv_output_filename, 'ab') as ofile:
    csv_column_names = ('row-num', 'message', 'page-count', 'display-name', 'web-page', 'original-asset')
    csv_writer = csv.DictWriter(ofile, csv_column_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    csv_writer.writeheader()
    csv_blank_tuple = (None, None, None, None, None, None)
    csv_row = dict(zip(csv_column_names, csv_blank_tuple))
    for de in dei[:]:
        if csv_row['row-num'] is not None:
            csv_writer.writerow(csv_row)
        row_num = de[0]
        e = de[1]
        csv_row = dict(zip(csv_column_names, (row_num, None, None, e['dn'], e['wp'], e['oa'])))
        pdf_file = os.path.join(pdf_base_dir, e['da'])
        main_loop_tag = '{0}] pdf({1})'.format(row_num, e['da'])
        if os.path.isfile(pdf_file):
            print '{0} Starting analysis: {1}'.format(main_loop_tag, pdf_file)
        else:
            csv_row['message'] = '{0} Local PDF not found'.format(main_loop_tag)
            print '{0} file: {1}'.format(csv_row['message'], pdf_file)
            continue
        row_num_padded = '{0:0>4}'.format(row_num)
        work_dir = os.path.join(extract_base_dir, row_num_padded)
        while os.path.exists(work_dir):
            temp = work_dir.rsplit(row_num_padded, 1)
            if temp[1] == '':
                n = 0
            else:
                n = int(temp[1].split('_', 1)) + 1
            work_dir = os.path.join(extract_base_dir, '{0}_{1}'.format(row_num_padded, n))
        if not os.path.isdir(work_dir):
            os.mkdir(work_dir)
        ppm_ext = '.pgm'
        pdf_to_image_cmd = ['pdftoppm', '-r', '300', '-gray', pdf_file, 'page']
        # pdf_to_image_cmd = ['pdftoppm', '-f', '1', '-l', '3', '-r', '300', '-gray', pdf_file, 'page']
        result_code = subprocess.call(pdf_to_image_cmd, cwd=work_dir)
        if 0 != result_code:
            csv_row['message'] = '{0} Error extracting images. Command {1} returned error code {2}'.format(
                main_loop_tag, pdf_to_image_cmd[0], result_code)
            print '{0} cmd: {1}'.format(csv_row['message'], pdf_to_image_cmd)
            continue
        csv_row['page-count'] = len(os.listdir(work_dir))
        print '{0} {1} image files extracted'.format(main_loop_tag, csv_row['page-count'])
        # TODO: factor out into option
        # Only process report with 3 pages
        if csv_row['page-count'] != 3:
            print "{0} skipping report because there aren't 3 pages".format(main_loop_tag)
            # clean up
            for f in os.listdir(work_dir):
                os.unlink(os.path.join(work_dir, f))
            os.rmdir(work_dir)
            continue
        for f in os.listdir(work_dir):
            temp = f.rsplit(ppm_ext, 1)
            if len(temp) != 2 or temp[1] != '':
                continue
            file_stem = temp[0]
            clean_file_stem = file_stem + '_clean'
            clean_file_name = clean_file_stem + ppm_ext
            print '{0} Cleaning {1} to {2}'.format(main_loop_tag, f, clean_file_name)
            clean_cmd = ['unpaper', '-v', '--pre-border', '100,120,70,70', '--mask', '50,50,2500,3250', '--deskew-scan-size', '2100', '--deskew-scan-depth', '0.9', '--deskew-scan-direction', 'left',
                         '--deskew-scan-step', '0.01', os.path.join(work_dir, f), os.path.join(work_dir, clean_file_name)]
            # clean_cmd = ['unpaper', '-vv', '--dpi', '300', '--mask-scan-size', '100', '--no-border-align', os.path.join(work_dir, f), os.path.join(work_dir, clean_file_name)]
            result_code = subprocess.call(clean_cmd, cwd=work_dir)
            if 0 != result_code:
                csv_row['message'] = '{0} Error cleaning image. Command {1} returned error code {2}'.format(main_loop_tag, clean_cmd[0], result_code)
                print '{0} cmd: {1}'.format(csv_row['message'], clean_cmd)
                continue
            ocr_cmd = ['tesseract', os.path.join(work_dir, clean_file_name), clean_file_stem, '-l', 'eng', 'hocr', 'pdfgeneral']
            result_code = subprocess.call(ocr_cmd, cwd=work_dir)
            if 0 != result_code:
                csv_row['message'] = '{0} Error during OCR of image {1}. Command {2} returned error code {3}'.format(main_loop_tag, f, ocr_cmd[0], result_code)
                print '{0} cmd: {1}'.format(csv_row['message'], clean_cmd)
                continue
            ocr_cmd = ['tesseract', os.path.join(work_dir, clean_file_name), clean_file_stem + 'p', '-l', 'eng', 'pdfgeneral']
            result_code = subprocess.call(ocr_cmd, cwd=work_dir)
            if 0 != result_code:
                csv_row['message'] = '{0} Error during OCR of image {1}. Command {2} returned error code {3}'.format(main_loop_tag, f, ocr_cmd[0], result_code)
                print '{0} cmd: {1}'.format(csv_row['message'], clean_cmd)
                continue
                # ocr_cmd = ['tesseract', os.path.join(work_dir, clean_file_name), clean_file_stem + 'd', '-l', 'eng', 'myconfigd']
                # result_code = subprocess.call(ocr_cmd, cwd=work_dir)
                # if 0 != result_code:
                # csv_row['message'] = '{0} Error during OCR of image {1}. Command {2} returned error code {3}'.format(
                # main_loop_tag, f, ocr_cmd[0], result_code)
                #     print '{0} cmd: {1}'.format(csv_row['message'], clean_cmd)
                #     continue

        # Convert images to PNGs
        # TODO: factor out into method
        for f in os.listdir(work_dir):
            temp = f.rsplit(ppm_ext, 1)
            if len(temp) != 2 or temp[1] != '':
                continue
            file_stem = temp[0]
            convert_cmd = ['pnmtopng', '-compression', '9', f]
            with open(os.path.join(work_dir, '{0}.png'.format(file_stem)), 'wb') as ostream:
                result_code = subprocess.call(convert_cmd, cwd=work_dir, stdout=ostream)
            if 0 != result_code:
                csv_row['message'] = '{0} Error during convert to png {1}. Command {2} returned error code {3}'.format(main_loop_tag, f, convert_cmd[0], result_code)
                print '{0} cmd: {1}'.format(csv_row['message'], clean_cmd)
            else:
                os.unlink(os.path.join(work_dir, f))

        csv_row['message'] = 'OK'
        csv_writer.writerow(csv_row)
        csv_row = dict(zip(csv_column_names, csv_blank_tuple))
