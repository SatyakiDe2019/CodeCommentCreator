def predStream(self, img, hsvVals, FrNo):
    try:
        pT1 = self.pT1
        pT2 = self.pT2
        pT3 = self.pT3
        pT4 = self.pT4

        #Find the color ball
        imgColor, mask = myColorFinder.update(img, hsvVals)

        #Find location of the red_ball
        imgContours, contours = cvzone.findContours(img, mask, minArea=500)

        if contours:
            posListX.append(contours[0]['center'][0])
            posListY.append(contours[0]['center'][1])

        if posListX:
            # Find the Coefficients
            A, B, C = np.polyfit(posListX, posListY, 2)

            for i, (posX, posY) in enumerate(zip(posListX, posListY)):
                pos = (posX, posY)
                cv2.circle(imgContours, pos, 10, (0,255,0), cv2.FILLED)

                # Using Karman Filter Prediction
                predicted = kf.predict(posX, posY)
                cv2.circle(imgContours, (predicted[0], predicted[1]), 12, (255,0,255), cv2.FILLED)

                ballDetectFlag = True
                if ballDetectFlag:
                    print('Balls Detected!')

                if i == 0:
                    cv2.line(imgContours, pos, pos, (0,255,0), 5)
                    cv2.line(imgContours, predicted, predicted, (255,0,255), 5)
                else:
                    predictedM = kf.predict(posListX[i-1], posListY[i-1])

                    cv2.line(imgContours, pos, (posListX[i-1], posListY[i-1]), (0,255,0), 5)
                    cv2.line(imgContours, predicted, predictedM, (255,0,255), 5)

            if len(posListX) < 10:

                # Calculation for best place to ball
                a1 = A
                b1 = B
                c1 = C - pT1

                X1 = int((- b1 - math.sqrt(b1**2 - (4*a1*c1)))/(2*a1))
                prediction1 = pT2 < X1 < pT3

                a2 = A
                b2 = B
                c2 = C - pT4

                X2 = int((- b2 - math.sqrt(b2**2 - (4*a2*c2)))/(2*a2))
                prediction2 = pT2 < X2 < pT3

                prediction = prediction1 | prediction2

            if prediction:
                print('Good Length Ball!')
                sMsg = "Good Length Ball - (" + str(FrNo) + ")"
                cvzone.putTextRect(imgContours, sMsg, (50,150), scale=5, thickness=5, colorR=(0,200,0), offset=20)
            else:
                print('Loose Ball!')
                sMsg = "Loose Ball - (" + str(FrNo) + ")"
                cvzone.putTextRect(imgContours, sMsg, (50,150), scale=5, thickness=5, colorR=(0,0,200), offset=20)

            return imgContours

    except Exception as e:
        x = str(e)
        print('Error predStream:', x)

        return img
