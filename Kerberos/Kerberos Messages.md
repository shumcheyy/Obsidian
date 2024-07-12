### Initial authentication (client <--> KDC AS):
• KRB_AS_REQ: Client to KDC Authentication Server, a TGT request.
• KRB_AS_REP: KDC AS to client, a TGT response.
### Requesting access to a service (client <--> KDC TGS):
• KRB_TGS_REQ: Client to KDC TGS, a service ticket request.
• KDC TGS to client, a service ticket response.
### Authenticating to a service (client <--> service):
• KRB_AP_REQ: Client to service/application, a service authentication request.
• KRB_AP_REP: Service/application to client, service authenticates to client.

## Initial authentication (client <--> KDC AS):

**KRB_AS_REQ (Authentication Service Request):**  
This is the first step in the Kerberos authentication process. The client sends a request to the Key Distribution Center's (KDC) Authentication Server (AS) for a Ticket-Granting Ticket (TGT). This request typically includes:

- The client's identity (usually a username)
- The Ticket-Granting Service (TGS) name
- A timestamp (to prevent replay attacks)
- A requested lifetime for the ticket

The client doesn't send a password at this stage. Instead, it uses a key derived from the user's password to encrypt part of the request[](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/b4af186e-b2ff-43f9-b18e-eedb366abf13)[](https://www.varonis.com/blog/kerberos-authentication-explained).

**KRB_AS_REP (Authentication Service Response):**  
If the KDC successfully authenticates the client, it responds with a KRB_AS_REP message containing:

- A session key for communication between the client and the TGS
- A Ticket-Granting Ticket (TGT)

The session key is encrypted with the client's secret key (derived from the user's password), while the TGT is encrypted with the TGS's secret key. The client can decrypt the session key using its password-derived key, but cannot decrypt the TGT itself.

## Requesting access to a service (client <--> KDC TGS):

**KRB_TGS_REQ (Ticket-Granting Service Request):**  
When the client wants to access a specific service, it sends a KRB_TGS_REQ to the KDC's Ticket-Granting Service (TGS). This request includes:

- The TGT received in the KRB_AS_REP
- The Service Principal Name (SPN) of the desired service
- An authenticator (encrypted with the session key from KRB_AS_REP)

**KRB_TGS_REP (Ticket-Granting Service Response):**  
The TGS verifies the TGT and authenticator. If valid, it responds with:

- A service ticket for the requested service
- A new session key for communication between the client and the service

The service ticket is encrypted with the service's secret key, while the new session key is encrypted with the session key from the KRB_AS_REP.

## Authenticating to a service (client <--> service):

**KRB_AP_REQ (Application Request):**  
The client sends the KRB_AP_REQ to the desired service, containing:

- The service ticket received in the KRB_TGS_REP
- A new authenticator encrypted with the session key from KRB_TGS_REP

**KRB_AP_REP (Application Response):**  
If mutual authentication is required, the service responds with a KRB_AP_REP. This message contains the timestamp from the client's authenticator, encrypted with the session key. This proves to the client that the service was able to decrypt the service ticket and read the authenticator[](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/b4af186e-b2ff-43f9-b18e-eedb366abf13)[](https://www.varonis.com/blog/kerberos-authentication-explained).This process allows for secure authentication without transmitting passwords over the network, and provides the basis for Single Sign-On (SSO) in Kerberos environments. Each ticket has a limited lifetime, enhancing security by reducing the window of opportunity for potential attacks.


# NONCE [Number used only once]

The term "nonce" stands for "number used once" or "number once". It's a unique value generated for a specific use in cryptographic operations. The main purpose of a nonce is to prevent replay attacks by ensuring that old communications cannot be reused. It adds freshness and uniqueness to each communication.

# PRIVILEGE ACCOUNT CERTIFICATE [PAC]

# Kerberos encryption algorithms and keys

RC4 key is client's NTLM MD4 hash.
AES key is derived from the client's password salted with client's
Realm + sAMAccountName in the form of "DOMAIN.COMsamaccountname" and hashed using string2key function PBKDF2+DK.

# Most common Kerberos errors cont.
• The client requested a ticket but did not include pre-authentication data with it. Windows Uses this technique to determine the supported encryption types.

• KDC_ERR_BADOPTION - Several reasons for rejection:

- The service account is not trusted for delegation.
- The service account is not trusted for delegation to the requested SPN.
- The user's account is marked as sensitive.
- The request was for a constrained delegation ticket to itself.
