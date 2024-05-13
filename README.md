
# Concaténation de plusieurs fichiers word

Compilation de rapports words.  
Cette application permet de compiler des rapports word en un seul rapport word au final.

Avant tout d'abord pour lancer la concaténation de documents depuis Streamlit, il vous faut au préalable constituer la liste des fichier que vous voulez fusionner, et puis les déposer dans le dossier : *'sorties_word_doc'*.


L'application streamlit(python) prends tous les documents word et les concatène et puis donne un rendud en word.

## Compilation de rapports word

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