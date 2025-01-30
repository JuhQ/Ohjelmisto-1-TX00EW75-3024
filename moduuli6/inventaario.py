def inventaario(tavarat):
    for tavara in tavarat:
        print(tavara)

inventaario([1,2,34,5,7])
inventaario([[123,2], ["hep", "juuu"], [True, False]])

reppu = ['Läppäri','Kahvikuppi']
inventaario(reppu)

reppu.append("Kirja")
inventaario(reppu)

reppu.remove("Läppäri")
inventaario(reppu)

"""
lompakko = ['500e', 'kolikoita']
inventaario(lompakko)
inventaario(reppu)
inventaario(['kissa','koira','mato'])
inventaario(['kissa','koira','mato','lintu'])
"""