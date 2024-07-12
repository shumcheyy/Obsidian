

# KERBEROASTING

1. Normal process: In a Windows network, when a user wants to access a service (like a file server or database), they request a special ticket called a Service Ticket from the domain controller. This ticket is encrypted using the password hash of the service account.
2. The attack: An attacker with valid domain credentials (even low-privileged ones) can request Service Tickets for any service in the domain.
3. Offline cracking: The attacker then extracts these tickets and attempts to crack the encryption offline to reveal the service account's password.
4. Why it works: Service accounts often have weak passwords that don't change frequently, making them vulnerable to cracking attempts.
5. Consequences: If successful, the attacker can gain access to the compromised service account, which often has elevated privileges.

Key points:

- It doesn't require admin rights to perform
- The actual cracking happens offline, making it hard to detect
- It exploits weak passwords and poor password management practices
- It's a popular technique because it's relatively simple and can yield high-value credentials

To defend against Kerberoasting, organizations should use strong, regularly rotated passwords for service accounts, implement proper monitoring, and use more secure account

# AS-REP ROASTING



