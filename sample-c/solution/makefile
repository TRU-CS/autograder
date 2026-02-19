CC = gcc
CFLAGS = -Wall -Wextra -fPIC
LDFLAGS = -shared

all: banking_system.out banking.so  # Ensure both targets are built

banking_system.out: banking_system.c
	$(CC) $(CFLAGS) banking_system.c -o banking_system.out

banking.so: banking_system.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o banking.so banking_system.c -lm -shared -fPIC -D SHARED_LIB

clean:
	rm -f banking_system.out banking.so