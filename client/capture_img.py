import cv2 as cv

global capture
capture = 0

cam = cv.VideoCapture(0)

def frames():
    global capture

    while True:
        success, frame = cam.read()
        if success:

            if (capture):
                capture = 0
                #TODO

            try:
                # Encode frame into memory buffer then to array of bytes
                _, buffer = cv.imencode('.jpg', cv.flip(frame,1))
                frame = buffer.tobytes()
                # Adjust frame to a format, needed for a http response
                yield(b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception:
                pass

        else:
            pass