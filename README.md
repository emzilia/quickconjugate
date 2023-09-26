# quickconjugate
conjugate Spanish verbs in the command line with web scraping, requests are made to:    
<https://conjugator.reverso.net>

### to install
First, read the ```install.sh``` file to see what it's doing to your system.   
Then, run the file with ```bash install.sh``` from within the same directory.    
The ```install.sh``` can be run a second time to remove the file from your ```$HOME/.local/bin```

### to use
Type the command followed by a Spanish verb.

example input:    
```conj aprender                 prints the present, future, and imperfect preterite tenses.```
output:
```
PRESENTE        FUTURO          PRETÉRITO (imp) PRETÉRITO (per)
aprendo         aprenderé       aprendía        aprendí
aprendes        aprenderás      aprendías       aprendiste
aprende         aprenderá       aprendía        aprendió
aprendemos      aprenderemos    aprendíamos     aprendimos
aprendéis       aprenderéis     aprendíais      aprendisteis
aprenden        aprenderán      aprendían       aprendieron
```
