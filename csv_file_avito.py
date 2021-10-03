import re
import time
from typing import Dict
import datetime
import requests
from bs4 import BeautifulSoup
import json
import csv
from random import choice
from random import uniform
count11 = 1
# num_room = int(input('Input number room = '))
num_range = int(input('Input number page parsing - '))
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
adress_region = 'Астраханская область' #str(input('Введите область поиска - '))
adress_city = 'Астрахань' #str(input('Введите город поиска - '))
adress_district = ''

count_flat_0 = 1
dict_chief = []
for i in range(num_range):
    n_page = count11
    # with open('href_cian_ru.json', encoding= 'utf-8') as file:
    #     prep_file_json = json.load(file)
    # with open(rf'C:\Python mini\venv\data_cian_2_room\7_7 страница_cian_ru.html', encoding='utf-8') as file:
    #                                                                                1_1 страница_AVITO_ru_2021-10-03
    #                                                                                1_1 страница_AVITO_ru2021-10-03 {parsing_day}
    with open(fr'C:\Python mini\venv\data_avito\{count11}_{count11} страница_AVITO_ru_{parsing_day}.html', encoding='utf-8') as file: #, encoding='utf-8'
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    block_item = soup.find_all('div', class_='index-root-KVurS')
    count1 = 1
    # keys = ['id_flat', 'name_flat', 'href_flat', 'adress_flat', 'price_all', 'price_per_metr', 'Saller', 'Saller href', 'subscribe_flat']
    keys = ['parsing_day', 'n_page', 'time_output_ad', 'type_of_ad', 'id_flat', 'type_of_flat', 'name_flat', 'href_flat', 'num_room',
            'squere_flat', 'price_all', 'price_per_metr', 'adress_flat', 'adress_area', 'adress_street', 'adress_build', 'saller', 'saller_agency',
            'href_saller_agency', 'num_floor', 'house_floor', 'num_of_entry', 'squere_flat_excel', 'price_per_metr_excel', 'subscribe_flat', 'period_time', 'adress_region', 'adress_city', 'adress_district']
    
    for item in block_item:
        block_name = soup.find_all('div', class_='iva-item-content-UnQQ4')           #'iva-item-root-Nj_hb photo-slider-slider-_PvpN iva-item-list-H_dpX iva-item-redesign-nV4C4 iva-item-responsive-gIKjW items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum'
        block_name1 = soup.find_all('div', class_='iva-item-root-Nj_hb photo-slider-slider-_PvpN iva-item-gallery-C2rIq iva-item-redesign-nV4C4 iva-item-responsive-gIKjW items-item-My3ih items-galleryItem-_KQnH js-catalog-item-enum')
        count_flat = 1
        
        for item_block_name in block_name:   # это блок для ВСЕХ объявлений!!!!!!!
            
            time_output_ad = item_block_name.find('div', class_='date-text-VwmJG text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs').text
            if item_block_name.find('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes'):
                href_flat = 'https://www.avito.ru' + item_block_name.find('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes').get('href')
            else:
                href_flat = 'None'
            id_flat = item_block_name.get('id')
            type_of_flat = 'plain'
            if item_block_name.find('h3', class_='title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL text-bold-SinUO'):
                type_of_ad = 'regular ad'
                name_flat = item_block_name.find('h3', class_='title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text.replace(u'квартира,', u'квартира;').replace(u'м²,', u'м²;')
                name_flat = name_flat.replace('апартаменты,', 'апартаменты;')
                name_flat2 = name_flat.replace(' ', '')
                name_flat1 = name_flat.split(';')
                num_room = name_flat1[0]
                squere_flat = float(name_flat1[1].replace(' м²', '').replace(' м²', '').replace(',', '.').replace(u'\xa0', ''))
                price_all = item_block_name.find('span', class_='price-text-E1Y7h text-text-LurtD text-size-s-BxGpL').text.replace(' ₽', '').replace(' ', '')
                price_per_metr = round(int(price_all) / squere_flat, 3)
                num_floor = name_flat1[2].replace(' ', '').replace(' ', '').replace('эт.', '').split('/')[0]
                house_floor = name_flat1[2].replace(' ', '').replace(' ', '').replace('эт.', '').split('/')[1]
            elif item_block_name.find('h3', class_='title-root-j7cja iva-item-title-_qCwt title-large-XIHQQ title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL text-bold-SinUO'):
                # VIP ADS
                type_of_ad = 'VIP ad'
                name_flat = item_block_name.find('h3', class_='title-root-j7cja iva-item-title-_qCwt title-large-XIHQQ title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text.replace(u'квартира,', u'квартира;').replace(u'м²,', u'м²;')
                name_flat = name_flat.replace('апартаменты,', 'апартаменты;')
                name_flat2 = name_flat.replace(' ', '')
                name_flat1 = name_flat.split(';')
                num_room = name_flat1[0]
                squere_flat = float(name_flat1[1].replace(' м²', '').replace(' м²', '').replace(',', '.').replace(u'\xa0', ''))
                price_all = item_block_name.find('span', class_='price-text-E1Y7h text-text-LurtD text-size-s-BxGpL').text.replace(' ₽', '').replace(
                    ' ', '')
                price_per_metr = round(int(price_all) / squere_flat, 3)
                num_floor = name_flat1[2].replace(' ', '').replace(' ', '').replace('эт.', '').split('/')[0]
                house_floor = name_flat1[2].replace(' ', '').replace(' ', '').replace('эт.', '').split('/')[1]

            adress_flat = item_block_name.find('span', class_='geo-address-QTv9k text-text-LurtD text-size-s-BxGpL').text
            if len(adress_flat.split(',')) == 2:  # 1. разделение адреса на район, улицу и дом
                adress_area = 'None'
                adress_street = adress_flat.split(',')[0].strip()
                adress_build = adress_flat.split(',')[1].strip()
            elif len(adress_flat.split(',')) == 3:
                adress_area = adress_flat.split(',')[0].strip()
                adress_street = adress_flat.split(',')[1].strip()
                adress_build = adress_flat.split(',')[2].strip()
            else:
                adress_area = 'None'
                adress_street = 'None'
                adress_build = 'None'
                
            saller2 = item_block_name.find_all('a', class_='link-link-MbQDP link-design-inherited-Ys4mw link-novisited-UCnee')  # новые имена владельца
            saller3 = item_block_name.find_all('span', class_='iva-item-text-_s_vh iva-item-textColor-gray44-Fq8XF text-text-LurtD text-size-s-BxGpL')
            # print('name_flat - ', name_flat)
            lst_saller2 = []
            lst_saller3 =[]
            for i in saller2:
                lst_saller2.append(i.text)
                href_saller_agency2 = 'https://www.avito.ru' + str(i.get('href'))
                # print('saller2', 'iterator - ', 'text  -', i.text, 'HREF', href_saller_agency, type(href_saller_agency))
            for i in saller3:
                lst_saller3.append(i.text)
                href_saller_agency3 = 'https://www.avito.ru' + str(i.get('href'))
                # print('saller3 ', 'iterator -', i.text, 'HREF', href_saller_agency, type(href_saller_agency))
            count_saller2, count_saller3 = len(lst_saller2), len(lst_saller3)
            if count_saller2 == 0 and count_saller3 == 0:
                saller = 'VIP ad'
                saller_agency = 'None - VIP ad'
                href_saller_agency = 'None - VIP ad'
                period_time = 'None - VIP ad'
                id_flat = 'None'
            elif count_saller2 == 0 and count_saller3 == 2:
                saller = lst_saller3[0]
                saller_agency = lst_saller3[0]
                href_saller_agency = 'None Агентство не определено - раскрывается в объявлении'
                period_time = lst_saller3[1]
                id_flat = href_flat[href_flat.find('et._')+4:]
            elif count_saller2 == 1 and count_saller3 == 1:
                saller = lst_saller2[0]
                saller_agency = lst_saller2[0]
                href_saller_agency = href_saller_agency2
                period_time = lst_saller3[0]
                id_flat = href_flat[href_flat.find('et._')+4:]
            elif count_saller2 == 1 and count_saller3 == 2:
                saller = lst_saller2[0]
                saller_agency = lst_saller3[0]
                href_saller_agency = href_saller_agency2
                period_time = lst_saller3[1]
                id_flat = href_flat[href_flat.find('et._')+4:]
            if item_block_name.find('div', class_='iva-item-text-_s_vh iva-item-description-S2pXQ text-text-LurtD text-size-s-BxGpL'):
                subscribe_flat = item_block_name.find('div', class_='iva-item-text-_s_vh iva-item-description-S2pXQ text-text-LurtD text-size-s-BxGpL').text
            # print('subscribe - ', subscribe_flat)
            # print(href_flat, id_flat)
            # print('saller - ',saller, ' ==', 'saller agency - ', saller_agency, 'href agency - ', href_saller_agency, period_time)
            # print(count_saller2, ' - ', count_saller3)
            print(' ------------------------------- ')
        
            num_of_entry = 1
            squere_flat_excel = str(squere_flat).replace('.', ',')
            price_per_metr_excel = str(price_per_metr).replace('.', ',')
            values = [parsing_day, n_page, time_output_ad, type_of_ad, id_flat, type_of_flat, name_flat2, href_flat, num_room, squere_flat,
                      price_all, price_per_metr, adress_flat, adress_area, adress_street, adress_build, saller, saller_agency, href_saller_agency,
                      num_floor, house_floor, num_of_entry, squere_flat_excel, price_per_metr_excel, subscribe_flat, period_time, adress_region, adress_city, adress_district]
            count_flat += 1
            dict1 = {x: y for x, y in zip(keys, values)}
            count_flat_0 += 1
            dict_chief.append(dict1)
            # print(values)
            
    print('Ends of - page # :', count11)
    count11 += 1
    print(' --------------------------------------------')
# print('D I C T --------------', dict_chief)
    #
with open(fr'csv_AVITO_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = ['parsing_day', 'n_page', 'time_output_ad', 'type_of_ad', 'id_flat', 'type_of_flat', 'name_flat', 'href_flat', 'num_room',
            'squere_flat', 'price_all', 'price_per_metr', 'adress_flat', 'adress_area', 'adress_street', 'adress_build', 'saller', 'saller_agency',
            'href_saller_agency', 'num_floor', 'house_floor', 'num_of_entry', 'squere_flat_excel', 'price_per_metr_excel', 'subscribe_flat', 'period_time', 'adress_region', 'adress_city', 'adress_district']
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




