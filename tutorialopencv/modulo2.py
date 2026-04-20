import cv2
cap  = cv2.VideoCapture(1) #Abre la cámara web, el argumento 0 se refiere a la cámara predeterminada del sistema. Si hay varias cámaras, puedes usar 1, 2, etc.

while True:
    ret, frame = cap.read() #ret es un bool que dice si la lectura del frame de la cámara fue exitosa, o no. Frame se refiere al frame captudrado como array de NumPy, igual que la imagen del modulo 1.

    if not ret: #Si la cámara falla o se desconecta, ret es False y el programa se detiene en vez de crashearse.
        break

    cv2.imshow("Cámara", frame) #Muestra el frame actual en la ventana, al estar dentro del loop, da la sensación de ser un video en tiempo real.

    if cv2.waitKey(0) & 0xFF == ord('q'): #Espera 1ms a que el usuario presione la tecla q, asi se sale del loop. EL & 0xFF es para asegurarse de que se capture la tecla correctamente en diferentes sistemas operativos.
        break

cap.release() # Libera la camara para que otros programas puedan usarla, es una buena práctica hacerlo al finalizar.
cv2.destroyAllWindows() #Cierra todas las ventanas que OpenCV abre limpiamente, es importante hacerlo para liberar recursos del sistema.