# Routes

## LOAD-BALANCER

### Status
- **GET** `http://MY_DOMAIN/`  
  Confirme si le serveur est en cours d'exécution.

### Partie DevOps
- **GET** `http://MY_DOMAIN/leader`  
  Récupère le domaine du leader REDIS.  
- **POST** `http://MY_DOMAIN/leader`  
  Déclenche l'élection d'un nouveau leader.  
- **ANY** `http://MY_DOMAIN/api/*ANY_WILDCARD*`  
  Transfère la requête vers `http://CONSULT_DB_SLAVE/*ANY_WILDCARD*`.

---

## CONSULT_DB_SLAVE

### Status
- **GET** `http://MY_DOMAIN/`  
  Confirme si le serveur est en cours d'exécution.  
- **GET** `http://MY_DOMAIN/health`  
  Confirme si REDIS est en cours d'exécution.

### Partie DevOps
- **POST** `http://MY_DOMAIN/elect-new`  
  **BODY :** `{ domain: string?, port: number? }`  
  Spécifie quel instance REDIS utiliser.

### Fonctionnalité Redis/Store
- **GET** `http://MY_DOMAIN/get-value/:key`  
  Lit une valeur associée à la clé donnée.  
- **GET** `http://MY_DOMAIN/keys`  
  Récupère toutes les clés stockées dans REDIS.  
- **POST** `http://MY_DOMAIN/set-value`  
  **BODY :** `{ key, value }`  
  Insère un objet dans le store.