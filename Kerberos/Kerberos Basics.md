High level overview


- When a user logins into the AD with his Usernames and Password, Kerberos upon verifying the creds issues a TGT(Ticket Granting Ticket). 
- Using that TGT, user can go to the Key Distribution Centre and request for service it requires.
- The KDC then gives another ticket upon verifying the TGT which is solely for accessing that service.
  
  
  ## Kerberos Terminology
  
  Objects registered in Kerberos realm are called user and service principles.
  
  User Principal Name(UPN) - Unique user Id (UserName@domain.com)
  
  Service Principal Name(SPN) - Unique Service Id (ServiceType/ServiceName.domain.com:CustomPort)
  
  No Duplicates UPN or SPN allowed
  
  ## Kerberos Key Distribution Centre
   
   An AD service which runs on all DCs under KRBTGT service account.
   
- Authentication Service authenticates principals and issues TGTs.
- Ticket Granting Service issues service tickets to authenticated principals.
  
  ## KRBTGT
  
- ### A service account used by KDC service.
- ### The trusted party in client-service authentication.
- ### Responsible for KAdmin service and change password process



  ## Kerberos Secret Keys

  Kerberos long term symmetric secret keys.
  Kerberos long-term asymmetric public keys.
  Kerberos short-term symmetric session keys.
  
  
  
  ## Kerberos long term symmetric secret keys.
  
- User key: A hash derived from user's password.
- System key: A hash derived from computer's password.
- Service key: A hash derived from service's password.
- Inter-realm key: A hash derived from domain trust's password.
  
### Kerberos long-term asymmetric public keys.

Public-key certificates stored on smart cards.

### Kerberos short-term symmetric session keys.

Session keys used for encrypting and decrypting service ticket
requests and responses.

## Kerberos Tickets

- Ticket Granting Ticket (TGT): A master ticket the Kerberos clients use
for requesting service tickets.
- Service Ticket (ST): A ticket the Kerberos clients use for authenticating
to a service encrypted with target service account key.
- Referral TGTs are used for cross-realm service access.
Once Kerberos issues a ticket, it discards it from system cache

![[Pasted image 20240713004939.png]]

### Credentials Cache
• Holds clients' secret keys and tickets.
• An area of RAM protected by LSASS.
• Content never paged to disk.
• Flushed on logoffs and reboots.

Note: System and service 's keys are stored in encrypted part of the
registry so they can survive reboots.
Note: Cached logon credentials are password verifiers.

