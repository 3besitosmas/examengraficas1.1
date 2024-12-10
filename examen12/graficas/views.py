from django.shortcuts import render

def graficas(request):
    # Datos para las seis gráficas
    context = {
        'data1': [5, 10, 15, 20],
        'labels1': ['Costo 1', 'Costo 2', 'Costo 3', ' Costo 4'],
        'data2': [30, 50, 65, 85],
        'labels2': ['Japon', 'Estados Unidos', 'Mexico', 'China'],
        'data3': [3, 5, 7, 10],
        'labels3': ['Almacen 1', 'Almacen 2', 'Almacen 3', 'Almacen 4'],
        'data4': [4, 12, 24, 16],
        'labels4': ['Bimestre 1', 'Bimestre 2', 'Bimestre 3', 'Bimestre 4'],
        'data5': [12, 14, 16, 18],
        'labels5': ['One Piece ', 'Dragon Ball', 'Citrus', 'Naruto'],
        'data6': [16, 24, 12, 20],
        'labels6': ['Samsung', 'iPhone de Apple', 'Xiaomi', 'Oppo'],
    }
    
    return render(request, 'graficas/graficas.html', context)
