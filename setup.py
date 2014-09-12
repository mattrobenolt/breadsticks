from __future__ import print_function
import sys

for arg in sys.argv:
    if arg in ('sdist', 'dist', 'build', 'register', 'upload'):
        from setuptools import setup
        setup(
            name='breadsticks',
            version='1.0.0',
            author='Matt Robenolt',
            author_email='matt@ydekproductions.com',
            url='https://github.com/mattrobenolt/breadsticks',
            license='BSD',
            classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python',
                'Topic :: Software Development',
            ],
        )
        sys.exit(0)

    if arg == 'develop':
        # Don't duplicate breadsticks if doing `pip install -e`
        sys.exit(0)

from random import random
import time

print()
print("Baking up fresh breadsticks. Please wait...")
print()
sys.stdout.flush()
total = 0
width = 40
while 1:
    i = int(width * total)
    dots = ('.' * i).ljust(width)
    print('[%s] %d%%' % (dots, total*100))
    sys.stdout.flush()
    if total == 1:
        break
    time.sleep(random()/2)
    total += random()/10
    total = min(1, total)
print("""

       `,.                                             
       :;,;,,,,,:.                                     
      ::::::::::,,,,.`                                 
      ::,;:::::':::::,:,,:                             
      :::::::;::::::::,:::,,,                          
      :;,:,:::;:::::::::::::.,..                       
       ::,;;:;;:;;:::::::::,;::,,,,                    
        :;;;;::::;;:::;;::::::::,,,,,.`                
         .::;;;:::;:;;;::::::::;,,,,::,,.`             
           `,,;;:::;:;;:,:::::;:::,::::::,,:`          
 ,;,;`.,...  .,::::::;,:::::::;;:::::,::,,:,,,`        
`::::::::,,,,.`.,::::;':::::::;;;;:::::::,,,;,,,.      
:;;;:::::;:,::,,,..,,:,::;:::::;;::::;::::,:,:,,,,,`   
;:,;:::,;::;::::::,,,,,,,:::::::::;::::::::::::,,,,,.  
::.::,;;;;:':::::,::::,,.,,,::;:::;:::::;:::::::,,+,,, 
.::::;;;;;;:::::::::::'::,,,,,:::::'::::::::::::::::',.
 :::;;::::;;;:;;::;::::,,:,,,,.,,::,::::::;:::::::::::,
  :::;;;;::;;:::;:::;:::::,,,,,:,,,,,,,::',:::::::::::,
   `.:;::::::::;:::::;::;::::::,:,:,,,,,,,::::::;;:;::,
      `,:;;::::;;::::::::;::::::;:,,:,,,,,,:::;:::::::,
       `.,:::::;;:::::::::;;;::::::,,,;,,,.,,,,:::;::, 
          `::,::::::;:::;;;:;::;;:::,:,:,,,,,.`.,,,.   
             .,,,,':::::::;;;::::::::::::,,,:,.        
                `,,,::::::::::::::::::::::::+,,,       
                    .,,:;;:::::;::::::::::::::;,,      
                       `,,,:::;:::::::,:::::::::,      
                           .,,,::,,;:::::::::::::      
                              ,:,:::;:::::;;:'::,      
                                 `,,:::::::;::::,      
                                   `.,:,,:::;:::       
                                       `,,,,,,`        

Boom. You got breadsticks. Enjoy.


""")
