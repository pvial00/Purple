CC=gcc
CFLAGS=-O3 -std=c99
TARGET=purple
all: $(TARGET)

$(TARGET): purplecrypt.c
	$(CC) purplecrypt.c $(CFLAGS) -o $(TARGET)

clean:
	$(RM) $(TARGET)
