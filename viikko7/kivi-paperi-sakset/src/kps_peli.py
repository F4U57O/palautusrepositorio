from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class Peli:
    
    @staticmethod
    def peli(vastaus):
        if vastaus.endswith('a'):
            kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.pelaa()
            return True
        elif vastaus.endswith('b'):
            yksinpeli = KPSTekoaly()
            yksinpeli.pelaa()
            return True
        elif vastaus.endswith('c'):
            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()
            return True
        else:
            return False