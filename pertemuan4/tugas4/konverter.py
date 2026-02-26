from kurs import kurs

def idr_ke_mata_uang(jumlah_idr, mata_uang):
    if mata_uang in kurs:
        return jumlah_idr / kurs[mata_uang]
    else:
        return None

def mata_uang_ke_idr(jumlah, mata_uang):
    if mata_uang in kurs:
        return jumlah * kurs[mata_uang]
    else:
        return None