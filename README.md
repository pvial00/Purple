# Purple

by Uvajda (KryptoMagick)

Purple is the follow on hand cipher to RedDye.  RedDye suffers from a bad known plaintext attack if one knows equal to the length of the key or greater, one can recover the rest of the message.  Purple hopes to solve this dilemma.

The key length for Purple as a hand cipher is 26 letters.

# Hand cipher usage:

Establish a 26 letter key, K.  Establish a counter C that iterates over the length of the key starting from left to right and always repeating, this simply iterates over the key (counter modulo 26)[Sequence 0-25].

Sum the values of all elements in the key modulo 26 and call that J.  Next lookup the J index in your key.  The resulting integer becomes J for the first round of encryption.

Calculate a new K[J] by summing ((K[C] + K[J]) modulo 26).

Then produce the output letter by summing ((K[J] + K[K[J]]) modulo 26).  The nested lookup takes the value of K[J] as an index to with which to find the third value or output integer.

ALPHABET:  A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
NUMBERS:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

Encryption - Example:

KEY:  ABCDEFGHIJKLMNOPQRSTUVWXYZ (INSECURE)

PLAINTEXT (MESSAGE):  ABC

Step 1.

INITIAL J INDEX = 13

J = K[J] = 13

((K[C] + K[J]) mod 26) = K[J] = 13

((K[K[J]] + K[J]) mod 26) = 0 (FIRST NUMBER OF THE KEY STREAM)


Step 1 - Letter 1.

J = K[J] = 13

K[C] = 0, K[J] = 13

((K[C] + K[J]) mod 26) = K[J] = 13

((K[K[J]] + K[J]) mod 26) = 0 (FIRST NUMBER OF THE KEY STREAM)


((0 + 0) mod 26) = 0 = A

((A + A) mod 26) = A


Step 2 - Letter 2.


J = K[J] = 13

K[C] = 2, K[J] = 13

((K[C] + K[J]) mod 26) = K[J] = 14

((K[K[J]] + K[J]) mod 26) = 2 (FIRST NUMBER OF THE KEY STREAM)


((2 + 1) mod 26) = 3 = D

((C + B) mod 26) = D


Step 3 - Letter 3.


J = K[J] = 14

K[C] = 2, K[J] = 14

((K[C] + K[J]) mod 26) = K[J] = 16

((K[K[J]] + K[J]) mod 26) = 6 (FIRST NUMBER OF THE KEY STREAM)


((6 + 2) mod 26) = 8 = I

((G + C) mod 26) = I

RESULT: ADI


Decryption Example: 

KEY:  ABCDEFGHIJKLMNOPQRSTUVWXYZ (INSECURE)

CIPHERTEXT (MESSAGE):  ABC

Step 1 - Letter 1.

INITIAL J INDEX = 13

J = K[J] = 13

((K[C] + K[J]) mod 26) = K[J] = 13

((K[K[J]] + K[J]) mod 26) = 0 (FIRST NUMBER OF THE KEY STREAM)

((0 + 0) mod 26) = 0 = A

((A + A) mod 26) = A


Step 2 - Letter 2.


J = K[J] = 13

K[C] = 1, K[J] = 13

((K[C] + K[J]) mod 26) = K[J] = 14

((K[K[J]] + K[J]) mod 26) = 2 (FIRST NUMBER OF THE KEY STREAM)


((2 + 1) mod 26) = 0 = Z

((A + A) mod 26) = Z


Step 3 - Letter 3.


J = K[J] = 14

K[C] = 2, K[J] = 14

((K[C] + K[J]) mod 26) = K[J] = 16

((K[K[J]] + K[J]) mod 26) = 6 (FIRST NUMBER OF THE KEY STREAM)


((6 + 2) mod 26) = 22 = W

((G + C) mod 26) = W

RESULT: AZW
