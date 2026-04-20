import cv2
cap = cv2.VideoCapture(0) #Abre la cámara web, el argumento 0 indica la cámara predeterminada.

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.putText(frame, "Hola Mundo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)
    '''
    cv2.putText — dibuja texto sobre el frame.
    frame — aquí no convierte nada, ya es un array desde cap.read(). Lo que hace es decirle a OpenCV dónde dibujar el texto, o sea, sobre cuál imagen.
    "Hola mundo" — el texto a mostrar.
    (50, 50) — son las coordenadas x, y donde empieza el texto.
    cv2.FONT_HERSHEY_SIMPLEX — el tipo de fuente.
    1  — el tamaño de la fuente. 
    (0, 255, 0) — no son coordenadas, es el color en BGR. (0, 255, 0), el orden es: Azul, Verde, Rojo.
    2 — es el grosor del texto en píxeles
    '''
    cv2.rectangle(frame, (100, 100), (300, 500), (255, 0, 0), 2)
    cv2.circle(frame, ( 400, 200), 50, (0, 0, 255), -1)

    cv2.imshow("Cámara", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()