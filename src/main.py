from sensores import SensorNivel, SensorTemperatura
for sensor in (SensorNivel("LT-101"), SensorTemperatura("TT-201")):
    print(f"{sensor.tag}: {sensor.valor():g} {sensor.unidade()}")
print("Consulte os TODOs e execute make test ETAPA=07 para o primeiro incremento.")
