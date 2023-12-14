from kps_peli import Peli



def main():
    kps = Peli()
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        
        if kps.peli(vastaus) == False:
            break          




if __name__ == "__main__":
    main()
