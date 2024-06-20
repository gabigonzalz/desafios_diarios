# Generador de Contraseñas Seguras

import random
import string
print("""8''''8                                                                                                                           
8    " eeee eeeee eeee eeeee  eeeee eeeee eeeee eeeee    eeeee eeee   eeee eeeee eeeee eeeee eeeee  eeeee eeeee eeee eeeee eeeee 
8e     8    8   8 8    8   8  8   8 8   8 8  88 8   8    8   8 8      8  8 8  88 8   8   8   8   8  8   8 8   " 8    8   8 8   " 
88  ee 8eee 8e  8 8eee 8eee8e 8eee8 8e  8 8   8 8eee8e   8e  8 8eee   8e   8   8 8e  8   8e  8eee8e 8eee8 8eeee 8eee 8eee8 8eeee 
88   8 88   88  8 88   88   8 88  8 88  8 8   8 88   8   88  8 88     88   8   8 88  8   88  88   8 88  8    88 88   88  8    88 
88eee8 88ee 88  8 88ee 88   8 88  8 88ee8 8eee8 88   8   88ee8 88ee   88e8 8eee8 88  8   88  88   8 88  8 8ee88 88ee 88  8 8ee88 
                                                                                                                                 """)

longitud = random.randint(8,16)

caracteres = string.ascii_letters + string.digits + string.punctuation
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

print(f"""                                          Contraseña generada: {contrasena}
""")
