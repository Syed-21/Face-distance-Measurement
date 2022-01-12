# Face-distance-Measurement
Project Face Distance Measurement
LIBRARIES USED:
•	Cvzone
•	MediaPipe
•	Pygame

DESCRIPTION:
	This python script is a very basic form of face distance measurement from the camera(any normal cam).
  One can easily change the limit of the alarm by changing the values of distance in a simple IF/ELSE statement which are conditional statements .
  The library cvzone detects a face and creates a face mesh around the face .As being used with a normal camera with no depth measurements sensors the point of interests taken are the distance between the two eyes as this distance can never change as long as the person lives .
  The library Pygame is used to load a .MP3 file from the hard drive and play it accordingly to the script or given conditions .This script can further be modified by using tensorflow or google colab Object detection modules and also with the help of IoT sensors to build complete Eyes.

USES:
	The sole purpose of this script is to provide eyes for the blind people as mentioned above with the help of IoT sensors and object detection modules that uses machine learning,
  we can clearly embed a camera into some sort of specks or glasses attach a camera to it and then connect the glasses(camera) via IP or wired to a raspberry Pi or some Arduino sensors or chips which then will not only recognizes face and play an alarm after some distance also it will detect the whole environment that the camera is seeing and warn the user about any object coming close to him or any hurdle or obstacle coming his way.
  We can also use some API’s attached to IoT sensors that if a sudden jerk or fall is detected which will direct the API to send a message along with the location of the blind to any SOS contact.

CONCLUSION:
	This will not totally help the blind but to some extent it surely will by warning them to not to hurt themselves.

