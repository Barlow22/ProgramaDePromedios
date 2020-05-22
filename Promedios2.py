def promedios(notaMat, notaLit, notaFis):
    promedio = (notaMat + notaLit + notaFis) / 3
    return promedio
def definirEstadoAlumno(promedioAlumno):
    
    if promedioAlumno > 6:
        print('Alumno: ' + nombreAlumno + '\n' + 'Promedio: ' + str(promedioAlumno) + '\n' + 'Estado: Aprobado.')
        if promedioAlumno >= 9:
            print('Alumno distinguido')
    elif promedioAlumno == 4 and promedioAlumno <= 5:
        print('Alumno: ' + nombreAlumno + '\n' + 'Promedio: ' + str(promedioAlumno) + '\n' + 'Estado: Recuperatorio.')
    elif promedioAlumno < 4:
        print('Alumno: ' + nombreAlumno + '\n' + 'Promedio: ' + str(promedioAlumno) + '\n' + 'Estado: Desaprobado.')


nombreAlumno = input('Ingrese el nombre del alumno: ')
nota1 = int(input('Ingrese la 1er nota: '))
nota2 = int(input('Ingrese la 2da nota: '))
nota3 = int(input('Ingrese la 3er nota: ' + '\n'))
promedioAlumno = promedios(nota1, nota2, nota3)
definirEstadoAlumno(promedioAlumno)