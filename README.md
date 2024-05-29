# UTILISATIONS 📣



# DÉVELOPPENTS
### Concaténation de plusieurs fichiers word

Compilation de rapports words.  
Cette application permet de compiler des rapports word en un seul rapport word au final.

Avant tout d'abord pour lancer la concaténation de documents depuis Streamlit, il vous faut au préalable constituer la liste des fichier que vous voulez fusionner, et puis les déposer dans le dossier : *'sorties_word_doc'*.


L'application streamlit(python) prends tous les documents word et les concatène et puis donne un rendud en word.

## Compilation de rapports word 🛠️

Pour lancer une application streamlit en local, il faudra appliquer les étapes suivantes :


- Ouvrir un terminal dans l'endroit contenant le script *"code.py"*  
- Puis saisir depuis le terminal la commande suivante :

```python
streamlit run app_compile_word.py
```

Voici le schéma du repo :  

```
/tests_data
|-- /.venv
	|-- /Downloads
	|-- /etc
	|-- /Include
	|-- /Lib
	|-- /Scripts
	|   |-- app_compile_word_up.py
	|-- /share
	|-- /Temp
|-- /sorties_word_doc
|-- /sorties_word_rft
|-- README.md
```

### Installations et dépendances 💻
#### Démarches à suivre
Pour constituer notre repo :   

**1**- Nous avons d'abord definie notre architechture de repo dont nous avons besoin comme le montre le schéma ci-dessus.

**2**- Ensuite, nous avons pointé ver le dossier principal du repo   
```cd /chemin/vers/votre/projet```

**3**- Puis créer notre environnement virtuel qui va accueillir notre programme python et ses dépendances.  
```python -m venv /chemin/vers/nouvel/environnement```

**4**- Par exemple, si vous voulez créer l'environnement virtuel dans le répertoire de votre projet, la commande serait :  
```python -m venv.venv```

**NB** : Normalement lors de la création de l'environnement virtuel, il y a eu un fichier .gitignore (txt) qui a été créé. Il faudra rajouter la commande suivante dans de fichier :   
```
# Exemple de contenu pour.gitignore
venv/ 
```  
Donc le fait d'ajouter dans le gitignore ce bout de code précédent permet de pouvoir intégré le .venv dans le repo.

**5**- Activez l'environnement virtuel : Activez l'environnement virtuel en utilisant la commande appropriée selon votre système d'exploitation.
```.\.venv\Scripts\activate``` et pour désactiver l'environnement :    
```.\.venv\Scripts\Deactivate```    

Et enfin, quand la MAJ du code python est terminée, vous pourrez créez le fichier de ```requirements.txt``` avec les commandes suivantes :  

```pip freeze > requirements.txt```    
```git add requirements.txt```    
```git commit -m "Add requirements.txt"```    
```git push```      


Rques : Si vous ne souhaitez pas inclure tous les paquets installés dans votre projet, mais seulement ceux qui sont effectivement utilisés, vous pouvez utiliser pipreqs. pipreqs analyse votre code pour identifier les paquets importés et génère un fichier requirements.txt plus concis. Pour l'utiliser, installez pipreqs et exécutez.

```pip install pipreqs```  
```pipreqs /chemin/vers/votre/projet```  

Ensuite :  
```pip install -r requirements.txt```  



