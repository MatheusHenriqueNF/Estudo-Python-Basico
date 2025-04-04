from pygeocoder import Geocoder

endereco = 'Avenida paulista, Sao Paulo, SP'

#result = Geocoder("CHAVE API").geocode(endereco).postal_code
result = Geocoder("CHAVE API").geocode(endereco).reverse_geocode("COODERNADAS")
print(result)