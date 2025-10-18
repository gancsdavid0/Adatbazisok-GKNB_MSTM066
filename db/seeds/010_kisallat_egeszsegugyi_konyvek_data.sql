INSERT INTO kisallat_egeszsegugyi_konyvek (id, allatok_id, befogadhato_allatok_id, szuletesei_datum, nev, ivar, suly,
                                           meret, ivartalanitva, szin, egeszsegi_allapot, mikrochip_szama)
VALUES (1, 1, 1, '2022-05-01', 'Buksi', 'kan', 8.5, 'kicsi', 1, 'barna', 'egészséges', 900112000123456),
       (2, 2, 6, '2020-10-10', 'Rex', 'kan', 32.0, 'nagy', 0, 'fekete', 'enyhe csípődiszplázia', 900112000123457),
       (3, 3, 5, NULL, 'Csőri', 'hím', 0.1, 'kicsi', 0, 'sárga', 'egészséges', NULL),
       (4, 4, 2, '2021-08-20', 'Cirmi', 'nőstény', 4.2, 'közepes', 1, 'cirmos', 'egészséges', 900112000123458),
       (5, 5, 3, '2022-11-30', 'Gombóc', 'hím', 0.05, 'kicsi', 0, 'arany', 'egészséges', NULL);
