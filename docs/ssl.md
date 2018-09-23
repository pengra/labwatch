# SSL & Other Security Reports
// Written on **September 23rd, 2018**

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            03:3c:2c:a3:27:13:19:0a:fb:d7:eb:c6:98:33:29:60:f3:92
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: (CA ID: 16418)
            commonName                = Let's Encrypt Authority X3
            organizationName          = Let's Encrypt
            countryName               = US
        Validity
            Not Before: Sep 23 09:08:17 2018 GMT
            Not After : Dec 22 09:08:17 2018 GMT
        Subject:
            commonName                = library.pengra.io
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:c1:89:c9:ec:26:ad:a3:56:74:27:e8:0e:86:b2:
                    00:87:08:32:1e:c2:44:b8:e9:e4:00:3a:50:07:18:
                    12:e9:24:50:c2:09:ca:37:44:e2:ad:60:59:6a:d9:
                    ce:82:03:76:7a:96:98:b1:f5:43:9b:a4:19:4d:45:
                    2b:d8:22:80:99:29:40:c6:0f:35:de:92:92:8d:c9:
                    da:ed:87:1f:76:ef:1d:13:0a:9a:6d:f7:4e:34:8f:
                    ac:f6:3e:90:68:1b:f6:d9:fa:63:7b:68:83:e5:b7:
                    90:17:57:f8:3d:ca:b9:4b:d9:69:16:31:0c:d7:b1:
                    09:91:71:71:0b:78:6b:c5:85:97:a9:cf:ea:35:9c:
                    46:b6:6a:54:bf:10:16:f8:7b:6f:98:b4:44:33:7c:
                    2a:8e:ae:53:b7:28:fb:ea:4c:6e:57:94:7c:ba:47:
                    20:a9:57:0e:8c:0f:57:66:dd:47:97:96:3d:a2:1c:
                    e7:5d:e4:fa:2f:a9:c8:9e:3b:fc:a0:2b:f3:4d:20:
                    09:ba:f9:b9:cb:5c:41:db:88:af:01:80:aa:01:40:
                    88:3d:c4:b0:44:e3:bb:46:0d:5b:c0:4d:80:7f:0a:
                    40:86:0f:91:34:ce:92:50:86:e2:90:99:8f:c7:92:
                    54:fc:06:13:b6:b4:4b:9f:bd:ea:04:51:81:96:f6:
                    c1:7f
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            X509v3 Extended Key Usage: 
                TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier:
                7F:19:FE:CE:A7:A2:EB:6A:37:D8:9F:00:83:3A:D3:A2:8A:D2:4F:44
            X509v3 Authority Key Identifier: 
                keyid:A8:4A:6A:63:04:7D:DD:BA:E6:D1:39:B7:A6:45:65:EF:F3:A8:EC:A1

            Authority Information Access: 
                OCSP - URI:http://ocsp.int-x3.letsencrypt.org
                CA Issuers - URI:http://cert.int-x3.letsencrypt.org/

            X509v3 Subject Alternative Name: 
                DNS:library.pengra.io
                DNS:norton.pengra.io
                DNS:pengrabot.ddns.net
                DNS:this.pengra.io
            X509v3 Certificate Policies: 
                Policy: 2.23.140.1.2.1
                Policy: 1.3.6.1.4.1.44947.1.1.1
                  CPS: http://cps.letsencrypt.org
                  User Notice:
                    Explicit Text: This Certificate may only be relied upon by Relying Parties and only in accordance with the Certificate Policy found at https://letsencrypt.org/repository/

            CT Precertificate Poison: critical
                0000 - 05                                       .
                0002 - <SPACES/NULS>

    Signature Algorithm: sha256WithRSAEncryption
         69:00:19:80:28:90:48:ac:ec:6a:c2:41:11:24:dc:1d:41:c8:
         6e:60:85:d8:33:87:74:fb:fa:2f:e5:a4:3c:06:c7:30:b5:87:
         8d:0b:64:57:06:3b:74:16:c2:71:a8:51:d0:c2:43:f2:2f:5a:
         83:64:11:84:67:70:d6:25:82:f0:f0:92:8f:ce:a6:f3:b6:1f:
         8f:48:be:9c:1c:83:b0:85:98:8c:09:a4:d2:c6:40:ff:8c:73:
         aa:88:09:6b:34:62:59:6a:2d:dd:59:a1:b9:ba:68:76:4c:64:
         c5:bd:91:db:6d:54:15:5a:2a:bb:66:ac:bd:30:b4:8b:80:0a:
         32:55:17:84:95:40:b5:a0:d5:10:30:ec:57:15:0f:bf:1b:bf:
         97:e2:c6:24:27:5c:89:3b:53:56:62:0e:1d:ae:36:60:e0:0b:
         38:f4:53:e3:47:2a:44:b7:1e:28:b3:ad:fa:42:e1:6f:7c:07:
         ad:bd:af:ac:57:e4:6f:91:39:7e:f6:14:9e:8b:88:5a:e2:7e:
         c9:9e:ec:d4:00:0f:1f:0e:7e:2a:90:b7:99:98:9d:c9:9d:56:
         f0:e4:0c:23:ca:fb:b7:07:14:67:10:41:d0:1a:c5:e7:b9:5f:
         fc:c8:3f:13:3f:bc:f3:ce:32:04:4c:08:10:44:f1:f0:10:5a:
         2f:f5:5c:2d
```

- [Read the full Report](https://www.ssllabs.com/ssltest/analyze.html?d=library.pengra.io&hideResults=on)