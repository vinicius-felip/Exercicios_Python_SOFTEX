times = 'Sport', 'Náutico', 'Santa Cruz', 'Salgueiro', 'Central', 'Afogados', 'Vitória', 'Petrolina', 'América','Flamengo ArcoVerde'

print ('------------------------------')

for i in times[:3]:
    print('{}º {}'.format(times.index(i)+1,i))
    
print('------------------------------')

for i in times[6:]:
    print('{}º {}'.format(times.index(i)+1,i))
    
print ('------------------------------')

for i in sorted(times):
    print('{}º {}'.format(times.index(i)+1,i))

print ('------------------------------')

print('Vitória está na {}º posição'.format(times.index('Vitória')+1))
    
