from app import app, db

from models.location import Location, Photo

with app.app_context():
    db.drop_all()
    db.create_all()


    #################### Locations ###########################

    seattle = Location(name='Seattle', country='U.S.A.', lat=47.6062, lng=-122.3321)
    db.session.add(seattle)

    olympia = Location(name='Olympia', country='U.S.A.', lat=47.0379, lng=-122.9007)
    db.session.add(olympia)

    portland = Location(name='Portland', country='U.S.A.', lat=45.5155, lng=-122.6793)
    db.session.add(portland)

    eugene = Location(name='Eugene', country='U.S.A.', lat=44.0521, lng=-123.0868)
    db.session.add(eugene)

    medford = Location(name='Medford', country='U.S.A.', lat=42.3265, lng=-122.8756)
    db.session.add(medford)

    sacramento = Location(name='Sacramento', country='U.S.A.', lat=38.5816, lng=-121.4944)
    db.session.add(sacramento)

    san_fran= Location(name='San Francisco', country='U.S.A.', lat=37.7749, lng=-122.4194)
    db.session.add(san_fran)

    guadalajara = Location(name='Guadalajara', country='Mexico', lat=20.6597, lng=-103.3496)
    db.session.add(guadalajara)

    tequila = Location(name='Tequila', country='Mexico', lat=20.88197, lng=-103.83569)
    db.session.add(tequila)

    guanajuato = Location(name='Guanajuato', country='Mexico', lat=21.0190, lng=-101.2574)
    db.session.add(guanajuato)

    san_miguel = Location(name='San Miguel de Allende', country='Mexico', lat=20.9144, lng=-100.7452)
    db.session.add(san_miguel)

    mexico_city = Location(name='Mexico City', country='Mexico', lat=19.4326, lng=-99.1332)
    db.session.add(mexico_city)

    oaxaca = Location(name='Oaxaca', country='Mexico', lat=17.0542, lng=-96.7132)
    db.session.add(oaxaca)

    san_jose_pacifico = Location(name='San Jose del Pacifico', country='Mexico', lat=16.1698, lng=-96.50451)
    db.session.add(san_jose_pacifico)

    escondido = Location(name='Puerto Escondido', country='Mexico', lat=15.8720, lng=-97.0767)
    db.session.add(escondido)

    san_cristobal = Location(name='San Cristobal de las Casas', country='Mexico', lat=18.4189, lng=-70.1031)
    db.session.add(san_cristobal)

    palenque = Location(name='Palenque', country='Mexico', lat=17.50953, lng=-91.98248)
    db.session.add(palenque)

    merida = Location(name='Merida', country='Mexico', lat=20.9674, lng=-89.5926)
    db.session.add(merida)

    mujeres = Location(name='Isla Mujeres', country='Mexico', lat=21.2322, lng=-86.7341)
    db.session.add(mujeres)

    holbox = Location(name='Isla Holbox', country='Mexico', lat=21.5308, lng=-87.2867)
    db.session.add(holbox)

    tulum = Location(name='Tulum', country='Mexico', lat=20.2114, lng=-87.4654)
    db.session.add(tulum)

    bacalar = Location(name='Lake Bacalar', country='Mexico', lat=18.747, lng=-88.318)
    db.session.add(bacalar)

    caye_caulker = Location(name='Caye Caulker', country='Belize', lat=17.7612, lng=-88.0277)
    db.session.add(caye_caulker)

    san_ignacio = Location(name='San Ignacio', country='Belize', lat=17.1523, lng=-89.0800)
    db.session.add(san_ignacio)

    tikal = Location(name='Tikal', country='Guatamala', lat=17.2220, lng=-89.6237)
    db.session.add(tikal)

    flores = Location(name='Flores', country='Guatamala', lat=16.9181, lng=-89.8926)
    db.session.add(flores)

    lanquin = Location(name='Lanquin (Zephyr Lodge)', country='Guatamala', lat=15.5753, lng=-89.9802)
    db.session.add(lanquin)

    semuc_champey = Location(name='Chemuc Champey', country='Guatamala', lat=15.5667, lng=-89.9667)
    db.session.add(semuc_champey)

    atitlan = Location(name='Lake Atitlan', country='Guatamala', lat=14.6907, lng=-91.20255)
    db.session.add(atitlan)

    atitlan = Location(name='Lake Atitlan', country='Guatamala', lat=14.6907, lng=-91.20255)
    db.session.add(atitlan)

    acatenango = Location(name='Volcan de Acatenango', country='Guatamala', lat=14.5005, lng=-90.8757)
    db.session.add(acatenango)

    antigua = Location(name='Antigua', country='Guatamala', lat=14.5586, lng=-90.7295)
    db.session.add(antigua)

    livingston = Location(name='Livingston', country='Guatamala', lat=15.8269, lng=-88.7530)
    db.session.add(livingston)

    utila = Location(name='Utila', country='Honduras', lat=16.0950, lng=-86.9274)
    db.session.add(utila)

    cangrejal_river = Location(name='Cangrejal River Lodge', country='Honduras', lat=15.7271, lng=-86.7357)
    db.session.add(cangrejal_river)

    DD = Location(name='D&D Brewery (Lake Yojoa)', country='Honduras', lat=14.9859, lng=-88.0918)
    db.session.add(DD)

    tegucigalpa = Location(name='Tegucigalpa', country='Honduras', lat=14.0723, lng=-87.1921)
    db.session.add(tegucigalpa)

    managua = Location(name='Managua', country='Nicaragua', lat=12.1150, lng=-86.2362)
    db.session.add(managua)

    san_jose = Location(name='San Jose', country='Costa Rica', lat=9.9281, lng=-84.0907)
    db.session.add(san_jose)

    puerto_viejo = Location(name='Puerto Viejo', country='Costa Rica', lat=9.6540, lng=-82.7549)
    db.session.add(puerto_viejo)

    bocas = Location(name='Bocas del Toro', country='Panama', lat=9.3403, lng=-82.2413)
    db.session.add(bocas)

    panama_city = Location(name='Panama City', country='Panama', lat=8.9824, lng=-79.5199)
    db.session.add(panama_city)

    san_blas = Location(name='San Blas Islands', country='Panama', lat=9.57, lng=-78.82)
    db.session.add(san_blas)

    #################### Photos ##################################

    mexico_city_ph_1 = Photo(image='test', location=mexico_city)
    db.session.add(mexico_city_ph_1)






    db.session.commit()
