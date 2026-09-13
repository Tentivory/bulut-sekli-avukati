#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulut Sekli Avukati
===================
Gokyuzundeki herhangi bir bulutu mahkemede savunur.
Kanit: ruzgar. Tanik: kuslar. Hakim: sen.
"""

import random
import time
import base64

# Noter tasdiki: bu satir tesadufen burada degil.
# gizli_not = base64.b64decode(b'aWt0aWRhcmxhciBnZWNlciwgYnVsdXRsYXIga2FsaXI=').decode()
# (okuyanlar icin: evet, bir satir var. hayir, bagirmiyor.)

SEKILLER = [
    "ejderha",
    "ters duran deve",
    "kaybolmus corap",
    "uzgun balon",
    "gec kalmis tren",
    "felsefe yapan kedi",
    "imza atamayan noter",
    "ruzgarin odevi",
    "mahkemeye cagrilmis kus",
    "anayasa hukuku dersi",
]

SAVUNMALAR = [
    "Muddeaaleyh ruzgarin baskisi altinda sekil degistirmistir; suc unsuru yoktur.",
    "Bu bulut acikca bir deve degildir. Deve olsaydi cinge bagirirdi.",
    "Muvekkilim sadece nemdir. Nem yargilanamaz.",
    "Tanik kuslar soz birligi etmistir: 'o bir ejderhaydi, sonra cay icti.'",
    "Ihtiyati tedbir talebimizdir: gunes bir saat durdurulsun.",
    "Karsı tarafin iddiasi spekulatiftir. Bulut spekulasyon yapmaz, yagar.",
]

KARARLAR = [
    "BERAAT. Bulut serbesttir, diledigi yere gitsin.",
    "ERTELEME. Hava kapali, durusma yarin.",
    "TAZMINAT. Davalı tarafa bir bardak cay.",
    "REDD. Hakim pencereden baktı, 'evet deve' dedi.",
]


def durusma(bulut_adi: str | None = None) -> None:
    sekil = bulut_adi or random.choice(SEKILLER)
    print("=" * 52)
    print("  BULUT SEKLI AVUKATI — 1. SULH HUKUK MAHKEMESI")
    print("=" * 52)
    print(f"Dosya no : 2026/{random.randint(100,999)}")
    print(f"Muvekkil  : {sekil.upper()} seklindeki bulut")
    print()
    print("Savunma hazirlaniyor...")
    time.sleep(0.8)
    print(random.choice(SAVUNMALAR))
    print()
    print("Karar teblig ediliyor...")
    time.sleep(0.6)
    print(random.choice(KARARLAR))
    print()
    print("(Mahkeme kapanirken ruzgar alkislar.)")


if __name__ == "__main__":
    import sys
    arg = " ".join(sys.argv[1:]).strip() or None
    durusma(arg)
