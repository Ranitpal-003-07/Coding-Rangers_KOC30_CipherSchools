def email_breaker():
  email = input("Enter Your Email: ").strip()
  # [input("Ener your Email: ").strip()] is used for to remove unnecessary spaces in the string/email
  username = email[:email.index('@')]
  #[:email.index('@')] is used to take the characters/letters from 1st to before '@' 
  domain = email[email.index('@') + 1:]
  #[email.index('@') + 1:] is used to take the characters/letters till the last one from thr leter whuch is after '@'
  domain_2= domain.upper()
  # [domain_2=domain.upper()] is used to capitalize all the letters in the string 'domain' and asign it to 'domain_2'
  username_2=username.upper()
  # [usernmae_2=username.upper()] is used to capitalize all the letters in the string 'username' and asign it to 'username_2'
  print(f"Your username is: {username_2}")
  # [f"Your username is: {username_2}"] is used to print Your username is: (value of username_2) 
  print(f"domain is: {domain_2}")
  return email_breaker()
email_breaker()