### full reverse function
### @ app.patika.dev/moduller/python-temel/proje

# Author: Fatih Yalçın
# 18th August, 2021
# linkedin.com/in/fatih-yalcin-/


def full_reverse(ls):
    new_ls = ls[:] # kopyalıyoruz, böylece ana liste değişmesin
    
    def main(new_ls):
        new_ls.reverse() # ilk adım listeyi ters çevirmek
        
        for i in new_ls: # listedeki her elemanı
            
            if type(i) == list: # eğer listeyse
                main(i) # aynı işlemleri o listeye de uygular

            # değilse bir şey yapmaz (zaten yeri değiştirildi)
            
        return new_ls
    
    return main(new_ls)


#testler
if __name__ == "__main__":
    ls1 = [1,2,6,7,3]
    print(full_reverse(ls1))
    ls2 = [1,9,[],[["asda",2], ["FFFF", [21321,87978,436546]]]]
    print(full_reverse(ls2))
