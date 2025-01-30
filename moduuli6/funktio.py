
def lempijuoma():
    return "Paha automaattikahvi"

def tervehdi():
    juoma = lempijuoma()
    jotain = 123
    print(f"{juoma} on hyvää kun sitä juo. Kannattaa juoda kahden tunnin välein?")
    if jotain == 123:
        print("Ehtolauseke toteutui")
        print(lempijuoma())
        return
    print("-------")
    print(f"{lempijuoma()} on hyvää kun sitä juo. Kannattaa juoda kahden tunnin välein?")


for i in range(50000):
    arvo = tervehdi()
    print(arvo)
