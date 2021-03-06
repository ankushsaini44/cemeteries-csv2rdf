#!/usr/bin/env python3
#  -*- coding: UTF-8 -*-
"""
Mapping of CSV columns to RDF properties
"""

from converters import add_trailing_zeros, parse_coordinate, split_cemetery_name
from namespaces import *

CEMETERY_MAPPING = {
    'onko': {'uri': SCHEMA_NS.status,
             'name_fi': 'Onko hautausmaa'},
    'tyyppi': {'uri': SCHEMA_NS.cemetery_type,
               'name_fi': 'Hautausmaan tyyppi',
               'name_en': 'Cemetery type'},
    'nro': {'uri': SCHEMA_NS.cemetery_id,
            'converter': add_trailing_zeros,
            'name_fi': 'Hautausmaan tunniste',
            'name_en': 'Cemetery identifier'},
    'nykyiset_kunnat': {'uri': SCHEMA_NS.narc_name,
                        'uri2': SCHEMA_NS.current_municipality,
                        'uri3': SCHEMA_NS.former_municipality,
                        'converter': split_cemetery_name,
                        'name_fi': 'Hautausmaan nimi tai paikkakunta Kansallisarkiston 90-luvun listauksessa',
                        'name2_fi': 'Nykyinen kunta',
                        'name3_fi': 'Entinen kunta',
                        'name_en':  'Name from National Archives\' data',
                        'name2_en': 'Current municipality',
                        'name3_en': 'Former kunta'},
    'kuva_1_yleiskuva_sankarihautausmaasta': {'uri': SCHEMA_NS.photograph_1,
                                              'name_fi': 'Valokuva 1',
                                              'name_en': 'Photograph 1'},
    'kuva_1_kuvaajan_nimi': {'uri': SCHEMA_NS.photographer_1,
                             'name_fi': 'Kuvaaja 1',
                             'name_en': 'Photographer 1'},
    'kuva_2_yksittäinen_hauta_risteineen_muistolaattoineen': {'uri': SCHEMA_NS.photograph_2,
                                                              'name_fi': 'Valokuva 2',
                                                              'name_en': 'Photograph 2'},
    'kuva_2_kuvaajan_nimi': {'uri': SCHEMA_NS.photographer_2,
                             'name_fi': 'Kuvaaja 2',
                             'name_en': 'Photographer 2'},
    'kuva_3_muistomerkki': {'uri': SCHEMA_NS.photograph_3,
                            'name_fi': 'Valokuva 3',
                            'name_en': 'Photograph 3'},
    'kuva_3_kuvaajan_nimi': {'uri': SCHEMA_NS.photographer_3,
                             'name_fi': 'Kuvaaja 3',
                             'name_en': 'Photographer 3'},
    'kuva_4_yleiskuva': {'uri': SCHEMA_NS.photograph_4,
                                                'name_fi': 'Valokuva 4',
                                                'name_en': 'Photograph 4'},
    'kuva_4_kuvaajan_nimi': {'uri': SCHEMA_NS.photographer_4,
                             'name_fi': 'Kuvaaja 4',
                             'name_en': 'Photographer 4'},
    'kuva_5_muu_muistomerkki': {'uri': SCHEMA_NS.photograph_5,
                                 'name_fi': 'Valokuva 5',
                                 'name_en': 'Photograph 5'},
    'kuva_5_kuvaajan_nimi': {'uri': SCHEMA_NS.photographer_5,
                             'name_fi': 'Kuvaaja 5',
                             'name_en': 'Photographer 5'},
    'kuvaukset_toteuttanut_kameraseura': {'uri': SCHEMA_NS.camera_club,
                                          'name_fi': 'Kuvaukset toteuttanut kameraseura',
                                          'name_en': 'Camera club'},
    'hautausmaan_nimi': {'uri': SKOS.prefLabel},
    'arkkitehti': {'uri': SCHEMA_NS.architect,
                   'name_fi': 'Arkkitehti',
                   'name_en': 'Architect'},
    'hautoja': {'uri': SCHEMA_NS.number_of_graves,
                   'name_fi': 'Hautojen lukumäärä',
                   'name_en': 'Number of graves'},
    'perustettu': {'uri': SCHEMA_NS.date_of_foundation,
                   'name_fi': 'Perustamisvuosi',
                   'name_en': 'Date of foundation'},
    'paljastettu': {'uri': SCHEMA_NS.memorial_unveiling_date,
                   'name_fi': 'Muistimerkin paljastamisaika',
                   'name_en': 'Memorial unveiling date'},
    'nimi': {'uri': SCHEMA_NS.memorial,
                   'name_fi': 'Muistomerkin nimi',
                   'name_en': 'Memorial'},
    'kuvanveistäjä': {'uri': SCHEMA_NS.memorial_sculptor,
                   'name_fi': 'Kuvanveistäjä',
                   'name_en': 'Sculptor'},
    'pituus_n': {'uri': WGS84.lat,
                 'converter': parse_coordinate},
    'leveys_e': {'uri': WGS84.long,
                 'converter': parse_coordinate},
    'tarkka_katuosoite': {'uri': SCHEMA_NS.address,
                   'name_fi': 'Osoite',
                   'name_en': 'Address'},
}
