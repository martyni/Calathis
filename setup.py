from distutils.core import setup

with open('requirements.txt') as reqs:
    requirements = [req.split('\n')[0] for req in reqs.readlines() ]

print(requirements)
setup(name='Calathis',
      version='1.0',
      description='Python Distribution Utilities',
      author='Martyn Pratt',
      author_email='martynjamespratt@gmail.com',
      packages=['Calathis'],
      install_requires=requirements,
      scripts=['make_gif_today','take_picture_now']
     )
