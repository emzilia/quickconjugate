# quickconjugate
Conjugate Spanish verbs in the command line with web scraping, requests are made to:    
<https://conjugator.reverso.net>

### to install
The recommended installation method is via [pipx](https://github.com/pypa/pipx), which greatly improves the UX of installing and managing python CLI apps; it can be found in the repos of most major distributions. After it's been installed, you can install quickconjugate by executing this command within your terminal:   
```pipx install git+https://github.com/emzilia/quickconjugate.git```

### to use
Type the command followed by a Spanish verb.

example input:    
```conj aprender```    
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
