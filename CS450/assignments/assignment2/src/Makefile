GCC_OPTIONS=-Wall -pedantic -I../include
GL_OPTIONS=-lGLEW -lglut -lGL
COPTIONS=$(GCC_OPTIONS) $(GL_OPTIONS)

all: prog

prog: sceneParser.o objParser.o initShader.o assignment2.o
	g++ -o prog sceneParser.o objParser.o initShader.o assignment2.o $(GL_OPTIONS)

objParser.o: objParser.cpp
	g++ $(GCC_OPTIONS) -c objParser.cpp

sceneParser.o: sceneParser.cpp
	g++ $(GCC_OPTIONS) -c sceneParser.cpp

initShader.o: initShader.cpp
	g++ $(GCC_OPTIONS) -c initShader.cpp

assignment2.o: assignment2.cpp
	g++ $(GCC_OPTIONS) -c assignment2.cpp

clean:
	-rm initShader.o
	-rm objParser.o
	-rm sceneParser.o
	-rm assignment2.o
	-rm prog
