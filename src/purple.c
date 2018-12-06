#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned char *purple_crypt(unsigned char *data, unsigned char *key, unsigned char *nonce, long datalen, int keylen, int noncelen) {
    int diff = 256 - keylen;
    int k[256] = {0};
    int j = 0;
    int i = 0;
    int c;
    int m = 256 / 2;
    int output;
    for (c=0; c < keylen; c++) {
        k[c % keylen] = (k[c % keylen] + key[c % keylen]) & 0xff;
        j = (j + k[c % keylen]) & 0xff; }
    for (c = 0; c < 256; c++) {
        k[j] = (k[c % keylen] + k[j]) & 0xff;
        j = k[j]; }
    for (c = 0; c < noncelen; c++) {
        k[c] = (k[c % noncelen] + nonce[c]) & 0xff;
        j = (j + k[c % noncelen]) & 0xff; }
    for (c = 0; c < 256; c++) {
        k[j] = (k[c % keylen] + k[j]) & 0xff;
        j = k[j]; }
    for (c = 0; c < diff; c++) {
        k[c+keylen] = (k[c] + k[(c + 1) % diff] + j) & 0xff;
	j = (k[j] + k[c % diff]) & 0xff; }
    for (c = 0; c < 256; c++) {
        k[c] = (k[c] + k[(c + m) & 0xff] + k[j]) & 0xff;
        j = (j + k[c]) & 0xff; }


   c = 0;
   for (int x = 0; x < datalen; x++) {
       j = k[j];
       k[j] = (k[c] + k[j]) & 0xff;
       output = (k[k[j]] + k[j]) & 0xff;
       data[x] = data[x] ^ output;
       c = (c + 1) & 0xff;
   } 
}

unsigned char * purple_random (unsigned char *buf, int num_bytes) {
    int keylen = 32;
    int noncelen = 16;
    unsigned char *key[keylen];
    unsigned char nonce[noncelen];
    FILE *randfile;
    randfile = fopen("/dev/urandom", "rb");
    fread(&nonce, noncelen, 1, randfile);
    fread(&key, keylen, 1, randfile);
    fclose(randfile);
    purple_crypt(buf, key, nonce, num_bytes, keylen, noncelen);
}
