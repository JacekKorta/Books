    
class MockResponse:
    
    def __init__(self):
        self.status_code = 200
        
    def json(self):
        return {
                "kind": "books#volumes",
                "totalItems": 596,
                "items": [
                    {
                        "kind": "books#volume",
                        "id": "sqRHAQAAMAAJ",
                        "etag": "BXfc3KmcvmQ",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/sqRHAQAAMAAJ",
                        "volumeInfo": {
                            "title": "War Information Series",
                            "authors": [
                                "United States. Committee on Public Information"
                            ],
                            "publishedDate": "1918",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "MINN:319510022616147"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "categories": [
                                "World War, 1914-1918"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.0.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=sqRHAQAAMAAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=sqRHAQAAMAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=sqRHAQAAMAAJ&pg=PA2&dq=war&hl=&cd=1&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=sqRHAQAAMAAJ&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=sqRHAQAAMAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=sqRHAQAAMAAJ&rdid=book-sqRHAQAAMAAJ&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/War_Information_Series.epub?id=sqRHAQAAMAAJ&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=sqRHAQAAMAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "PUBLICATIONS OF THE COMMITTEE 61 pages 32 pages 16 pages 16 pages <br>\n22 pages Titles marked with a star ( * ) are of especial value in the study of the <br>\n<b>war</b> and are frequently referred to in this outline . I. RED WHITE AND BLUE <br>\nSERIES&nbsp;..."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "kxOAhtU27hgC",
                        "etag": "1Bz2PZ8+/c4",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/kxOAhtU27hgC",
                        "volumeInfo": {
                            "title": "Handbook on Education and the War",
                            "subtitle": "Based on Proceedings of the National Institute on Education and the War, Sponsored by the U. S. Office of Education Wartime Commission at American University, Washington, D. C., August 28 Through 31, 1942. Federal Security Agency. U. S. Office of Education",
                            "authors": [
                                "National Institute on Education and the War",
                                "National institute on education and the war, Washington, D. C., 1942"
                            ],
                            "publishedDate": "1943",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "UIUC:30112074907053"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "pageCount": 344,
                            "printType": "BOOK",
                            "categories": [
                                "Education"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.0.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=kxOAhtU27hgC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=kxOAhtU27hgC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=kxOAhtU27hgC&pg=PA334&dq=war&hl=&cd=2&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=kxOAhtU27hgC&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=kxOAhtU27hgC"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=kxOAhtU27hgC&rdid=book-kxOAhtU27hgC&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/Handbook_on_Education_and_the_War.epub?id=kxOAhtU27hgC&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=kxOAhtU27hgC&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Based on Proceedings of the National Institute on Education and the <b>War</b>, <br>\nSponsored by the U. S. Office of Education Wartime Commission at American <br>\nUniversity, Washington, D. C., August 28 Through 31, 1942. Federal Security <br>\nAgency."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "K0xIAAAAYAAJ",
                        "etag": "x7oDcSD2isY",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/K0xIAAAAYAAJ",
                        "volumeInfo": {
                            "title": "War Expenditures",
                            "subtitle": "Hearings Before Subcommittee No. 5 (ordnance) ... Sixty-sixth Congress ... on War Expenditures ... Serial 6",
                            "authors": [
                                "United States. Congress. House. Select Committee on Expenditures in the War Department"
                            ],
                            "publishedDate": "1921",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "COLUMBIA:CU09374310"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "categories": [
                                "World War, 1914-1918"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.2.3.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=K0xIAAAAYAAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=K0xIAAAAYAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=K0xIAAAAYAAJ&pg=PA5222&dq=war&hl=&cd=3&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=K0xIAAAAYAAJ&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=K0xIAAAAYAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=K0xIAAAAYAAJ&rdid=book-K0xIAAAAYAAJ&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/War_Expenditures.epub?id=K0xIAAAAYAAJ&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": True,
                                "downloadLink": "http://books.google.pl/books/download/War_Expenditures.pdf?id=K0xIAAAAYAAJ&hl=&output=pdf&sig=ACfU3U3HAvSeOxERDoAlnKLroA_aZWiUEw&source=gbs_api"
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=K0xIAAAAYAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Mr. P. W. HARE , Director of Sales , <b>War</b> Department , Washington , D. C. <br>\nAttention Maj . Squire . DEAR Sir : Confirming telephone conversation this <br>\nmorning with reference to <b>War</b> Department sugar to be purchased by this board , <br>\nwe beg to&nbsp;..."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "BbxFAQAAMAAJ",
                        "etag": "7QfdtdqL2f8",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/BbxFAQAAMAAJ",
                        "volumeInfo": {
                            "title": "Decisions of the Appeal Section, War Department, Claims Board",
                            "subtitle": "Successor to the Board of Contract Adjustment, V. 1-8, Jan. 1919-Aug. 1921",
                            "authors": [
                                "United States. Claims board. (War Dept.)"
                            ],
                            "publishedDate": "1921",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "CHI:71665068"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "categories": [
                                "Defense contracts"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "1.2.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=BbxFAQAAMAAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=BbxFAQAAMAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=BbxFAQAAMAAJ&pg=PR7&dq=war&hl=&cd=4&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=BbxFAQAAMAAJ&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=BbxFAQAAMAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=BbxFAQAAMAAJ&rdid=book-BbxFAQAAMAAJ&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/Decisions_of_the_Appeal_Section_War_Depa.epub?id=BbxFAQAAMAAJ&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=BbxFAQAAMAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Successor to the Board of Contract Adjustment, V. 1-8, Jan. 1919-Aug. 1921 <br>\nUnited States. Claims board. (<b>War</b> Dept.) Case No. Name of claimant . Subject <br>\nmatter . Page . 278 4 349 404 611 417 733 730 26 36 345 490 360 51 81 389 <br>\n629 741&nbsp;..."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "0PvgQ2J45xIC",
                        "etag": "RwQFNMp0g+I",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/0PvgQ2J45xIC",
                        "volumeInfo": {
                            "title": "Naval War College Review",
                            "authors": [
                                "Naval War College (U.S.)"
                            ],
                            "publishedDate": "1991",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "STANFORD:36105112099853"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "categories": [
                                "International relations"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "1.1.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=0PvgQ2J45xIC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=0PvgQ2J45xIC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=0PvgQ2J45xIC&pg=RA3-PA32&dq=war&hl=&cd=5&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=0PvgQ2J45xIC&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=0PvgQ2J45xIC"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=0PvgQ2J45xIC&rdid=book-0PvgQ2J45xIC&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/Naval_War_College_Review.epub?id=0PvgQ2J45xIC&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=0PvgQ2J45xIC&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Even before the Gulf <b>War</b> , General Lobov thus asserted that surprise ACM strikes <br>\ncan ensure not only the operational - tactical but also the strategic initiative on the <br>\nfuture battlefield . &quot; He went so far argue that the use of ACMs \u201c raises the&nbsp;..."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "iQY3AQAAMAAJ",
                        "etag": "lmugdI9uAs8",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/iQY3AQAAMAAJ",
                        "volumeInfo": {
                            "title": "A History of England from the Conclusion of the Great War in 1815",
                            "authors": [
                                "Sir Spencer Walpole"
                            ],
                            "publishedDate": "1890",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "PSU:000023974579"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "categories": [
                                "Great Britain"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.1.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=iQY3AQAAMAAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=iQY3AQAAMAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=iQY3AQAAMAAJ&pg=PA55&dq=war&hl=&cd=6&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=iQY3AQAAMAAJ&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=iQY3AQAAMAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=iQY3AQAAMAAJ&rdid=book-iQY3AQAAMAAJ&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/A_History_of_England_from_the_Conclusion.epub?id=iQY3AQAAMAAJ&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=iQY3AQAAMAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "66 land , \u201d said Canning , was to hinder the impress of a joint character from <br>\nbeing affixed to the <b>war</b> \u2014 if <b>war</b> there must be \u2014with Spain ; to take care that the <br>\n<b>war</b> should not grow out of an assumed jurisdiction of the Congress ; and this I <br>\nsay&nbsp;..."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "4aPvAAAAMAAJ",
                        "etag": "EzVf1Xb3N2I",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/4aPvAAAAMAAJ",
                        "volumeInfo": {
                            "title": "Norman County, Minnesota, in the World War",
                            "publishedDate": "1922",
                            "description": "Consists primarily of photographs with brief biographies of Norman County residents active in foreign and domestic U.S. World War I efforts, including soldiers, Home Service workers, Red Cross members, Home Guard members, and others.",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "WISC:89066170978"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": False
                            },
                            "pageCount": 184,
                            "printType": "BOOK",
                            "categories": [
                                "Norman County (Minn.)"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.1.3.0.preview.0",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=4aPvAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=4aPvAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=4aPvAAAAMAAJ&dq=war&hl=&cd=7&source=gbs_api",
                            "infoLink": "http://books.google.pl/books?id=4aPvAAAAMAAJ&dq=war&hl=&source=gbs_api",
                            "canonicalVolumeLink": "https://books.google.com/books/about/Norman_County_Minnesota_in_the_World_War.html?hl=&id=4aPvAAAAMAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "NOT_FOR_SALE",
                            "isEbook": False
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "NO_PAGES",
                            "embeddable": False,
                            "publicDomain": False,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False
                            },
                            "pdf": {
                                "isAvailable": True
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=4aPvAAAAMAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "NONE",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Consists primarily of photographs with brief biographies of Norman County residents active in foreign and domestic U.S. World War I efforts, including soldiers, Home Service workers, Red Cross members, Home Guard members, and others."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "nj5uRjMSkYMC",
                        "etag": "iwEX+K2nRrs",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/nj5uRjMSkYMC",
                        "volumeInfo": {
                            "title": "The Origin of the Late War: Traced from the Beginning of the Constitution, Etc",
                            "authors": [
                                "George Lunt"
                            ],
                            "publishedDate": "1866",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "BL:A0023377384"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "pageCount": 491,
                            "printType": "BOOK",
                            "categories": [
                                "United States"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.1.1.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=nj5uRjMSkYMC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=nj5uRjMSkYMC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=nj5uRjMSkYMC&pg=PA1&dq=war&hl=&cd=8&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=nj5uRjMSkYMC&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=nj5uRjMSkYMC"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=nj5uRjMSkYMC&rdid=book-nj5uRjMSkYMC&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/The_Origin_of_the_Late_War_Traced_from_t.epub?id=nj5uRjMSkYMC&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=nj5uRjMSkYMC&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "ORIGIN OF THE LATE <b>WAR</b> . . CHAPTER I. Staternent of the Question .-- General <br>\nSentiment of the Country , in regard to Slavery , before the <b>War</b> .--- Condition of <br>\nthe Negroes in the North and in the South .-- The Slaves of Jonathan Edwards ."
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "fgc9AAAAYAAJ",
                        "etag": "eUnhdhzZyIY",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/fgc9AAAAYAAJ",
                        "volumeInfo": {
                            "title": "Investigation of the War Department",
                            "subtitle": "Hearings Before the Committee on Military Affairs, United States Senate, Sixty-fifth Congress, Second Session, for the Purpose of Inquiring from the Different Branches of the Service of the War Department as to the Progress Made in the Matter of Providing for Ordnance, Small Arms, Munitions, Etc., in Connection with the Present War and to Ascertain the Government Need Therefor ...",
                            "publishedDate": "1918",
                            "industryIdentifiers": [
                                {
                                    "type": "OTHER",
                                    "identifier": "NYPL:33433019657950"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "printType": "BOOK",
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.1.2.0.full.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=fgc9AAAAYAAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=fgc9AAAAYAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=fgc9AAAAYAAJ&printsec=frontcover&dq=war&hl=&cd=9&source=gbs_api",
                            "infoLink": "https://play.google.com/store/books/details?id=fgc9AAAAYAAJ&source=gbs_api",
                            "canonicalVolumeLink": "https://play.google.com/store/books/details?id=fgc9AAAAYAAJ"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "FREE",
                            "isEbook": True,
                            "buyLink": "https://play.google.com/store/books/details?id=fgc9AAAAYAAJ&rdid=book-fgc9AAAAYAAJ&rdot=1&source=gbs_api"
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "ALL_PAGES",
                            "embeddable": True,
                            "publicDomain": True,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False,
                                "downloadLink": "http://books.google.pl/books/download/Investigation_of_the_War_Department.epub?id=fgc9AAAAYAAJ&hl=&output=epub&source=gbs_api"
                            },
                            "pdf": {
                                "isAvailable": True,
                                "downloadLink": "http://books.google.pl/books/download/Investigation_of_the_War_Department.pdf?id=fgc9AAAAYAAJ&hl=&output=pdf&sig=ACfU3U0Eu2cVf9b42foVHnFBdRo6zStloA&source=gbs_api"
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=fgc9AAAAYAAJ&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "FULL_PUBLIC_DOMAIN",
                            "quoteSharingAllowed": False
                        }
                    },
                    {
                        "kind": "books#volume",
                        "id": "Cl1jchisklcC",
                        "etag": "grWjAvXXORM",
                        "selfLink": "https://www.googleapis.com/books/v1/volumes/Cl1jchisklcC",
                        "volumeInfo": {
                            "title": "Peace, War, and Mental Health",
                            "subtitle": "Couples Therapists Look at the Dynamics",
                            "authors": [
                                "Barbara Jo Brothers"
                            ],
                            "publisher": "Psychology Press",
                            "publishedDate": "1992",
                            "description": "Discover how issues of world war and peace relate to the dynamics of couples therapy in this thought-provoking book. In Peace, War, and Mental Health, couples therapists provide diverse views on the links between strengthening marriages and preventing and solving international disputes. Although the contributors vary in their approaches to this issue, a common theme is the belief that couples as well as countries need to build bridges, not walls, for healthy relationships and they need to strive to learn what others are really feeling, thinking, or needing underneath the defenses others exhibit. The contributing therapists in Peace, War, and Mental Health explore the various links between couples in conflict and nations at war. Chapters describe how prevention strategies used for couples in therapy may be applied to the well-being of the world as a whole and how significant change is possible through the involvement of only a small percentage of the population. Other chapters focus on specific tools for couples therapy such as outlines of the major tasks of relationship building and traps that mitigate against good relationship construction, a description of the nuts and bolts of conflict resolution, and the use of flashcards to help both members of the pair present his or her real feelings to the other. Some of the intriguing topics covered in this book include: the relationship between psychotherapy and spirituality and the paradox of individuals longing to belong since each is a part of the whole the role of gender on war and its potential impact on peace the failure of the humanistic movement societal attitudes linking domestic violence and large scale violence how the potential for resolution of differences in couples can be applied to peace among nations how prevention may be expanded to include the \"mental health\" of the whole world--Part V of an interview with Virginia Satir Peace, War, and Mental Health helps therapists look at international peace and couples therapy with new perspectives, a necessity in today's rapidly changing family and world climate.",
                            "industryIdentifiers": [
                                {
                                    "type": "ISBN_10",
                                    "identifier": "1560244372"
                                },
                                {
                                    "type": "ISBN_13",
                                    "identifier": "9781560244370"
                                }
                            ],
                            "readingModes": {
                                "text": False,
                                "image": True
                            },
                            "pageCount": 161,
                            "printType": "BOOK",
                            "categories": [
                                "Medical"
                            ],
                            "maturityRating": "NOT_MATURE",
                            "allowAnonLogging": False,
                            "contentVersion": "0.2.4.0.preview.1",
                            "panelizationSummary": {
                                "containsEpubBubbles": False,
                                "containsImageBubbles": False
                            },
                            "imageLinks": {
                                "smallThumbnail": "http://books.google.com/books/content?id=Cl1jchisklcC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                                "thumbnail": "http://books.google.com/books/content?id=Cl1jchisklcC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
                            },
                            "language": "en",
                            "previewLink": "http://books.google.pl/books?id=Cl1jchisklcC&printsec=frontcover&dq=war&hl=&cd=10&source=gbs_api",
                            "infoLink": "http://books.google.pl/books?id=Cl1jchisklcC&dq=war&hl=&source=gbs_api",
                            "canonicalVolumeLink": "https://books.google.com/books/about/Peace_War_and_Mental_Health.html?hl=&id=Cl1jchisklcC"
                        },
                        "saleInfo": {
                            "country": "PL",
                            "saleability": "NOT_FOR_SALE",
                            "isEbook": False
                        },
                        "accessInfo": {
                            "country": "PL",
                            "viewability": "PARTIAL",
                            "embeddable": True,
                            "publicDomain": False,
                            "textToSpeechPermission": "ALLOWED",
                            "epub": {
                                "isAvailable": False
                            },
                            "pdf": {
                                "isAvailable": False
                            },
                            "webReaderLink": "http://play.google.com/books/reader?id=Cl1jchisklcC&hl=&printsec=frontcover&source=gbs_api",
                            "accessViewStatus": "SAMPLE",
                            "quoteSharingAllowed": False
                        },
                        "searchInfo": {
                            "textSnippet": "Some of the intriguing topics covered in this book include: the relationship between psychotherapy and spirituality and the paradox of individuals longing to belong since each is a part of the whole the role of gender on war and its ..."
                        }
                    }
                ]
            }