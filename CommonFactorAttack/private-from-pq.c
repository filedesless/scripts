#include <stdlib.h>
#include <openssl/bn.h>
#include <openssl/rsa.h>
#include <openssl/engine.h>

// from: http://www.loyalty.org/~schoen/rsa/

int
main (int argc, char *argv[])
{

  BIGNUM *n = BN_new ();
  BIGNUM *d = BN_new ();
  BIGNUM *e = BN_new ();
  BIGNUM *p = BN_new ();
  BIGNUM *q = BN_new ();
  BIGNUM *p1 = BN_new ();
  BIGNUM *q1 = BN_new ();
  BIGNUM *dmp1 = BN_new ();
  BIGNUM *dmq1 = BN_new ();
  BIGNUM *iqmp = BN_new ();
  BIGNUM *phi = BN_new ();
  BN_CTX *ctx = BN_CTX_new ();
  RSA *key = RSA_new ();

  if (argc < 3)
    {
      fprintf (stderr, "usage: %s p q\n", argv[0]);
      exit (1);
    }

  if (!(BN_dec2bn (&p, argv[1])) || !(BN_dec2bn (&q, argv[2]))) {
      fprintf (stderr, "usage: %s p q\n", argv[0]);
      exit (1);
  }

  if (!(BN_is_prime (p, BN_prime_checks, NULL, ctx, NULL)) ||
      !(BN_is_prime (q, BN_prime_checks, NULL, ctx, NULL))) {
      fprintf (stderr, "Arguments must both be prime!\n", argv[0]);
      exit (1);
  }

  BN_dec2bn (&e, "65537");

  /* Calculate RSA private key parameters */

  /* n = p*q */
  BN_mul (n, p, q, ctx);
  /* p1 = p-1 */
  BN_sub (p1, p, BN_value_one ());
  /* q1 = q-1 */
  BN_sub (q1, q, BN_value_one ());
  /* phi(pq) = (p-1)*(q-1) */
  BN_mul (phi, p1, q1, ctx);
  /* d = e^-1 mod phi */
  BN_mod_inverse (d, e, phi, ctx);
  /* dmp1 = d mod (p-1) */
  BN_mod (dmp1, d, p1, ctx);
  /* dmq1 = d mod (q-1) */
  BN_mod (dmq1, d, q1, ctx);
  /* iqmp = q^-1 mod p */
  BN_mod_inverse (iqmp, q, p, ctx);

  /* Populate key data structure */
  key->n = n;
  key->e = e;
  key->d = d;
  key->p = p;
  key->q = q;
  key->dmp1 = dmp1;
  key->dmq1 = dmq1;
  key->iqmp = iqmp;

  /* Output the private key in human-readable and PEM forms */
  RSA_print_fp (stdout, key, 5);
  printf("\n");
  PEM_write_RSAPrivateKey (stdout, key, NULL, NULL, 0, 0, NULL);

  /* Release allocated objects */
  BN_CTX_free (ctx);
  RSA_free(key); /* also frees n, e, d, p, q, dmp1, dmq1, iqmp */
  BN_clear_free (phi);
  BN_clear_free (p1);
  BN_clear_free (q1);

}
