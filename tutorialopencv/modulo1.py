import cv2 #Llama a la libreria OpenCV

imagen = cv2.imread("cat.jpg") #Lee la imagen y la convierte en un array de números, pasa a ser una cuadrícula de pixeles entre 0 y 255.
print(type(imagen)) #Imprime el tipo de date de la variable imagen, un array de numpy
print(imagen.shape) #.shape devuelve las dimensiones de la iamgen, en este caso, alto, ancho y número de canales (3 para RGB). Es una tupla.
print(imagen[100, 100]) #Accede al pixel en la filla 100, columna 100 y lo imprime, asi se accede a posiciones en un array de NumPy
cv2.imshow("Mi imagen", imagen) #Muestra la imagen en una ventana, dibuja el array como una imagen, el primer argumento es el nombre de la ventana y el segundo es el array.
cv2.waitKey(0) #Espera a que el usuario presione una tecla, el argumento es el tiempo en milisegundos que espera, 0 significa esperar indefinidamente.
cv2.destroyAllWindows() #Cierra todas las ventanas que OpenCV abre limpiamente.
