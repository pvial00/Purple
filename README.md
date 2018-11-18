# Purple

Purple is the follow on hand cipher to RedDye.  RedDye suffers from a bad known plaintext attack if one knows equal to the length of the key or greater, one can recover the rest of the message.  Purple hopes to solve this dilemma.

The key length for Purple as a hand cipher is 26 letters.

# Hand cipher usage:

Establish a 26 letter key, K.  Establish a counter C that iterates over the length of the key starting from left to right and always repeating, this simply iterates over the key (counter mod 26).

Sum the values of all elements in the key mod 26 and call that J.  Next lookup the J index in your key.  That now becomes the new J for the first round.

Calculate a new K[J] by summing K[C] + K[J] + K[K[J]] mod 26.  The nested lookup takes the value of K[J] as an index to find the third value to add.

Then produce the output letter by K[K[J]], which is to use K[J] as a index and use the letter found at that index as the output letter.

Example:

KEY:  ABCDEFGHIJKLMNOPQRSTUVWXYZ (INSECURE!)

MESSAGE:  TOOMANYSECRETS


FIRST ROUND EXAMPLE


INITIAL J INDEX = 13

J = K[J] = 13

K[C] + K[J] + K[K[J]] mod 26 = K[J] = 0

K[K[J]] + K[J] mod 26 = 0 (THIS IS WHAT YOU ADD TO THE PLAINTEXT LETTER mod 26)


CIPHERTEXT: TQWCIHKYDHVUXYH
