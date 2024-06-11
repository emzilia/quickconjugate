# quickconjugate
conjugate Spanish verbs with a simple API using web scraping, requests are made to:    
<https://conjugator.reverso.net>

### dependencies installed via pip    
lxml    
requests    
flask  

### to run
Clone the repo with ```git clone https://github.com:emzilia/quickconjugate```  
Checkout the web app ```git checkout webapp```  
Build the dockerfile ```docker build .``` or ```podman build .```  
Run the docker image ```docker run -d --network host <image ID>``` or ```podman run -d --network host <image ID>```  
The ```-d``` operand runs the container in a detached state, ```--network host``` uses the host computer's network.   

### to use
Direct API requests to:
```localhost:5000/api/conjugate?verb={VERB}``` where {VERB} is the specific Spanish verb to be conjugated.  
Substitute ```localhost``` with the server's IP if being run remotely.  
This was created as a test however and has little practical use, so it's unlikely you would actually be doing this.   

example input:    
```curl http://localhost:5000/api/conjugate?verb=aprender```    
output:
```
{
  "aprender": "[['aprendo', 'aprendes', 'aprende', 'aprendemos', 'aprend\u00e9is', 'aprenden'], ['aprender\u00e9', 'aprender\u00e1s', 'aprender\u00e1', 'aprenderemos', 'aprender\u00e9is', 'aprender\u00e1n'], ['aprend\u00eda', 'aprend\u00edas', 'aprend\u00eda', 'aprend\u00edamos', 'aprend\u00edais', 'aprend\u00edan'], ['aprend\u00ed', 'aprendiste', 'aprendi\u00f3', 'aprendimos', 'aprendisteis', 'aprendieron']]"
}
```
You get a bunch of gnarly escape codes though
